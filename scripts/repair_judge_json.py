#!/usr/bin/env python3
"""Recover parse_error judgments of compare_gt_graph_semantics.py whose raw output is valid JSON once a missing
closing quote and/or brace is appended (e.g. '{"status":"no_match",...,"reason":"...}'). The LLM's own verdict is
kept unchanged; repaired rows get "json_repair" with what was appended, and are listed in json_repairs.jsonl.
Rows that cannot be recovered this way are left as parse_error (summarize will then stop and ask for review)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", type=Path, required=True)
    args = ap.parse_args()
    cands = {json.loads(l)["gt"]["gt_id"]: json.loads(l) for l in (args.output_dir / "candidates.jsonl").open(encoding="utf-8")}
    repairs = []
    for path in sorted(args.output_dir.glob("judgments_*.jsonl")):
        rows = [json.loads(l) for l in path.open(encoding="utf-8")]
        changed = False
        for row in rows:
            if row.get("status") != "parse_error":
                continue
            raw = (row.get("raw_output") or "").strip()
            for suffix in ("}", '"}', '"}}'):
                try:
                    rec = json.loads(raw + suffix)
                    allowed = {e["edge_id"] for e in cands[row["gt_id"]]["candidates"]}
                    assert rec["status"] in {"match", "partial", "no_match"}
                    assert rec["status"] == "no_match" or rec.get("edge_id") in allowed
                except (ValueError, KeyError, AssertionError):
                    continue
                row.update({"status": rec["status"], "edge_id": rec.get("edge_id"), "reason": rec.get("reason", ""),
                            "json_repair": f"appended {suffix!r} to raw_output"})
                repairs.append({"file": path.name, "gt_id": row["gt_id"], "status": rec["status"], "appended": suffix})
                changed = True
                break
        if changed:
            with path.open("w", encoding="utf-8") as f:
                for row in rows:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
    if repairs:
        with (args.output_dir / "json_repairs.jsonl").open("a", encoding="utf-8") as f:
            for r in repairs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(json.dumps({"repaired": repairs}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
