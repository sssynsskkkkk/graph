"""Build EDC input chunks from the two alternative text sources used in the experiments.

  text      : data/text/<slug>.txt        (section-structured plain text exported from the parsed pages)
  sentences : data/final_sentences_keep_incomplete.jsonl  (Code-KG style decomposition into simple sentences)
"""
from __future__ import annotations
import collections
import json
import pathlib
import re

from .chunk import chunk_record

TEXT_DIR_DEFAULT = "data/text"
SENT_FILE_DEFAULT = "data/final_sentences_keep_incomplete.jsonl"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def text_file_to_record(path: pathlib.Path) -> dict:
    """Parse a data/text file ('# Title', 'Source: url', '## Section' + lines) into a record for chunk_record()."""
    lines = path.read_text(encoding="utf-8").split("\n")
    title, url, sections, cur = None, None, [], None
    for line in lines:
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        elif line.startswith("Source: "):
            url = line[8:].strip()
        elif line.startswith("## "):
            heading = line[3:].strip()
            cur = {"id": slugify(heading), "page": "main", "heading": heading, "lines": []}
            sections.append(cur)
        elif line.strip() and cur is not None:
            cur["lines"].append(line.rstrip())
    for s in sections:
        s["text"] = "\n".join(s["lines"])
    return {"name": title, "title": title, "slug": path.stem, "url": url, "sections": sections}


def chunks_from_text(text_dir: pathlib.Path, max_chars: int, min_chars: int, exclude: list[str]) -> dict[str, list[dict]]:
    out = {}
    for f in sorted(text_dir.glob("*.txt")):
        rec = text_file_to_record(f)
        out[rec["slug"]] = chunk_record(rec, max_chars, min_chars, None, True, exclude)
    return out


def sentence_provenance(row: dict) -> dict:
    """Where a decomposed sentence came from: the sentence given to the decomposer ('original_sentence', after
    coreference resolution when that stage ran) and the untouched page sentence ('raw_sentence', if recorded)."""
    return {"sentence": row.get("sentence"), "kind": row.get("output_kind"), "record_id": row.get("source_record_id"),
            "output_index": row.get("output_index"),
            "decomposer_input": row.get("original_sentence"),
            "raw_sentence": row.get("raw_sentence") or row.get("original_sentence"),
            "coref_changed": bool(row.get("raw_sentence")) and row.get("raw_sentence") != row.get("original_sentence")}


def chunks_from_sentences(path: pathlib.Path, max_chars: int, sentence_level: bool = False,
                          exclude_headings: tuple[str, ...] = ("popular faq",), keep_incomplete: bool = True) -> dict[str, list[dict]]:
    """Group decomposed sentences by (drug, section) in file order and pack them into chunks of <= max_chars.
    With sentence_level=True every sentence becomes its own chunk (closest to the EDC paper's sentence-level setting)."""
    rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    by_drug: dict[str, list[dict]] = collections.defaultdict(list)
    for r in rows:
        if not keep_incomplete and r.get("output_kind") == "incomplete_passthrough":
            continue
        if (r.get("section_title") or "").strip().lower() in exclude_headings:
            continue
        by_drug[r["source_file"].replace(".txt", "")].append(r)
    out: dict[str, list[dict]] = {}
    for slug, rs in by_drug.items():
        drug = rs[0]["drug"]
        chunks, cur, cur_len, sec_counter = [], [], 0, collections.Counter()
        cur_rows: list[dict] = []
        cur_sec = None

        def flush():
            if cur:
                sid = slugify(cur_sec or "section")
                idx = sec_counter[sid]
                sec_counter[sid] += 1
                chunks.append({"chunk_id": f"{slug}#{sid}#{idx}", "drug": drug, "slug": slug, "section_id": sid,
                               "section_heading": cur_sec or "", "page": "sentences", "text": "\n".join(cur),
                               "source_url": f"https://www.drugs.com/{slug.replace('__', '/')}.html",
                               "n_sentences": len(cur), "sentences": [sentence_provenance(r) for r in cur_rows]})

        for r in rs:
            sec = r.get("section_title") or ""
            sent = (r.get("sentence") or "").strip()
            if not sent:
                continue
            if sec != cur_sec or sentence_level or (cur and cur_len + len(sent) + 1 > max_chars):
                flush()
                cur, cur_len, cur_rows = [], 0, []
                cur_sec = sec
            cur.append(sent)
            cur_rows.append(r)
            cur_len += len(sent) + 1
        flush()
        out[slug] = chunks
    return out
