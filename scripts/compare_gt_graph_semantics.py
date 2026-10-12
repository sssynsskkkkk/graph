#!/usr/bin/env python3
"""Extract the embedded KG, retrieve candidates, and compare GT meaning locally.

The outputs are provisional semantic-overlap estimates, not benchmark P/R/F1.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOT = Path("/home/heesun/.cache/huggingface/hub")


def local_model(name: str) -> str:
    base = MODEL_ROOT / name
    return str(base / "snapshots" / (base / "refs/main").read_text().strip())


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKC", value).casefold()).strip()


def document_slug(source_file: str) -> str:
    # The source downloader encodes URL subdirectories as __ in TXT filenames.
    return Path(source_file).stem.replace("__", "/")


def prepare(output_dir: Path, gt_path: Path, html_path: Path, reuse_dir: Path | None = None) -> None:
    import numpy as np
    import torch
    from transformers import AutoModel, AutoTokenizer

    raw = html_path.read_bytes()
    html = raw.decode("utf-8")
    match = re.search(r'<script\b[^>]*\bid=["\']kg-data["\'][^>]*>(.*?)</script>', html, re.S)
    if not match:
        raise ValueError("No embedded kg-data JSON found")
    graph = json.loads(match.group(1))
    nodes = {node["id"]: node for node in graph["nodes"]}
    definitions = {row["r"]: row.get("def", "") for row in graph["relations"]}
    gt = [json.loads(line) for line in gt_path.open(encoding="utf-8")]
    if not gt:
        raise ValueError("GT reference file is empty")
    if len({row["gt_id"] for row in gt}) != len(gt):
        raise ValueError("Duplicate GT IDs")
    slugs = {document_slug(row["source_file"]) for row in gt}
    selected_edges = []
    for index, edge in enumerate(graph["edges"]):
        if not slugs.intersection(edge.get("dr", [])):
            continue
        selected_edges.append({
            "edge_id": index, "subject": nodes[edge["s"]]["l"],
            "relationship": edge["r"], "object": nodes[edge["o"]]["l"],
            "subject_id": edge["s"], "object_id": edge["o"],
            "subject_type": nodes[edge["s"]].get("t"),
            "object_type": nodes[edge["o"]].get("t"),
            "document_slugs": edge.get("dr", []), "count": edge.get("c"),
            "section": edge.get("sec"), "raw_relationship": edge.get("raw"),
            "relation_definition": definitions.get(edge["r"], ""),
            "chunk_id": edge.get("ch"),
            "evidence_text": graph.get("chunks", {}).get(edge.get("ch"), ""),
        })

    output_dir.mkdir(parents=True, exist_ok=True)
    edge_file_name = "graph_selected_edges.jsonl"
    write_jsonl(output_dir / edge_file_name, selected_edges)
    write_jsonl(output_dir / "gt_reference.jsonl", gt)
    documents = []
    for rank in sorted({row["rank"] for row in gt}):
        row = next(row for row in gt if row["rank"] == rank)
        slug = document_slug(row["source_file"])
        labels = {normalized(node["l"]): node["id"] for node in graph["nodes"]}
        name = row["document_drug_name"]
        documents.append({
            "rank": rank, "drug": row["ranking_drug_name"], "document_slug": slug,
            "document_present": any(slug in e["document_slugs"] for e in selected_edges),
            "document_edge_count": sum(slug in e["document_slugs"] for e in selected_edges),
            "literal_document_drug_node": labels.get(normalized(name)),
            "gt_count": sum(row["rank"] == rank for row in gt),
        })

    embedding_name = local_model("models--Qwen--Qwen3-Embedding-0.6B")
    tokenizer = AutoTokenizer.from_pretrained(embedding_name, local_files_only=True, padding_side="left")
    model = AutoModel.from_pretrained(embedding_name, local_files_only=True, dtype=torch.bfloat16).to("cuda:0").eval()

    def encode(texts: list[str]) -> np.ndarray:
        vectors = []
        for start in range(0, len(texts), 48):
            encoded = tokenizer(texts[start:start+48], padding=True, truncation=True,
                                max_length=384, return_tensors="pt").to("cuda:0")
            with torch.inference_mode():
                # With left padding, the final token is the final valid token.
                emb = model(**encoded).last_hidden_state[:, -1].float()
                emb = torch.nn.functional.normalize(emb, p=2, dim=1)
            vectors.append(emb.cpu().numpy())
            if start % 960 == 0:
                print(f"embedded={min(start+48,len(texts))}/{len(texts)}", flush=True)
        return np.concatenate(vectors)

    edge_texts = [f"{e['subject']} | {e['relationship']} | {e['object']}" for e in selected_edges]
    gt_texts = [f"{e['entity_1']} | {e['relationship']} | {e['entity_2']}" for e in gt]
    embeddings = encode(edge_texts + gt_texts)
    edge_embeddings = embeddings[:len(selected_edges)]
    gt_embeddings = embeddings[len(selected_edges):]
    candidates = []
    for index, row in enumerate(gt):
        slug = document_slug(row["source_file"])
        positions = [i for i, edge in enumerate(selected_edges) if slug in edge["document_slugs"]]
        scores = edge_embeddings[positions] @ gt_embeddings[index]
        # Include the best whole-triple retrievals and an exact tail lexical candidate.
        order = np.argsort(-scores)
        chosen = list(order[:7])
        exact_tail = [j for j, p in enumerate(positions)
                      if normalized(selected_edges[p]["object"]) == normalized(row["entity_2"])]
        for j in sorted(exact_tail, key=lambda j: -float(scores[j]))[:2]:
            if j not in chosen:
                chosen.append(j)
        choices = []
        for j in chosen:
            edge = dict(selected_edges[positions[j]])
            edge["retrieval_cosine"] = float(scores[j])
            choices.append(edge)
        candidates.append({"gt": row, "candidates": choices})

    reused_count = 0
    if reuse_dir:
        previous_meta = json.loads((reuse_dir / "metadata.json").read_text())
        if previous_meta["graph_sha256"] != hashlib.sha256(raw).hexdigest():
            raise ValueError("Cannot reuse judgments: graph content changed")
        previous_pairs = {row["gt"]["gt_id"]: row for row in
                          (json.loads(line) for line in (reuse_dir / "candidates.jsonl").open(encoding="utf-8"))}
        previous_judgments = {}
        for path in sorted(reuse_dir.glob("judgments_*.jsonl")):
            for line in path.open(encoding="utf-8"):
                row = json.loads(line)
                previous_judgments[row["gt_id"]] = row
        reused = []
        for index, pair in enumerate(candidates):
            gt_id = pair["gt"]["gt_id"]
            previous_pair = previous_pairs.get(gt_id)
            if previous_pair and previous_pair["gt"] == pair["gt"] and gt_id in previous_judgments:
                # Retain the exact original candidates and judgments for a comparable extension.
                candidates[index] = previous_pair
                reused.append(previous_judgments[gt_id])
        reused_count = len(reused)
        write_jsonl(output_dir / "judgments_reused.jsonl", reused)
    write_jsonl(output_dir / "candidates.jsonl", candidates)
    meta = {"graph_file": str(html_path), "graph_sha256": hashlib.sha256(raw).hexdigest(),
            "gt_file": str(gt_path), "gt_sha256": hashlib.sha256(gt_path.read_bytes()).hexdigest(),
            "graph_total_edges": len(graph["edges"]), "graph_total_nodes": len(graph["nodes"]),
            "graph_total_document_count": len({s for e in graph["edges"] for s in e.get("dr", [])}),
            f"top{max(row['rank'] for row in gt)}_edge_count": len(selected_edges), "gt_count": len(gt),
            "selected_edge_count": len(selected_edges), "edge_file": edge_file_name,
            "selected_document_count": len(documents),
            "rank_range": [min(row["rank"] for row in gt), max(row["rank"] for row in gt)],
            "embedding_model": embedding_name, "documents": documents,
            "reused_judgment_count": reused_count,
            "reused_from": str(reuse_dir) if reuse_dir else None,
            "judge_prompt_sha256": hashlib.sha256(SYSTEM.encode()).hexdigest(),
            "retrieval_cosine_threshold": None,
            "candidate_selection": "within-document top-7 triple cosine plus up to 2 exact-tail candidates"}
    (output_dir / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k:meta[k] for k in ["graph_total_edges","selected_edge_count","gt_count","reused_judgment_count"]}), flush=True)


SYSTEM = """Compare one source-grounded drug relation reference with candidate knowledge-graph EDGES.
Return a compact JSON object only: {"status":"match|partial|no_match","edge_id":integer_or_null,"reason":"short explanation"}.
Use the canonical subject, relationship and object of each edge. Raw_relationship and evidence are for auditing only;
they must NOT rescue a wrongly canonicalized edge. This is overlap of actual graph assertions, not of document text.
match: the SAME directed fact and all material qualifications are represented. Equivalent abbreviations/synonyms are allowed.
partial: the core directed fact is recognizable, BUT some population, formulation, time, dose role, co-therapy, modality,
regulatory approval status, or other important qualifier is missing/overgeneralized. Differences must be mentioned.
no_match: no candidate represents the same core fact; wrong drug, direction, negation, target or dose is no_match.
Specific rules:
- A brand/subtype is not automatically equivalent to a generic ingredient. Adderall XR is not immediate-release Adderall;
  Wellbutrin XL is not immediate-release bupropion; sertraline oral solution is not a capsule.
- simvastatin/Zocor are NOT atorvastatin/Lipitor; rosuvastatin is NOT atorvastatin.
- 'administered via breast milk' is NOT 'passes into breast milk'. Drug class and ingredient are different relations.
- 'should inform doctor about' is NOT contraindication or a confirmed drug interaction.
- can/may-cause, adverse-event reports and certain causation differ in modality.
- not approved, contraindicated and not effective are different. An absence of approval is not a prohibition.
- A matching adverse symptom with the wrong cause or different allergy drug is no_match.
- General warnings do not prove precise boxed-warning status. A dose without initial/maximum role is partial at best.
- Edge direction may differ ONLY for an explicitly inverse relation expressing the identical fact.
Judge ONLY given edges, not your medical knowledge. If nothing supports the fact, use no_match, edge_id=null.
reason must be <=20 words. Use evidence ONLY to check retained qualifiers on a candidate with already correct core meaning.
"""


def concept(value: str) -> str:
    """Conservative, explicit synonym normalization for auditable core matches."""
    text = normalized(value)
    synonyms = {
        "hypertension": "high blood pressure",
        "high blood pressure hypertension": "high blood pressure",
        "major depressive disorder mdd": "major depressive disorder",
        "mdd": "major depressive disorder",
        "ocd": "obsessive compulsive disorder",
        "obsessive compulsive disorder ocd": "obsessive compulsive disorder",
        "ptsd": "posttraumatic stress disorder",
        "posttraumatic stress disorder ptsd": "posttraumatic stress disorder",
        "sad": "seasonal affective disorder",
        "social anxiety disorder sad": "social anxiety disorder",
        "pmdd": "premenstrual dysphoric disorder",
        "premenstrual dysphoric disorder pmdd": "premenstrual dysphoric disorder",
        "myocardial infarction mi": "heart attack", "myocardial infarction": "heart attack",
        "dvt": "deep vein thrombosis", "deep vein thrombosis dvt": "deep vein thrombosis",
        "pe": "pulmonary embolism", "pulmonary embolism pe": "pulmonary embolism",
        "cns stimulants": "central nervous system stimulants",
        "hmg coa reductase inhibitors statins": "statins",
        "hmg coa reductase inhibitors": "statins",
        "ppi": "proton pump inhibitors", "proton pump inhibitor": "proton pump inhibitors",
        "ssri": "selective serotonin reuptake inhibitors",
        "ssris": "selective serotonin reuptake inhibitors",
        "selective serotonin reuptake inhibitors ssris": "selective serotonin reuptake inhibitors",
        "angiotensin converting enzyme ace inhibitors": "ace inhibitors",
        "angiotensin converting enzyme inhibitors": "ace inhibitors",
        "nausea vomiting": "nausea and vomiting",
        "fluid retention": "edema", "drowsiness somnolence": "drowsiness",
        "somnolence": "drowsiness", "tiredness": "fatigue",
        "sleep problems insomnia": "insomnia",
        "blood in urine": "hematuria", "blood in the urine": "hematuria",
        "paracetamol": "acetaminophen",
        "t4": "thyroxine", "thyroxine t4": "thyroxine",
    }
    return synonyms.get(text, text)


def subject_match(a: str, b: str) -> str | None:
    a, b = normalized(a), normalized(b)
    aliases = {"amlodipine besylate":"amlodipine", "albuterol inhalation":"albuterol",
               "hydrochlorothiazide hctz":"hydrochlorothiazide", "lipitor":"atorvastatin",
               "crestor":"rosuvastatin", "zocor":"simvastatin",
               # Explicitly listed as ergocalciferol brands in the source TXT, lines 74-76.
               "calciferol":"ergocalciferol", "drisdol":"ergocalciferol", "calcidol":"ergocalciferol",
               "pantoprazole oral injection":"pantoprazole"}
    if aliases.get(a,a) == aliases.get(b,b):
        return "exact"
    forms = {"wellbutrin xl":("bupropion","extended"),
             "wellbutrin sr":("bupropion","sustained"),
             "adderall xr":("adderall","extended"),
             "sertraline oral solution":("sertraline","solution"),
             "pantoprazole oral injection":("pantoprazole",None)}

    def family(text: str) -> tuple[str,str | None] | None:
        if text in forms:
            return forms[text]
        for drug in ["bupropion","adderall","sertraline","metformin","metoprolol","pantoprazole",
                     "levothyroxine","hydrochlorothiazide","gabapentin"]:
            if re.search(rf"\b{drug}\b",text):
                if any(word in text for word in ["combined", "withdrawal", "discontinuation", "overdose"]):
                    return None
                form=next((v for k,v in [("immediate","immediate"),("extended","extended"),
                     ("sustained","sustained"),("solution","solution"),("tablets","tablet"),
                     ("capsules","capsule"),("injection","injection")]
                     if k in text),None)
                return drug,form
        return None

    fa,fb=family(a),family(b)
    if fa and fb and fa[0]==fb[0]:
        if fa[1] and fb[1] and fa[1]!=fb[1]:
            return None
        return "scope_difference"
    return None


def relation_family(gt_id: str, edge_relation: str) -> tuple[bool,bool]:
    """Return core-compatible, and whether the relation loses specificity."""
    families = {
        "used_to_treat": {"treats"}, "approved_for":{"treats","used in population"},
        "used_to_prevent":{"treats","reduces"}, "used_for":{"treats","may be used for"},
        "may_be_used_for":{"treats","may be used for"}, "used_in":{"used in population"},
        "reduces_risk_of":{"reduces"}, "increases_risk_of":{"increases","has warning"},
        "may_increase_risk_of":{"increases","has warning"},
        "belongs_to":{"belongs to drug class"}, "contains":{"contains ingredient"},
        "has_active_ingredient":{"contains ingredient"}, "may_contain":{"contains ingredient"},
        "may_cause":{"causes","has symptom","has warning"}, "causes":{"causes"},
        "has_reported_adverse_event":{"has symptom","causes","has warning"},
        "has_boxed_warning_for":{"has warning"},
        "should_not_be_used_in":{"contraindicated in"},
        "should_not_be_combined_with":{"contraindicated in"},
        "not_approved_for":{"not used for"},"not_used_for":{"not used for"},
        "should_not_be_used_for":{"not used for","contraindicated in"},
        "does_not_treat":{"not used for"}, "does_not_stop":{"does not stop","not used for"},
        "lowers":{"lowers level of","reduces"},"decreases":{"lowers level of","reduces"},
        "raises":{"increases"},"increases":{"increases"},"may_lower":{"lowers level of","reduces"},
        "may_raise":{"increases"},"may_increase":{"increases"},"may_decrease":{"reduces"},
        "passes_into":{"passes into"},"may_pass_into":{"passes into"},
        "metabolized_by":{"metabolized by"}, "may_mask":{"can mask"},
        "has_property":{"is","has controlled substance schedule"},
        "administration_timing":{"has administration instruction"},
        "administration_instruction":{"has administration instruction"},
        "administration_frequency":{"has administration instruction"},
    }
    if gt_id in {"initial_dose","maintenance_dose","maximum_dose","dose_range","recommended_dose","usual_dose"}:
        return edge_relation=="has dose",True
    compatible=edge_relation in families.get(gt_id,set())
    lost=gt_id in {"approved_for","used_to_prevent","has_boxed_warning_for","has_active_ingredient",
                 "may_contain","may_cause","has_reported_adverse_event","not_approved_for",
                 "may_lower","may_raise","may_increase","may_decrease","may_pass_into",
                 "may_mask","may_increase_risk_of"}
    return compatible,lost


def conservative_rule_match(gt: dict, candidates: list[dict]) -> tuple[dict,str,str] | None:
    choices=[]
    for edge in candidates:
        subject=subject_match(gt["entity_1"],edge["subject"])
        compatible,lost=relation_family(gt["relation_id"],edge["relationship"])
        if not subject or not compatible or concept(gt["entity_2"]) != concept(edge["object"]):
            continue
        partial=bool(gt["qualifiers"]) or lost or subject!="exact"
        status="partial" if partial else "match"
        reason="Same core fact via explicit synonym rules."
        if partial:
            reason="Same core fact; verify qualifiers, formulation scope or relation specificity."
        choices.append((partial,edge,status,reason))
    if choices:
        _,edge,status,reason=min(choices,key=lambda x:(x[0],-x[1].get("retrieval_cosine",0)))
        return edge,status,reason
    return None


def dose_amounts(text: str) -> dict[str, set[float]]:
    """Extract explicit quantities for detecting demonstrably different doses.

    This is a conservative contradiction check, not a full dosage equivalence
    parser. Unit conversions are limited to mass units. Shared range endpoints
    are not rejected here and still require qualifier/role review.
    """
    unit_pattern = r"mg|mcg|µg|μg|milligrams?|micrograms?|g|grams?|ml|milliliters?|tablets?|capsules?|units?"
    number = r"\d+(?:\.\d+)?"
    result: dict[str, set[float]] = defaultdict(set)

    def add(value: str, unit: str) -> None:
        unit = unit.casefold()
        factors = {"g":1000.0,"gram":1000.0,"grams":1000.0,
                   "mg":1.0,"milligram":1.0,"milligrams":1.0,
                   "mcg":0.001,"µg":0.001,"μg":0.001,"microgram":0.001,"micrograms":0.001}
        if unit in factors:
            key, amount = "mass_mg", float(value)*factors[unit]
        else:
            key = {"milliliter":"ml","milliliters":"ml"}.get(unit,unit.rstrip("s"))
            amount = float(value)
        result[key].add(round(amount,9))

    for value, unit in re.findall(rf"({number})\s*({unit_pattern})\b",text,re.I):
        add(value,unit)
    for low, high, unit in re.findall(rf"({number})\s*(?:to|[-–—])\s*({number})\s*({unit_pattern})\b",text,re.I):
        add(low,unit);add(high,unit)
    return dict(result)


def contradiction_reason(gt: dict, edge: dict) -> str | None:
    dose_relations = {"initial_dose","maintenance_dose","maximum_dose","dose_range",
                      "recommended_dose","usual_dose","dose_may_be_increased_to"}
    if gt["relation_id"] in dose_relations:
        ref = dose_amounts(gt["entity_2"])
        candidate = dose_amounts(edge["object"])
        for unit in ref.keys() & candidate.keys():
            if ref[unit].isdisjoint(candidate[unit]):
                return "Explicit dose amounts conflict; a different dose is not a partial match."
    # These targets are related concepts but not interchangeable facts.
    target = concept(gt["entity_2"])
    distinct = {"abuse","misuse","addiction"}
    if target in distinct and concept(edge["object"]) in distinct - {target}:
        return "Abuse, misuse and addiction are distinct targets; candidate does not represent this reference fact."
    return None


def judge(output_dir: Path, shard: int, shards: int, batch_size: int) -> None:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    path = output_dir / f"judgments_{shard}.jsonl"
    existing = {}
    for existing_path in (path, output_dir / "judgments_reused.jsonl"):
        if not existing_path.exists():
            continue
        for line in existing_path.open(encoding="utf-8"):
            record = json.loads(line)
            existing[record["gt_id"]] = record
    rows = [json.loads(line) for i,line in enumerate((output_dir/"candidates.jsonl").open(encoding="utf-8"))
            if i % shards == shard]
    rows = [row for row in rows if row["gt"]["gt_id"] not in existing]
    print(f"shard={shard} targets={len(rows)}", flush=True)
    if not rows:
        return
    model_name = local_model("models--Qwen--Qwen3.5-9B")
    tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True, padding_side="left")
    model = AutoModelForCausalLM.from_pretrained(model_name, local_files_only=True,
                 dtype=torch.bfloat16, device_map={"":0}, low_cpu_mem_usage=True).eval()
    with path.open("a", encoding="utf-8") as stream:
        for start in range(0,len(rows),batch_size):
            batch = rows[start:start+batch_size]
            prompts = []
            for row in batch:
                gt = row["gt"]
                reference = {key:gt[key] for key in ["entity_1","relationship","entity_2","qualifiers"]}
                edges = []
                for edge in row["candidates"]:
                    edges.append({key:edge[key] for key in ["edge_id","subject","relationship","object",
                                                           "relation_definition"]})
                user = json.dumps({"reference":reference,"candidate_edges":edges},ensure_ascii=False)
                prompts.append(tokenizer.apply_chat_template(
                    [{"role":"system","content":SYSTEM},{"role":"user","content":user}],
                    tokenize=False,add_generation_prompt=True,enable_thinking=False))
            inputs = tokenizer(prompts,return_tensors="pt",padding=True,truncation=True,max_length=4096).to(model.device)
            with torch.inference_mode():
                generated = model.generate(**inputs,max_new_tokens=128,do_sample=False,
                         pad_token_id=tokenizer.pad_token_id,eos_token_id=tokenizer.eos_token_id)
            outputs = tokenizer.batch_decode(generated[:,inputs["input_ids"].shape[1]:],skip_special_tokens=True)
            for row,raw in zip(batch,outputs):
                result = {"status":"parse_error","edge_id":None,"reason":"Unparseable judge response"}
                try:
                    result = json.loads(re.search(r'\{.*\}',raw,re.S).group(0))
                    assert result["status"] in {"match","partial","no_match"}
                    allowed = {edge["edge_id"] for edge in row["candidates"]}
                    if result["status"] != "no_match":
                        assert result["edge_id"] in allowed
                except (AttributeError,ValueError,KeyError,AssertionError):
                    result = {"status":"parse_error","edge_id":None,"reason":"Invalid judge response"}
                result.update({"gt_id":row["gt"]["gt_id"],"rank":row["gt"]["rank"],"raw_output":raw,
                               "judge_model":model_name})
                stream.write(json.dumps(result,ensure_ascii=False)+"\n")
                stream.flush()
            if start % (batch_size*10) == 0:
                print(f"judged={min(start+len(batch),len(rows))}/{len(rows)}",flush=True)
    print("completed",flush=True)


def summarize(output_dir: Path) -> None:
    meta = json.loads((output_dir/"metadata.json").read_text())
    for file_key, hash_key in [("graph_file", "graph_sha256"), ("gt_file", "gt_sha256")]:
        if hashlib.sha256(Path(meta[file_key]).read_bytes()).hexdigest() != meta[hash_key]:
            raise ValueError(f"Input changed since prepare: {meta[file_key]}")
    candidates = [json.loads(line) for line in (output_dir/"candidates.jsonl").open(encoding="utf-8")]
    all_graph_edges=[json.loads(line) for line in (output_dir/meta.get("edge_file", "graph_top25_edges.jsonl")).open(encoding="utf-8")]
    by_document=defaultdict(list)
    for graph_edge in all_graph_edges:
        for slug in graph_edge["document_slugs"]:
            by_document[slug].append(graph_edge)
    judgments = {}
    for path in sorted(output_dir.glob("judgments_*.jsonl")):
        for line in path.open(encoding="utf-8"):
            row=json.loads(line);judgments[row["gt_id"]]=row
    missing = [pair["gt"]["gt_id"] for pair in candidates if pair["gt"]["gt_id"] not in judgments]
    if missing:
        raise ValueError(f"Judgments incomplete: {len(missing)} missing; first IDs: {missing[:5]}")
    results=[]
    for pair in candidates:
        gt=pair["gt"];j=judgments.get(gt["gt_id"],{})
        j=dict(j)
        original_status=j.get("status","not_judged")
        # A few responses contain a complete JSON body with just the closing brace omitted.
        if j.get("status")=="parse_error":
            try:
                recovered=json.loads(j["raw_output"].strip()+"}")
                assert recovered["status"] in {"match","partial","no_match"}
                assert recovered["status"] == "no_match" or recovered.get("edge_id") in {e["edge_id"] for e in pair["candidates"]}
                j.update(recovered)
            except (ValueError,KeyError,AssertionError):
                pass
        edge=next((e for e in pair["candidates"] if e["edge_id"]==j.get("edge_id")),None)
        method="LLM_candidate_judgment"
        slug=document_slug(gt["source_file"])
        retrieved_ids={edge["edge_id"] for edge in pair["candidates"]}
        extended=pair["candidates"]+[edge for edge in by_document[slug] if edge["edge_id"] not in retrieved_ids]
        rule=conservative_rule_match(gt,extended)
        if rule:
            edge,status,reason=rule
            j.update(status=status,reason=reason,edge_id=edge["edge_id"])
            method="explicit_core_match_with_conservative_qualifier_handling"
        elif j.get("status")=="match" and gt["qualifiers"]:
            j.update(status="partial",reason="Core match proposed by LLM; material qualifiers need separate confirmation.")
            method="LLM_match_downgraded_for_qualifier_review"
        if edge and j.get("status")=="match":
            ref_numbers=set(re.findall(r"\d+(?:\.\d+)?",gt["entity_2"]))
            edge_numbers=set(re.findall(r"\d+(?:\.\d+)?",edge["object"]))
            missing_numbers=ref_numbers-edge_numbers
            scoped=subject_match(gt["entity_1"],edge["subject"])=="scope_difference"
            if missing_numbers or scoped:
                j.update(status="partial",reason="Core match proposed, but a quantity or formulation/ingredient scope differs.")
                method="LLM_match_downgraded_for_quantity_or_scope"
            if gt["relation_id"] in {"used_in","used_to_treat","approved_for"}:
                reference_population = set(re.findall(r"\b(?:adults|children)\b",normalized(gt["entity_2"])))
                candidate_population = set(re.findall(r"\b(?:adults|children)\b",normalized(edge["object"])))
                if reference_population == {"adults","children"} and candidate_population in [{"adults"},{"children"}]:
                    j.update(status="partial",reason="Candidate covers only adults or children, not the full reference population.")
                    method="LLM_match_downgraded_for_population_scope"
        if edge and j.get("status") in {"match","partial"}:
            conflict = contradiction_reason(gt,edge)
            if conflict:
                j.update(status="no_match",reason=conflict)
                method="explicit_contradiction_guard"
                edge = None
        results.append({"gt_id":gt["gt_id"],"rank":gt["rank"],"drug":gt["ranking_drug_name"],
                        "reference_triple":[gt["entity_1"],gt["relationship"],gt["entity_2"]],
                        "qualifiers":gt["qualifiers"],"status":j.get("status","not_judged"),
                        "reason":j.get("reason",""),"graph_edge":edge,
                        "judgment_method":method,"original_llm_status":original_status,
                        "best_retrieval_cosine":max(e["retrieval_cosine"] for e in pair["candidates"]),
                        "matched_candidate_cosine":edge.get("retrieval_cosine") if edge else None,
                        "source_file":gt["source_file"],"line_start":gt["line_start"],
                        "line_end":gt["line_end"],"reference_evidence":gt["evidence_text"],
                        "candidate_edges":pair["candidates"]})
    unresolved = [row["gt_id"] for row in results if row["status"] not in {"match", "partial", "no_match"}
                  or (row["status"] in {"match", "partial"} and not row["graph_edge"])]
    if unresolved:
        raise ValueError(f"Invalid judgments require retry or review: {unresolved[:10]}")
    write_jsonl(output_dir/"semantic_comparison.jsonl",results)
    counts=Counter(row["status"] for row in results)
    docs=[]
    for doc in meta["documents"]:
        c=Counter(row["status"] for row in results if row["rank"]==doc["rank"])
        docs.append({**doc,"semantic_counts":dict(c),
                     "match_percent":round(100*c["match"]/doc["gt_count"],1),
                     "match_or_partial_percent":round(100*(c["match"]+c["partial"])/doc["gt_count"],1)})
    summary={"metric":"provisional_AI_judged_reference_overlap_not_precision_recall_F1",
             "gt_status":"AI_draft_not_exhaustive_not_human_gold",
             "graph_selected_document_presence":sum(doc["document_present"] for doc in docs),
             "selected_document_count":len(docs),
             "reference_count":len(results),"status_counts":dict(counts),
             "status_percentages":{key:round(100*counts[key]/len(results),2) for key in ["match","partial","no_match"]},
             "match_percent":round(100*counts["match"]/len(results),1),
             "match_or_partial_percent":round(100*(counts["match"]+counts["partial"])/len(results),1),
             "graph_selected_unique_edge_count":meta.get("selected_edge_count",meta.get("top25_edge_count",0)),
             "reused_judgment_count":meta.get("reused_judgment_count",0),
             "cosine_used_for":"candidate retrieval only, not a correctness threshold",
             "qualification_handling":"Conservatively partial whenever GT has qualifiers, even if a candidate might retain them",
             "contradiction_guard_count":sum(r["judgment_method"]=="explicit_contradiction_guard" for r in results),
             "contradiction_guard_policy":"Disjoint explicit dose quantities and distinct abuse/misuse/addiction targets are not partial matches",
             "macro_match_percent":round(sum(d["match_percent"] for d in docs)/len(docs),1),
             "macro_match_or_partial_percent":round(sum(d["match_or_partial_percent"] for d in docs)/len(docs),1),
             "aggregation":"Micro percentages weight each selected GT relation equally; macro weights each drug equally",
             "retrieval_limitations":"no_match means neither an explicit synonym rule match in all same-document edges nor a semantic LLM match in top retrieved candidates; not proven absent from full graph",
             "documents":docs}
    groups = []
    for label, start, end in [("ranks_1_25",1,25),("ranks_26_50",26,50)]:
        group = [r for r in results if start <= r["rank"] <= end]
        if not group:
            continue
        c = Counter(r["status"] for r in group)
        groups.append({"group":label,"reference_count":len(group),"status_counts":dict(c),
                       "match_percent":round(100*c["match"]/len(group),1),
                       "match_or_partial_percent":round(100*(c["match"]+c["partial"])/len(group),1)})
    summary["rank_groups"] = groups
    (output_dir/"summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
    write_jsonl(output_dir/"contradiction_guard_audit.jsonl",[
        {"gt_id":r["gt_id"],"rank":r["rank"],"reference_triple":r["reference_triple"],
         "status":r["status"],"reason":r["reason"],
         "original_judgment":judgments[r["gt_id"]],
         "rejected_edge":next((e for e in r["candidate_edges"] if e["edge_id"]==judgments[r["gt_id"]].get("edge_id")),None)}
        for r in results if r["judgment_method"]=="explicit_contradiction_guard"])
    with (output_dir/"semantic_comparison.csv").open("w",encoding="utf-8-sig",newline="") as stream:
        fields=["gt_id","rank","drug","status","reference_subject","reference_relation","reference_object",
                "reference_qualifiers","graph_subject","graph_relation","graph_object","reason",
                "best_retrieval_cosine","matched_candidate_cosine","judgment_method",
                "source_file","line_start","line_end","reviewer_status","reviewer_notes"]
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
        for row in results:
            edge=row["graph_edge"] or {}
            writer.writerow({"gt_id":row["gt_id"],"rank":row["rank"],"drug":row["drug"],"status":row["status"],
                "reference_subject":row["reference_triple"][0],"reference_relation":row["reference_triple"][1],
                "reference_object":row["reference_triple"][2],"reference_qualifiers":json.dumps(row["qualifiers"],ensure_ascii=False),
                "graph_subject":edge.get("subject",""),"graph_relation":edge.get("relationship",""),
                "graph_object":edge.get("object",""),"reason":row["reason"],"source_file":row["source_file"],
                "best_retrieval_cosine":row["best_retrieval_cosine"],
                "matched_candidate_cosine":row["matched_candidate_cosine"],"judgment_method":row["judgment_method"],
                "line_start":row["line_start"],"line_end":row["line_end"]})
    with (output_dir/"per_drug_summary.csv").open("w",encoding="utf-8-sig",newline="") as stream:
        fields=["rank","drug","gt_count","graph_edge_count","match","partial","not_found",
                "match_percent","match_or_partial_percent"]
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
        for doc in docs:
            c=doc["semantic_counts"]
            writer.writerow({"rank":doc["rank"],"drug":doc["drug"],"gt_count":doc["gt_count"],
                "graph_edge_count":doc["document_edge_count"],"match":c.get("match",0),
                "partial":c.get("partial",0),"not_found":c.get("no_match",0),
                "match_percent":doc["match_percent"],"match_or_partial_percent":doc["match_or_partial_percent"]})

    lines=["# GT 초안과 팀원 그래프의 의미 비교", "",
        f"우리 GT의 약물 문서 {len(docs)}개 중 {sum(doc['document_present'] for doc in docs)}개가 팀원 그래프에 포함됩니다. 그래프 전체는 {meta['graph_total_document_count']}개 문서, "
        f"{meta['graph_total_edges']:,}개 관계이며 비교 대상 {len(docs)}개 문서에 연결된 고유 관계는 {meta.get('selected_edge_count',meta.get('top25_edge_count',0)):,}개입니다.", "",
        "문서의 존재와 노드 이름의 일치는 구별했습니다. 약물 문서 키(`dr`)로 범위를 제한했으며, "
        "Amlodipine/Amlodipine besylate 같은 동의 표현은 허용했습니다. "
        "Bupropion/Wellbutrin XL, Adderall/Adderall XR, Sertraline/sertraline oral solution은 "
        "제형·제품 범위를 그대로 동일하다고 가정하지 않았습니다.", "",
        "## 전체 결과", "", "| 자동 판정 | GT 수 | 비율 |", "|---|---:|---:|"]
    for label,key in [("일치 후보","match"),("부분 일치 후보","partial"),("대응 후보 미확인","no_match")]:
        count=counts[key];lines.append(f"| {label} | {count} | {100*count/len(results):.1f}% |")
    lines.extend(["",f"일치와 부분 일치를 합하면 **{counts['match']+counts['partial']} / {len(results)} "
                  f"({summary['match_or_partial_percent']}%)**입니다.", "",
                  "이 비율은 GT 초안에서 선택한 관계의 의미 겹침에 대한 자동 추정입니다. "
                  "전체 그래프 Precision/Recall/F1이나 확정된 정확도가 아닙니다.", "",
                  "## 판정 기준", "",
                  "- 일치 후보: 개체·관계·방향의 의미가 대응하고 별도 조건 확인이 요구되지 않은 자동 판정.",
                  "- 부분 일치 후보: 핵심 사실이 대응하지만 연령·병용약·제형·초기/최대 용량·가능성·허가 여부 등을 확인해야 함. "
                  "보수적인 규칙에서는 조건이 있는 GT를 부분 일치로 분류하므로, 실제로 조건이 보존된 사례도 여기에 포함될 수 있음.",
                  "- 대응 후보 미확인: 명시적 동의어 규칙으로 같은 문서 전체 관계를 찾지 못하고, "
                  "임베딩으로 검색한 후보에서도 LLM이 대응을 찾지 못함. 전체 그래프에 절대 없다는 증명은 아님.", "",
                  "## 약물별 결과", "", "| 순위 | 약물 | GT | 일치 | 부분 일치 | 미확인 | 일치+부분 |",
                  "|---:|---|---:|---:|---:|---:|---:|"])
    for doc in docs:
        c=doc["semantic_counts"]
        lines.append(f"| {doc['rank']} | {doc['drug']} | {doc['gt_count']} | {c.get('match',0)} | "
                     f"{c.get('partial',0)} | {c.get('no_match',0)} | {doc['match_or_partial_percent']}% |")
    lines.extend(["", "## 방법 및 한계", "",
        "1. HTML의 `kg-data` JSON을 추출했습니다. 화면 표시나 브라우저 자바스크립트 실행은 사용하지 않았습니다.",
        "2. GT 원본 파일명과 그래프 관계의 문서 출처(`dr`)를 연결했습니다.",
        "3. 로컬 Qwen3-Embedding-0.6B로 GT별 같은 문서의 상위 7개 관계를 찾고, "
        "object 문자열이 정확히 일치하는 후보를 최대 2개 추가했습니다.",
        "4. Qwen3.5-9B가 canonical subject/relation/object를 비교했습니다. "
        "사전 명시한 동의어·관계 대응 규칙을 같은 문서의 모든 관계에 추가 적용했습니다.",
        "5. 조건, 수치, 제형의 누락을 보수적으로 처리했습니다. 모든 판정은 사람이 확인할 수 있도록 CSV에 남겼습니다.", "",
        "Cosine similarity는 후보를 찾기 위한 검색 점수이며 정답 점수가 아닙니다. "
        "`cos(a,b) = (a·b) / (||a|| ||b||)`로 계산하며, 정규화한 임베딩의 내적을 사용합니다. "
        "0.8 이상을 일치로 처리하는 등의 threshold는 설정하지 않았습니다. "
        "후보를 찾은 뒤 동의어·관계 규칙과 LLM의 의미 판정으로 세 범주를 나눕니다.", "",
        "GT의 `qualifiers`가 비어 있지 않으면 보수적으로 부분 일치로 처리합니다. "
        "따라서 부분 일치에는 실제 조건 누락뿐 아니라 조건을 아직 확인하지 못한 사례도 포함됩니다. "
        "LLM 프롬프트에는 GT, 조건, 후보 canonical 관계와 관계 정의를 넣지만 원문 문단은 넣지 않습니다.", "",
        f"기존 입력과 그래프 해시 및 GT 내용이 동일한 {meta.get('reused_judgment_count',0)}개 판정을 재사용했습니다.", "",
        f"수치 불일치 등의 명시적 모순 검사로 {summary['contradiction_guard_count']}개 LLM 판정을 미확인으로 보정했습니다. "
        "이 검사는 기존 25개와 추가 25개 모두에 적용했습니다. 서로 다른 용량이나 "
        "abuse/misuse/addiction을 같은 핵심 사실로 세지 않기 위한 보정이며, 모든 판정 오류를 잡는 검사는 아닙니다.", "",
        f"GT {len(results):,}개 자체가 사람이 검수하지 않은 부분 주석 초안입니다. 임베딩 후보 검색과 LLM 판정에도 오류가 있을 수 있으며, "
        "Qwen3.5-9B는 앞선 문장 분해에도 사용된 모델이므로 평가기의 독립성을 보장하지 않습니다. "
        "실험/논문의 확정 성능 수치로 사용하려면 GT와 비교 판정을 독립적으로 사람이 검수해야 합니다.", "",
        "원래 관계(`raw_relationship`)나 근거 chunk가 맞더라도 canonical 그래프 관계가 "
        "다른 의미로 바뀌었다면 동일한 관계로 간주하지 않았습니다.", "",
        "파일: `semantic_comparison.csv`, `semantic_comparison.jsonl`, `per_drug_summary.csv`, `summary.json`. "
        "원본 그래프 파일과 GT 파일은 수정하지 않았습니다."])
    audit=[]
    patterns=[
        ("atorvastatin","Atorvastatin","contraindicated in","allergy to Metformin",
         "알레르기 대상 약물이 다릅니다. atorvastatin.txt 69행은 atorvastatin 알레르기를 말합니다.",
         "data/text-only/text-only/atorvastatin.txt",69),
        ("atorvastatin","Atorvastatin","belongs to drug class","Zocor",
         "atorvastatin.txt 7행의 약물 계열은 HMG-CoA reductase inhibitors/statins입니다. Zocor는 계열명으로 대응하지 않습니다.",
         "data/text-only/text-only/atorvastatin.txt",7),
        ("adderall","Adderall XR","administered via","breast milk in small amounts",
         "adderall.txt 63행의 'passes into breast milk'가 투여 경로로 바뀌었습니다. 모유 이행과 모유를 통한 투여는 다른 의미입니다.",
         "data/text-only/text-only/adderall.txt",63),
        ("carvedilol","Metoprolol","belongs to drug class","beta blocker",
         "carvedilol 문서 출처의 그래프 관계가 Metoprolol을 주어로 사용합니다. 서로 다른 약물 이름을 같은 개체로 간주하지 않았습니다.",
         "data/text-only/text-only/carvedilol.txt",5),
        ("cetirizine","Levocetirizine","belongs to drug class","second generation antihistamine",
         "cetirizine 문서 출처의 그래프 관계가 Levocetirizine을 주어로 사용합니다. 유사한 계열이어도 약물 자체의 동일성을 가정하지 않았습니다.",
         "data/text-only/text-only/cetirizine.txt",5),
    ]
    for slug,subject,relation,obj,reason,source_path,line_number in patterns:
        edge=next((e for e in all_graph_edges if slug in e["document_slugs"]
                   and e["subject"]==subject and e["relationship"]==relation and e["object"]==obj),None)
        if edge:
            original=(ROOT/source_path).read_text().splitlines()[line_number-1]
            audit.append({"graph_edge":edge,"source_file":source_path,"line_number":line_number,
                          "source_line":original,"audit_note_ko":reason})
    write_jsonl(output_dir/"graph_audit_examples.jsonl",audit)
    lines.extend(["", "## 직접 확인한 정규화 문제 사례", ""])
    for example in audit:
        edge=example["graph_edge"]
        lines.extend([f"- 그래프: `{edge['subject']} → {edge['relationship']} → {edge['object']}`",
                      f"  {example['audit_note_ko']}"])
    (output_dir/"report_ko.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({k:summary[k] for k in ["reference_count","status_counts","match_percent","match_or_partial_percent"]},ensure_ascii=False,indent=2))


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("stage",choices=["prepare","judge","summarize"])
    parser.add_argument("--output-dir",type=Path,default=ROOT/"data/gt_graph_semantic_comparison")
    parser.add_argument("--gt-file",type=Path,default=ROOT/"data/gt_top25_review/gold_triplets_draft.jsonl")
    parser.add_argument("--graph-file",type=Path,default=ROOT/"data/kg_explorer_edc_ec_g.html")
    parser.add_argument("--reuse-dir",type=Path)
    parser.add_argument("--shard",type=int,default=0)
    parser.add_argument("--shards",type=int,default=2)
    parser.add_argument("--batch-size",type=int,default=4)
    args=parser.parse_args()
    if args.stage=="prepare":prepare(args.output_dir,args.gt_file,args.graph_file,args.reuse_dir)
    elif args.stage=="judge":judge(args.output_dir,args.shard,args.shards,args.batch_size)
    else:summarize(args.output_dir)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
