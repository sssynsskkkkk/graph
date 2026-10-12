#!/usr/bin/env python3
"""Precision of KG triples against the original drug page (blind LLM judgment of a stratified sample).

For every KG (explorer HTML with embedded kg-data), sample --per-drug EDC-extracted edges per drug document
(structured-metadata edges are excluded: they are copied from page fields, not extracted). Each sampled triple is
judged against the ORIGINAL page section it was extracted from (data/text-only/text-only/<drug>.txt, the section whose
heading matches the edge's section id), whatever text the extractor actually saw (original chunk or decomposed
sentences). Items from all KGs are shuffled together and the judge is not told which KG an item comes from.

Labels
  correct    the passage states (or directly entails) the triple, with the right entities, direction and meaning
  partial    the core fact is in the passage but the triple drops an important qualifier or stretches the relation
  incorrect  not stated / wrong entity / wrong direction / negation or modality flipped / relation misrepresents the text
Precision = correct / n (strict) and (correct + partial) / n (lenient), with 95% Wilson intervals.

Stages: prepare (sample + evidence), judge (OpenAI-compatible server), summarize.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import random
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SYSTEM = """You verify knowledge-graph triples extracted from a consumer drug-information web page.
You get the drug page name, one section of the ORIGINAL page text, and one triple (subject, relation, object), with the
relation's definition. Decide whether the triple is a faithful statement of what this passage says.
Return compact JSON only: {"label":"correct|partial|incorrect","error":"none|not_in_text|wrong_entity|wrong_direction|negation_or_modality|wrong_relation|uninformative|missing_qualifier","reason":"short"}
correct: the passage states or directly entails the triple; subject, object, direction and relation meaning all fit.
  Paraphrases, synonyms and reasonable generalisation of wording are fine. The subject need not be the page's drug.
partial: the core fact is in the passage, but an important qualifier (population, formulation, dose role, condition,
  timing, co-medication) is lost so the triple overgeneralises, or the relation is a loose fit for the stated fact.
incorrect: the passage does not state it (not_in_text); an entity is wrong or swapped for another drug/brand
  (wrong_entity); the direction is reversed (wrong_direction); a negation, possibility or uncertainty is turned into a
  definite claim or vice versa (negation_or_modality); the relation asserts a different kind of fact than the text, e.g.
  'tell your doctor if you have X' turned into 'contraindicated in X', or 'passes into breast milk' turned into
  'administered via breast milk' (wrong_relation); or the triple is too vague to carry information (uninformative).
Judge only from the passage, not from medical knowledge. Use error "none" for correct, "missing_qualifier" or
"wrong_relation" for partial."""


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_graph(html_path: Path) -> dict:
    html = html_path.read_text(encoding="utf-8")
    m = re.search(r'<script\b[^>]*\bid=["\']kg-data["\'][^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1))


def page_sections(text_dir: Path) -> dict[str, dict[str, str]]:
    """file slug ('mtm/ergocalciferol' style, as in edge 'dr') -> {section slug: section text}."""
    out = {}
    for path in text_dir.glob("*.txt"):
        sections, cur = {}, None
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                cur = slugify(line[3:])
                sections.setdefault(cur, [f"## {line[3:].strip()}"])
            elif cur and line.strip():
                sections[cur].append(line)
        out[path.stem.replace("__", "/")] = {k: "\n".join(v) for k, v in sections.items()}
    return out


def prepare(args) -> None:
    rng = random.Random(args.seed)
    sections = page_sections(args.text_dir)
    items = []
    for spec in args.graph:
        name, html = spec.split("=", 1)
        g = load_graph(Path(html))
        nodes = {n["id"]: n for n in g["nodes"]}
        defs = {r["r"]: r.get("def", "") for r in g["relations"]}
        by_drug = collections.defaultdict(list)
        for i, e in enumerate(g["edges"]):
            if "edc" in e["src"] and e.get("ch") and e.get("dr"):
                by_drug[e["dr"][0]].append(i)
        for drug in sorted(by_drug):
            for i in rng.sample(by_drug[drug], min(args.per_drug, len(by_drug[drug]))):
                e = g["edges"][i]
                sec_text = sections.get(drug, {}).get(e.get("sec") or "")
                items.append({"kg": name, "edge_id": i, "drug": drug, "section": e.get("sec"),
                              "subject": nodes[e["s"]]["l"], "relation": e["r"], "object": nodes[e["o"]]["l"],
                              "relation_definition": defs.get(e["r"], ""),
                              "evidence_source": "original_section" if sec_text else "extractor_chunk",
                              "evidence": sec_text or g["chunks"].get(e["ch"], "")})
    rng.shuffle(items)
    for k, it in enumerate(items):
        it["item_id"] = k
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / "items.jsonl").open("w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    c = collections.Counter((it["kg"], it["evidence_source"]) for it in items)
    print(json.dumps({f"{k[0]}:{k[1]}": v for k, v in sorted(c.items())}), flush=True)


def judge(args) -> None:
    from openai import OpenAI
    client = OpenAI(base_url=args.base_url, api_key="EMPTY", timeout=900)
    items = [json.loads(l) for l in (args.output_dir / "items.jsonl").open(encoding="utf-8")]
    out_path = args.output_dir / "judgments.jsonl"
    done = {json.loads(l)["item_id"] for l in out_path.open(encoding="utf-8")} if out_path.exists() else set()
    todo = [it for it in items if it["item_id"] not in done]
    print(f"items={len(items)} todo={len(todo)}", flush=True)

    def run(it: dict) -> dict:
        user = json.dumps({"drug_page": it["drug"], "passage": it["evidence"],
                           "triple": {"subject": it["subject"], "relation": it["relation"], "object": it["object"]},
                           "relation_definition": it["relation_definition"]}, ensure_ascii=False)
        resp = client.chat.completions.create(
            model=args.model, temperature=0.0, max_tokens=200,
            messages=[{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
            extra_body={"chat_template_kwargs": {"enable_thinking": False}})
        raw = resp.choices[0].message.content or ""
        try:
            res = json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
            assert res["label"] in {"correct", "partial", "incorrect"}
        except (AttributeError, ValueError, KeyError, AssertionError):
            res = {"label": "parse_error", "error": None, "reason": "unparseable"}
        return {"item_id": it["item_id"], "kg": it["kg"], **res, "raw_output": raw, "judge_model": args.model}

    with out_path.open("a", encoding="utf-8") as f, ThreadPoolExecutor(args.workers) as pool:
        for k, res in enumerate(pool.map(run, todo), 1):
            f.write(json.dumps(res, ensure_ascii=False) + "\n")
            f.flush()
            if k % 100 == 0:
                print(f"judged={k}/{len(todo)}", flush=True)


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (100 * (c - h), 100 * (c + h))


def summarize(args) -> None:
    items = {it["item_id"]: it for it in (json.loads(l) for l in (args.output_dir / "items.jsonl").open(encoding="utf-8"))}
    judg = [json.loads(l) for l in (args.output_dir / "judgments.jsonl").open(encoding="utf-8")]
    # The judge sometimes writes an incorrect-error type into "label" (e.g. {"label":"uninformative",...}); those are
    # incorrect by definition. Anything else unparseable stays "parse_error" and counts as not correct.
    incorrect_errors = {"not_in_text", "wrong_entity", "wrong_direction", "negation_or_modality", "wrong_relation",
                        "uninformative"}
    for j in judg:
        if j["label"] == "parse_error":
            m = re.search(r'"label"\s*:\s*"([a-z_]+)"', j.get("raw_output") or "")
            if m and m.group(1) in incorrect_errors:
                j.update(label="incorrect", error=m.group(1), label_normalized_from=m.group(1))
    by_kg = collections.defaultdict(list)
    for j in judg:
        by_kg[j["kg"]].append(j)
    summary = {}
    for kg, js in by_kg.items():
        n = len(js)
        lab = collections.Counter(j["label"] for j in js)
        err = collections.Counter(j.get("error") for j in js if j["label"] == "incorrect")
        strict, lenient = lab["correct"], lab["correct"] + lab["partial"]
        summary[kg] = {"n": n, "labels": dict(lab), "incorrect_errors": dict(err.most_common()),
                       "labels_normalized_from_error_type": sum(bool(j.get("label_normalized_from")) for j in js),
                       "precision_strict": round(100 * strict / n, 1), "precision_strict_ci95": [round(x, 1) for x in wilson(strict, n)],
                       "precision_lenient": round(100 * lenient / n, 1), "precision_lenient_ci95": [round(x, 1) for x in wilson(lenient, n)]}
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    rows = []
    for j in judg:
        it = items[j["item_id"]]
        rows.append({k: it[k] for k in ("kg", "drug", "section", "subject", "relation", "object")} |
                    {"label": j["label"], "error": j.get("error"), "reason": j.get("reason")})
    import csv
    with (args.output_dir / "judged_triples.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["kg"], r["drug"])))
    print(json.dumps(summary, indent=1), flush=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["prepare", "judge", "summarize"])
    ap.add_argument("--graph", action="append", default=[], help="name=path/to/kg_explorer.html (repeatable)")
    ap.add_argument("--text-dir", type=Path, default=ROOT / "data/text-only/text-only")
    ap.add_argument("--output-dir", type=Path, default=ROOT / "data/kg_precision_eval")
    ap.add_argument("--per-drug", type=int, default=10)
    ap.add_argument("--seed", type=int, default=13)
    ap.add_argument("--base-url", default="http://localhost:8003/v1")
    ap.add_argument("--model", default="judge-llm")
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()
    {"prepare": prepare, "judge": judge, "summarize": summarize}[args.stage](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
