"""Example queries over the exported KG (pandas + networkx). Usage: python scripts/query_examples.py [output/kg]"""
import pathlib
import sys

import pandas as pd

kg = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[1] / "output" / "kg")
t = pd.read_csv(kg / "triples.csv")
e = pd.read_csv(kg / "entities.csv")
print(f"KG: {len(e)} entities, {len(t)} triples, {t.relation.nunique()} relations\n")

print("1) Relations by frequency")
print(t.relation.value_counts().head(15).to_string(), "\n")

print("2) Side effects shared by the most drugs")
se = t[t.relation.isin(["has side effect", "has serious side effect"])]
print(se.groupby("object").drugs.nunique().sort_values(ascending=False).head(10).to_string(), "\n")

print("3) What does each drug treat? (first 5 drugs)")
tr = t[t.relation == "treats"].groupby("subject").object.apply(lambda s: ", ".join(sorted(set(s))[:6]))
print(tr.head(5).to_string(), "\n")

print("4) Drug-drug interaction edges whose object is itself one of the 50 drugs")
drugs = set(e[e.type == "Drug"].label.str.lower())
dd = t[(t.relation == "interacts with") & (t.object.str.lower().isin(drugs))]
print(dd[["subject", "object"]].drop_duplicates().head(15).to_string(index=False), "\n")

print("5) Two-hop: drugs in the same drug class (via 'belongs to drug class')")
dc = t[t.relation == "belongs to drug class"].groupby("object").subject.apply(lambda s: sorted(set(s)))
print(dc[dc.map(len) > 1].head(10).to_string(), "\n")

try:
    import networkx as nx
    G = nx.read_graphml(kg / "kg.graphml")
    deg = sorted(G.degree, key=lambda kv: -kv[1])[:10]
    print("6) Highest-degree nodes:", [(G.nodes[n].get("label", n), d) for n, d in deg])
except Exception as ex:  # pragma: no cover
    print("networkx example skipped:", ex)
