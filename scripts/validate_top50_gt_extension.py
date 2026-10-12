#!/usr/bin/env python3
"""Verify that the top-50 annotation export preserves the previous top-25 draft."""

from __future__ import annotations

import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream]


def main() -> None:
    root = Path("data/gt_top50_review")
    previous = read_jsonl(Path("data/gt_top25_review/gold_triplets_draft.jsonl"))
    combined = read_jsonl(root / "gold_triplets_draft.jsonl")
    preserved = [row for row in combined if row["rank"] <= 25]
    added = [row for row in combined if row["rank"] >= 26]
    assert preserved == previous, "Existing top-25 records changed"
    assert {row["rank"] for row in added} == set(range(26, 51))
    assert {row["rank"] for row in combined} == set(range(1, 51))
    assert len({row["source_file"] for row in combined}) == 50
    assert len({row["gt_id"] for row in combined}) == len(combined)
    assert combined == preserved + added, "Unexpected rank ordering"
    report = {
        "extension_validation_passed": True,
        "existing_top25_records_unchanged": True,
        "preserved_triple_count": len(preserved),
        "added_rank_range": [26, 50],
        "added_triple_count": len(added),
        "combined_rank_range": [1, 50],
        "combined_drug_count": 50,
        "combined_triple_count": len(combined),
        "clinical_or_semantic_correctness_certified": False,
    }
    (root / "extension_validation.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
