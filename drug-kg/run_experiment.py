#!/usr/bin/env python
"""Run an EDC experiment on an alternative text source and (optionally) KGGen entity canonicalization.

Layout: output/experiments/<exp>/{chunks,edc,schema,kg,entity_canon,kg_canon,audit,audit_canon}/ + stages.json + run.log

Examples
  python run_experiment.py --exp text_edc      --input text      --stage all
  python run_experiment.py --exp decomp_edc    --input sentences --stage all
  python run_experiment.py --exp decomp_edc_ec --from-exp decomp_edc --entity-canon kggen --stage all
  python run_experiment.py --exp smoke --input sentences --drugs 1 --max-chunks 2 --entity-canon kggen --stage all
"""
from __future__ import annotations
import argparse
import collections
import csv
import json
import logging
import pathlib
import shutil
import subprocess
import sys
import time

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from drugkg.config import ROOT, Config  # noqa: E402
from drugkg.inputs import SENT_FILE_DEFAULT, TEXT_DIR_DEFAULT, chunks_from_sentences, chunks_from_text  # noqa: E402

log = logging.getLogger("drugkg.exp")


def fname(slug: str) -> str:
    return slug.replace("/", "__")


class Experiment:
    def __init__(self, name: str, cfg: Config):
        self.name, self.cfg = name, cfg
        self.dir = ROOT / "output" / "experiments" / name
        for sub in ("chunks", "edc", "schema", "kg"):
            (self.dir / sub).mkdir(parents=True, exist_ok=True)
        self.stages_path = self.dir / "stages.json"
        self.stages = json.loads(self.stages_path.read_text()) if self.stages_path.exists() else {}

    def record(self, stage: str, seconds: float, **extra) -> None:
        self.stages[stage] = {"seconds": round(seconds, 1), "finished_at": time.strftime("%Y-%m-%d %H:%M:%S"), **extra}
        self.stages_path.write_text(json.dumps(self.stages, indent=2, ensure_ascii=False), encoding="utf-8")

    # ------------------------------------------------------------------ helpers
    def slugs(self) -> list[str]:
        return sorted(p.stem for p in (self.dir / "chunks").glob("*.jsonl"))

    def load_chunks(self, slug: str) -> list[dict]:
        return [json.loads(l) for l in (self.dir / "chunks" / f"{fname(slug)}.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

    def parsed_record(self, slug: str) -> dict | None:
        p = ROOT / "data" / "parsed" / f"{fname(slug)}.json"
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


# ---------------------------------------------------------------------- stages
def stage_prepare(exp: Experiment, args) -> None:
    t0 = time.time()
    ch = exp.cfg.section("chunking")
    if args.input == "text":
        chunks = chunks_from_text(ROOT / (args.text_dir or TEXT_DIR_DEFAULT), int(ch.get("max_chars", 1100)),
                                  int(ch.get("min_chars", 150)), ch.get("exclude_sections") or [])
    elif args.input == "sentences":
        chunks = chunks_from_sentences(ROOT / (args.sentences_file or SENT_FILE_DEFAULT), int(ch.get("max_chars", 1100)),
                                       sentence_level=args.sentence_level, keep_incomplete=not args.drop_incomplete)
    elif args.input == "chunks":  # reuse the main pipeline's chunks
        chunks = {p.stem: [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
                  for p in (ROOT / "data" / "chunks").glob("*.jsonl")}
    else:
        raise SystemExit(f"unknown input {args.input}")
    selected = select_slugs(sorted(chunks), args.drugs)
    n = 0
    for slug in selected:
        with open(exp.dir / "chunks" / f"{fname(slug)}.jsonl", "w", encoding="utf-8") as f:
            for c in chunks[slug]:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        n += len(chunks[slug])
    log.info("prepared %d drugs, %d chunks from input=%s", len(selected), n, args.input)
    exp.record("prepare", time.time() - t0, input=args.input, n_drugs=len(selected), n_chunks=n,
               sentence_level=args.sentence_level)


def select_slugs(slugs: list[str], selector: str | None) -> list[str]:
    if not selector or selector == "all":
        return slugs
    if selector.isdigit():
        return slugs[: int(selector)]
    wanted = {s.strip().lower() for s in selector.split(",")}
    return [s for s in slugs if s.lower() in wanted or s.replace("__", "/").lower() in wanted]


def build_edc(exp: Experiment, iterations: int | None):
    from drugkg.edc.framework import EDCFramework
    from drugkg.edc.schema import Embedder, Schema
    from drugkg.llm import build_llm
    cfg = exp.cfg
    if iterations is not None:
        cfg.raw.setdefault("edc", {})["refinement_iterations"] = iterations
    llm = build_llm(cfg)
    if not llm.ping():
        raise SystemExit("LLM server is not reachable. Start it with: bash scripts/serve_vllm.sh")
    emb_cfg = cfg.section("embedder")
    embedder = Embedder(emb_cfg.get("model", "BAAI/bge-base-en-v1.5"), emb_cfg.get("device", "cpu"))
    live = exp.dir / "schema" / "schema.csv"
    schema = Schema.load(live if live.exists() else cfg.path("edc.schema_path"), embedder, default_origin="seed")
    return llm, embedder, schema, EDCFramework(cfg, llm, schema)


def stage_extract(exp: Experiment, args) -> None:
    t0 = time.time()
    llm, embedder, schema, edc = build_edc(exp, args.iterations)
    done = 0
    for slug in exp.slugs():
        out = exp.dir / "edc" / f"{fname(slug)}.json"
        if out.exists() and not args.force:
            continue
        chunks = exp.load_chunks(slug)
        if args.max_chunks:
            chunks = chunks[: args.max_chunks]
        if not chunks:
            continue
        t1 = time.time()
        log.info("=== %s: %d chunks", slug, len(chunks))
        result = edc.run_drug(chunks)
        result.update({"name": chunks[0]["drug"], "slug": slug, "n_chunks": len(chunks), "seconds": round(time.time() - t1, 1),
                       "llm_model": llm.model_id})
        out.write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
        schema.save(exp.dir / "schema" / "schema.csv")
        done += 1
        log.info("%s: %d final triplets in %.0fs; schema %d; llm %s", slug, len(result["final_triplets"]), time.time() - t1,
                 len(schema), llm.stats)
    exp.record("extract", time.time() - t0, drugs_extracted=done, llm_model=llm.model_id, llm_stats=llm.stats,
               schema_size=len(schema))


def stage_consolidate(exp: Experiment, args) -> None:
    from drugkg.edc.consolidate import consolidate_schema
    from drugkg.edc.prompts import Prompts
    t0 = time.time()
    llm, embedder, schema, _ = build_edc(exp, None)
    edc_cfg = exp.cfg.section("edc")
    merge_map = consolidate_schema(schema, llm, Prompts(), float(edc_cfg.get("consolidate_sim", 0.85))) \
        if edc_cfg.get("consolidate_schema", True) else {}
    (exp.dir / "schema" / "relation_merge_map.json").write_text(json.dumps(merge_map, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("consolidation: %d merges", len(merge_map))
    exp.record("consolidate", time.time() - t0, n_merges=len(merge_map), llm_stats=llm.stats)


def _load_schema_for_export(exp: Experiment):
    from drugkg.edc.schema import Embedder, Schema
    emb_cfg = exp.cfg.section("embedder")
    embedder = Embedder(emb_cfg.get("model", "BAAI/bge-base-en-v1.5"), emb_cfg.get("device", "cpu"))
    live = exp.dir / "schema" / "schema.csv"
    return embedder, Schema.load(live if live.exists() else exp.cfg.path("edc.schema_path"), embedder)


def stage_export(exp: Experiment, args) -> None:
    from drugkg.export import export_all
    from drugkg.postprocess import KGBuilder
    t0 = time.time()
    embedder, schema = _load_schema_for_export(exp)
    merge_path = exp.dir / "schema" / "relation_merge_map.json"
    merge_map = json.loads(merge_path.read_text(encoding="utf-8")) if merge_path.exists() else {}
    pp = exp.cfg.section("postprocess")
    merge_map.update({str(k): str(v) for k, v in (pp.get("relation_merges") or {}).items()})
    builder = KGBuilder(schema, merge_map, int(pp.get("max_entity_chars", 120)), pp.get("drop_relations"),
                        int(pp.get("min_enriched_relation_count", 1)))
    n = 0
    for slug in exp.slugs():
        rec = exp.parsed_record(slug)
        edc_path = exp.dir / "edc" / f"{fname(slug)}.json"
        if rec is None:  # minimal record when no parsed page exists
            chunks = exp.load_chunks(slug)
            rec = {"name": chunks[0]["drug"], "title": chunks[0]["drug"], "slug": slug, "url": chunks[0].get("source_url")}
        if not args.no_structured and exp.parsed_record(slug) is not None:
            builder.add_structured(rec)
        if edc_path.exists():
            builder.add_edc(rec, json.loads(edc_path.read_text(encoding="utf-8")))
            n += 1
    entities, triples = builder.finalize()
    stats = export_all(entities, triples, schema, exp.dir / "kg",
                       meta={"experiment": exp.name, "n_drugs": n, "relation_merges": merge_map, "structured": not args.no_structured})
    log.info("exported %s: %d entities, %d triples, %d relations", exp.name, stats["n_entities"], stats["n_triples"],
             stats["n_relations_used"])
    exp.record("export", time.time() - t0, n_entities=stats["n_entities"], n_triples=stats["n_triples"],
               n_relations=stats["n_relations_used"])


def stage_canon_entities(exp: Experiment, args) -> None:
    """KGGen FULL deduplication applied to the exported KG -> kg_canon/ (+ entity_canon/ cluster files)."""
    from drugkg.entity_canon import kggen_canonicalize
    from drugkg.export import export_all
    from drugkg.llm import build_llm
    t0 = time.time()
    kg = exp.dir / "kg"
    if not (kg / "triples.jsonl").exists():
        raise SystemExit("run --stage export first")
    llm = build_llm(exp.cfg)
    if not llm.ping():
        raise SystemExit("LLM server is not reachable")
    embedder, schema = _load_schema_for_export(exp)
    entities = {e["id"]: e for e in csv.DictReader(open(kg / "entities.csv", encoding="utf-8"))}
    triples = [json.loads(l) for l in (kg / "triples.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    labels = sorted({e["label"] for e in entities.values()})
    edges = sorted({t["relation"] for t in triples})
    ec = exp.cfg.section("entity_canon")
    guarded = args.entity_canon == "kggen_guarded"
    type_map = {e["label"]: e["type"] for e in entities.values()} if guarded else None
    res = kggen_canonicalize(llm, embedder, labels, edges, float(ec.get("semhash_threshold", 0.95)),
                             int(ec.get("cluster_size", 128)), int(ec.get("top_k", 16)), int(ec.get("workers", 16)),
                             canon_edges=not args.no_canon_edges, numeric_guard=bool(ec.get("numeric_guard", True)),
                             type_map=type_map, strict_prompt=guarded)
    out = exp.dir / "entity_canon"
    out.mkdir(exist_ok=True)
    (out / "entity_clusters.json").write_text(json.dumps(res["entity_clusters"], indent=1, ensure_ascii=False), encoding="utf-8")
    (out / "edge_clusters.json").write_text(json.dumps(res["edge_clusters"], indent=1, ensure_ascii=False), encoding="utf-8")
    (out / "entity_map.json").write_text(json.dumps(res["entity_map"], indent=1, ensure_ascii=False), encoding="utf-8")
    (out / "stats.json").write_text(json.dumps(res["stats"], indent=2), encoding="utf-8")
    log.info("KGGen canonicalization: %s", res["stats"])

    # ---- rewrite the KG with representatives (merge triples, re-vote entity types)
    emap, rmap = res["entity_map"], res["edge_map"]
    for rep, members in res["edge_clusters"].items():
        if rep not in schema.relations:  # alias proposed by the LM: inherit the most frequent member's definition/types
            src = max(members, key=lambda m: sum(t["count"] for t in triples if t["relation"] == m))
            r = schema.relations.get(src)
            if r:
                schema.add(rep, r["definition"], r["subject_type"], r["object_type"], origin="kggen-alias", example=r.get("example"))
    new_ents: dict[str, dict] = {}
    votes: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    merged: dict[tuple, dict] = {}
    for t in triples:
        s_lab, o_lab = emap.get(t["subject"], t["subject"]), emap.get(t["object"], t["object"])
        rel = rmap.get(t["relation"], t["relation"])
        if rel not in schema.relations:
            continue
        sid, oid = _eid(s_lab), _eid(o_lab)
        if sid == oid:
            continue
        for eid, lab, typ in ((sid, s_lab, t["subject_type"]), (oid, o_lab, t["object_type"])):
            new_ents.setdefault(eid, {"id": eid, "label": lab, "type": typ, "mentions": 0})
            new_ents[eid]["mentions"] += t["count"]
            votes[eid][typ] += t["count"]
        key = (sid, rel, oid)
        m = merged.get(key)
        if m is None:
            m = merged[key] = {"subject": s_lab, "subject_id": sid, "relation": rel, "object": o_lab, "object_id": oid,
                               "relation_origin": schema.relations[rel]["origin"], "count": 0, "drugs": set(), "sources": set(),
                               "provenance": [], "merged_from": set()}
        m["count"] += t["count"]
        m["drugs"].update(t["drugs"])
        m["sources"].update(t["sources"])
        m["provenance"].extend(t["provenance"][: max(0, 20 - len(m["provenance"]))])
        if t["subject"] != s_lab or t["object"] != o_lab or t["relation"] != rel:
            m["merged_from"].add(f"{t['subject']} | {t['relation']} | {t['object']}")
    for eid, v in votes.items():
        new_ents[eid]["type"] = "Drug" if v.get("Drug") else v.most_common(1)[0][0]
    out_triples = []
    for m in merged.values():
        m["subject_type"], m["object_type"] = new_ents[m["subject_id"]]["type"], new_ents[m["object_id"]]["type"]
        m["drugs"], m["sources"], m["merged_from"] = sorted(m["drugs"]), sorted(m["sources"]), sorted(m["merged_from"])
        out_triples.append(m)
    out_triples.sort(key=lambda x: (x["drugs"][0] if x["drugs"] else "", x["relation"], x["subject"], x["object"]))
    ents = sorted(new_ents.values(), key=lambda e: (-e["mentions"], e["label"]))
    stats = export_all(ents, out_triples, schema, exp.dir / "kg_canon",
                       meta={"experiment": exp.name, "entity_canonicalization": f"KGGen (Mo et al. 2025) FULL{' + guards' if guarded else ''}", **res["stats"]})
    log.info("kg_canon: %d entities, %d triples, %d relations (from %d / %d)", stats["n_entities"], stats["n_triples"],
             stats["n_relations_used"], len(entities), len(triples))
    exp.record("canon_entities", time.time() - t0, **res["stats"], n_entities_out=stats["n_entities"],
               n_triples_out=stats["n_triples"], llm_calls=llm.stats)


def _eid(label: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")[:120] or "x"


def stage_audit(exp: Experiment, args) -> None:
    t0 = time.time()
    py = sys.executable
    for kg, out in (("kg", "audit"), ("kg_canon", "audit_canon")):
        if (exp.dir / kg / "triples.jsonl").exists():
            subprocess.run([py, str(ROOT / "scripts" / "audit_entities.py"), "--kg", str(exp.dir / kg), "--out", str(exp.dir / out),
                            "--quiet"], check=True)
            log.info("audit written to %s", exp.dir / out)
    exp.record("audit", time.time() - t0)


def copy_from(exp: Experiment, src_name: str) -> None:
    src = ROOT / "output" / "experiments" / src_name
    if not (src / "edc").exists():
        raise SystemExit(f"--from-exp {src_name}: no extraction outputs found")
    for sub in ("chunks", "edc", "schema"):
        shutil.rmtree(exp.dir / sub, ignore_errors=True)
        shutil.copytree(src / sub, exp.dir / sub)
    log.info("copied chunks/edc/schema from experiment %s", src_name)
    exp.record("copy_from", 0, source=src_name)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exp", required=True)
    ap.add_argument("--config", default=str(ROOT / "config.yaml"))
    ap.add_argument("--stage", default="all", choices=["prepare", "extract", "consolidate", "export", "canon_entities", "audit", "all"])
    ap.add_argument("--input", default="text", choices=["text", "sentences", "chunks"])
    ap.add_argument("--text-dir", default=None)
    ap.add_argument("--sentences-file", default=None)
    ap.add_argument("--sentence-level", action="store_true", help="one decomposed sentence per chunk")
    ap.add_argument("--drop-incomplete", action="store_true", help="skip 'incomplete_passthrough' sentences")
    ap.add_argument("--from-exp", default=None, help="reuse chunks/edc/schema of another experiment (skips extraction)")
    ap.add_argument("--entity-canon", default="none", choices=["none", "kggen", "kggen_guarded"],
                    help="kggen = KGGen FULL as published; kggen_guarded = + same-type restriction and stricter instruction")
    ap.add_argument("--no-canon-edges", action="store_true", help="KGGen: canonicalize entities only, not relations")
    ap.add_argument("--no-structured", action="store_true", help="do not add structured metadata triples")
    ap.add_argument("--drugs", default="all")
    ap.add_argument("--max-chunks", type=int, default=None)
    ap.add_argument("--iterations", type=int, default=None)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    cfg = Config.load(args.config)
    exp = Experiment(args.exp, cfg)
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format=fmt,
                        handlers=[logging.StreamHandler(), logging.FileHandler(exp.dir / "run.log", encoding="utf-8")])
    for noisy in ("httpx", "httpx2", "urllib3", "sentence_transformers", "openai"):
        logging.getLogger(noisy).setLevel(logging.WARNING)
    (exp.dir / "config_snapshot.yaml").write_text(yaml.safe_dump(cfg.raw, allow_unicode=True), encoding="utf-8")
    log.info("experiment=%s stage=%s input=%s args=%s", exp.name, args.stage, args.input, vars(args))

    run_all = args.stage == "all"
    if args.from_exp and (run_all or args.stage == "prepare"):
        copy_from(exp, args.from_exp)
    elif run_all or args.stage == "prepare":
        stage_prepare(exp, args)
    if (run_all and not args.from_exp) or args.stage == "extract":
        stage_extract(exp, args)
    if (run_all and not args.from_exp) or args.stage == "consolidate":
        stage_consolidate(exp, args)
    if run_all or args.stage == "export":
        stage_export(exp, args)
    if (run_all and args.entity_canon != "none") or args.stage == "canon_entities":
        stage_canon_entities(exp, args)
    if run_all or args.stage == "audit":
        stage_audit(exp, args)


if __name__ == "__main__":
    main()
