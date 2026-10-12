"""Compare experiments under output/experiments/* -> output/report/experiments_comparison.md (+ .json).
Usage: python scripts/compare_experiments.py [exp1 exp2 ...]   (default: all experiments with a kg/stats.json)"""
import collections
import glob
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXP = ROOT / "output" / "experiments"
names = sys.argv[1:] or sorted(p.parent.parent.name for p in EXP.glob("*/kg/stats.json"))


def load(p):
    return json.load(open(p, encoding="utf-8")) if pathlib.Path(p).exists() else {}


def edc_stats(exp_dir):
    st, n_open, n_final, n_chunks, secs = collections.Counter(), 0, 0, 0, 0.0
    for f in glob.glob(str(exp_dir / "edc" / "*.json")):
        r = json.load(open(f, encoding="utf-8"))
        it = r["iterations"][-1]
        n_chunks += r["n_chunks"]; secs += r.get("seconds", 0); n_final += len(r["final_triplets"])
        for c in it["chunks"]:
            n_open += len(c["oie"])
            for x in c["schema_canonicalization"]:
                st[x["status"]] += 1
    return {"n_chunks": n_chunks, "open_triplets": n_open, "final_triplets": n_final, "extract_seconds": round(secs), **{f"status_{k}": v for k, v in st.items()}}


rows = {}
for name in names:
    d = EXP / name
    kg = load(d / "kg" / "stats.json"); kgc = load(d / "kg_canon" / "stats.json")
    au = load(d / "audit" / "summary.json"); auc = load(d / "audit_canon" / "summary.json")
    stages = load(d / "stages.json"); ec = load(d / "entity_canon" / "stats.json")
    def audit_row(a):
        if not a:
            return {}
        b = a.get("by_issue", {})
        return {"entities_with_issue": a.get("n_entities_with_any_issue"),
                "dup_groups": sum(a.get("duplicate_groups", {}).values()),
                "sentence_like_concepts": b.get("D1_sentence_like_concept", {}).get("entities"),
                "composite": b.get("D2_multiple_concepts", {}).get("entities"),
                "alias_split": b.get("A3_alias_split_from_core", {}).get("entities"),
                "type_mismatch_entities": b.get("B3_type_mismatch_with_relation", {}).get("entities"),
                "boilerplate_hubs": b.get("G1_boilerplate_hub", {}).get("entities")}
    row = {"model": stages.get("extract", {}).get("llm_model"), "input": stages.get("prepare", {}).get("input") or stages.get("copy_from", {}).get("source"),
           **edc_stats(d),
           "kg_entities": kg.get("n_entities"), "kg_triples": kg.get("n_triples"), "kg_relations": kg.get("n_relations_used"),
           "kg_relations_enriched": kg.get("n_relations_enriched"),
           **{f"audit_{k}": v for k, v in audit_row(au).items()},
           "stage_seconds": {k: v.get("seconds") for k, v in stages.items()}}
    if kgc:
        row.update({"canon_entities": kgc.get("n_entities"), "canon_triples": kgc.get("n_triples"), "canon_relations": kgc.get("n_relations_used"),
                    "canon_lm_calls": ec.get("lm_calls"), "canon_entities_after_semhash": ec.get("entities_after_semhash"),
                    **{f"audit_canon_{k}": v for k, v in audit_row(auc).items()}})
    rows[name] = row

(ROOT / "output" / "report").mkdir(parents=True, exist_ok=True)
(ROOT / "output" / "report" / "experiments_comparison.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
keys = []
for r in rows.values():
    for k in r:
        if k not in keys and k != "stage_seconds":
            keys.append(k)
lines = ["# Experiment comparison", "", "| metric | " + " | ".join(rows) + " |", "|---|" + "---|" * len(rows)]
for k in keys:
    lines.append(f"| {k} | " + " | ".join(str(rows[n].get(k, "")) for n in rows) + " |")
lines += ["", "Stage seconds: " + json.dumps({n: r["stage_seconds"] for n, r in rows.items()})]
(ROOT / "output" / "report" / "experiments_comparison.md").write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
