#!/usr/bin/env python3
"""Check source provenance and export consistency, not clinical correctness."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data/gt_top25_review"))
    args = parser.parse_args()
    root = args.data_dir
    rows = [json.loads(line) for line in (root / "gold_triplets_draft.jsonl").open(encoding="utf-8")]
    summary = json.loads((root / "summary.json").read_text(encoding="utf-8"))
    schema = json.loads((root / "relation_schema.json").read_text(encoding="utf-8"))
    csv_rows = list(csv.DictReader((root / "gold_triplets_review.csv").open(encoding="utf-8-sig", newline="")))
    ids = {row["gt_id"] for row in rows}
    assert len(ids) == len(rows), "Duplicate GT IDs"
    assert len(rows) == summary["triple_count"] == len(csv_rows)
    assert {row["gt_id"] for row in csv_rows} == ids
    rank_start, rank_end = summary["rank_range"]
    expected_ranks = set(range(rank_start, rank_end + 1))
    assert {row["rank"] for row in rows} == expected_ranks
    assert all(row["review_status"] == "pending_human_review" for row in rows)
    assert summary["human_reviewed"] is False and summary["exhaustive"] is False

    original_path = Path("data/text-only/decomposition_raw/decomposition.jsonl")
    original_ids = None
    if original_path.exists():
        original_ids = {json.loads(line)["record_id"] for line in original_path.open(encoding="utf-8")}

    source_cache = {}
    dose_rows = 0
    for row in rows:
        for key in ("entity_1", "relationship", "entity_2", "evidence_text"):
            assert isinstance(row[key], str) and row[key].strip(), (row["gt_id"], key)
        assert row["relationship"] == schema[row["relation_id"]]
        source = row["source_file"]
        if source not in source_cache:
            data = Path(source).read_bytes()
            source_cache[source] = (data.decode("utf-8-sig"), hashlib.sha256(data).hexdigest())
        text, sha = source_cache[source]
        assert row["source_sha256"] == sha, row["gt_id"]
        assert text[row["evidence_char_start"]:row["evidence_char_end"]] == row["evidence_text"], row["gt_id"]
        assert row["source_record_ids"], row["gt_id"]
        if original_ids is not None:
            assert set(row["source_record_ids"]) <= original_ids, row["gt_id"]
        if row["relation_id"] in {"initial_dose", "usual_dose", "maintenance_dose", "recommended_dose",
                                  "maximum_dose", "dose_range", "dose_may_be_increased_to"}:
            import re
            dose_rows += 1
            object_numbers = set(re.findall(r"\d+(?:\.\d+)?", row["entity_2"]))
            source_numbers = set(re.findall(r"\d+(?:\.\d+)?", row["evidence_text"]))
            assert object_numbers <= source_numbers, (row["gt_id"], "unsupported numeric value")

    per_drug_rows = []
    for path in sorted((root / "by_drug").glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        assert all(row["rank"] == doc["rank"] for row in doc["triples"])
        per_drug_rows.extend(doc["triples"])
    assert len(per_drug_rows) == len(rows)
    assert {row["gt_id"] for row in per_drug_rows} == ids

    codekg = json.loads((root / "codekg_format_draft.json").read_text(encoding="utf-8"))
    assert len(codekg) == len(expected_ranks)
    assert {t["gt_id"] for doc in codekg for t in doc["triples"]} == ids
    report = {
        "structural_validation_passed": True,
        "triple_count": len(rows),
        "drug_count": len(source_cache),
        "all_expected_ranks_present": True,
        "rank_range": [rank_start, rank_end],
        "duplicate_gt_ids": 0,
        "source_hash_and_evidence_offsets_verified": True,
        "unmapped_gt_count": 0,
        "source_ids_match_original_decomposition": original_ids is not None,
        "csv_and_per_drug_and_codekg_counts_match": True,
        "dose_numeric_values_verified_against_evidence": dose_rows,
        "clinical_or_semantic_correctness_certified": False,
        "human_review_status": "pending",
        "rank_counts": dict(sorted(Counter(row["rank"] for row in rows).items())),
    }
    (root / "validation_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                                 encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
