#!/usr/bin/env python3
"""Decompose classified sentences with one local chat LLM and CoDe-KG prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


CODEKG_DIR = Path(__file__).resolve().parents[1] / "external" / "CoDe-KG_EMNLP_2025" / "CoDe-KG"
sys.path.insert(0, str(CODEKG_DIR))
from prompts import (  # noqa: E402
    SIMPLIFY_COMPLEX_SYSTEM,
    SIMPLIFY_COMPLEX_USER,
    SIMPLIFY_COMPOUND_COMPLEX_SYSTEM,
    SIMPLIFY_COMPOUND_COMPLEX_USER,
    SIMPLIFY_COMPOUND_SYSTEM,
    SIMPLIFY_COMPOUND_USER,
)


PROMPTS = {
    "Compound Sentence": (SIMPLIFY_COMPOUND_SYSTEM, SIMPLIFY_COMPOUND_USER),
    "Complex Sentence": (SIMPLIFY_COMPLEX_SYSTEM, SIMPLIFY_COMPLEX_USER),
    "Compound-Complex Sentence": (
        SIMPLIFY_COMPOUND_COMPLEX_SYSTEM,
        SIMPLIFY_COMPOUND_COMPLEX_USER,
    ),
}


def parse_sentences(raw: str) -> list[str]:
    results: list[str] = []
    for line in raw.splitlines():
        line = line.strip()
        match = re.match(r"^S\d+\s*(?:->|→|:)\s*(.+?)\s*$", line, re.IGNORECASE)
        if match:
            sentence = match.group(1).strip()
            if sentence:
                results.append(sentence)
    return results


def record_id(row: dict, index: int) -> str:
    return "|".join(
        [
            str(row.get("source_file", "")),
            str(row.get("line_number", "")),
            str(row.get("sentence_index", "")),
            str(index),
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-jsonl", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "decomposition.jsonl"
    rows = [json.loads(line) for line in args.input_jsonl.open(encoding="utf-8")]
    for index, row in enumerate(rows):
        row["record_id"] = record_id(row, index)

    completed: set[str] = set()
    if output_path.exists():
        for line in output_path.open(encoding="utf-8"):
            try:
                completed.add(json.loads(line)["record_id"])
            except (json.JSONDecodeError, KeyError):
                pass

    # Record pass-through and excluded inputs before loading the large model.
    with output_path.open("a", encoding="utf-8") as stream:
        for row in rows:
            if row["record_id"] in completed or row["predicted_label"] in PROMPTS:
                continue
            label = row["predicted_label"]
            result = dict(row)
            result.update(
                {
                    "status": "passthrough" if label == "Simple Sentence" else "excluded_incomplete",
                    "simplified_sentences": [row["sentence"]] if label == "Simple Sentence" else [],
                    "raw_output": None,
                    "parse_success": label == "Simple Sentence",
                }
            )
            stream.write(json.dumps(result, ensure_ascii=False) + "\n")
            completed.add(row["record_id"])

    targets = [row for row in rows if row["predicted_label"] in PROMPTS and row["record_id"] not in completed]
    print(
        f"input={len(rows)} already_completed={len(completed)} decomposition_targets={len(targets)}",
        flush=True,
    )

    if targets:
        tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
        tokenizer.padding_side = "left"
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(
            args.model,
            local_files_only=True,
            dtype=torch.bfloat16,
            device_map={"": 0},
            low_cpu_mem_usage=True,
        ).eval()
        print(f"model_loaded={args.model} device={next(model.parameters()).device}", flush=True)

        with output_path.open("a", encoding="utf-8") as stream:
            for start in range(0, len(targets), args.batch_size):
                batch = targets[start : start + args.batch_size]
                rendered: list[str] = []
                for row in batch:
                    system, user_template = PROMPTS[row["predicted_label"]]
                    messages = [
                        {"role": "system", "content": system.strip()},
                        {"role": "user", "content": user_template.format(sentence=row["sentence"]).strip()},
                    ]
                    rendered.append(
                        tokenizer.apply_chat_template(
                            messages,
                            tokenize=False,
                            add_generation_prompt=True,
                            enable_thinking=False,
                        )
                    )

                encoded = tokenizer(
                    rendered,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=2048,
                ).to(model.device)
                with torch.inference_mode():
                    generated = model.generate(
                        **encoded,
                        max_new_tokens=args.max_new_tokens,
                        do_sample=False,
                        use_cache=True,
                        pad_token_id=tokenizer.pad_token_id,
                        eos_token_id=tokenizer.eos_token_id,
                    )
                prompt_length = encoded["input_ids"].shape[1]
                outputs = tokenizer.batch_decode(generated[:, prompt_length:], skip_special_tokens=True)
                for row, raw in zip(batch, outputs):
                    simplified = parse_sentences(raw)
                    result = dict(row)
                    result.update(
                        {
                            "status": "decomposed",
                            "simplified_sentences": simplified,
                            "raw_output": raw.strip(),
                            "parse_success": bool(simplified),
                        }
                    )
                    stream.write(json.dumps(result, ensure_ascii=False) + "\n")
                    stream.flush()

                done = min(start + len(batch), len(targets))
                if start == 0 or (start // args.batch_size) % 25 == 0:
                    print(f"decomposed={done}/{len(targets)}", flush=True)

    final_rows = [json.loads(line) for line in output_path.open(encoding="utf-8")]
    status_counts = Counter(row["status"] for row in final_rows)
    parse_failures = sum(row["status"] == "decomposed" and not row["parse_success"] for row in final_rows)
    simplified_count = sum(len(row["simplified_sentences"]) for row in final_rows)
    summary = {
        "input": str(args.input_jsonl),
        "model": args.model,
        "input_sentence_count": len(rows),
        "output_record_count": len(final_rows),
        "input_label_counts": dict(sorted(Counter(row["predicted_label"] for row in rows).items())),
        "status_counts": dict(sorted(status_counts.items())),
        "simplified_sentence_count": simplified_count,
        "decomposition_parse_failures": parse_failures,
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
