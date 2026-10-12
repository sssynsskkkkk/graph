"""Relation redundancy per KG: pairwise cosine similarity of relation *definitions* (same embedder as EDC canonicalization).

Usage: python scripts/relation_redundancy.py [--kg DIR ...]   (default: main + every experiment kg / kg_canon)
Writes output/report/relation_redundancy.md and .json
"""
import argparse, csv, json, os, pathlib, sys
os.environ.setdefault("MPLCONFIGDIR", os.path.expanduser("~/.cache/matplotlib"))
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from drugkg.edc.schema import Embedder  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
THRESHOLDS = (0.80, 0.85, 0.90, 0.95)


def kg_dirs():
    out = [(ROOT / "output" / "kg", "main (4B)")]
    for d in sorted((ROOT / "output" / "experiments").glob("*")):
        if d.name == "smoke":
            continue
        st = json.loads((d / "stages.json").read_text()) if (d / "stages.json").exists() else {}
        for sub, suf in (("kg", ""), ("kg_canon", " (canon)")):
            if (d / sub / "schema.csv").exists() and not ("copy_from" in st and sub == "kg"):
                out.append((d / sub, d.name + suf))
    return out


def analyse(kg_dir, embedder):
    rows = [r for r in csv.DictReader(open(kg_dir / "schema.csv", encoding="utf-8"))]
    rels = [r["relation"] for r in rows]
    defs = [r["definition"] for r in rows]
    n_tr = {r["relation"]: int(r.get("n_triples") or 0) for r in rows}
    origin = {r["relation"]: r.get("origin", "") for r in rows}
    E = embedder.encode(defs)
    S = E @ E.T
    np.fill_diagonal(S, -1)
    n = len(rels)
    iu = np.triu_indices(n, 1)
    sims = S[iu]
    nearest = S.max(axis=1)
    total_triples = sum(n_tr.values()) or 1
    res = {"kg": str(kg_dir.relative_to(ROOT)), "n_relations": n, "n_triples": total_triples,
           "mean_nearest_sim": round(float(nearest.mean()), 4), "median_nearest_sim": round(float(np.median(nearest)), 4),
           "mean_pair_sim": round(float(sims.mean()), 4)}
    for t in THRESHOLDS:
        pairs = int((sims >= t).sum())
        rel_with_dup = [rels[i] for i in range(n) if nearest[i] >= t]
        res[f"pairs_ge_{t}"] = pairs
        res[f"relations_with_neighbour_ge_{t}"] = len(rel_with_dup)
        res[f"triple_share_with_neighbour_ge_{t}"] = round(sum(n_tr[r] for r in rel_with_dup) / total_triples, 3)
    order = np.argsort(-sims)[:12]
    res["top_pairs"] = [(rels[iu[0][k]], rels[iu[1][k]], round(float(sims[k]), 3), origin[rels[iu[0][k]]], origin[rels[iu[1][k]]])
                        for k in order]
    seed_idx = [i for i, r in enumerate(rels) if origin[r] == "seed"]
    if len(seed_idx) > 1:
        Ss = S[np.ix_(seed_idx, seed_idx)]
        res["seed_only_mean_nearest"] = round(float(Ss.max(axis=1).mean()), 4)
        res["seed_only_pairs_ge_0.85"] = int((Ss[np.triu_indices(len(seed_idx), 1)] >= 0.85).sum())
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kg", action="append", default=None)
    args = ap.parse_args()
    emb = Embedder("BAAI/bge-base-en-v1.5", "cpu")
    targets = [(ROOT / k, k) for k in args.kg] if args.kg else kg_dirs()
    results = [dict(analyse(d, emb), label=label) for d, label in targets]
    out = ROOT / "output" / "report"
    (out / "relation_redundancy.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    lines = ["# Relation redundancy (cosine similarity of relation definitions, bge-base-en-v1.5)", "",
             "| KG | relations | mean nearest-neighbour sim | pairs ≥0.85 | pairs ≥0.90 | relations with a neighbour ≥0.85 | share of triples under those relations | seed-only mean nearest | seed-only pairs ≥0.85 |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['label']} | {r['n_relations']} | {r['mean_nearest_sim']:.3f} | {r['pairs_ge_0.85']} | {r['pairs_ge_0.9']} | "
                     f"{r['relations_with_neighbour_ge_0.85']} | {r['triple_share_with_neighbour_ge_0.85']:.0%} | "
                     f"{r.get('seed_only_mean_nearest', float('nan')):.3f} | {r.get('seed_only_pairs_ge_0.85', '')} |")
    for r in results:
        lines += ["", f"## {r['label']}: most similar relation pairs", "", "| relation A | relation B | cosine | origins |", "|---|---|---|---|"]
        lines += [f"| {a} | {b} | {s:.3f} | {oa}/{ob} |" for a, b, s, oa, ob in r["top_pairs"]]
    (out / "relation_redundancy.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:12]))


if __name__ == "__main__":
    main()
