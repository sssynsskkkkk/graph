#!/usr/bin/env python3
"""Extract article sentences from saved Drugs.com HTML and classify them."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import nltk
import torch
from bs4 import BeautifulSoup, Tag
from nltk.tokenize import sent_tokenize
from transformers import AutoModelForSequenceClassification, AutoTokenizer


SKIP_ANCESTOR_SELECTORS = (
    "nav, aside, form, footer, script, style, noscript, .noprint, [data-nosnippet], "
    ".ddc-related-link-group, .ddc-carousel-scroll, .ddc-main-content-head"
)

CORE_H2_IDS = {
    "uses",
    "overview",
    "warnings",
    "contraindications",
    "side-effects",
    "before-taking",
    "pregnancy",
    "directions",
    "dosage",
    "missed-dose",
    "overdose",
    "what-to-avoid",
    "interactions",
    "storage",
    "ingredients",
}


def ensure_nltk() -> None:
    for resource, package in (("tokenizers/punkt", "punkt"), ("tokenizers/punkt_tab", "punkt_tab")):
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(package, quiet=False)


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_records(html_path: Path, core_h2_only: bool = False) -> list[dict]:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8", errors="replace"), "html.parser")
    content = soup.select_one("#content") or soup.select_one("main") or soup.body
    if content is None:
        return []

    drug = clean_text((content.select_one("h1") or soup.title).get_text(" ", strip=True))
    skipped_node_ids = {id(node) for node in content.select(SKIP_ANCESTOR_SELECTORS)}
    section = None
    section_id = None
    subsection = None
    include_section = not core_h2_only
    records: list[dict] = []
    block_index = 0

    for element in content.find_all(["h2", "h3", "p", "li"]):
        if id(element) in skipped_node_ids or any(id(parent) in skipped_node_ids for parent in element.parents):
            continue
        text = clean_text(element.get_text(" ", strip=True))
        if not text:
            continue
        if element.name == "h2":
            section = text
            section_id = element.get("id")
            subsection = None
            include_section = not core_h2_only or section_id in CORE_H2_IDS
            continue
        if element.name == "h3":
            subsection = text
            continue
        if not include_section:
            continue

        for sentence_index, sentence in enumerate(sent_tokenize(text)):
            sentence = clean_text(sentence)
            if not sentence:
                continue
            records.append(
                {
                    "drug": drug,
                    "source_file": html_path.name,
                    "section_title": section,
                    "section_id": section_id,
                    "subsection_title": subsection,
                    "block_index": block_index,
                    "sentence_index": sentence_index,
                    "sentence": sentence,
                }
            )
        block_index += 1
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data/raw-crawling/raw-crawling"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/raw-crawling/sentence_classification"))
    parser.add_argument("--model-dir", type=Path, default=Path("models/codekg_bert_large/final_model"))
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--limit-files", type=int)
    parser.add_argument(
        "--core-h2-only",
        action="store_true",
        help="Use only content under core medical h2 sections, up to the next h2.",
    )
    args = parser.parse_args()

    ensure_nltk()
    html_paths = sorted(args.data_dir.glob("*.html"))
    if args.limit_files is not None:
        html_paths = html_paths[: args.limit_files]
    if not html_paths:
        raise RuntimeError(f"No HTML files found in {args.data_dir}")

    records = [
        record
        for path in html_paths
        for record in extract_records(path, core_h2_only=args.core_h2_only)
    ]
    print(f"html_files={len(html_paths)} sentences={len(records)}", flush=True)

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
                model.config.id2label[i]: float(value) for i, value in enumerate(probs)
            }
        if start == 0 or (start // args.batch_size) % 25 == 0:
            print(f"classified={min(start + args.batch_size, len(records))}/{len(records)}", flush=True)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / "sentence_classification.jsonl").open("w", encoding="utf-8") as stream:
        for row in records:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")

    drugs = []
    for html_path in html_paths:
        rows = [row for row in records if row["source_file"] == html_path.name]
        counts = Counter(row["predicted_label"] for row in rows)
        payload = {
            "drug": rows[0]["drug"] if rows else html_path.stem,
            "source_file": str(html_path),
            "model": str(args.model_dir),
            "sentence_count": len(rows),
            "label_counts": dict(sorted(counts.items())),
            "sentences": rows,
        }
        (args.output_dir / f"{html_path.stem}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        drugs.append({key: payload[key] for key in ("drug", "source_file", "sentence_count", "label_counts")})

    total_counts = Counter(row["predicted_label"] for row in records)
    summary = {
        "model": str(args.model_dir),
        "core_h2_only": args.core_h2_only,
        "html_count": len(html_paths),
        "sentence_count": len(records),
        "label_counts": dict(sorted(total_counts.items())),
        "drugs": drugs,
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary["label_counts"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
