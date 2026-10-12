#!/usr/bin/env python3
"""Attach the untouched page sentence to every decomposed sentence produced from coreference-resolved text.

final_sentences_keep_incomplete.jsonl already records 'original_sentence' (the sentence given to the decomposer,
i.e. after pronoun resolution). This adds:
  raw_sentence : the same sentence in the original page text (before pronoun resolution)
  raw_line     : the whole original line (paragraph or list item) it came from
  line_number  : line number in data/text-only/text-only/<file>
Sentences are matched by (file, line number, sentence index); if pronoun resolution changed how NLTK splits that
line, the whole original line is used as raw_sentence and 'raw_match' says so.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from classify_drugs_pilot_sentences import ensure_nltk, extract_directory_records  # noqa: E402


def build_raw_lookup(raw_dir: Path, coref_dir: Path):
    """Return lookup(record_id) -> {raw_sentence, raw_line, line_number, raw_match}."""
    ensure_nltk()
    raw_records, _ = extract_directory_records(raw_dir)
    coref_records, _ = extract_directory_records(coref_dir)
    raw_by_line: dict[tuple, list[str]] = defaultdict(list)
    coref_by_line: dict[tuple, list[str]] = defaultdict(list)
    for r in raw_records:
        raw_by_line[(r["source_file"], r["line_number"])].append(r["sentence"])
    for r in coref_records:
        coref_by_line[(r["source_file"], r["line_number"])].append(r["sentence"])
    raw_lines = {p.name: p.read_text(encoding="utf-8-sig").splitlines() for p in raw_dir.glob("*.txt")}

    def lookup(record_id: str) -> dict:
        source_file, line_number, sentence_index, _ = record_id.split("|")
        key, idx = (source_file, int(line_number)), int(sentence_index)
        raw_sents, coref_sents = raw_by_line.get(key, []), coref_by_line.get(key, [])
        raw_line = raw_lines[source_file][int(line_number) - 1].strip()
        raw_line = raw_line[2:] if raw_line.startswith("- ") else raw_line
        if len(raw_sents) == len(coref_sents) and idx < len(raw_sents):
            return {"raw_sentence": raw_sents[idx], "raw_line": raw_line, "line_number": int(line_number), "raw_match": "sentence"}
        return {"raw_sentence": raw_line, "raw_line": raw_line, "line_number": int(line_number), "raw_match": "line"}

    return lookup


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--final-jsonl", type=Path, required=True)
    ap.add_argument("--raw-dir", type=Path, default=Path("data/text-only/text-only"))
    ap.add_argument("--coref-dir", type=Path, default=Path("data/text-only/coref/text"))
    args = ap.parse_args()

    lookup = build_raw_lookup(args.raw_dir, args.coref_dir)
    rows = [json.loads(l) for l in args.final_jsonl.open(encoding="utf-8")]
    stats = Counter()
    for row in rows:
        row.update(lookup(row["source_record_id"]))
        row["coref_changed"] = row["raw_match"] == "sentence" and row["raw_sentence"] != row["original_sentence"]
        stats[row["raw_match"]] += 1
        stats["coref_changed"] += row["coref_changed"]

    with args.final_jsonl.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps({"rows": len(rows), **stats}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
