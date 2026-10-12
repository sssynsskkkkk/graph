"""EDC orchestration per drug: Extract -> Define -> Canonicalize (+ optional refinement iterations, EDC+R)."""
from __future__ import annotations
import json
import logging

from .canonicalize import SchemaCanonicalizer
from .parsing import normalize_relation, parse_raw_entities, parse_raw_triplets, parse_relation_definition
from .prompts import Prompts
from .retriever import SchemaRetriever
from .schema import Schema

log = logging.getLogger(__name__)


class EDCFramework:
    def __init__(self, cfg, llm, schema: Schema, prompts: Prompts | None = None):
        edc = cfg.section("edc")
        self.llm = llm
        self.schema = schema
        self.prompts = prompts or Prompts()
        self.iterations = int(edc.get("refinement_iterations", 0))
        self.canonicalizer = SchemaCanonicalizer(schema, llm, self.prompts, top_k=int(edc.get("top_k_candidates", 5)),
                                                 auto_accept_sim=float(edc.get("auto_accept_sim", 0.97)),
                                                 new_relation_merge_sim=float(edc.get("new_relation_merge_sim", 0.8)),
                                                 enrich=bool(edc.get("enrich_schema", True)))
        self.retriever = SchemaRetriever(schema, top_k=int(edc.get("relation_hint_top_k", 10)))

    # ------------------------------------------------------------------ Extract
    def extract(self, chunks: list[dict], entity_hints: list[list[str]] | None = None,
                relation_hints: list[str] | None = None) -> tuple[list[list[list[str]]], list[str]]:
        if entity_hints is None:
            prompts = [self.prompts.oie_prompt(c) for c in chunks]
        else:
            prompts = [self.prompts.oie_refine_prompt(c, eh, rh) for c, eh, rh in zip(chunks, entity_hints, relation_hints)]
        raws = self.llm.chat_many(prompts, desc="extract")
        return [parse_raw_triplets(r) for r in raws], raws

    # ------------------------------------------------------------------ Define
    def define(self, chunks: list[dict], triplets_list: list[list[list[str]]]) -> list[dict[str, str]]:
        idx = [i for i, t in enumerate(triplets_list) if t]
        prompts = [self.prompts.sd_prompt(chunks[i], triplets_list[i]) for i in idx]
        raws = self.llm.chat_many(prompts, desc="define")
        defs: list[dict[str, str]] = [{} for _ in chunks]
        for i, raw in zip(idx, raws):
            defs[i] = parse_relation_definition(raw)
            missing = {normalize_relation(t[1]) for t in triplets_list[i]} - set(defs[i])
            if missing:
                log.debug("chunk %s: no definition for %s", chunks[i]["chunk_id"], sorted(missing))
        return defs

    # ------------------------------------------------------------------ Canonicalize
    def canonicalize(self, chunks: list[dict], triplets_list, defs_list) -> list[list[dict]]:
        items, owners = [], []
        for ci, (chunk, trips, defs) in enumerate(zip(chunks, triplets_list, defs_list)):
            for t in trips:
                items.append({"chunk_text": chunk["text"], "triplet": list(t), "definitions": defs})
                owners.append(ci)
        results = self.canonicalizer.canonicalize_batch(items) if items else []
        grouped: list[list[dict]] = [[] for _ in chunks]
        for it, res, ci in zip(items, results, owners):
            s, r, o = it["triplet"]
            grouped[ci].append({"triplet": [s, res["canonical"], o] if res["canonical"] else None,
                                "raw_relation": r, "definition": it.get("definition") or it["definitions"].get(r),
                                "status": res["status"], "candidates": [[c, round(sc, 4)] for c, sc in res.get("candidates", [])],
                                "answer": res.get("answer")})
        return grouped

    # ------------------------------------------------------------------ Refinement hints (EDC+R)
    def refinement_hints(self, chunks: list[dict], prev_canon: list[list[dict]]) -> tuple[list[list[str]], list[str]]:
        ee_raws = self.llm.chat_many([self.prompts.ee_prompt(c) for c in chunks], desc="entities")
        extracted = [parse_raw_entities(r) for r in ee_raws]
        prev_entities, prev_relations = [], []
        for res in prev_canon:
            ents, rels = [], []
            for r in res:
                if r["triplet"]:
                    ents.extend([r["triplet"][0], r["triplet"][2]])
                    rels.append(r["triplet"][1])
            prev_entities.append(list(dict.fromkeys(ents)))
            prev_relations.append(list(dict.fromkeys(rels)))
        em_raws = self.llm.chat_many([self.prompts.em_prompt(c, pe, ex) for c, pe, ex in zip(chunks, prev_entities, extracted)],
                                     desc="merge-entities")
        entity_hints = []
        for raw, pe, ex in zip(em_raws, prev_entities, extracted):
            merged = parse_raw_entities(raw) or list(dict.fromkeys(pe + ex))
            entity_hints.append(merged)
        relation_hints = []
        for chunk, rels in zip(chunks, prev_relations):
            hint_rels = list(rels)
            for r in self.retriever.retrieve(chunk["text"]):
                if r not in hint_rels:
                    hint_rels.append(r)
                if len(hint_rels) >= self.retriever.top_k:
                    break
            lines = []
            for i, r in enumerate(hint_rels):
                if r not in self.schema:
                    continue
                info = self.schema.relations[r]
                line = f"{i + 1}. {r}: {info['definition']}"
                if info.get("example"):
                    line += f"\nFor example, {json.dumps(info['example'], ensure_ascii=False)}"
                lines.append(line)
            relation_hints.append("\n".join(lines))
        return entity_hints, relation_hints

    # ------------------------------------------------------------------ Per-drug driver
    def run_drug(self, chunks: list[dict]) -> dict:
        iterations_out = []
        prev_canon: list[list[dict]] | None = None
        for it in range(self.iterations + 1):
            if it == 0:
                trips, raws = self.extract(chunks)
                ent_hints, rel_hints = None, None
            else:
                ent_hints, rel_hints = self.refinement_hints(chunks, prev_canon)
                trips, raws = self.extract(chunks, ent_hints, rel_hints)
            defs = self.define(chunks, trips)
            canon = self.canonicalize(chunks, trips, defs)
            per_chunk = []
            for i, c in enumerate(chunks):
                per_chunk.append({"chunk_id": c["chunk_id"], "section_id": c["section_id"], "section_heading": c["section_heading"],
                                  "text": c["text"], "entity_hint": ent_hints[i] if ent_hints else None,
                                  "relation_hint": rel_hints[i] if rel_hints else None, "oie_raw": raws[i], "oie": trips[i],
                                  "schema_definition": defs[i], "schema_canonicalization": canon[i]})
            iterations_out.append({"iteration": it, "chunks": per_chunk})
            prev_canon = canon
            n_trip = sum(len(t) for t in trips)
            n_can = sum(1 for cc in canon for r in cc if r["triplet"])
            log.info("iteration %d: %d chunks, %d open triplets, %d canonical triplets, schema size %d",
                     it, len(chunks), n_trip, n_can, len(self.schema))
        final = []
        for c, res in zip(chunks, prev_canon or []):
            for r in res:
                if r["triplet"]:
                    final.append({"chunk_id": c["chunk_id"], "section_id": c["section_id"], "triplet": r["triplet"],
                                  "raw_relation": r["raw_relation"], "status": r["status"]})
        return {"iterations": iterations_out, "final_triplets": final}
