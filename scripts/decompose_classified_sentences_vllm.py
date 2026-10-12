#!/usr/bin/env python3
"""Same as decompose_classified_sentences.py (CoDe-KG prompts, greedy decoding, thinking disabled, same output format),
but generation goes through an OpenAI-compatible vLLM server instead of transformers.generate (much faster)."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from openai import OpenAI

sys.path.insert(0, str(Path(__file__).resolve().parent))
from decompose_classified_sentences import PROMPTS, parse_sentences, record_id  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-jsonl", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--base-url", default="http://localhost:8001/v1")
    parser.add_argument("--model", default="codekg-llm")
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--repair-max-new-tokens", type=int, default=1024)
    parser.add_argument("--workers", type=int, default=32)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = [json.loads(line) for line in args.input_jsonl.open(encoding="utf-8")]
    for index, row in enumerate(rows):
        row["record_id"] = record_id(row, index)
    client = OpenAI(base_url=args.base_url, api_key="EMPTY", timeout=600)

    def run(row: dict) -> dict:
        label = row["predicted_label"]
        result = dict(row)
        if label not in PROMPTS:
            result.update({"status": "passthrough" if label == "Simple Sentence" else "excluded_incomplete",
                           "simplified_sentences": [row["sentence"]] if label == "Simple Sentence" else [],
                           "raw_output": None, "parse_success": label == "Simple Sentence"})
            return result
        system, user_template = PROMPTS[label]
        messages = [{"role": "system", "content": system.strip()},
                    {"role": "user", "content": user_template.format(sentence=row["sentence"]).strip()}]

        def generate(max_tokens: int):
            return client.chat.completions.create(
                model=args.model, temperature=0.0, max_tokens=max_tokens, messages=messages,
                extra_body={"chat_template_kwargs": {"enable_thinking": False}}).choices[0]

        choice = generate(args.max_new_tokens)
        repaired = False
        if choice.finish_reason == "length":  # same as repair_truncated_decompositions.py: regenerate with a larger budget
            choice, repaired = generate(args.repair_max_new_tokens), True
        raw = choice.message.content or ""
        simplified = parse_sentences(raw)
        result.update({"status": "decomposed", "simplified_sentences": simplified, "raw_output": raw.strip(),
                       "parse_success": bool(simplified), "finish_reason": choice.finish_reason, "repaired": repaired})
        return result

    with ThreadPoolExecutor(args.workers) as pool:
        final_rows = []
        for k, res in enumerate(pool.map(run, rows), 1):
            final_rows.append(res)
            if k % 1000 == 0:
                print(f"processed={k}/{len(rows)}", flush=True)
    with (args.output_dir / "decomposition.jsonl").open("w", encoding="utf-8") as stream:
        for res in final_rows:
            stream.write(json.dumps(res, ensure_ascii=False) + "\n")

    summary = {
        "input": str(args.input_jsonl), "model": args.model, "input_sentence_count": len(rows),
        "output_record_count": len(final_rows),
        "input_label_counts": dict(sorted(Counter(r["predicted_label"] for r in rows).items())),
        "status_counts": dict(sorted(Counter(r["status"] for r in final_rows).items())),
        "simplified_sentence_count": sum(len(r["simplified_sentences"]) for r in final_rows),
        "decomposition_parse_failures": sum(r["status"] == "decomposed" and not r["parse_success"] for r in final_rows),
        "repaired_outputs": sum(bool(r.get("repaired")) for r in final_rows),
        "still_truncated_outputs": sum(r.get("finish_reason") == "length" for r in final_rows),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
