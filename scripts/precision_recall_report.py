#!/usr/bin/env python3
"""Combine GT-coverage recall (compare_gt_graph_semantics.py summaries) and sampled precision (precision_judge.py)."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {"text_edc": "원문 입력 + EDC", "decomp_edc": "문장 분해 + EDC",
          "coref_decomp_edc": "대명사 치환 + 문장 분해 + EDC",
          "coref_decomp_edc_r2": "대명사 치환 + 문장 분해 + EDC (2차 실행)", "kggen_canon": "문장 분해 + EDC + KGGen 정규화 (팀원)"}


def f1(p: float, r: float) -> float:
    return 0.0 if p + r == 0 else 2 * p * r / (p + r)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--recall", action="append", default=[], help="name=dir with summary.json")
    ap.add_argument("--precision-dir", type=Path, action="append", required=True,
                    help="precision_judge.py output dir(s); summaries are merged (repeatable)")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    prec = {}
    for d in args.precision_dir:
        prec.update(json.loads((d / "summary.json").read_text()))
    rec = {}
    for spec in args.recall:
        name, d = spec.split("=", 1)
        rec[name] = (json.loads((Path(d) / "summary.json").read_text()), Path(d))
    names = [n for n in rec] + [n for n in prec if n not in rec]

    md = ["# 정확도·재현율 비교 (자동 판정)", "",
          "- **재현율**: GT 초안 1,894개(50개 약, 사람 미검수·비완전 주석) 중 KG가 담은 비율. 팀원 스크립트 "
          "`compare_gt_graph_semantics.py`를 그대로 사용(Qwen3-Embedding 후보 검색 + Qwen3.5-9B 판정). "
          "엄격 = match, 관대 = match + partial.",
          "- **정확도**: KG마다 EDC 트리플을 약별 10개씩 무작위 추출(500개)해, 해당 트리플이 나온 **원래 페이지 섹션 원문**과 "
          "대조. Qwen3.5-27B가 KG 출처를 모른 채 섞어서 판정. 엄격 = correct, 관대 = correct + partial. 괄호는 95% 신뢰구간.",
          "- F1은 같은 기준(엄격끼리, 관대끼리)의 정확도와 재현율로 계산한 참고값입니다.", "",
          "| KG | 트리플 | 정확도 엄격 | 정확도 관대 | 재현율 엄격 | 재현율 관대 | F1 엄격 | F1 관대 |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for n in names:
        p = prec.get(n)
        r = rec.get(n, (None, None))[0]
        ps, pl = (p["precision_strict"], p["precision_lenient"]) if p else (None, None)
        rs, rl = (r["match_percent"], r["match_or_partial_percent"]) if r else (None, None)
        edges = r.get("graph_selected_unique_edge_count") if r else None
        cell = lambda v, ci=None: "–" if v is None else (f"{v:.1f}" + (f" ({ci[0]:.0f}–{ci[1]:.0f})" if ci else ""))
        md.append(f"| {LABELS.get(n, n)} | {edges if edges is not None else '–'} | "
                  f"{cell(ps, p and p['precision_strict_ci95'])} | {cell(pl, p and p['precision_lenient_ci95'])} | "
                  f"{cell(rs)} | {cell(rl)} | {cell(f1(ps, rs) if p and r else None)} | {cell(f1(pl, rl) if p and r else None)} |")

    md += ["", "## 정확도: 틀린 트리플의 오류 유형 (500개 중 개수)", "",
           "| 오류 유형 | " + " | ".join(LABELS.get(n, n) for n in prec) + " |", "|---|" + "---:|" * len(prec)]
    errs = sorted({e for p in prec.values() for e in p["incorrect_errors"]}, key=str)
    for e in errs:
        md.append(f"| {e} | " + " | ".join(str(p["incorrect_errors"].get(e, 0)) for p in prec.values()) + " |")

    md += ["", "## 재현율: 약별 (관대 기준 %, match+partial)", "",
           "| 약 | GT | " + " | ".join(LABELS.get(n, n) for n in rec) + " |", "|---|---:|" + "---:|" * len(rec)]
    per = {}
    for n, (_, d) in rec.items():
        with (d / "per_drug_summary.csv").open(encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                per.setdefault((int(row["rank"]), row["drug"], row.get("gt_count") or row.get("gt")), {})[n] = row
    for (rank, drug, gt), rows in sorted(per.items()):
        cells = []
        for n in rec:
            row = rows.get(n)
            if not row:
                cells.append("–")
                continue
            m, pa = int(row.get("match", 0)), int(row.get("partial", 0))
            cells.append(f"{100 * (m + pa) / int(gt):.0f}")
        md.append(f"| {drug} | {gt} | " + " | ".join(cells) + " |")

    md += ["", "## 한계", "",
           "- GT는 사람이 검수하지 않은 AI 초안이고, 문서의 일부 관계만 주석했습니다. 재현율은 'GT 초안 커버리지'입니다.",
           "- 두 판정 모두 LLM 자동 판정이며 오류가 있습니다. 재현율 판정 모델(Qwen3.5-9B)은 문장 분해에도 쓰였습니다.",
           "- 정확도는 KG당 500개 표본 추정이라 신뢰구간 안의 차이는 우연일 수 있습니다.",
           f"- 판정 원자료: " + ", ".join(f"`{d}/judged_triples.csv`" for d in args.precision_dir) + ", 재현율은 각 디렉터리의 `semantic_comparison.csv`."]
    args.out.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md[:12 + len(names)]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
