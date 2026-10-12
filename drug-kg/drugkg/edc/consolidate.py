"""Post-hoc schema consolidation: merge near-duplicate enriched relations (embedding similarity + LLM yes/no)."""
from __future__ import annotations
import logging

from .prompts import Prompts
from .schema import Schema

log = logging.getLogger(__name__)


def consolidate_schema(schema: Schema, llm, prompts: Prompts, sim_threshold: float = 0.80, top_k: int = 5) -> dict[str, str]:
    """Return a mapping {relation -> canonical relation} for relations that should be merged."""
    merge_map: dict[str, str] = {}
    enriched = [n for n, r in schema.relations.items() if r["origin"] != "seed"]
    enriched.sort(key=lambda n: schema.relations[n]["count"])  # rare relations first
    for rel in enriched:
        info = schema.relations[rel]
        cands = [(c, s) for c, s in schema.retrieve(info["definition"], top_k + 1, exclude={rel}) if s >= sim_threshold]
        cands = [(c, s) for c, s in cands if c not in merge_map]  # don't merge into something already merged away
        cands.sort(key=lambda cs: (-(schema.relations[cs[0]]["origin"] == "seed"), -cs[1]))
        for cand, score in cands[:top_k]:
            if schema.relations[cand]["count"] < info["count"] and schema.relations[cand]["origin"] != "seed":
                continue
            prompt = prompts.merge_prompt(rel, info["definition"], info.get("example"), cand,
                                          schema.relations[cand]["definition"], schema.relations[cand].get("example"))
            ans = llm.chat(prompt, max_tokens=3).strip().lower()
            if ans.startswith("yes"):
                merge_map[rel] = cand
                log.info("merge '%s' -> '%s' (sim %.3f)", rel, cand, score)
                break
    # resolve chains a->b->c
    for k in list(merge_map):
        seen = {k}
        v = merge_map[k]
        while v in merge_map and v not in seen:
            seen.add(v)
            v = merge_map[v]
        merge_map[k] = v
    return merge_map
