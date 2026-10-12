"""Entity (and edge) canonicalization ported from KGGen's "Resolution" stage.

Reference: Mo et al., "KGGen: Extracting Knowledge Graphs from Plain Text with Language Models", arXiv:2502.09956 (2025),
code https://github.com/stair-lab/kg-gen (src/kg_gen/utils/deduplicate.py, llm_deduplicate.py, steps/_3_deduplicate.py).

The FULL method of KGGen is reproduced step by step:
  1. semhash deduplication  : NFKC-normalize, singularize tokens (inflect), SemHash self-deduplicate at cosine >= 0.95
  2. k-means pre-clustering : S-BERT embeddings, k = n // 128, greedy assignment with at most 128 items per cluster
  3. LM deduplication       : for each cluster, pop an item, retrieve its top-16 neighbours with rank fusion
                              (0.5 * BM25 + 0.5 * cosine), ask the LM for exact duplicates + a representative alias,
                              remove the duplicates from the cluster, repeat until the cluster is empty
  4. rewrite every relation (subject, predicate, object) with the representatives.
Deviations from the original code are marked with "NOTE".
"""
from __future__ import annotations
import json
import logging
import re
import unicodedata
from concurrent.futures import ThreadPoolExecutor

import numpy as np

log = logging.getLogger(__name__)

_NUM = re.compile(r"\d+(?:\.\d+)?")


def numbers_differ(a: str, b: str) -> bool:
    """True when the two strings carry different numeric tokens (e.g. '1 mg' vs '5 mg').
    NOTE (deviation from KGGen): dose/strength literals must never be merged on surface similarity alone, so merges
    between strings with different numbers are rejected in both the semhash and the LM step (config: numeric_guard)."""
    return _NUM.findall(a) != _NUM.findall(b)


GUARDED_EXTRA = (" Duplicates must refer to exactly the same real-world thing: different drugs, brand names, ingredients, "
                 "formulations, doses, or a general category versus one of its members are NOT duplicates.")

DEDUP_INSTRUCTIONS = ("Find duplicate {plural} for the item and an alias that best represents the duplicates. Duplicates are "
                      "those that are the same in meaning, such as with variation in tense, plural form, stem form, case, "
                      "abbreviation, shorthand. Return an empty list if there are none.")


# ---------------------------------------------------------------------------------------------- step 1: semhash
class SemHashDedup:
    """Port of kg_gen.utils.deduplicate.DeduplicateList."""

    def __init__(self, threshold: float = 0.95, numeric_guard: bool = True):
        import inflect
        self.threshold = threshold
        self.numeric_guard = numeric_guard
        self.inflect = inflect.engine()
        self.original_map: dict[str, str] = {}   # original -> normalized/singular
        self.items_map: dict[str, str] = {}      # normalized -> representative original
        self.duplicates: dict[str, str] = {}
        self.deduplicated: list[str] = []

    def _singularize(self, text: str) -> str:
        toks = []
        for tok in text.split():
            sing = self.inflect.singular_noun(tok)
            toks.append(sing if isinstance(sing, str) and sing else tok)
        return " ".join(toks).strip()

    def deduplicate(self, items: list[str]) -> dict[str, str]:
        """Return mapping original -> representative original."""
        from semhash import SemHash
        normalized = set()
        for item in items:
            sing = self._singularize(unicodedata.normalize("NFKC", item))
            self.original_map[item] = sing
            self.items_map.setdefault(sing, item)
            normalized.add(sing)
        if not normalized:
            return {}
        result = SemHash.from_records(records=list(normalized)).self_deduplicate(threshold=self.threshold)
        # semhash >= 0.3 exposes the removed records as `filtered` (DuplicateRecord.record / .duplicate_of);
        # older versions (used by KGGen) exposed `duplicates` with a nested list.
        for dup in getattr(result, "filtered", None) or getattr(result, "duplicates", []):
            rep_norm = getattr(dup, "duplicate_of", None)
            if rep_norm is None and getattr(dup, "duplicates", None):
                rep_norm = dup.duplicates[0][0]
            if rep_norm and rep_norm in self.items_map:
                if self.numeric_guard and numbers_differ(dup.record, rep_norm):
                    continue
                self.items_map[dup.record] = self.items_map[rep_norm]
                self.duplicates.setdefault(dup.record, rep_norm)
        self.deduplicated = list(result.selected)
        return {item: self.items_map[self.original_map[item]] for item in items}


# ---------------------------------------------------------------------------------------------- steps 2-3: LM dedup
class LLMDeduplicate:
    """Port of kg_gen.utils.llm_deduplicate.LLMDeduplicate (dspy.Predict replaced by a JSON-answering chat call)."""

    def __init__(self, llm, embedder, nodes: list[str], edges: list[str], cluster_size: int = 128, top_k: int = 16,
                 workers: int = 16, numeric_guard: bool = True, type_map: dict[str, str] | None = None,
                 strict_prompt: bool = False):
        from rank_bm25 import BM25Okapi
        self.llm, self.embedder = llm, embedder
        self.numeric_guard = numeric_guard
        # "guarded" variant (deviation from KGGen): candidates and duplicates restricted to the same entity type,
        # and the instruction is tightened so that distinct drugs/brands/doses are not merged.
        self.type_map = type_map or {}
        self.strict_prompt = strict_prompt
        self.nodes, self.edges = list(nodes), list(edges)
        self.cluster_size, self.top_k, self.workers = cluster_size, top_k, workers
        self.node_emb = embedder.encode(self.nodes) if self.nodes else np.zeros((0, 1))
        self.edge_emb = embedder.encode(self.edges) if self.edges else np.zeros((0, 1))
        self.node_bm25 = BM25Okapi([t.lower().split() for t in self.nodes]) if self.nodes else None
        self.edge_bm25 = BM25Okapi([t.lower().split() for t in self.edges]) if self.edges else None
        self.node_clusters: list[list[str]] = []
        self.edge_clusters: list[list[str]] = []
        self.calls = 0

    # -- retrieval: rank fusion of BM25 and embedding similarity (equal weights), as in KGGen
    def get_relevant_items(self, query: str, kind: str) -> list[str]:
        items = self.nodes if kind == "node" else self.edges
        bm25 = self.node_bm25 if kind == "node" else self.edge_bm25
        emb = self.node_emb if kind == "node" else self.edge_emb
        bm25_scores = bm25.get_scores(query.lower().split())
        q = self.embedder.encode_one(query)
        cos = emb @ q  # embeddings are L2-normalized
        combined = 0.5 * bm25_scores + 0.5 * cos
        order = np.argsort(combined)[::-1]
        if kind == "node" and self.type_map:
            qt = self.type_map.get(query)
            order = [i for i in order if self.type_map.get(items[i]) == qt]
        return [items[i] for i in order[: self.top_k]]

    # -- k-means into clusters of <= cluster_size items (KGGen: init="random", n_init=1, max_iter=20)
    def cluster(self) -> None:
        from scipy.spatial.distance import cdist
        from sklearn.cluster import KMeans
        for kind, emb, items in (("node", self.node_emb, self.nodes), ("edge", self.edge_emb, self.edges)):
            n = len(items)
            if n == 0:
                continue
            k = max(1, n // self.cluster_size)
            if k == 1:
                clusters = [list(range(n))]
            else:
                km = KMeans(n_clusters=k, init="random", n_init=1, max_iter=20, tol=0.0, algorithm="lloyd", random_state=0)
                km.fit(emb.astype(np.float32))
                order = np.argsort(cdist(emb, km.cluster_centers_), axis=1)
                clusters, assigned = [[] for _ in range(k)], np.zeros(n, dtype=bool)
                for rank in range(k):
                    for i in range(n):
                        if not assigned[i] and len(clusters[order[i, rank]]) < self.cluster_size:
                            clusters[order[i, rank]].append(i)
                            assigned[i] = True
                left = np.where(~assigned)[0]
                if len(left):
                    clusters.append(left.tolist())
            named = [[items[i] for i in c] for c in clusters if c]
            if kind == "node":
                self.node_clusters = named
            else:
                self.edge_clusters = named
            log.info("%s k-means: %d items -> %d clusters (sizes %s...)", kind, n, len(named), [len(c) for c in named[:6]])

    def _ask(self, item: str, candidates: list[str], kind: str) -> tuple[list[str], str]:
        plural, singular = ("entities", "entity") if kind == "node" else ("edges", "edge")
        prompt = (DEDUP_INSTRUCTIONS.format(plural=plural) + (GUARDED_EXTRA if self.strict_prompt else "") + "\n\n"
                  f"item: {json.dumps(item, ensure_ascii=False)}\n"
                  f"set: {json.dumps(candidates, ensure_ascii=False)}\n\n"
                  "Respond with a JSON object with exactly these fields:\n"
                  f'  "duplicates": list of exact matches to items in the {plural} set that are duplicates of the item\n'
                  f'  "alias": best {singular} name to represent the duplicates, ideally from the {plural} set\n'
                  "JSON:")
        raw = self.llm.chat(prompt, max_tokens=256)
        self.calls += 1
        try:
            s = raw.strip()
            if s.startswith("```"):
                s = re.sub(r"^```[a-zA-Z]*\n?|```$", "", s).strip()
            l, r = s.find("{"), s.rfind("}")
            data = json.loads(s[l:r + 1])
            dups = [d for d in data.get("duplicates", []) if isinstance(d, str)]
            alias = data.get("alias") if isinstance(data.get("alias"), str) and data.get("alias").strip() else item
            return dups, alias.strip()
        except Exception:
            log.debug("unparseable dedup answer for %r: %r", item, raw[:120])
            return [], item

    def deduplicate_cluster(self, cluster: list[str], kind: str) -> dict[str, set[str]]:
        cluster = cluster.copy()
        item_clusters: dict[str, set[str]] = {}
        while cluster:
            item = cluster.pop()
            relevant = self.get_relevant_items(item, kind)
            dups, alias = self._ask(item, relevant, kind)
            dups = [d for d in dict.fromkeys(dups)  # the LM may list the same string twice
                    if d in cluster and d != item and not (self.numeric_guard and numbers_differ(d, item))
                    and (kind != "node" or not self.type_map or self.type_map.get(d) == self.type_map.get(item))]
            if dups:
                for d in dups:
                    if d in cluster:
                        cluster.remove(d)
                item_clusters.setdefault(alias, set()).update([item, *dups])
            else:
                # NOTE: KGGen adds the returned alias to the entity set even when no duplicates were found;
                # we keep the item itself as its own representative (the relation rewrite behaves identically).
                item_clusters.setdefault(item, set()).add(item)
        return item_clusters

    def deduplicate(self) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
        ent_clusters: dict[str, set[str]] = {}
        edge_clusters: dict[str, set[str]] = {}
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            node_f = [pool.submit(self.deduplicate_cluster, c, "node") for c in self.node_clusters]
            edge_f = [pool.submit(self.deduplicate_cluster, c, "edge") for c in self.edge_clusters]
            for f in node_f:
                for rep, members in f.result().items():
                    ent_clusters.setdefault(rep, set()).update(members)
            for f in edge_f:
                for rep, members in f.result().items():
                    edge_clusters.setdefault(rep, set()).update(members)
        return ent_clusters, edge_clusters


# ---------------------------------------------------------------------------------------------- driver
def _resolve_chain(mapping: dict[str, str]) -> dict[str, str]:
    out = {}
    for k in mapping:
        v, seen = mapping[k], {k}
        while v in mapping and mapping[v] != v and v not in seen:
            seen.add(v)
            v = mapping[v]
        out[k] = v
    return out


def kggen_canonicalize(llm, embedder, entities: list[str], edges: list[str], semhash_threshold: float = 0.95,
                       cluster_size: int = 128, top_k: int = 16, workers: int = 16, canon_edges: bool = True,
                       numeric_guard: bool = True, type_map: dict[str, str] | None = None, strict_prompt: bool = False) -> dict:
    """Run KGGen FULL deduplication. Returns {'entity_map': {label -> representative}, 'edge_map': {...}, 'stats': {...},
    'entity_clusters': {rep -> [members]}, 'edge_clusters': {...}}."""
    stats = {"n_entities_in": len(entities), "n_edges_in": len(edges), "numeric_guard": numeric_guard,
             "type_guard": bool(type_map), "strict_prompt": strict_prompt}
    # step 1: semhash
    sh_e = SemHashDedup(semhash_threshold, numeric_guard)
    ent_map1 = sh_e.deduplicate(entities)
    if type_map:  # guarded variant: undo semhash merges across entity types
        ent_map1 = {e: (r if type_map.get(r) == type_map.get(e) else e) for e, r in ent_map1.items()}
    stats["entities_after_semhash"] = len(set(ent_map1.values()))
    if canon_edges and edges:
        sh_r = SemHashDedup(semhash_threshold, numeric_guard)
        edge_map1 = sh_r.deduplicate(edges)
    else:
        edge_map1 = {e: e for e in edges}
    stats["edges_after_semhash"] = len(set(edge_map1.values()))
    log.info("semhash: entities %d -> %d, edges %d -> %d", len(entities), stats["entities_after_semhash"], len(edges),
             stats["edges_after_semhash"])
    # steps 2-3: k-means + LM dedup on the semhash survivors
    nodes = sorted(set(ent_map1.values()))
    edge_items = sorted(set(edge_map1.values())) if canon_edges else []
    lm = LLMDeduplicate(llm, embedder, nodes, edge_items, cluster_size, top_k, workers, numeric_guard,
                        type_map={n: type_map.get(n) for n in nodes} if type_map else None, strict_prompt=strict_prompt)
    lm.cluster()
    ent_clusters, edge_clusters = lm.deduplicate()
    ent_map2 = {m: rep for rep, ms in ent_clusters.items() for m in ms}
    edge_map2 = {m: rep for rep, ms in edge_clusters.items() for m in ms}
    entity_map = _resolve_chain({e: ent_map2.get(ent_map1[e], ent_map1[e]) for e in entities})
    edge_map = _resolve_chain({e: edge_map2.get(edge_map1[e], edge_map1[e]) for e in edges})
    stats.update({"entities_after_lm": len(set(entity_map.values())), "edges_after_lm": len(set(edge_map.values())),
                  "lm_calls": lm.calls, "n_node_clusters": len(lm.node_clusters), "n_edge_clusters": len(lm.edge_clusters)})
    inv_e: dict[str, list[str]] = {}
    for k, v in entity_map.items():
        inv_e.setdefault(v, []).append(k)
    inv_r: dict[str, list[str]] = {}
    for k, v in edge_map.items():
        inv_r.setdefault(v, []).append(k)
    return {"entity_map": entity_map, "edge_map": edge_map, "stats": stats,
            "entity_clusters": {k: sorted(v) for k, v in inv_e.items() if len(v) > 1},
            "edge_clusters": {k: sorted(v) for k, v in inv_r.items() if len(v) > 1}}
