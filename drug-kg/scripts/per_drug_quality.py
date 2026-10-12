#!/usr/bin/env python
"""Per-drug quality of EDC-extracted triples (structured metadata triples excluded), compared across KGs.

Metrics per drug (from <kg>/neo4j/{nodes,relationships}.csv):
  centric   % of triples whose subject is the drug's own node
  seed      % of triples using a seed-schema relation (not an enriched one)
  conform   % of seed-relation triples whose subject/object types match the schema domain/range
  clean     % of triples whose object is a short concept (<= 6 words, not a clause)
  quality   mean of the four
Usage: python scripts/per_drug_quality.py text_edc=output/experiments/text_edc/kg ... --out output/report/x.md
"""
from __future__ import annotations
import argparse
import collections
import csv
import pathlib
import re
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[1]


def analyze(kg_dir: pathlib.Path, seed: dict) -> dict[str, dict]:
    nodes = {r["id:ID"]: r for r in csv.DictReader(open(kg_dir / "neo4j" / "nodes.csv", encoding="utf-8"))}
    by = collections.defaultdict(list)
    for r in csv.DictReader(open(kg_dir / "neo4j" / "relationships.csv", encoding="utf-8")):
        if "edc" in r["sources"].split(";"):
            for d in r["drugs"].split(";"):
                by[d].append(r)

    def clean(label: str) -> bool:
        return len(label.split()) <= 6 and not re.search(r"[,.;:]\s|\b(if|when|should|may|do not)\b", label.lower())

    out = {}
    for d, rs in by.items():
        hub = collections.Counter(r[":START_ID"] for r in rs).most_common(1)[0][0]
        seeded = [r for r in rs if r["relation"] in seed]
        conform = [r for r in seeded if nodes[r[":START_ID"]]["type"] == seed[r["relation"]][0]
                   and nodes[r[":END_ID"]]["type"] == seed[r["relation"]][1]]
        m = {"n": len(rs), "centric": 100 * sum(r[":START_ID"] == hub for r in rs) / len(rs),
             "seed": 100 * len(seeded) / len(rs), "conform": 100 * len(conform) / max(1, len(seeded)),
             "clean": 100 * sum(clean(nodes[r[":END_ID"]]["label"]) for r in rs) / len(rs),
             "enriched_rels": len({r["relation"] for r in rs if r["relation"] not in seed})}
        m["quality"] = (m["centric"] + m["seed"] + m["conform"] + m["clean"]) / 4
        out[d] = m
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("kgs", nargs="+", help="name=kg_dir")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    seed = {r["relation"]: (r["subject_type"], r["object_type"])
            for r in csv.DictReader(open(ROOT / "schemas" / "drug_seed_schema.csv", encoding="utf-8"))}
    res = {}
    for spec in args.kgs:
        name, path = spec.split("=", 1)
        p = pathlib.Path(path)
        res[name] = analyze(p if p.is_absolute() else ROOT / p, seed)
    names = list(res)
    keys = ["n", "centric", "seed", "conform", "clean", "enriched_rels", "quality"]
    md = ["# Per-drug quality of EDC triples", "",
          "EDC-extracted triples only (structured metadata excluded). centric = subject is the drug itself; seed = seed-schema "
          "relation; conform = subject/object types match the relation's domain/range; clean = object is a short concept "
          "(<= 6 words, not a clause); quality = mean of the four. Automatic proxies, not precision.", "",
          "## Overall (mean over drugs; n = total triples)", "", "| metric | " + " | ".join(names) + " |",
          "|---|" + "---|" * len(names)]
    for k in keys:
        vals = []
        for n in names:
            v = [m[k] for m in res[n].values()]
            vals.append(f"{sum(v):,}" if k == "n" else f"{statistics.mean(v):.1f}")
        md.append(f"| {k} | " + " | ".join(vals) + " |")
    drugs = sorted(set().union(*[set(r) for r in res.values()]))
    last = names[-1]
    md += ["", f"## Per drug (sorted by {last} quality; Δ = {last} − {names[0]})", "",
           "| drug | " + " | ".join(f"{n} n / quality" for n in names) + f" | Δ quality |", "|---|" + "---|" * (len(names) + 1)]
    for d in sorted(drugs, key=lambda d: -res[last].get(d, {"quality": 0})["quality"]):
        cells = [f"{res[n][d]['n']} / {res[n][d]['quality']:.1f}" if d in res[n] else "–" for n in names]
        delta = res[last][d]["quality"] - res[names[0]][d]["quality"] if d in res[last] and d in res[names[0]] else float("nan")
        md.append(f"| {d} | " + " | ".join(cells) + f" | {delta:+.1f} |")
    out = pathlib.Path(args.out)
    out = out if out.is_absolute() else ROOT / out
    out.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md[:8 + len(keys)]))


if __name__ == "__main__":
    main()
