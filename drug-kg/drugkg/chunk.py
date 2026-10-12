"""Split parsed page sections into LLM-sized text chunks with provenance."""
from __future__ import annotations
import re

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\"'])")


def _split_long(line: str, max_chars: int) -> list[str]:
    if len(line) <= max_chars:
        return [line]
    pieces, cur = [], ""
    for sent in SENT_SPLIT.split(line):
        if cur and len(cur) + len(sent) + 1 > max_chars:
            pieces.append(cur)
            cur = sent
        else:
            cur = f"{cur} {sent}".strip()
    if cur:
        pieces.append(cur)
    return pieces


def chunk_record(record: dict, max_chars: int = 1100, min_chars: int = 150, include: list[str] | None = None,
                 include_unlisted: bool = True, exclude: list[str] | None = None) -> list[dict]:
    include = set(include or [])
    exclude = set(exclude or [])
    chunks: list[dict] = []
    drug = record.get("title") or record.get("name")
    seen_ids: dict[str, int] = {}
    for section in record.get("sections", []):
        sid = section["id"]
        seen_ids[sid] = seen_ids.get(sid, 0) + 1
        if seen_ids[sid] > 1:  # pages occasionally repeat an h2 id (e.g. two 'warnings' sections)
            sid = f"{sid}-{seen_ids[sid]}"
        base_id = sid.split(":", 1)[-1]
        if base_id in exclude or sid in exclude:
            continue
        if not include_unlisted and base_id not in include:
            continue
        lines: list[str] = []
        for line in section["lines"]:
            lines.extend(_split_long(line, max_chars))
        groups: list[list[str]] = []
        cur: list[str] = []
        cur_len = 0
        for line in lines:
            if cur and cur_len + len(line) + 1 > max_chars:
                groups.append(cur)
                cur, cur_len = [], 0
            cur.append(line)
            cur_len += len(line) + 1
        if cur:
            groups.append(cur)
        # merge a tiny trailing group into the previous one
        if len(groups) >= 2 and sum(len(l) for l in groups[-1]) < min_chars:
            groups[-2].extend(groups.pop())
        for i, g in enumerate(groups):
            text = "\n".join(g).strip()
            if len(text) < 20:
                continue
            chunks.append({"chunk_id": f"{record['slug']}#{sid}#{i}", "drug": drug, "slug": record["slug"],
                           "section_id": sid, "section_heading": section["heading"], "page": section.get("page", "main"),
                           "text": text, "source_url": record.get("url")})
    return chunks
