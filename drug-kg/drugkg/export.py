"""Export the KG as JSONL/CSV, Neo4j import files, RDF Turtle, GraphML and a stats summary."""
from __future__ import annotations
import csv
import json
import pathlib
import re
from collections import Counter

NS = "http://drugkg.example.org/"


def rel_type(rel: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "_", rel.upper()).strip("_")


def export_all(entities: list[dict], triples: list[dict], schema, out_dir: pathlib.Path, meta: dict | None = None) -> dict:
    out_dir = pathlib.Path(out_dir)
    (out_dir / "neo4j").mkdir(parents=True, exist_ok=True)

    with open(out_dir / "triples.jsonl", "w", encoding="utf-8") as f:
        for t in triples:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    with open(out_dir / "triples.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["subject", "relation", "object", "subject_type", "object_type", "count", "drugs", "sources", "relation_origin"])
        for t in triples:
            w.writerow([t["subject"], t["relation"], t["object"], t["subject_type"], t["object_type"], t["count"],
                        ";".join(t["drugs"]), ";".join(t["sources"]), t["relation_origin"]])
    with open(out_dir / "entities.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "label", "type", "mentions"])
        for e in entities:
            w.writerow([e["id"], e["label"], e["type"], e["mentions"]])
    used = Counter(t["relation"] for t in triples)
    with open(out_dir / "schema.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["relation", "definition", "subject_type", "object_type", "origin", "n_triples"])
        for name, r in schema.relations.items():
            if used[name]:
                w.writerow([name, r["definition"], r["subject_type"], r["object_type"], r["origin"], used[name]])

    # ---- Neo4j (neo4j-admin import format + LOAD CSV script)
    with open(out_dir / "neo4j" / "nodes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id:ID", "label", "type", ":LABEL", "mentions:int"])
        for e in entities:
            w.writerow([e["id"], e["label"], e["type"], f"Entity;{e['type']}", e["mentions"]])
    with open(out_dir / "neo4j" / "relationships.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([":START_ID", ":END_ID", ":TYPE", "relation", "count:int", "drugs", "sources"])
        for t in triples:
            w.writerow([t["subject_id"], t["object_id"], rel_type(t["relation"]), t["relation"], t["count"],
                        ";".join(t["drugs"]), ";".join(t["sources"])])
    (out_dir / "neo4j" / "import.cypher").write_text(
        "// Load with: cypher-shell -f import.cypher   (copy nodes.csv / relationships.csv into Neo4j's import/ folder)\n"
        "CREATE CONSTRAINT entity_id IF NOT EXISTS FOR (e:Entity) REQUIRE e.id IS UNIQUE;\n"
        "LOAD CSV WITH HEADERS FROM 'file:///nodes.csv' AS row\n"
        "MERGE (e:Entity {id: row.`id:ID`}) SET e.label = row.label, e.type = row.type, e.mentions = toInteger(row.`mentions:int`)\n"
        "WITH e, row CALL apoc.create.addLabels(e, [row.type]) YIELD node RETURN count(*);\n"
        "LOAD CSV WITH HEADERS FROM 'file:///relationships.csv' AS row\n"
        "MATCH (s:Entity {id: row.`:START_ID`}), (o:Entity {id: row.`:END_ID`})\n"
        "CALL apoc.merge.relationship(s, row.`:TYPE`, {}, {relation: row.relation, count: toInteger(row.`count:int`), "
        "drugs: split(row.drugs, ';'), sources: split(row.sources, ';')}, o) YIELD rel RETURN count(*);\n"
        "// Without APOC: CREATE (s)-[:RELATED {type: row.`:TYPE`}]->(o) instead of apoc.merge.relationship.\n",
        encoding="utf-8")

    # ---- RDF Turtle
    try:
        from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
        g = Graph()
        ns = Namespace(NS)
        g.bind("dkg", ns)
        ent_uri = {e["id"]: URIRef(NS + "entity/" + e["id"]) for e in entities}
        for e in entities:
            g.add((ent_uri[e["id"]], RDF.type, URIRef(NS + "type/" + e["type"])))
            g.add((ent_uri[e["id"]], RDFS.label, Literal(e["label"])))
        for name, r in schema.relations.items():
            if used[name]:
                p = URIRef(NS + "relation/" + rel_type(name).lower())
                g.add((p, RDF.type, RDF.Property))
                g.add((p, RDFS.label, Literal(name)))
                g.add((p, RDFS.comment, Literal(r["definition"])))
        for t in triples:
            g.add((ent_uri[t["subject_id"]], URIRef(NS + "relation/" + rel_type(t["relation"]).lower()), ent_uri[t["object_id"]]))
        g.serialize(out_dir / "kg.ttl", format="turtle")
    except Exception as e:  # pragma: no cover
        print("rdf export skipped:", e)

    # ---- GraphML (networkx)
    try:
        import networkx as nx
        G = nx.MultiDiGraph()
        for e in entities:
            G.add_node(e["id"], label=e["label"], type=e["type"], mentions=e["mentions"])
        for t in triples:
            G.add_edge(t["subject_id"], t["object_id"], key=t["relation"], relation=t["relation"], count=t["count"],
                       drugs=";".join(t["drugs"]))
        nx.write_graphml(G, out_dir / "kg.graphml")
    except Exception as e:  # pragma: no cover
        print("graphml export skipped:", e)

    stats = {
        "n_entities": len(entities), "n_triples": len(triples), "n_relations_used": len(used),
        "n_relations_seed": sum(1 for n in used if schema.relations[n]["origin"] == "seed"),
        "n_relations_enriched": sum(1 for n in used if schema.relations[n]["origin"] != "seed"),
        "entities_by_type": dict(Counter(e["type"] for e in entities).most_common()),
        "triples_by_relation": dict(used.most_common()),
        "triples_by_source": dict(Counter(s for t in triples for s in t["sources"]).most_common()),
        "triples_per_drug": dict(Counter(d for t in triples for d in t["drugs"]).most_common()),
    }
    if meta:
        stats.update(meta)
    (out_dir / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    return stats
