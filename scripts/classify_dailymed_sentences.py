#!/usr/bin/env python3
"""Classify sentences in the 50 downloaded DailyMed labels with CoDe-KG BERT-Large."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import nltk
import torch
from nltk.tokenize import sent_tokenize
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def ensure_nltk() -> None:
    for resource, package in (("tokenizers/punkt", "punkt"), ("tokenizers/punkt_tab", "punkt_tab")):
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(package, quiet=False)


def split_sentences(text: str) -> list[str]:
    if not text or not text.strip():
        return []
    return [sentence.strip() for sentence in sent_tokenize(text.strip()) if sentence.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data/dailymed_top50_2024"))
    parser.add_argument("--model-dir", type=Path, default=Path("models/codekg_bert_large/final_model"))
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--max-length", type=int, default=512)
    args = parser.parse_args()

    ensure_nltk()
    label_paths = sorted(args.data_dir.glob("[0-9][0-9]_*/label.json"))
    if len(label_paths) != 50:
        raise RuntimeError(f"Expected 50 label files, found {len(label_paths)}")

    records: list[dict] = []
    for label_path in label_paths:
        label = json.loads(label_path.read_text(encoding="utf-8"))
        drug_dir = label_path.parent.name
        for section_index, section in enumerate(label.get("sections", [])):
            section_text = section.get("text") or ""
            for sentence_index, sentence in enumerate(split_sentences(section_text)):
                records.append({
                    "rank": label["rank"],
                    "drug": label["query_name"],
                    "drug_dir": drug_dir,
                    "setid": label["selected_label"]["setid"],
                    "source_url": label["source_url"],
                    "section_index": section_index,
                    "section_code": section.get("code"),
                    "section_title": section.get("title"),
                    "sentence_index": sentence_index,
                    "sentence": sentence,
                })
    print(f"labels={len(label_paths)} sentences={len(records)}", flush=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(args.model_dir)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model.to(device)
    if torch.cuda.device_count() > 1:
        model = torch.nn.DataParallel(model)
    model.eval()
    config = model.module.config if isinstance(model, torch.nn.DataParallel) else model.config

    for start in range(0, len(records), args.batch_size):
        batch_records = records[start : start + args.batch_size]
        sentences = [item["sentence"] for item in batch_records]
        encoded = tokenizer(
            sentences,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=args.max_length,
        ).to(device)
        with torch.inference_mode(), torch.autocast(device_type="cuda", enabled=device.type == "cuda"):
            logits = model(**encoded).logits
            probabilities = torch.softmax(logits.float(), dim=-1)
        confidence, predicted = probabilities.max(dim=-1)
        for item, pred, conf in zip(batch_records, predicted.cpu().tolist(), confidence.cpu().tolist()):
            item["predicted_label"] = config.id2label[int(pred)]
            item["confidence"] = float(conf)
        if start == 0 or (start // args.batch_size) % 25 == 0:
            print(f"classified={min(start + args.batch_size, len(records))}/{len(records)}", flush=True)

    master_path = args.data_dir / "sentence_classification.jsonl"
    with master_path.open("w", encoding="utf-8") as stream:
        for item in records:
            stream.write(json.dumps(item, ensure_ascii=False) + "\n")

    total_counts = Counter(item["predicted_label"] for item in records)
    drug_summaries = []
    for label_path in label_paths:
        drug_dir = label_path.parent.name
        drug_records = [item for item in records if item["drug_dir"] == drug_dir]
        counts = Counter(item["predicted_label"] for item in drug_records)
        payload = {
            "drug": drug_records[0]["drug"] if drug_records else drug_dir,
            "rank": drug_records[0]["rank"] if drug_records else None,
            "model": str(args.model_dir),
            "sentence_count": len(drug_records),
            "label_counts": dict(sorted(counts.items())),
            "sentences": drug_records,
        }
        (label_path.parent / "sentence_classification.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        drug_summaries.append({key: payload[key] for key in ("rank", "drug", "sentence_count", "label_counts")})

    summary = {
        "model": str(args.model_dir),
        "label_count": len(label_paths),
        "sentence_count": len(records),
        "label_counts": dict(sorted(total_counts.items())),
        "drugs": drug_summaries,
    }
    (args.data_dir / "sentence_classification_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary["label_counts"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
