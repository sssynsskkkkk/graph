"""Robust parsers for LLM outputs (triplets, relation definitions, entity lists)."""
from __future__ import annotations
import ast
import json
import re


def normalize_relation(rel: str) -> str:
    rel = rel.strip().strip("'\"`").replace("_", " ").replace("-", " ")
    rel = re.sub(r"\s+", " ", rel).strip().lower()
    return rel


def clean_entity(ent: str) -> str:
    ent = str(ent).strip().strip("'\"`").strip()
    ent = re.sub(r"\s+", " ", ent)
    ent = ent.rstrip(".;,")
    return ent


def _valid_triple(t) -> bool:
    return isinstance(t, (list, tuple)) and len(t) == 3 and all(isinstance(x, str) and x.strip() not in ("", "_") for x in t)


def parse_raw_triplets(raw: str) -> list[list[str]]:
    """Parse '[[s, r, o], ...]' from a completion. Tries JSON first, then bracket matching (as in the EDC code)."""
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\n?|```$", "", raw).strip()
    triples: list[list[str]] = []
    for loader in (json.loads, ast.literal_eval):
        try:
            data = loader(raw)
            if isinstance(data, list) and all(_valid_triple(t) for t in data):
                triples = [[clean_entity(t[0]), normalize_relation(t[1]), clean_entity(t[2])] for t in data]
                break
        except Exception:
            continue
    if not triples:
        stack, pairs = [], []
        for i, c in enumerate(raw):
            if c == "[":
                stack.append(i)
            elif c == "]" and stack:
                pairs.append((stack.pop(), i))
        for l, r in pairs:
            s = raw[l:r + 1]
            for loader in (json.loads, ast.literal_eval):
                try:
                    t = loader(s)
                except Exception:
                    continue
                if _valid_triple(t):
                    triples.append([clean_entity(t[0]), normalize_relation(t[1]), clean_entity(t[2])])
                break
    seen, out = set(), []
    for t in triples:
        if not t[0] or not t[1] or not t[2] or t[0].lower() == t[2].lower():
            continue
        key = (t[0].lower(), t[1], t[2].lower())
        if key not in seen:
            seen.add(key)
            out.append(t)
    return out


def parse_relation_definition(raw: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in raw.splitlines():
        line = line.strip().lstrip("-*0123456789. ").strip()
        if ":" not in line:
            continue
        rel, desc = line.split(":", 1)
        rel = normalize_relation(rel)
        desc = desc.strip().strip("'\"")
        if not rel or rel == "answer" or len(desc) < 10:
            continue
        out[rel] = desc
    return out


def parse_raw_entities(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\n?|```$", "", raw).strip()
    l, r = raw.find("["), raw.rfind("]")
    if l == -1 or r == -1:
        return []
    for loader in (json.loads, ast.literal_eval):
        try:
            data = loader(raw[l:r + 1])
            if isinstance(data, list):
                ents = [clean_entity(x) for x in data if isinstance(x, str) and clean_entity(x)]
                seen, out = set(), []
                for e in ents:
                    if e.lower() not in seen:
                        seen.add(e.lower())
                        out.append(e)
                return out
        except Exception:
            continue
    return []
