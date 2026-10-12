#!/usr/bin/env python3
"""Validate evaluation completeness/provenance, not semantic or clinical truth."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream]


def main() -> None:
    root = Path("data/gt_graph_semantic_comparison_top50")
    meta = json.loads((root / "metadata.json").read_text())
    summary = json.loads((root / "summary.json").read_text())
    references = read_jsonl(root / "gt_reference.jsonl")
    rows = read_jsonl(root / "semantic_comparison.jsonl")
    candidates = read_jsonl(root / "candidates.jsonl")
    edges = {r["edge_id"]: r for r in read_jsonl(root / meta["edge_file"])}
    gt = {r["gt_id"]: r for r in references}
    documents = {d["rank"]: d for d in meta["documents"]}
    expected = set(range(1,51))
    assert len(rows) == len(references) == len(candidates) == 1894
    assert len({r["gt_id"] for r in rows}) == len(rows)
    assert {r["gt_id"] for r in rows} == set(gt)
    assert {r["rank"] for r in rows} == expected == set(documents)
    assert len(edges) == 11746 == summary["graph_selected_unique_edge_count"]
    assert all(d["document_present"] for d in documents.values())
    assert dict(Counter(r["status"] for r in rows)) == summary["status_counts"]
    assert all(r["status"] in {"match","partial","no_match"} for r in rows)
    for row in rows:
        ref = gt[row["gt_id"]]
        assert row["reference_triple"] == [ref["entity_1"],ref["relationship"],ref["entity_2"]]
        assert row["qualifiers"] == ref["qualifiers"]
        assert row["reference_evidence"] == ref["evidence_text"]
        assert -1.000001 <= row["best_retrieval_cosine"] <= 1.000001
        if row["status"] == "match":
            assert not row["qualifiers"], row["gt_id"]
        if row["status"] in {"match","partial"}:
            edge = row["graph_edge"]
            assert edge is not None
            original = edges[edge["edge_id"]]
            for key in ["subject","relationship","object"]:
                assert edge[key] == original[key]
            assert documents[row["rank"]]["document_slug"] in edge["document_slugs"]
        assert 7 <= len(row["candidate_edges"]) <= 9
        for candidate in row["candidate_edges"]:
            assert candidate["edge_id"] in edges
            assert documents[row["rank"]]["document_slug"] in candidate["document_slugs"]

    csv_rows = list(csv.DictReader((root / "semantic_comparison.csv").open(encoding="utf-8-sig")))
    drug_rows = list(csv.DictReader((root / "per_drug_summary.csv").open(encoding="utf-8-sig")))
    assert len(csv_rows) == len(rows) and {r["gt_id"] for r in csv_rows} == set(gt)
    assert len(drug_rows) == 50 and {int(r["rank"]) for r in drug_rows} == expected
    assert sum(int(r["gt_count"]) for r in drug_rows) == len(rows)
    for file_key, hash_key in [("graph_file","graph_sha256"),("gt_file","gt_sha256")]:
        assert hashlib.sha256(Path(meta[file_key]).read_bytes()).hexdigest() == meta[hash_key]
    report = {
        "evaluation_export_validation_passed": True,
        "reference_count": len(rows),
        "drug_count": len(documents),
        "rank_range": [1,50],
        "graph_edge_count": len(edges),
        "unjudged_or_invalid_results": 0,
        "inputs_unchanged_since_prepare": True,
        "candidate_and_positive_matches_scoped_to_correct_document": True,
        "qualifier_bearing_match_count": 0,
        "csv_and_per_drug_counts_verified": True,
        "reused_raw_judgments": meta["reused_judgment_count"],
        "recovered_truncated_judge_json_count": sum(r["original_llm_status"]=="parse_error" for r in rows),
        "explicit_contradiction_corrections": summary["contradiction_guard_count"],
        "status_counts": summary["status_counts"],
        "semantic_or_clinical_correctness_certified": False,
        "human_reviewed": False,
    }
    (root / "validation_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
