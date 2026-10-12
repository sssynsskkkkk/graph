#!/usr/bin/env python3
"""Classify sentences from the cleaned, Markdown-like drugs HTML pilot text."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import nltk
import torch
from nltk.tokenize import sent_tokenize
from transformers import AutoModelForSequenceClassification, AutoTokenizer


TOP_HEADING = re.compile(r"^(.{1,100}?)\s+—\s+(.+)$")
MARKDOWN_HEADING = re.compile(r"^#{1,6}\s+(.+)$")
LIST_ITEM = re.compile(r"^\s*[-*]\s+(.+)$")


def ensure_nltk() -> None:
    for resource, package in (("tokenizers/punkt", "punkt"), ("tokenizers/punkt_tab", "punkt_tab")):
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(package, quiet=False)


def extract_records(path: Path) -> tuple[list[dict], list[str]]:
    records: list[dict] = []
    drug_order: list[str] = []
    current_drug: str | None = None
    section: str | None = None
    subsection: str | None = None

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        line = re.sub(r"\s+", " ", raw_line).strip()
        if not line:
            continue

        heading_match = TOP_HEADING.match(line)
        if heading_match:
            current_drug, section = heading_match.groups()
            subsection = None
            if current_drug not in drug_order:
                drug_order.append(current_drug)
            continue

        markdown_match = MARKDOWN_HEADING.match(line)
        if markdown_match:
            subsection = markdown_match.group(1)
            continue

        list_match = LIST_ITEM.match(line)
        source_kind = "list_item" if list_match else "paragraph"
        text = list_match.group(1) if list_match else line
        for sentence_index, sentence in enumerate(sent_tokenize(text)):
            sentence = sentence.strip()
            if sentence:
                records.append(
                    {
                        "drug": current_drug,
                        "section_title": section,
                        "subsection_title": subsection,
                        "source_kind": source_kind,
                        "line_number": line_number,
                        "sentence_index": sentence_index,
                        "sentence": sentence,
                    }
                )
    return records, drug_order


def extract_directory_records(input_dir: Path) -> tuple[list[dict], list[str]]:
    records: list[dict] = []
    drug_order: list[str] = []

    for path in sorted(input_dir.glob("*.txt")):
        drug = path.stem
        section: str | None = None
        subsection: str | None = None
        for line_number, raw_line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
            line = re.sub(r"\s+", " ", raw_line).strip()
            if not line:
                continue
            if line.startswith("# "):
                drug = line[2:].strip()
                if drug not in drug_order:
                    drug_order.append(drug)
                continue
            if line.startswith("### "):
                subsection = line[4:].strip()
                continue
            if line.startswith("## "):
                section = line[3:].strip()
                subsection = None
                continue
            if line.lower().startswith("source:"):
                continue

            list_match = LIST_ITEM.match(line)
            source_kind = "list_item" if list_match else "paragraph"
            text = list_match.group(1) if list_match else line
            for sentence_index, sentence in enumerate(sent_tokenize(text)):
                sentence = sentence.strip()
                if sentence:
                    records.append(
                        {
                            "drug": drug,
                            "source_file": path.name,
                            "section_title": section,
                            "subsection_title": subsection,
                            "source_kind": source_kind,
                            "line_number": line_number,
                            "sentence_index": sentence_index,
                            "sentence": sentence,
                        }
                    )
        if drug not in drug_order:
            drug_order.append(drug)

    return records, drug_order


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("data/drugs_html_pilot.txt"))
    parser.add_argument("--input-dir", type=Path)
    parser.add_argument("--input-jsonl", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("data/drugs_html_pilot_classification"))
    parser.add_argument("--model-dir", type=Path, default=Path("models/codekg_bert_large/final_model"))
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--max-length", type=int, default=512)
    args = parser.parse_args()

    ensure_nltk()
    if args.input_jsonl:
        records = [json.loads(line) for line in args.input_jsonl.open(encoding="utf-8")]
        drug_order = list(dict.fromkeys(row["drug"] for row in records))
        source = str(args.input_jsonl)
    elif args.input_dir:
        records, drug_order = extract_directory_records(args.input_dir)
        source = str(args.input_dir)
    else:
        records, drug_order = extract_records(args.input)
        source = str(args.input)
    print(f"drugs={len(drug_order)} sentences={len(records)}", flush=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(args.model_dir, local_files_only=True)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model.to(device).eval()
    print(f"device={device} labels={model.config.id2label}", flush=True)

    for start in range(0, len(records), args.batch_size):
        batch = records[start : start + args.batch_size]
        encoded = tokenizer(
            [row["sentence"] for row in batch],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=args.max_length,
        ).to(device)
        with torch.inference_mode(), torch.autocast(device_type="cuda", enabled=device.type == "cuda"):
            probabilities = torch.softmax(model(**encoded).logits.float(), dim=-1)
        confidence, predicted = probabilities.max(dim=-1)
        for row, pred, conf, probs in zip(
            batch,
            predicted.cpu().tolist(),
            confidence.cpu().tolist(),
            probabilities.cpu().tolist(),
        ):
            row["predicted_label"] = model.config.id2label[int(pred)]
            row["confidence"] = float(conf)
            row["probabilities"] = {
                model.config.id2label[index]: float(value) for index, value in enumerate(probs)
            }
        if start == 0 or (start // args.batch_size) % 25 == 0:
            print(f"classified={min(start + args.batch_size, len(records))}/{len(records)}", flush=True)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    master_path = args.output_dir / "sentence_classification.jsonl"
    with master_path.open("w", encoding="utf-8") as stream:
        for row in records:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")

    drug_summaries = []
    for drug in drug_order:
        rows = [row for row in records if row["drug"] == drug]
        counts = Counter(row["predicted_label"] for row in rows)
        drug_summaries.append(
            {
                "drug": drug,
                "sentence_count": len(rows),
                "label_counts": dict(sorted(counts.items())),
            }
        )

    total_counts = Counter(row["predicted_label"] for row in records)
    summary = {
        "source": source,
        "model": str(args.model_dir),
        "drug_count": len(drug_order),
        "sentence_count": len(records),
        "label_counts": dict(sorted(total_counts.items())),
        "source_kind_counts": dict(sorted(Counter(row["source_kind"] for row in records).items())),
        "drugs": drug_summaries,
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary["label_counts"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
