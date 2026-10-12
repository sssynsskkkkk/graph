#!/usr/bin/env python
"""End-to-end pipeline: fetch Drugs.com pages -> parse/chunk -> EDC extraction -> schema consolidation -> KG export.

Examples
  python run_pipeline.py --stage all                       # everything, all 50 drugs
  python run_pipeline.py --stage parse --dry-run           # chunk statistics only (no LLM)
  python run_pipeline.py --stage extract --drugs 3 --max-chunks 4   # quick pilot on the first 3 drugs
  python run_pipeline.py --stage extract --drugs metformin,lisinopril --force
"""
from __future__ import annotations
import argparse
import json
import logging
import pathlib
import sys
import time

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from drugkg.config import ROOT, Config  # noqa: E402
from drugkg.chunk import chunk_record  # noqa: E402
from drugkg.parse import parse_main_page, parse_subpage  # noqa: E402
from drugkg.scrape import PAGE_PATHS, PoliteFetcher, fetch_drug_pages, resolve_drug_urls  # noqa: E402

log = logging.getLogger("drugkg")


def setup_logging(out_dir: pathlib.Path, verbose: bool) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO, format=fmt,
                        handlers=[logging.StreamHandler(), logging.FileHandler(out_dir / "pipeline.log", encoding="utf-8")])
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpx2").setLevel(logging.WARNING)
    logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def load_drugs(cfg: Config, selector: str | None) -> list[dict]:
    data = yaml.safe_load((ROOT / "drugs" / "top50.yaml").read_text(encoding="utf-8"))
    drugs = data["drugs"]
    if not selector or selector == "all":
        return drugs
    if selector.isdigit():
        return drugs[: int(selector)]
    wanted = {s.strip().lower() for s in selector.split(",") if s.strip()}
    return [d for d in drugs if d["name"].lower() in wanted or (d.get("slug") or "").lower() in wanted
            or d["name"].lower().replace(" ", "-") in wanted]


def fname(slug: str) -> str:
    """File-system safe name for a slug such as 'mtm/ergocalciferol'."""
    return slug.replace("/", "__")


def url_map(cfg: Config) -> dict:
    p = cfg.path("scrape.url_map")
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


# ---------------------------------------------------------------------- stages
def stage_fetch(cfg: Config, drugs: list[dict]) -> None:
    sc = cfg.section("scrape")
    fetcher = PoliteFetcher(cfg.path("scrape.raw_dir"), tuple(sc.get("delay_range", (6, 10))), int(sc.get("max_retries", 4)))
    umap = resolve_drug_urls(drugs, fetcher, cfg.path("scrape.url_map"))
    for d in drugs:
        slug = umap.get(d["name"], {}).get("slug")
        if not slug:
            continue
        pages = fetch_drug_pages(slug, list(sc.get("pages", ["main"])), fetcher)
        log.info("%s: pages %s", d["name"], sorted(pages))


def stage_parse(cfg: Config, drugs: list[dict], dry_run: bool = False) -> list[dict]:
    sc, ch = cfg.section("scrape"), cfg.section("chunking")
    raw_dir, parsed_dir, chunk_dir = cfg.path("scrape.raw_dir"), ROOT / "data" / "parsed", ROOT / "data" / "chunks"
    parsed_dir.mkdir(parents=True, exist_ok=True)
    chunk_dir.mkdir(parents=True, exist_ok=True)
    umap = url_map(cfg)
    records, total_chunks = [], 0
    for d in drugs:
        info = umap.get(d["name"]) or {}
        slug = info.get("slug")
        if not slug:
            log.warning("%s: no resolved URL (run --stage fetch first)", d["name"])
            continue
        main_html = raw_dir / PoliteFetcher.cache_name(PAGE_PATHS["main"].format(slug=slug))
        if not main_html.exists():
            log.warning("%s: raw html missing (%s)", d["name"], main_html)
            continue
        record = parse_main_page(main_html.read_text(encoding="utf-8"), info.get("url"), d["name"], slug)
        record["rank"] = d.get("rank")
        for page in sc.get("pages", ["main"]):
            if page == "main":
                continue
            p = raw_dir / PoliteFetcher.cache_name(PAGE_PATHS[page].format(slug=slug))
            if p.exists():
                record["sections"].extend(parse_subpage(p.read_text(encoding="utf-8"), page))
        chunks = chunk_record(record, int(ch.get("max_chars", 1100)), int(ch.get("min_chars", 150)),
                              ch.get("include_sections"), bool(ch.get("include_unlisted_sections", True)),
                              ch.get("exclude_sections"))
        (parsed_dir / f"{fname(slug)}.json").write_text(json.dumps(record, indent=1, ensure_ascii=False), encoding="utf-8")
        with open(chunk_dir / f"{fname(slug)}.jsonl", "w", encoding="utf-8") as f:
            for c in chunks:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        total_chunks += len(chunks)
        log.info("%s (%s): %d sections, %d chunks, %d chars", d["name"], slug, len(record["sections"]), len(chunks),
                 sum(len(c["text"]) for c in chunks))
        records.append(record)
    log.info("parsed %d drugs, %d chunks total", len(records), total_chunks)
    return records


def build_edc(cfg: Config, schema_path: pathlib.Path | None = None):
    from drugkg.edc.framework import EDCFramework
    from drugkg.edc.schema import Embedder, Schema
    from drugkg.llm import build_llm
    llm = build_llm(cfg)
    if not llm.ping():
        raise SystemExit("LLM server is not reachable. Start it with: bash scripts/serve_vllm.sh")
    emb_cfg = cfg.section("embedder")
    embedder = Embedder(emb_cfg.get("model", "BAAI/bge-base-en-v1.5"), emb_cfg.get("device", "cpu"))
    schema_dir = cfg.path("output.schema_dir")
    live = schema_dir / "schema.csv"
    if schema_path is None:
        schema_path = live if live.exists() else cfg.path("edc.schema_path")
    schema = Schema.load(schema_path, embedder, default_origin="seed")
    return llm, embedder, schema, EDCFramework(cfg, llm, schema)


def stage_extract(cfg: Config, drugs: list[dict], max_chunks: int | None, force: bool, iterations: int | None) -> None:
    if iterations is not None:
        cfg.raw.setdefault("edc", {})["refinement_iterations"] = iterations
    llm, embedder, schema, edc = build_edc(cfg)
    edc_dir, schema_dir, chunk_dir = cfg.path("output.edc_dir"), cfg.path("output.schema_dir"), ROOT / "data" / "chunks"
    edc_dir.mkdir(parents=True, exist_ok=True)
    umap = url_map(cfg)
    for d in drugs:
        slug = (umap.get(d["name"]) or {}).get("slug")
        if not slug or not (chunk_dir / f"{fname(slug)}.jsonl").exists():
            log.warning("%s: no chunks; run --stage parse first", d["name"])
            continue
        out = edc_dir / f"{fname(slug)}.json"
        if out.exists() and not force:
            log.info("%s: already extracted (use --force to redo)", d["name"])
            continue
        chunks = [json.loads(l) for l in (chunk_dir / f"{fname(slug)}.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
        if max_chunks:
            chunks = chunks[:max_chunks]
        t0 = time.time()
        log.info("=== %s (%s): %d chunks", d["name"], slug, len(chunks))
        result = edc.run_drug(chunks)
        result.update({"name": d["name"], "slug": slug, "n_chunks": len(chunks), "seconds": round(time.time() - t0, 1),
                       "llm_model": llm.model})
        out.write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
        schema.save(schema_dir / "schema.csv")
        log.info("%s: %d final triplets in %.0fs; schema now %d relations; llm stats %s", d["name"],
                 len(result["final_triplets"]), time.time() - t0, len(schema), llm.stats)


def stage_consolidate(cfg: Config) -> None:
    from drugkg.edc.consolidate import consolidate_schema
    from drugkg.edc.prompts import Prompts
    llm, embedder, schema, _ = build_edc(cfg)
    schema_dir = cfg.path("output.schema_dir")
    edc_cfg = cfg.section("edc")
    merge_map = {}
    if edc_cfg.get("consolidate_schema", True):
        merge_map = consolidate_schema(schema, llm, Prompts(), float(edc_cfg.get("consolidate_sim", 0.88)))
    (schema_dir / "relation_merge_map.json").write_text(json.dumps(merge_map, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("consolidation: %d relations merged (%s)", len(merge_map), schema_dir / "relation_merge_map.json")


def stage_export(cfg: Config, drugs: list[dict]) -> None:
    from drugkg.edc.schema import Embedder, Schema
    from drugkg.export import export_all
    from drugkg.postprocess import KGBuilder
    schema_dir, edc_dir, parsed_dir = cfg.path("output.schema_dir"), cfg.path("output.edc_dir"), ROOT / "data" / "parsed"
    emb_cfg = cfg.section("embedder")
    schema_path = schema_dir / "schema.csv" if (schema_dir / "schema.csv").exists() else cfg.path("edc.schema_path")
    schema = Schema.load(schema_path, Embedder(emb_cfg.get("model"), emb_cfg.get("device", "cpu")))
    merge_path = schema_dir / "relation_merge_map.json"
    merge_map = json.loads(merge_path.read_text(encoding="utf-8")) if merge_path.exists() else {}
    pp = cfg.section("postprocess")
    merge_map.update({str(k): str(v) for k, v in (pp.get("relation_merges") or {}).items()})
    builder = KGBuilder(schema, merge_map, int(pp.get("max_entity_chars", 120)), pp.get("drop_relations"),
                        int(pp.get("min_enriched_relation_count", 1)))
    umap = url_map(cfg)
    n_drugs = 0
    for d in drugs:
        slug = (umap.get(d["name"]) or {}).get("slug")
        if not slug or not (parsed_dir / f"{fname(slug)}.json").exists():
            continue
        record = json.loads((parsed_dir / f"{fname(slug)}.json").read_text(encoding="utf-8"))
        builder.add_structured(record)
        if (edc_dir / f"{fname(slug)}.json").exists():
            builder.add_edc(record, json.loads((edc_dir / f"{fname(slug)}.json").read_text(encoding="utf-8")))
        else:
            log.warning("%s: no EDC output yet; only structured triples included", d["name"])
        n_drugs += 1
    entities, triples = builder.finalize()
    stats = export_all(entities, triples, schema, cfg.path("output.kg_dir"),
                       meta={"n_drugs": n_drugs, "relation_merges": merge_map, "source": "https://www.drugs.com/"})
    log.info("exported KG: %d entities, %d triples, %d relations -> %s", stats["n_entities"], stats["n_triples"],
             stats["n_relations_used"], cfg.path("output.kg_dir"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=str(ROOT / "config.yaml"))
    ap.add_argument("--stage", default="all", choices=["fetch", "parse", "extract", "consolidate", "export", "all"])
    ap.add_argument("--drugs", default="all", help="'all', a count (e.g. 5), or comma-separated names/slugs")
    ap.add_argument("--max-chunks", type=int, default=None, help="limit chunks per drug (pilot runs)")
    ap.add_argument("--iterations", type=int, default=None, help="override edc.refinement_iterations")
    ap.add_argument("--force", action="store_true", help="re-run extraction for drugs that already have output")
    ap.add_argument("--dry-run", action="store_true", help="parse stage: only report chunk statistics")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    cfg = Config.load(args.config)
    setup_logging(cfg.path("output.dir"), args.verbose)
    drugs = load_drugs(cfg, args.drugs)
    log.info("stage=%s drugs=%d", args.stage, len(drugs))
    if args.stage in ("fetch", "all"):
        stage_fetch(cfg, drugs)
    if args.stage in ("parse", "all"):
        stage_parse(cfg, drugs, args.dry_run)
        if args.dry_run:
            return
    if args.stage in ("extract", "all"):
        stage_extract(cfg, drugs, args.max_chunks, args.force, args.iterations)
    if args.stage in ("consolidate", "all"):
        stage_consolidate(cfg)
    if args.stage in ("export", "all"):
        stage_export(cfg, drugs)


if __name__ == "__main__":
    main()
