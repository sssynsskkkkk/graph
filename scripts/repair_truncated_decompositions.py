#!/usr/bin/env python3
"""Regenerate decomposition rows whose prior output hit the token ceiling."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from decompose_classified_sentences import PROMPTS, parse_sentences


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-jsonl", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--threshold", type=int, default=250)
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--batch-size", type=int, default=2)
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    tokenizer.padding_side = "left"
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    rows = [json.loads(line) for line in args.result_jsonl.open(encoding="utf-8")]
    repair_indices = [
        index
        for index, row in enumerate(rows)
        if row.get("status") == "decomposed"
        and len(tokenizer.encode(row.get("raw_output") or "", add_special_tokens=False)) >= args.threshold
    ]
    print(f"rows={len(rows)} repair_targets={len(repair_indices)}", flush=True)
    if not repair_indices:
        return 0

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        local_files_only=True,
        dtype=torch.bfloat16,
        device_map={"": 0},
        low_cpu_mem_usage=True,
    ).eval()

    for start in range(0, len(repair_indices), args.batch_size):
        indices = repair_indices[start : start + args.batch_size]
        rendered = []
        for index in indices:
            row = rows[index]
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
        for index, raw in zip(indices, outputs):
            simplified = parse_sentences(raw)
            rows[index]["raw_output"] = raw.strip()
            rows[index]["simplified_sentences"] = simplified
            rows[index]["parse_success"] = bool(simplified)
            rows[index]["repaired_token_limit"] = True
        print(f"repaired={min(start + len(indices), len(repair_indices))}/{len(repair_indices)}", flush=True)

    temporary = args.result_jsonl.with_suffix(".jsonl.tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    temporary.replace(args.result_jsonl)
    print(f"wrote={args.result_jsonl}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
