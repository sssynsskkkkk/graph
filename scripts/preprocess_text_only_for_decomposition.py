#!/usr/bin/env python3
"""Create a context-restored alternative to the raw text-only sentence records."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


IMPERATIVE = re.compile(
    r"^(avoid|tell|take|keep|call|seek|use|ask|follow|stop|contact|talk|store|swallow|"
    r"rinse|read|give|check|get|protect|dispose|place|shake|inject|replace|remove|apply|"
    r"wear|drink|eat|wait|watch|monitor|report|inform|notify)\b",
    re.IGNORECASE,
)
DO_NOT = re.compile(r"^do not\s+", re.IGNORECASE)
NEVER = re.compile(r"^never\s+", re.IGNORECASE)
DOSE_FIELD = re.compile(
    r"^(initial|maintenance|maximum|recommended|usual|starting)\s+dose:\s*(.+)$",
    re.IGNORECASE,
)


def finish_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if text and text[-1] not in ".?!":
        text += "."
    return text


def normalize_imperative(text: str) -> tuple[str, bool]:
    text = finish_sentence(text)
    if DO_NOT.match(text):
        return "You should not " + DO_NOT.sub("", text, count=1), True
    if NEVER.match(text):
        return "You should never " + NEVER.sub("", text, count=1), True
    if IMPERATIVE.match(text):
        return "You should " + text[0].lower() + text[1:], True
    return text, False


def normalize_standalone(text: str) -> tuple[str, list[str]]:
    operations: list[str] = []
    dose = DOSE_FIELD.match(text.strip())
    if dose:
        text = f"The {dose.group(1).lower()} dose is {dose.group(2)}"
        operations.append("dose_field_to_sentence")
    text, changed = normalize_imperative(text)
    if changed:
        operations.append("imperative_subject_restored")
    return finish_sentence(text), operations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-jsonl",
        type=Path,
        default=Path("data/text-only/sentence_classification/sentence_classification.jsonl"),
    )
    parser.add_argument(
        "--output-jsonl",
        type=Path,
        default=Path("data/text-only/preprocessed/sentences.jsonl"),
    )
    args = parser.parse_args()

    rows = [json.loads(line) for line in args.input_jsonl.open(encoding="utf-8")]
    output: list[dict] = []
    removed_headings = 0
    combined_lists = 0
    imperative_restored = 0
    index = 0

    while index < len(rows):
        row = rows[index]
        text = row["sentence"].strip()

        # A colon line immediately followed by list items supplies their missing context.
        if text.endswith(":") and index + 1 < len(rows) and rows[index + 1]["source_kind"] == "list_item":
            cursor = index + 1
            while (
                cursor < len(rows)
                and rows[cursor]["source_kind"] == "list_item"
                and rows[cursor].get("source_file") == row.get("source_file")
                and rows[cursor].get("section_title") == row.get("section_title")
            ):
                item = rows[cursor]
                combined = text[:-1].rstrip() + " " + item["sentence"].lstrip()
                normalized, operations = normalize_standalone(combined)
                operations.insert(0, "list_context_joined")
                imperative_restored += int("imperative_subject_restored" in operations)
                new_row = {
                    key: value
                    for key, value in item.items()
                    if key not in {"predicted_label", "confidence", "probabilities", "sentence"}
                }
                new_row.update(
                    {
                        "sentence": normalized,
                        "original_sentence": item["sentence"],
                        "context_sentence": text,
                        "preprocessing_operations": operations,
                    }
                )
                output.append(new_row)
                combined_lists += 1
                cursor += 1
            index = cursor
            continue

        # Short colon-terminated labels are structural subheadings, not sentences.
        if text.endswith(":") and len(text.split()) <= 12:
            removed_headings += 1
            index += 1
            continue

        normalized, operations = normalize_standalone(text)
        imperative_restored += int("imperative_subject_restored" in operations)
        new_row = {
            key: value
            for key, value in row.items()
            if key not in {"predicted_label", "confidence", "probabilities", "sentence"}
        }
        new_row.update(
            {
                "sentence": normalized,
                "original_sentence": text,
                "context_sentence": None,
                "preprocessing_operations": operations,
            }
        )
        output.append(new_row)
        index += 1

    args.output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with args.output_jsonl.open("w", encoding="utf-8") as stream:
        for row in output:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(
        json.dumps(
            {
                "input_sentences": len(rows),
                "output_sentences": len(output),
                "removed_structural_headings": removed_headings,
                "list_items_with_context": combined_lists,
                "imperatives_with_subject_restored": imperative_restored,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
