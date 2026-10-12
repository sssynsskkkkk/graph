#!/usr/bin/env python3
"""Package independently authored, source-grounded annotations for human review.

This script only expands the manually authored annotation specification. It does
not run a triple extraction model or infer clinical facts from the documents.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


RELATIONS = {
    "used_to_treat": "is used to treat",
    "used_to_prevent": "is used to prevent",
    "used_for": "is used for",
    "may_be_used_for": "may be used for",
    "used_in": "is used in",
    "used_with": "is used with",
    "approved_for": "is approved for",
    "not_approved_for": "is not approved for",
    "not_used_for": "is not used for",
    "should_not_be_used_for": "should not be used for",
    "does_not_treat": "does not treat",
    "reduces_risk_of": "reduces the risk of",
    "may_not_reduce_risk_of": "may not reduce the risk of",
    "increases_risk_of": "increases the risk of",
    "may_increase_risk_of": "may increase the risk of",
    "associated_with_increased_risk_of": "is associated with increased risk of",
    "belongs_to": "belongs to",
    "does_not_belong_to": "does not belong to",
    "contains": "contains",
    "may_contain": "may contain",
    "has_active_ingredient": "has active ingredient",
    "synthetic_form_of": "is a synthetic form of",
    "replaces": "replaces",
    "has_property": "has property",
    "has_brand_name": "has brand name",
    "available_as": "is available as",
    "inhibits": "inhibits",
    "does_not_inhibit": "does not inhibit",
    "blocks": "blocks",
    "binds_to": "binds to",
    "relaxes": "relaxes",
    "widens": "widens",
    "delays": "delays",
    "lowers": "lowers",
    "may_lower": "may lower",
    "raises": "raises",
    "may_raise": "may raise",
    "increases": "increases",
    "may_increase": "may increase",
    "decreases": "decreases",
    "may_decrease": "may decrease",
    "improves": "improves",
    "may_improve": "may improve",
    "does_not_stop": "does not stop",
    "causes": "causes",
    "may_cause": "may cause",
    "has_reported_adverse_event": "has reported adverse event",
    "may_harm": "may harm",
    "may_mask": "may mask",
    "has_boxed_warning_for": "has a boxed warning for",
    "should_not_be_used_in": "should not be used in",
    "should_not_be_combined_with": "should not be combined with",
    "may_need_avoidance_with": "may need to be avoided with",
    "avoid_combination_with": "should avoid combination with",
    "may_interact_with": "may interact with",
    "requires_medication_review_with": "requires medication review with",
    "requires_separation_from": "requires dose separation from",
    "may_reduce_absorption_of": "may reduce absorption of",
    "may_delay_absorption_of": "may delay absorption of",
    "increases_levels_of": "increases blood levels of",
    "may_increase_levels_of": "may increase blood levels of",
    "may_decrease_levels_of": "may decrease blood levels of",
    "may_decrease_effectiveness_of": "may decrease effectiveness of",
    "passes_into": "passes into",
    "may_pass_into": "may pass into",
    "not_interchangeable_with": "is not interchangeable with",
    "metabolized_by": "is metabolized by",
    "does_not_require_dose_adjustment_in": "does not require dose adjustment in",
    "initial_dose": "has initial dose",
    "usual_dose": "has usual dose",
    "recommended_dose": "has recommended dose",
    "maintenance_dose": "has maintenance dose",
    "maximum_dose": "has maximum dose",
    "dose_range": "has dose range",
    "dose_may_be_increased_to": "dose may be increased to",
    "dose_based_on": "dose is based on",
    "initiation_not_recommended_in": "initiation is not recommended in",
    "administration_timing": "has administration timing",
    "administration_frequency": "has administration frequency",
    "administration_instruction": "has administration instruction",
    "discontinuation_timing": "should be discontinued",
    "discard_timing": "should be discarded",
    "treatment_duration": "has treatment duration",
    "administered_via": "is administered via",
    "should_not_be_administered_via": "should not be administered via",
    "should_not_be_mixed_with": "should not be mixed with",
    "has_duration_of_action": "has duration of action",
    "storage_temperature": "has storage temperature",
    "requires_monitoring_of": "requires monitoring of",
    "may_delay": "may delay",
    "duration_of_use_limit": "has duration of use limit",
}


def dump_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank-file", type=Path, default=Path("data/top50.yaml"))
    parser.add_argument("--source-dir", type=Path, default=Path("data/text-only/text-only"))
    parser.add_argument("--spec", type=Path, default=Path("data/gt_top25_review/annotation_spec.json"))
    parser.add_argument("--extra-spec", type=Path, action="append", default=[])
    parser.add_argument("--rank-start", type=int, default=1)
    parser.add_argument("--rank-end", type=int, default=25)
    parser.add_argument("--output-dir", type=Path, default=Path("data/gt_top25_review"))
    parser.add_argument("--sentence-index", type=Path,
                        default=Path("data/text-only/sentence_classification/sentence_classification.jsonl"))
    args = parser.parse_args()

    ranking = {}
    for line in args.rank_file.read_text(encoding="utf-8").splitlines():
        match = re.search(r"rank:\s*(\d+),\s*name:\s*(\"[^\"]*\"|[^,}]+)", line)
        if match:
            ranking[int(match.group(1))] = match.group(2).strip().strip('"')

    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    for extra_path in args.extra_spec:
        extra = json.loads(extra_path.read_text(encoding="utf-8"))
        assert extra["annotation_status"] == spec["annotation_status"]
        assert extra["coverage"] == spec["coverage"]
        spec["drugs"].extend(extra["drugs"])
    assert sorted(drug["rank"] for drug in spec["drugs"]) == list(range(args.rank_start, args.rank_end + 1))
    assert spec["annotation_status"] == "ai_draft_pending_human_review"

    sentence_index: dict[str, list[dict]] = defaultdict(list)
    if args.sentence_index.exists():
        for index, line in enumerate(args.sentence_index.open(encoding="utf-8")):
            record = json.loads(line)
            record["source_record_id"] = (
                f"{record['source_file']}|{record['line_number']}|{record['sentence_index']}|{index}"
            )
            sentence_index[record["source_file"]].append(record)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.extra_spec:
        dump_json(args.output_dir / "annotation_spec.json", spec)
    per_drug_dir = args.output_dir / "by_drug"
    per_drug_dir.mkdir(exist_ok=True)
    triples: list[dict] = []
    passages: list[dict] = []
    drug_summaries: list[dict] = []

    for drug in sorted(spec["drugs"], key=lambda item: item["rank"]):
        rank = drug["rank"]
        assert rank in ranking, f"Missing rank {rank} in {args.rank_file}"
        source_path = args.source_dir / drug["file"]
        source_bytes = source_path.read_bytes()
        source_text = source_bytes.decode("utf-8-sig")
        source_lines = source_text.splitlines(keepends=True)
        offsets = [0]
        for line in source_lines:
            offsets.append(offsets[-1] + len(line))
        sha256 = hashlib.sha256(source_bytes).hexdigest()
        section_by_line = {}
        section = None
        for line_number, line in enumerate(source_lines, 1):
            if line.startswith("## "):
                section = line[3:].strip()
            section_by_line[line_number] = section
        source_url = next((line.removeprefix("Source:").strip() for line in source_lines
                           if line.startswith("Source:")), None)
        drug_rows: list[dict] = []
        selected_line_numbers: set[int] = set()
        source_ids: set[str] = set()

        for annotation in drug["annotations"]:
            start, end = annotation["lines"]
            assert 1 <= start <= end <= len(source_lines), f"Invalid lines for {source_path}"
            relation = annotation["relation"]
            assert relation in RELATIONS, relation
            assert annotation["objects"] and all(x.strip() for x in annotation["objects"])
            qualifiers = dict(annotation.get("qualifiers", {}))
            context_line_numbers = qualifiers.pop("context_lines", [])
            selected = set(range(start, end + 1)) | set(context_line_numbers)
            selected_line_numbers.update(selected)
            matching_source_ids = [row["source_record_id"] for row in sentence_index[drug["file"]]
                                   if row["line_number"] in selected]
            source_ids.update(matching_source_ids)
            evidence = source_text[offsets[start - 1]:offsets[end]]
            context = [{"line_number": number, "text": source_lines[number - 1].rstrip("\r\n")}
                       for number in context_line_numbers]

            passage_id = f"rank{rank:02d}_L{start:03d}_{end:03d}"
            passage = next((p for p in passages if p["passage_id"] == passage_id), None)
            if passage is None:
                passage = {"passage_id": passage_id, "rank": rank,
                           "source_file": str(source_path), "line_start": start, "line_end": end,
                           "evidence_text": evidence, "gt_ids": [], "fully_annotated": False}
                passages.append(passage)

            for obj in annotation["objects"]:
                subject = annotation.get("subject", drug["entity"])
                gt_id = f"GT{rank:02d}_{len(drug_rows) + 1:04d}"
                record = {
                    "gt_id": gt_id,
                    "rank": rank,
                    "ranking_drug_name": ranking[rank],
                    "document_drug_name": source_lines[0].lstrip("# ").strip(),
                    "entity_1": subject,
                    "relationship": RELATIONS[relation],
                    "entity_2": obj,
                    "relation_id": relation,
                    "qualifiers": qualifiers,
                    "review_status": "pending_human_review",
                    "annotation_origin": "independently_authored_by_Codex_from_source_TXT",
                    "coverage": "selected_source_passages_not_exhaustive",
                    "source_file": str(source_path),
                    "source_sha256": sha256,
                    "source_url": source_url,
                    "section_title": section_by_line[start],
                    "line_start": start,
                    "line_end": end,
                    "evidence_char_start": offsets[start - 1],
                    "evidence_char_end": offsets[end],
                    "evidence_text": evidence,
                    "additional_context": context,
                    "passage_id": passage_id,
                    "source_record_ids": matching_source_ids,
                }
                assert source_text[record["evidence_char_start"]:record["evidence_char_end"]] == evidence
                drug_rows.append(record)
                triples.append(record)
                passage["gt_ids"].append(gt_id)

        canonical_keys = [(r["entity_1"].casefold(), r["relation_id"], r["entity_2"].casefold(),
                           json.dumps(r["qualifiers"], sort_keys=True)) for r in drug_rows]
        assert len(canonical_keys) == len(set(canonical_keys)), f"Duplicate assertions for rank {rank}"
        file_name = f"{rank:02d}_{source_path.stem}.json"
        dump_json(per_drug_dir / file_name, {"rank": rank, "drug": ranking[rank],
                  "annotation_status": spec["annotation_status"],
                  "exhaustive": False, "triples": drug_rows})
        drug_summaries.append({"rank": rank, "drug": ranking[rank], "source_file": str(source_path),
                               "source_sha256": sha256, "triple_count": len(drug_rows),
                               "selected_line_count": len(selected_line_numbers),
                               "source_text_unit_count": len(sentence_index[drug["file"]]),
                               "selected_source_text_unit_count": len(source_ids),
                               "per_drug_file": str(per_drug_dir / file_name)})

    dump_jsonl(args.output_dir / "gold_triplets_draft.jsonl", triples)
    dump_jsonl(args.output_dir / "source_passages.jsonl", passages)
    csv_fields = ["gt_id", "rank", "ranking_drug_name", "entity_1", "relationship", "entity_2",
                  "relation_id", "qualifiers", "review_status", "source_file", "section_title",
                  "line_start", "line_end", "evidence_text", "additional_context", "source_record_ids",
                  "corrected_entity_1", "corrected_relationship", "corrected_entity_2", "reviewer", "review_notes"]
    with (args.output_dir / "gold_triplets_review.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=csv_fields, extrasaction="ignore")
        writer.writeheader()
        for row in triples:
            csv_row = dict(row)
            for key in ("qualifiers", "additional_context", "source_record_ids"):
                csv_row[key] = json.dumps(csv_row[key], ensure_ascii=False)
            writer.writerow(csv_row)

    grouped = []
    for drug in drug_summaries:
        grouped.append({"doc_id": f"rank{drug['rank']:02d}", "rank": drug["rank"], "drug": drug["drug"],
                        "review_status": "pending_human_review", "exhaustive": False,
                        "triples": [{"gt_id": row["gt_id"], "Entity 1": row["entity_1"],
                                     "Relationship": row["relationship"], "Entity 2": row["entity_2"],
                                     "qualifiers": row["qualifiers"]}
                                    for row in triples if row["rank"] == drug["rank"]]})
    dump_json(args.output_dir / "codekg_format_draft.json", grouped)
    used_relations = sorted({row["relation_id"] for row in triples})
    dump_json(args.output_dir / "relation_schema.json", {key: RELATIONS[key] for key in used_relations})
    unit_count_key = f"source_text_unit_count_top{args.rank_end}"
    summary = {"rank_range": [args.rank_start, args.rank_end], "drug_count": len(drug_summaries), "triple_count": len(triples),
               "annotation_status": spec["annotation_status"], "human_reviewed": False,
               "exhaustive": False, "coverage": spec["coverage"],
               "source_rank_file": str(args.rank_file), "source_directory": str(args.source_dir),
               "relation_count": len(used_relations),
               "relation_counts": dict(sorted(Counter(r["relation_id"] for r in triples).items())),
               "passage_count": len(passages),
               unit_count_key: sum(d["source_text_unit_count"] for d in drug_summaries),
               "selected_source_text_unit_count": sum(d["selected_source_text_unit_count"] for d in drug_summaries),
               "unmapped_gt_count": sum(not row["source_record_ids"] for row in triples),
               "drugs": drug_summaries}
    dump_json(args.output_dir / "summary.json", summary)
    print(json.dumps({key: summary[key] for key in ("drug_count", "triple_count", "relation_count",
                     "passage_count", unit_count_key, "selected_source_text_unit_count",
                     "unmapped_gt_count")}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
