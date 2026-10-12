#!/usr/bin/env python3
"""Flatten decomposition output while retaining incomplete inputs unchanged."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-jsonl", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    rows = [json.loads(line) for line in args.input_jsonl.open(encoding="utf-8")]
    # The decomposition job appends generated records after pass-through records.
    # Restore the original source order using the final index in record_id.
    rows.sort(key=lambda row: int(row["record_id"].rsplit("|", 1)[-1]))
    output: list[dict] = []

    for row in rows:
        status = row["status"]
        if status == "decomposed":
            sentences = row["simplified_sentences"]
            output_kind = "llm_decomposed"
        elif status == "passthrough":
            sentences = [row["sentence"]]
            output_kind = "simple_passthrough"
        elif status == "excluded_incomplete":
            sentences = [row["sentence"]]
            output_kind = "incomplete_passthrough"
        else:
            raise ValueError(f"Unknown status: {status}")

        for output_index, sentence in enumerate(sentences):
            output.append(
                {
                    "drug": row.get("drug"),
                    "source_file": row.get("source_file"),
                    "section_title": row.get("section_title"),
                    "subsection_title": row.get("subsection_title"),
                    "source_record_id": row.get("record_id"),
                    "source_label": row.get("predicted_label"),
                    "source_status": status,
                    "output_kind": output_kind,
                    "output_index": output_index,
                    "original_sentence": row.get("sentence"),
                    "sentence": sentence,
                }
            )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = args.output_dir / "final_sentences_keep_incomplete.jsonl"
    txt_path = args.output_dir / "final_sentences_keep_incomplete.txt"
    with jsonl_path.open("w", encoding="utf-8") as stream:
        for row in output:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    with txt_path.open("w", encoding="utf-8") as stream:
        for row in output:
            stream.write(row["sentence"].replace("\n", " ").strip() + "\n")

    summary = {
        "source": str(args.input_jsonl),
        "input_record_count": len(rows),
        "output_sentence_count": len(output),
        "output_kind_counts": dict(sorted(Counter(row["output_kind"] for row in output).items())),
        "drug_count": len({row["drug"] for row in output if row.get("drug")}),
        "jsonl": str(jsonl_path),
        "txt": str(txt_path),
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
