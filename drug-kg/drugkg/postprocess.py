"""Turn per-drug EDC results + page metadata into a deduplicated, typed knowledge graph."""
from __future__ import annotations
import re
from collections import Counter, defaultdict

PRONOUNS = {"this medicine", "this medication", "this drug", "the medicine", "the medication", "the drug", "it", "medicine",
            "medication", "this product", "the product", "drug", "this"}
ARTICLES = re.compile(r"^(the|a|an)\s+", re.I)
TYPE_PRIORITY = ["Drug", "DrugClass", "Condition", "SideEffect", "Symptom", "Substance", "Ingredient"]


QUOTES = "'\"`“”‘’"


def clean_label(text: str) -> str:
    t = re.sub(r"\s+", " ", str(text)).strip().strip(QUOTES).strip()
    if t.startswith("(") and t.endswith(")"):
        t = t[1:-1].strip()
    prev = None
    while prev != t:
        prev = t
        t = ARTICLES.sub("", t).strip().strip(QUOTES).rstrip(".;,:").strip()
    return t


def entity_key(text: str) -> str:
    return clean_label(text).lower()


def canonical_drug_label(record: dict) -> str:
    """Page title without a trailing parenthetical, e.g. 'Hydrochlorothiazide (HCTZ)' -> 'Hydrochlorothiazide'."""
    title = record.get("title") or record.get("name") or ""
    return re.sub(r"\s*\([^)]*\)\s*$", "", title).strip() or title


def entity_id(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", key).strip("_")[:120]


def drug_alias_keys(record: dict) -> set[str]:
    title = record.get("title") or ""
    aliases = {title, canonical_drug_label(record), record.get("name") or "", (record.get("slug") or "").replace("-", " ")}
    aliases |= set(re.findall(r"\(([^)]*)\)", title))  # abbreviations such as HCTZ
    aliases |= {f"{a} tablets" for a in list(aliases)} | {f"{a} tablet" for a in list(aliases)}
    return {entity_key(a) for a in aliases if a} | PRONOUNS


class KGBuilder:
    def __init__(self, schema, merge_map: dict[str, str] | None = None, max_entity_chars: int = 120,
                 drop_relations: list[str] | None = None, min_enriched_relation_count: int = 1):
        self.schema = schema
        self.merge_map = merge_map or {}
        self.max_entity_chars = max_entity_chars
        self.drop_relations = set(drop_relations or [])
        self.min_enriched_count = max(1, int(min_enriched_relation_count))
        self.entities: dict[str, dict] = {}
        self.triples: dict[tuple, dict] = {}
        self._type_votes: dict[str, Counter] = defaultdict(Counter)

    # ------------------------------------------------------------------ entities
    def _entity(self, text: str, etype: str, aliases: set[str], canonical_label: str) -> str | None:
        key = entity_key(text)
        if not key or len(key) > self.max_entity_chars:
            return None
        if key in aliases:
            key, text, etype = entity_key(canonical_label), canonical_label, "Drug"
        eid = entity_id(key)
        if not eid:
            return None
        ent = self.entities.get(eid)
        if ent is None:
            label = clean_label(text) or key
            ent = self.entities[eid] = {"id": eid, "label": label, "type": etype, "mentions": 0}
        ent["mentions"] += 1
        self._type_votes[eid][etype] += 1
        return eid

    def _add(self, s_text, rel, o_text, drug_slug: str, prov: dict, aliases: set[str], canonical_label: str) -> None:
        rel = self.merge_map.get(rel, rel)
        if rel in self.drop_relations or rel not in self.schema.relations:
            return
        info = self.schema.relations[rel]
        sid = self._entity(s_text, info["subject_type"], aliases, canonical_label)
        oid = self._entity(o_text, info["object_type"], aliases, canonical_label)
        if not sid or not oid or sid == oid:
            return
        key = (sid, rel, oid)
        t = self.triples.get(key)
        if t is None:
            t = self.triples[key] = {"subject_id": sid, "relation": rel, "object_id": oid, "count": 0, "drugs": set(),
                                     "sources": set(), "provenance": []}
        t["count"] += 1
        t["drugs"].add(drug_slug)
        t["sources"].add(prov.get("source", "edc"))
        if len(t["provenance"]) < 20:
            t["provenance"].append(prov)

    # ------------------------------------------------------------------ inputs
    def add_structured(self, record: dict) -> None:
        """High-precision triples from page metadata (subtitle block, info box, related-drug carousel)."""
        label = canonical_drug_label(record)
        aliases = drug_alias_keys(record)
        prov = {"source": "structured", "drug": record["slug"], "url": record.get("url")}
        add = lambda r, o: self._add(label, r, o, record["slug"], prov, aliases, label)
        gen = record.get("generic_name")
        if gen and entity_key(gen) != entity_key(label):
            add("has generic name", gen)
        for b in record.get("brand_names") or []:
            if entity_key(b) != entity_key(label):
                add("has brand name", b)
        for dc in record.get("drug_classes") or []:
            add("belongs to drug class", dc["name"])
        for df in record.get("dosage_forms") or []:
            add("has dosage form", df["form"])
            for s in df.get("strengths") or []:
                add("has strength", s)
        for rd in record.get("related_drugs") or []:
            add("similar to", rd["name"])
        if record.get("fda_approval_year"):
            add("fda approval year", record["fda_approval_year"])
        csa = record.get("csa_schedule") or ""
        if csa and "not a controlled" not in csa.lower() and "n/a" not in csa.lower():
            add("has controlled substance schedule", csa)
        if record.get("availability"):
            add("has availability", record["availability"])

    def add_edc(self, record: dict, edc_result: dict, iteration: int | None = None) -> None:
        label = canonical_drug_label(record)
        aliases = drug_alias_keys(record)
        for ft in edc_result["final_triplets"]:
            s, r, o = ft["triplet"]
            prov = {"source": "edc", "drug": record["slug"], "chunk_id": ft["chunk_id"], "section": ft["section_id"],
                    "raw_relation": ft["raw_relation"], "status": ft["status"], "url": record.get("url")}
            self._add(s, r, o, record["slug"], prov, aliases, label)

    # ------------------------------------------------------------------ output
    def finalize(self) -> tuple[list[dict], list[dict]]:
        if self.min_enriched_count > 1:  # drop rare enriched relations (likely extraction noise)
            per_rel = Counter(rel for (_, rel, _) in self.triples)
            rare = {rel for rel, n in per_rel.items() if n < self.min_enriched_count and self.schema.relations[rel]["origin"] != "seed"}
            self.triples = {k: v for k, v in self.triples.items() if k[1] not in rare}
            used = {k[0] for k in self.triples} | {k[2] for k in self.triples}
            self.entities = {eid: e for eid, e in self.entities.items() if eid in used}
            self._type_votes = defaultdict(Counter, {eid: v for eid, v in self._type_votes.items() if eid in used})
        for eid, votes in self._type_votes.items():
            best = max(votes.items(), key=lambda kv: (kv[1], -TYPE_PRIORITY.index(kv[0]) if kv[0] in TYPE_PRIORITY else -99))
            self.entities[eid]["type"] = "Drug" if votes.get("Drug") else best[0]
        triples = []
        for (sid, rel, oid), t in self.triples.items():
            info = self.schema.relations[rel]
            triples.append({"subject": self.entities[sid]["label"], "subject_id": sid, "subject_type": self.entities[sid]["type"],
                            "relation": rel, "object": self.entities[oid]["label"], "object_id": oid,
                            "object_type": self.entities[oid]["type"], "relation_origin": info["origin"],
                            "count": t["count"], "drugs": sorted(t["drugs"]), "sources": sorted(t["sources"]),
                            "provenance": t["provenance"]})
        triples.sort(key=lambda x: (x["drugs"][0] if x["drugs"] else "", x["relation"], x["subject"], x["object"]))
        entities = sorted(self.entities.values(), key=lambda e: (-e["mentions"], e["label"]))
        return entities, triples
