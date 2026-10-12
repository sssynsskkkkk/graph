#!/usr/bin/env python3
"""Per-sentence trace of the coref -> classification -> decomposition pipeline.

For every sentence of the original page text it records
  raw_sentence     the sentence as it appears on the page (data/text-only/text-only)
  coref_sentence   the same sentence after pronoun resolution (input of the classifier and the decomposer)
  coref_edits      [[original words, replacement], ...]
  label            BERT sentence-complexity class (+ confidence)
  status           decomposed | passthrough (simple) | excluded_incomplete (kept as is)
  decomposer_output  raw LLM answer of the decomposition prompt
  decomposed       [{output_index, sentence}, ...] sentences handed to EDC

Writes <out>/trace.jsonl, <out>/md/<file>.md (human-readable, one file per drug) and <out>/summary.json.
"""

from __future__ import annotations

import argparse
import difflib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from attach_raw_sentences import build_raw_lookup  # noqa: E402


def word_edits(before: str, after: str) -> list[list[str]]:
    a, b = before.split(), after.split()
    edits = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op != "equal":
            edits.append([" ".join(a[i1:i2]), " ".join(b[j1:j2])])
    return edits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--decomposition-jsonl", type=Path, required=True)
    ap.add_argument("--final-jsonl", type=Path, required=True)
    ap.add_argument("--raw-dir", type=Path, default=Path("data/text-only/text-only"))
    ap.add_argument("--coref-dir", type=Path, default=Path("data/text-only/coref/text"))
    ap.add_argument("--output-dir", type=Path, required=True)
    args = ap.parse_args()

    lookup = build_raw_lookup(args.raw_dir, args.coref_dir)
    final_by_record = defaultdict(list)
    for line in args.final_jsonl.open(encoding="utf-8"):
        r = json.loads(line)
        final_by_record[r["source_record_id"]].append({"output_index": r["output_index"], "sentence": r["sentence"],
                                                       "kind": r["output_kind"]})
    rows = [json.loads(l) for l in args.decomposition_jsonl.open(encoding="utf-8")]
    rows.sort(key=lambda r: int(r["record_id"].rsplit("|", 1)[-1]))

    (args.output_dir / "md").mkdir(parents=True, exist_ok=True)
    stats, per_file = Counter(), defaultdict(list)
    with (args.output_dir / "trace.jsonl").open("w", encoding="utf-8") as out:
        for r in rows:
            raw = lookup(r["record_id"])
            edits = word_edits(raw["raw_sentence"], r["sentence"]) if raw["raw_match"] == "sentence" else []
            t = {"record_id": r["record_id"], "drug": r["drug"], "source_file": r["source_file"],
                 "section_title": r.get("section_title"), "subsection_title": r.get("subsection_title"),
                 "source_kind": r.get("source_kind"), "line_number": raw["line_number"],
                 "sentence_index": r.get("sentence_index"), "raw_sentence": raw["raw_sentence"],
                 "raw_line": raw["raw_line"], "raw_match": raw["raw_match"], "coref_sentence": r["sentence"],
                 "coref_edits": edits, "label": r["predicted_label"], "confidence": round(r.get("confidence", 0), 3),
                 "status": r["status"], "repaired": bool(r.get("repaired")), "decomposer_output": r.get("raw_output"),
                 "decomposed": final_by_record.get(r["record_id"], [])}
            out.write(json.dumps(t, ensure_ascii=False) + "\n")
            per_file[r["source_file"]].append(t)
            stats["sentences"] += 1
            stats[f"status_{t['status']}"] += 1
            stats["coref_changed_sentences"] += bool(edits)
            stats["coref_edits"] += len(edits)
            stats["decomposed_sentences_out"] += len(t["decomposed"])
            stats["no_output_sentences"] += not t["decomposed"]

    for source_file, ts in per_file.items():
        md = [f"# {ts[0]['drug']} — pronoun resolution → sentence classification → decomposition", "",
              f"Source: `{args.raw_dir / source_file}` · {len(ts)} sentences · "
              f"{sum(bool(t['coref_edits']) for t in ts)} changed by pronoun resolution · "
              f"{sum(len(t['decomposed']) for t in ts)} sentences sent to EDC", ""]
        section = None
        for t in ts:
            if t["section_title"] != section:
                section = t["section_title"]
                md += [f"## {section}", ""]
            md.append(f"**L{t['line_number']}.{t['sentence_index']}** `{t['label']}` ({t['confidence']}) → `{t['status']}`"
                      + (" · repaired" if t["repaired"] else ""))
            md.append(f"- original: {t['raw_sentence']}")
            if t["coref_edits"]:
                md.append(f"- pronoun resolved: {t['coref_sentence']}")
                md.append("  - edits: " + "; ".join(f"“{a}” → “{b}”" for a, b in t["coref_edits"]))
            elif t["raw_match"] == "line" and t["coref_sentence"] != t["raw_sentence"]:
                md.append(f"- pronoun resolved (line re-split): {t['coref_sentence']}")
            if t["status"] == "decomposed":
                for d in t["decomposed"]:
                    md.append(f"  - S{d['output_index'] + 1}: {d['sentence']}")
                if not t["decomposed"]:
                    md.append("  - (decomposition produced no parsable sentence)")
            md.append("")
        (args.output_dir / "md" / f"{Path(source_file).stem}.md").write_text("\n".join(md), encoding="utf-8")

    (args.output_dir / "summary.json").write_text(json.dumps(dict(stats), indent=2), encoding="utf-8")
    print(json.dumps(dict(stats)), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
