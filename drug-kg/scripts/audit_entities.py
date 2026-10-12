"""Audit entity-level errors in an exported KG.

Usage: python scripts/audit_entities.py [--kg output/kg] [--out output/report/entity_audit]  -> entity_issues.csv, duplicate_groups.csv, summary.json
Each entity can carry several issue tags. Nothing is modified; this only reports.
"""
import collections, csv, glob, json, pathlib, re

import argparse
ROOT = pathlib.Path(__file__).resolve().parents[1]
_ap = argparse.ArgumentParser()
_ap.add_argument("--kg", default=str(ROOT / "output" / "kg"), help="KG directory (entities.csv, triples.jsonl, schema.csv)")
_ap.add_argument("--out", default=str(ROOT / "output" / "report" / "entity_audit"))
_ap.add_argument("--quiet", action="store_true")
_args = _ap.parse_args()
KG, OUT = pathlib.Path(_args.kg), pathlib.Path(_args.out)
OUT.mkdir(parents=True, exist_ok=True)

E = {e["id"]: e for e in csv.DictReader(open(KG / "entities.csv", encoding="utf-8"))}
T = [json.loads(l) for l in open(KG / "triples.jsonl", encoding="utf-8")]
SCHEMA = {r["relation"]: r for r in csv.DictReader(open(KG / "schema.csv", encoding="utf-8"))}
PARSED = {json.load(open(f))["slug"]: json.load(open(f)) for f in glob.glob(str(ROOT / "data" / "parsed" / "*.json"))}

deg, as_subj, drugs_of = collections.Counter(), collections.Counter(), collections.defaultdict(set)
rels_of = collections.defaultdict(collections.Counter)
for t in T:
    for side in ("subject_id", "object_id"):
        deg[t[side]] += 1
        drugs_of[t[side]].update(t["drugs"])
    as_subj[t["subject_id"]] += 1
    rels_of[t["object_id"]][t["relation"]] += 1

issues = collections.defaultdict(list)          # entity_id -> [(tag, detail)]
def flag(eid, tag, detail=""):
    issues[eid].append((tag, detail))

CONCEPT = {"Drug", "DrugClass", "Condition", "SideEffect", "Symptom", "Substance", "Ingredient", "LabTest",
           "DosageForm", "Route", "Organization", "Mechanism", "Therapy", "Population"}
LITERAL = {"Instruction", "Warning", "Dose", "Strength", "Year", "Schedule", "Availability", "Other"}

# ---------------------------------------------------------------- A. core drug nodes (the 50 page drugs)
core = {}  # slug -> entity id of the page drug
for t in T:
    if "structured" in t["sources"] and t["relation"] == "has availability":
        core[t["drugs"][0]] = t["subject_id"]
for slug, eid in core.items():
    rec, label = PARSED.get(slug, {}), E[eid]["label"]
    if label[:1].islower():
        flag(eid, "A1_core_label_case", f"page drug shown in lowercase: '{label}'")
    if re.search(r"\b(inhalation|nasal spray|tablets?|injection|oral|and)\b", label, re.I):
        flag(eid, "A2_core_label_from_title", f"label taken from page title: '{label}' (generic: {rec.get('generic_name')})")
    # aliases of this drug that exist as separate nodes carrying their own facts
    aliases = set(rec.get("brand_names") or []) | ({rec["generic_name"]} if rec.get("generic_name") else set())
    for a in aliases:
        aid = re.sub(r"[^a-z0-9]+", "_", a.lower()).strip("_")
        if aid in E and aid != eid and as_subj[aid] > 0:
            flag(aid, "A3_alias_split_from_core", f"alias of {label} with {as_subj[aid]} own facts")

# ---------------------------------------------------------------- B. type errors
DISEASE_WORDS = re.compile(r"(syndrome|disease|pressure|pain|infection|failure|disorder|cancer|diabetes|attack|"
                           r"reaction|bleeding|inhibitors?$|trial|SURPASS|study)", re.I)
for eid, e in E.items():
    if e["type"] == "Drug" and eid not in core.values() and DISEASE_WORDS.search(e["label"]):
        flag(eid, "B1_non_drug_typed_as_drug", f"subject of {as_subj[eid]} triples")
    if e["type"] == "Other":
        flag(eid, "B2_untyped_other")
# types that may legitimately fill another type's slot (Drug is a Substance, a symptom can be a condition, ...)
COMPATIBLE = {"Substance": {"Drug", "Ingredient", "DrugClass"}, "Therapy": {"Drug", "DrugClass"},
              "Ingredient": {"Substance", "Drug"}, "Drug": {"DrugClass"},
              "Condition": {"SideEffect", "Symptom"}, "SideEffect": {"Symptom", "Condition"}, "Symptom": {"SideEffect", "Condition"},
              "Instruction": {"Dose"}, "Dose": {"Strength", "Instruction"}}
range_viol = collections.Counter()
for t in T:
    exp = SCHEMA.get(t["relation"], {}).get("object_type")
    if exp and exp != "Other" and t["object_type"] != exp and t["object_type"] not in COMPATIBLE.get(exp, set()):
        range_viol[(t["relation"], exp, t["object_type"])] += 1
        flag(t["object_id"], "B3_type_mismatch_with_relation", f"{t['relation']} expects {exp}")
for eid, c in rels_of.items():  # same node used as treated condition and as side effect
    if c["treats"] and (c["has side effect"] or c["has serious side effect"]) and E[eid]["type"] not in ("Drug",):
        flag(eid, "B4_both_indication_and_side_effect", f"treats×{c['treats']}, side effect×{c['has side effect'] + c['has serious side effect']}")

# ---------------------------------------------------------------- C. duplicates / surface variants
def k_exact(s):  # case, plural, punctuation, hyphen
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower().replace("-", " "))
    return " ".join(w[:-1] if w.endswith("s") and len(w) > 3 and not w.endswith("ss") else w for w in s.split())
MODS = r"\b(severe|mild|serious|signs? of|symptoms? of|new or worsening|worsening|unusual|sudden|extreme|possible|risk of|increased)\b"
FORM = r"\b(tablets?|capsules?|oral|injection|solution|suspension|extended release|delayed release|immediate release|er|xr|sr|dr|fda|generic|pen|kwikpen)\b"
def k_mod(s):
    s = re.sub(r"\([^)]*\)", " ", s.lower())
    s = re.sub(MODS, " ", s); s = re.sub(FORM, " ", s)
    return k_exact(s)
groups = {}
for name, keyf in (("C1_exact_variant", k_exact), ("C2_modifier_or_form_variant", k_mod)):
    g = collections.defaultdict(list)
    for eid, e in E.items():
        if e["type"] in CONCEPT:
            key = keyf(e["label"])
            if key:
                g[(e["type"] if name == "C1_exact_variant" else "*", key)].append(eid)
    for key, ids in g.items():
        if len(ids) > 1:
            if name == "C2_modifier_or_form_variant" and len({k_exact(E[i]['label']) for i in ids}) == 1:
                continue  # already covered by C1
            groups[(name, key)] = ids
            for i in ids:
                flag(i, name, " | ".join(E[j]["label"] for j in ids[:6]))
cross_type = collections.defaultdict(set)  # same surface form, different types (split nodes)
for eid, e in E.items():
    cross_type[k_exact(e["label"])].add(e["type"])

# ---------------------------------------------------------------- D. non-atomic entities
for eid, e in E.items():
    lab, n = e["label"], len(e["label"].split())
    if e["type"] in CONCEPT and n >= 6:
        flag(eid, "D1_sentence_like_concept", f"{n} words")
    if e["type"] in CONCEPT and re.search(r",| and | or |/|;", lab) and not re.search(r"\b(amphetamine and|hydrocodone and|and acetaminophen)\b", lab, re.I) and n <= 12:
        flag(eid, "D2_multiple_concepts", "list/conjunction inside one entity")
    if e["type"] in LITERAL and n >= 6:
        flag(eid, "D3_sentence_literal", f"{n} words ({e['type']})")

# ---------------------------------------------------------------- E. relation words leaked into entity
LEAK = re.compile(r"^(treats?|used (to|for)|may (cause|increase|decrease|reduce)|causes?|increases?|decreases?|reduces?|"
                  r"lowers?|prevents?|helps?|to (treat|reduce|prevent|lower|help)|avoid|do not|should|can cause|is used)\b", re.I)
for eid, e in E.items():
    if e["type"] in CONCEPT and LEAK.search(e["label"]):
        flag(eid, "E1_relation_word_in_entity")

# ---------------------------------------------------------------- F. vague / generic referents
VAGUE = re.compile(r"^(your |other |any |some |certain |all |these |this |that |such |many |several )|"
                   r"^(doctor|healthcare provider|patient|patients|medicine|medicines|medication|medications|drug|drugs|"
                   r"it|them|you|people|other people|children|adults|yes|no)$", re.I)
for eid, e in E.items():
    if VAGUE.search(e["label"]):
        flag(eid, "F1_vague_or_generic")
    if len(e["label"]) <= 2 or re.fullmatch(r"[\d.,% ]+", e["label"]):
        flag(eid, "F2_too_short_or_bare_number")

# ---------------------------------------------------------------- G. boilerplate hubs
for eid, e in E.items():
    if e["type"] in LITERAL and len(drugs_of[eid]) >= 15:
        flag(eid, "G1_boilerplate_hub", f"shared by {len(drugs_of[eid])} drugs")

# ---------------------------------------------------------------- H. value formatting
for eid, e in E.items():
    if e["type"] in ("Dose", "Strength") and re.search(r"\d(mg|mcg|ml|g|units?)\b|\d\s*milligrams?", e["label"], re.I):
        flag(eid, "H1_unit_format", "no space / spelled-out unit")

# ---------------------------------------------------------------- I. wrong subject
for t in T:
    if t["subject_type"] != "Drug" and SCHEMA.get(t["relation"], {}).get("subject_type") == "Drug":
        flag(t["subject_id"], "I1_non_drug_subject", f"{t['subject']} --{t['relation']}--> {t['object']}")

# ---------------------------------------------------------------- write
with open(OUT / "entity_issues.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["entity_id", "label", "type", "degree", "n_drugs", "issue", "detail"])
    for eid, lst in sorted(issues.items(), key=lambda kv: -deg[kv[0]]):
        for tag, detail in dict.fromkeys(lst):
            w.writerow([eid, E[eid]["label"], E[eid]["type"], deg[eid], len(drugs_of[eid]), tag, detail])
with open(OUT / "duplicate_groups.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["kind", "key", "n", "labels", "types"])
    for (kind, key), ids in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        w.writerow([kind, key[1], len(ids), " | ".join(E[i]["label"] for i in ids), " | ".join(sorted({E[i]['type'] for i in ids}))])

tag_ents = collections.defaultdict(set)
for eid, lst in issues.items():
    for tag, _ in lst:
        tag_ents[tag].add(eid)
summary = {
    "n_entities": len(E), "n_entities_with_any_issue": len(issues),
    "by_issue": {tag: {"entities": len(ids), "triples_touched": sum(deg[i] for i in ids),
                       "examples": [E[i]["label"] for i in sorted(ids, key=lambda i: -deg[i])[:8]]}
                 for tag, ids in sorted(tag_ents.items())},
    "duplicate_groups": collections.Counter(k for k, _ in groups),
    "same_surface_different_type": sum(1 for v in cross_type.values() if len(v) > 1),
    "top_type_mismatches": [f"{r}: expects {a}, got {b} ×{n}" for (r, a, b), n in range_viol.most_common(12)],
    "literal_vs_concept": {"concept": sum(1 for e in E.values() if e["type"] in CONCEPT),
                           "literal": sum(1 for e in E.values() if e["type"] in LITERAL)},
}
(OUT / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
if not _args.quiet:
    print(json.dumps(summary, indent=1, ensure_ascii=False))
