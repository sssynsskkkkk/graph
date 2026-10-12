"""Schema canonicalization: embedding retrieval over relation definitions + LLM verification (+ enrichment)."""
from __future__ import annotations
import logging
import re

from .parsing import normalize_relation
from .schema import ENTITY_TYPES, Schema
from .prompts import Prompts

log = logging.getLogger(__name__)


def _loose_equal(a: str, b: str) -> bool:
    strip = lambda s: re.sub(r"^(has|is|was)\s+", "", s).replace(" ", "")
    return a == b or strip(a) == strip(b)


class SchemaCanonicalizer:
    def __init__(self, schema: Schema, llm, prompts: Prompts, top_k: int = 5, auto_accept_sim: float = 0.97,
                 new_relation_merge_sim: float = 0.80, enrich: bool = True):
        self.schema = schema
        self.llm = llm
        self.prompts = prompts
        self.top_k = top_k
        self.auto_accept_sim = auto_accept_sim
        self.merge_sim = new_relation_merge_sim
        self.enrich = enrich

    # ------------------------------------------------------------------ helpers
    def _parse_choice(self, answer: str, letters: list[str], cand_names: list[str]) -> str | None:
        m = re.search(r"\b([A-Z])\b", answer.strip()[:10])
        if not m:
            return None
        letter = m.group(1)
        if letter in letters:
            return cand_names[letters.index(letter)]
        return None

    def _infer_types(self, relation: str, definition: str, example) -> tuple[str, str]:
        ans = self.llm.chat(self.prompts.type_prompt(relation, definition, example), max_tokens=40)
        st, ot = "Drug", "Other"
        for line in ans.splitlines():
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            v = v.strip().strip("'\"`.")
            match = next((t for t in ENTITY_TYPES if t.lower() == v.lower()), None)
            if "subject" in k.lower() and match:
                st = match
            elif "object" in k.lower() and match:
                ot = match
        return st, ot

    # ------------------------------------------------------------------ main
    def canonicalize_batch(self, items: list[dict]) -> list[dict]:
        """items: [{chunk_text, triplet, definitions}] -> per-item result dicts.

        Stage A: relations already in the schema are canonical (direct).
        Stage B: otherwise retrieve top-k candidates by definition embedding and ask the LLM (parallel).
        Stage C: relations rejected by the LLM are added to the schema (enrich) sequentially, with a check
                 against relations added earlier in the same batch to avoid near-duplicates.
        """
        results: list[dict | None] = [None] * len(items)
        verify_jobs = []  # (idx, prompt, letters, cand_names, cands_with_scores)
        for i, it in enumerate(items):
            trip = it["triplet"]
            rel = normalize_relation(trip[1])
            trip[1] = rel
            definition = it["definitions"].get(rel)
            if rel in self.schema:
                results[i] = {"canonical": rel, "status": "direct", "candidates": []}
                continue
            if not definition:
                definition = f"The subject entity {rel} the object entity."
                it["no_definition"] = True
            it["definition"] = definition
            cands = self.schema.retrieve(definition, self.top_k)
            if cands and cands[0][1] >= self.auto_accept_sim and _loose_equal(cands[0][0], rel):
                results[i] = {"canonical": cands[0][0], "status": "auto", "candidates": cands}
                continue
            if not cands:
                results[i] = {"canonical": None, "status": "pending", "candidates": []}
                continue
            prompt, letters = self.prompts.sc_prompt(it["chunk_text"], trip, definition,
                                                     [(c, self.schema.definition(c)) for c, _ in cands])
            verify_jobs.append((i, prompt, letters, [c for c, _ in cands], cands))

        answers = self.llm.chat_many([j[1] for j in verify_jobs], max_tokens=5, desc="canonicalize") if verify_jobs else []
        pending: list[int] = [i for i, r in enumerate(results) if r is not None and r["status"] == "pending"]
        for (i, _, letters, cand_names, cands), ans in zip(verify_jobs, answers):
            chosen = self._parse_choice(ans, letters, cand_names)
            if chosen:
                results[i] = {"canonical": chosen, "status": "mapped", "candidates": cands, "answer": ans}
            else:
                results[i] = {"canonical": None, "status": "pending", "candidates": cands, "answer": ans}
                pending.append(i)

        new_in_batch: set[str] = set()
        for i in sorted(pending):
            it = items[i]
            rel = it["triplet"][1]
            definition = it["definition"]
            if rel in self.schema:  # added earlier in this batch (or identical name)
                results[i].update({"canonical": rel, "status": "direct"})
            else:
                merged = None
                if new_in_batch:
                    near = [(c, s) for c, s in self.schema.retrieve(definition, self.top_k, restrict_to=new_in_batch)
                            if s >= self.merge_sim]
                    if near:
                        prompt, letters = self.prompts.sc_prompt(it["chunk_text"], it["triplet"], definition,
                                                                 [(c, self.schema.definition(c)) for c, _ in near])
                        merged = self._parse_choice(self.llm.chat(prompt, max_tokens=5), letters, [c for c, _ in near])
                if merged:
                    results[i].update({"canonical": merged, "status": "mapped_new"})
                elif self.enrich:
                    st, ot = self._infer_types(rel, definition, it["triplet"])
                    self.schema.add(rel, definition, st, ot, origin="enriched", example=it["triplet"])
                    new_in_batch.add(rel)
                    results[i].update({"canonical": rel, "status": "enriched"})
                else:
                    results[i].update({"canonical": None, "status": "dropped"})
        for r in results:
            if r and r.get("canonical"):
                self.schema.bump(r["canonical"])
        return results  # type: ignore[return-value]
