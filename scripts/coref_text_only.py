#!/usr/bin/env python3
"""CoDe-KG coreference stage applied to the text-only drug pages (run before sentence classification/decomposition).

Uses the original CoDe-KG coref prompt and parser (external/CoDe-KG_EMNLP_2025/CoDe-KG/{prompts,coref_stage}.py):
the text is tokenized with indices, the LLM returns {Expression, StartToken, EndToken, RefersTo} blocks, and each
expression is replaced with its antecedent. Output keeps the input file layout ('# drug', '## section', '- item'), so
classify_drugs_pilot_sentences.py --input-dir can consume it unchanged.

Deviations from CoDe-KG (which processes ~250-word abstracts):
  * pages are processed per section, in blocks of <= --block-words words split at line boundaries; the drug name and
    section heading are prepended as context tokens so that "this medicine" / "it" can be resolved, but only tokens
    of the block itself are rewritten;
  * spans are validated: indices must be inside the block and the surface tokens must match "Expression";
  * first/second person pronouns (you, your, we, ...) address the reader and are not rewritten;
  * the punctuation attached to a replaced token is kept, and possessives (its/their) become "<antecedent>'s";
  * decoding is greedy (temperature 0) instead of sampling at 0.7, for reproducibility.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from openai import OpenAI

CODEKG_DIR = Path(__file__).resolve().parents[1] / "external" / "CoDe-KG_EMNLP_2025" / "CoDe-KG"
sys.path.insert(0, str(CODEKG_DIR))
from coref_stage import build_coref_prompt, parse_coref_output  # noqa: E402
from tokenize_paper import format_pairs  # noqa: E402

LIST_ITEM = re.compile(r"^(\s*[-*]\s+)(.+)$")
EDGE_PUNCT = re.compile(r"^(\W*)(.*?)(\W*)$", re.DOTALL)
READER_PRONOUNS = {"i", "me", "my", "mine", "myself", "you", "your", "yours", "yourself", "yourselves",
                   "we", "us", "our", "ours", "ourselves"}
POSSESSIVES = {"its", "their", "theirs", "his", "her", "hers"}
# Only anaphoric expressions are rewritten: third-person pronouns and demonstrative/definite references to the drug.
PRONOUNS = {"it", "its", "itself", "they", "them", "their", "theirs", "themselves", "he", "him", "his", "she", "her",
            "this", "these", "that", "those"}
DETERMINERS = {"this", "these", "that", "those", "the"}
GENERIC_NOUNS = {"medicine", "medicines", "medication", "medications", "drug", "drugs", "product", "products",
                 "tablet", "tablets", "capsule", "capsules", "injection", "inhaler", "spray", "solution", "combination"}
# "it" as a dummy subject/object ("it is not known whether", "make it harder", "if it is almost time")
EXPLETIVE_IT = re.compile(r"^it\s+(is|was|may be|can be|will be|could be|might be|has been|takes?|took|helps?)\s+"
                          r"(not\s+)?(known|important|possible|almost|best|safe|unsafe|easier|harder|difficult|"
                          r"recommended|necessary|likely|unlikely|unknown|up to|okay|ok|\d|several|a few|weeks?|"
                          r"months?|days?|hours?|time)", re.IGNORECASE)
EXPLETIVE_IT_OBJ = re.compile(r"\b(make|makes|making|made|find|finds)\s+it\s+(harder|easier|difficult|more|less|hard|easy)"
                              r"|\b(does|did|will|would|can)\s+it\s+take\b|\bat\s+it\s+another\s+way", re.IGNORECASE)
# "This is not a complete list of side effects" refers to the preceding list, not to the drug
# "this medication guide" / "the drug label" are documents, not the drug
COMPOUND_HEADS = {"guide", "guides", "label", "labels", "leaflet", "insert", "sheet", "sheets", "information", "class",
                  "classes", "group", "interactions", "interaction", "checker", "list"}
NOT_COMPLETE_LIST = re.compile(r"^(this|these)\s+(is|are)\s+not\s+(a\s+)?(complete|all)", re.IGNORECASE)


def core(token: str) -> str:
    return EDGE_PUNCT.match(token).group(2)


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def parse_page(path: Path) -> tuple[list[dict], str]:
    """Return the file as a list of line dicts and the drug title."""
    lines, drug = [], path.stem
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        entry = {"raw": raw, "kind": "other"}
        stripped = raw.strip()
        if stripped.startswith("# ") and drug == path.stem:
            drug = stripped[2:].strip()
            entry["kind"] = "title"
        elif stripped.startswith("## "):
            entry.update(kind="section", heading=stripped[3:].strip())
        elif stripped.startswith("### "):
            entry.update(kind="subsection", heading=stripped[4:].strip())
        elif stripped and not stripped.lower().startswith("source:"):
            m = LIST_ITEM.match(raw)
            entry.update(kind="content", prefix=m.group(1) if m else "", text=m.group(2) if m else stripped)
        lines.append(entry)
    return lines, drug


def make_blocks(lines: list[dict], drug: str, block_words: int) -> list[dict]:
    """Group content lines per section into blocks of <= block_words words."""
    blocks, heading, cur = [], "", []

    def flush():
        if cur:
            blocks.append({"drug": drug, "heading": heading, "line_ids": list(cur)})
            cur.clear()

    for i, entry in enumerate(lines):
        if entry["kind"] == "section":
            flush()
            heading = entry["heading"]
        elif entry["kind"] == "content":
            n = sum(len(lines[j]["text"].split()) for j in cur)
            if cur and n + len(entry["text"].split()) > block_words:
                flush()
            cur.append(i)
    flush()
    return blocks


def block_tokens(block: dict, lines: list[dict]) -> tuple[list[str], int, list[tuple[int, int]]]:
    """Context tokens + block tokens; returns (tokens, n_context, [(line_id, token_index)])."""
    context = f"{block['drug']}. {block['heading']}".split()
    tokens, owner = list(context), []
    for line_id in block["line_ids"]:
        for tok in lines[line_id]["text"].split():
            owner.append((line_id, len(tokens)))
            tokens.append(tok)
    return tokens, len(context), owner


# a bare demonstrative is a pronoun only when a verb (or punctuation) follows: "These are ..." vs "These side effects ..."
FOLLOWS_PRONOUN = {"is", "are", "was", "were", "may", "can", "will", "could", "should", "might", "must", "does", "do",
                   "did", "has", "have", "had", "include", "includes", "cause", "causes", "also", "usually", "often",
                   "includes", "means", "helps", "help", "works", "work", "lowers", "increases", "reduces"}


def bare_demonstrative_ok(tokens: list[str], en: int) -> bool:
    if EDGE_PUNCT.match(tokens[en]).group(3) or en + 1 >= len(tokens):
        return True
    return norm(core(tokens[en + 1])) in FOLLOWS_PRONOUN


def is_anaphor(words: list[str]) -> bool:
    if len(words) == 1:
        return words[0] in PRONOUNS - {"that"}  # bare "that" is mostly a relative pronoun / conjunction
    return len(words) == 2 and words[0] in DETERMINERS and words[1] in GENERIC_NOUNS


def is_expletive_it(tokens: list[str], st: int) -> bool:
    after = " ".join(core(t) for t in tokens[st:st + 6])
    around = " ".join(core(t) for t in tokens[max(0, st - 2):st + 3])
    return bool(EXPLETIVE_IT.match(after) or EXPLETIVE_IT_OBJ.search(around))


def validate(spans: list[dict], tokens: list[str], n_context: int) -> tuple[list[dict], list[dict]]:
    accepted, rejected, used = [], [], set()
    for s in spans:
        st, en, exp = s["StartToken"], s["EndToken"], s["Expression"].strip()
        ref = s["RefersTo"] = s["RefersTo"].strip().strip(".,;:!?\"'")
        reason = None
        if not (n_context <= st <= en < len(tokens)) or en - st > 5:
            reason = "index_out_of_block"
        elif norm(" ".join(core(t) for t in tokens[st:en + 1])) != norm(exp):
            reason = "expression_mismatch"
        if reason is None:
            # the LLM often marks only one token of "this medicine": widen the span to the full noun phrase
            words = norm(exp).split()
            if len(words) == 1 and words[0] in DETERMINERS and en + 1 < len(tokens) \
                    and norm(core(tokens[en + 1])) in GENERIC_NOUNS and not EDGE_PUNCT.match(tokens[en]).group(3):
                en += 1
            elif len(words) == 1 and words[0] in GENERIC_NOUNS and st - 1 >= n_context \
                    and norm(core(tokens[st - 1])) in DETERMINERS:
                st -= 1
            exp = " ".join(core(t) for t in tokens[st:en + 1])
            words = norm(exp).split()
            ref_words = norm(ref).split()
            if norm(exp) in READER_PRONOUNS:
                reason = "reader_pronoun"
            elif not is_anaphor(words):
                reason = "not_pronoun"
            elif len(words) == 1 and words[0] in {"this", "these", "those"} and not bare_demonstrative_ok(tokens, en):
                reason = "demonstrative_determiner"
            elif words[-1] in GENERIC_NOUNS and en + 1 < len(tokens) and not EDGE_PUNCT.match(tokens[en]).group(3) \
                    and norm(core(tokens[en + 1])) in COMPOUND_HEADS:
                reason = "compound_noun"
            elif len(words) == 1 and NOT_COMPLETE_LIST.match(" ".join(core(t) for t in tokens[st:st + 6])):
                reason = "list_reference"
            elif words == ["it"] and is_expletive_it(tokens, st):
                reason = "expletive_it"
            elif not ref_words or ref_words == words or len(ref_words) > 8 \
                    or all(w in PRONOUNS | DETERMINERS | GENERIC_NOUNS | READER_PRONOUNS for w in ref_words):
                reason = "bad_antecedent"
            elif f" {norm(ref)} " not in f" {norm(' '.join(core(t) for t in tokens[:st]))} ":
                reason = "antecedent_not_in_preceding_text"
            elif used & set(range(st, en + 1)):
                reason = "overlap"
        if reason:
            rejected.append({**s, "reason": reason})
        else:
            used |= set(range(st, en + 1))
            accepted.append({**s, "StartToken": st, "EndToken": en, "Expression": exp,
                             "llm_span": [s["StartToken"], s["EndToken"]]})
    return accepted, rejected


def apply_spans(tokens: list[str], spans: list[dict]) -> list[str]:
    out = list(tokens)
    for s in spans:
        st, en, ref = s["StartToken"], s["EndToken"], s["RefersTo"].strip()
        lead = EDGE_PUNCT.match(tokens[st]).group(1)
        trail = EDGE_PUNCT.match(tokens[en]).group(3)
        if norm(s["Expression"]).split()[-1] in POSSESSIVES and not ref.endswith("'s"):
            ref += "'s"
        if core(tokens[st])[:1].isupper():
            ref = ref[:1].upper() + ref[1:]
        out[st] = lead + ref + trail
        for k in range(st + 1, en + 1):
            out[k] = ""
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, default=Path("data/text-only/text-only"))
    ap.add_argument("--output-dir", type=Path, default=Path("data/text-only/coref"))
    ap.add_argument("--base-url", default="http://localhost:8001/v1")
    ap.add_argument("--model", default="codekg-llm")
    ap.add_argument("--block-words", type=int, default=250)
    ap.add_argument("--max-tokens", type=int, default=2048)
    ap.add_argument("--workers", type=int, default=24)
    ap.add_argument("--files", nargs="*", help="only these file stems (pilot)")
    ap.add_argument("--reuse-log", type=Path, help="re-validate LLM outputs saved in a previous coref_spans.jsonl "
                                                    "instead of calling the LLM (same blocks/settings required)")
    args = ap.parse_args()

    client = OpenAI(base_url=args.base_url, api_key="EMPTY", timeout=600)
    text_dir = args.output_dir / "text"
    text_dir.mkdir(parents=True, exist_ok=True)
    paths = sorted(args.input_dir.glob("*.txt"))
    if args.files:
        paths = [p for p in paths if p.stem in set(args.files)]

    pages, jobs = {}, []
    for path in paths:
        lines, drug = parse_page(path)
        pages[path.name] = lines
        for b_idx, block in enumerate(make_blocks(lines, drug, args.block_words)):
            jobs.append((path.name, b_idx, block))

    saved = {}
    if args.reuse_log:
        for line in args.reuse_log.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            saved[(r["file"], r["block"])] = (r["text"], r["raw_output"])

    def run(job):
        name, b_idx, block = job
        tokens, n_context, owner = block_tokens(block, pages[name])
        if args.reuse_log:
            text, raw = saved[(name, b_idx)]
            assert text == " ".join(tokens[n_context:]), f"block mismatch {name}#{b_idx}"
        else:
            prompt = build_coref_prompt(format_pairs([(t, i) for i, t in enumerate(tokens)]))
            resp = client.chat.completions.create(
                model=args.model, messages=[{"role": "user", "content": prompt}], temperature=0.0,
                max_tokens=args.max_tokens, extra_body={"chat_template_kwargs": {"enable_thinking": False}})
            raw = resp.choices[0].message.content or ""
        accepted, rejected = validate(parse_coref_output(raw), tokens, n_context)
        return name, b_idx, block, tokens, n_context, owner, raw, accepted, rejected

    print(f"files={len(paths)} blocks={len(jobs)}", flush=True)
    results = []
    with ThreadPoolExecutor(args.workers) as pool:
        for k, res in enumerate(pool.map(run, jobs), 1):
            results.append(res)
            if k % 50 == 0 or k == len(jobs):
                print(f"coref blocks {k}/{len(jobs)}", flush=True)

    stats = Counter()
    with (args.output_dir / "coref_spans.jsonl").open("w", encoding="utf-8") as log:
        for name, b_idx, block, tokens, n_context, owner, raw, accepted, rejected in results:
            new_tokens = apply_spans(tokens, accepted)
            lines = pages[name]
            per_line: dict[int, list[str]] = {}
            for line_id, t_idx in owner:
                per_line.setdefault(line_id, []).append(new_tokens[t_idx])
            for line_id, toks in per_line.items():
                lines[line_id]["new_text"] = " ".join(t for t in toks if t)
            stats["blocks"] += 1
            stats["accepted"] += len(accepted)
            for r in rejected:
                stats[f"rejected_{r['reason']}"] += 1
            log.write(json.dumps({"file": name, "block": b_idx, "heading": block["heading"], "n_context": n_context,
                                  "text": " ".join(tokens[n_context:]), "raw_output": raw, "accepted": accepted,
                                  "rejected": rejected}, ensure_ascii=False) + "\n")

    for name, lines in pages.items():
        out = []
        for entry in lines:
            if entry["kind"] == "content":
                out.append(entry["prefix"] + entry.get("new_text", entry["text"]))
            else:
                out.append(entry["raw"])
        (text_dir / name).write_text("\n".join(out) + "\n", encoding="utf-8")

    changed_lines = sum(e.get("new_text", e.get("text")) != e.get("text") for ls in pages.values() for e in ls
                        if e["kind"] == "content")
    summary = {"input_dir": str(args.input_dir), "model": args.model, "files": len(pages), **stats,
               "changed_lines": changed_lines,
               "content_lines": sum(e["kind"] == "content" for ls in pages.values() for e in ls)}
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
