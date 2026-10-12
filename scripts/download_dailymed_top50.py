#!/usr/bin/env python3
"""Download one representative current DailyMed SPL for each ClinCalc Top-50 drug.

The script preserves the first 100 (newest) DailyMed search candidates and stores
the selected SPL as raw XML, plain text, and section-oriented JSON.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path


API = "https://dailymed.nlm.nih.gov/dailymed/services/v2"
USER_AGENT = "DrugKnowledgeGraphAcademicProject/1.0 (DailyMed API client)"
NS = {"v3": "urn:hl7-org:v3"}


def fetch(url: str, attempts: int = 5) -> bytes:
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == attempts:
                raise
            delay = min(30, 2 ** attempt)
            logging.warning("request failed (%s/%s): %s; retry in %ss", attempt, attempts, exc, delay)
            time.sleep(delay)
    raise RuntimeError("unreachable")


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def published_timestamp(value: str) -> float:
    try:
        return parsedate_to_datetime(value).timestamp()
    except (TypeError, ValueError):
        return 0.0


def candidate_score(drug: dict, candidate: dict) -> tuple:
    title = norm(candidate.get("title", ""))
    name = norm(drug["name"])
    ingredients = [norm(item) for item in drug["ingredients"]]
    all_ingredients = all(item in title for item in ingredients)
    # Prefer labels whose title starts with the requested generic name. This
    # avoids selecting a combination such as Caduet for atorvastatin.
    starts_name = title.startswith(name)
    starts_ingredient = any(title.startswith(item) for item in ingredients)
    extra_combo_hint = " and " in title.split("[")[0]
    return (
        int(all_ingredients),
        int(starts_name),
        int(starts_ingredient),
        -int(extra_combo_hint and not drug["is_combination"]),
        published_timestamp(candidate.get("published_date", "")),
        int(candidate.get("spl_version", 0)),
    )


def element_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    text = " ".join(part.strip() for part in element.itertext() if part.strip())
    return re.sub(r"\s+", " ", text).strip()


def parse_spl(xml_bytes: bytes) -> tuple[dict, str]:
    root = ET.fromstring(xml_bytes)
    document_code = root.find("v3:code", NS)
    title = element_text(root.find("v3:title", NS))
    sections = []
    for section in root.findall(".//v3:section", NS):
        heading = element_text(section.find("v3:title", NS))
        body = element_text(section.find("v3:text", NS))
        code = section.find("v3:code", NS)
        if not heading and not body:
            continue
        sections.append({
            "code": code.get("code") if code is not None else None,
            "code_system": code.get("codeSystem") if code is not None else None,
            "title": heading or None,
            "text": body or None,
        })
    info = {
        "document_title": title or None,
        "document_code": document_code.get("code") if document_code is not None else None,
        "document_type": document_code.get("displayName") if document_code is not None else None,
        "sections": sections,
    }
    plain = "\n\n".join(
        filter(None, [title] + [f"{s['title']}\n{s['text']}" for s in sections])
    )
    return info, plain


def search_candidates(name: str) -> dict:
    query = urllib.parse.urlencode({
        "drug_name": name,
        "name_type": "generic",
        "pagesize": 100,
        "page": 1,
    })
    return json.loads(fetch(f"{API}/spls.json?{query}"))


def download_one(drug: dict, output_root: Path, delay: float) -> dict:
    target = output_root / f"{drug['rank']:02d}_{drug['slug']}"
    target.mkdir(parents=True, exist_ok=True)
    search = search_candidates(drug["name"])
    candidates = search.get("data", [])
    (target / "search_results.json").write_text(
        json.dumps(search, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if not candidates:
        raise RuntimeError(f"no DailyMed results for {drug['name']}")

    ranked = sorted(candidates, key=lambda item: candidate_score(drug, item), reverse=True)
    chosen = ranked[0]
    setid = chosen["setid"]
    time.sleep(delay)
    xml_bytes = fetch(f"{API}/spls/{urllib.parse.quote(setid)}.xml")
    parsed, plain = parse_spl(xml_bytes)
    (target / "label.xml").write_bytes(xml_bytes)
    (target / "label.txt").write_text(plain + "\n", encoding="utf-8")

    record = {
        "rank": drug["rank"],
        "query_name": drug["name"],
        "ingredients": drug["ingredients"],
        "selected_label": chosen,
        "selection_method": "best name/ingredient match among newest 100 search results",
        "candidate_count_returned": len(candidates),
        "candidate_count_total": search.get("metadata", {}).get("total_elements"),
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source": "DailyMed, U.S. National Library of Medicine",
        "source_url": f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={setid}",
        "api_url": f"{API}/spls/{setid}.xml",
        "sha256": hashlib.sha256(xml_bytes).hexdigest(),
        **parsed,
    }
    (target / "label.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return {
        "rank": drug["rank"],
        "query_name": drug["name"],
        "status": "ok",
        "setid": setid,
        "published_date": chosen.get("published_date"),
        "title": chosen.get("title"),
        "document_type": parsed.get("document_type"),
        "directory": target.name,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("data/clincalc_top50_2024.json"))
    parser.add_argument("--output", type=Path, default=Path("data/dailymed_top50_2024"))
    parser.add_argument("--delay", type=float, default=0.5, help="seconds between API calls")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    source = json.loads(args.input.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output / "manifest.json"
    prior = {}
    if manifest_path.exists():
        prior = {item["rank"]: item for item in json.loads(manifest_path.read_text()).get("drugs", [])}

    results = []
    for drug in source["drugs"]:
        existing = prior.get(drug["rank"])
        if existing and existing.get("status") == "ok":
            logging.info("[%02d/50] skip completed %s", drug["rank"], drug["name"])
            results.append(existing)
            continue
        logging.info("[%02d/50] downloading %s", drug["rank"], drug["name"])
        try:
            result = download_one(drug, args.output, args.delay)
            logging.info("[%02d/50] selected %s", drug["rank"], result["title"])
        except Exception as exc:  # keep the batch resumable
            logging.exception("[%02d/50] failed %s", drug["rank"], drug["name"])
            result = {"rank": drug["rank"], "query_name": drug["name"], "status": "error", "error": str(exc)}
        results.append(result)
        manifest = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "input": str(args.input),
            "source": "DailyMed REST API v2",
            "drugs": sorted(results + [v for k, v in prior.items() if k > drug["rank"]], key=lambda x: x["rank"]),
        }
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        time.sleep(args.delay)

    ok = sum(item["status"] == "ok" for item in results)
    logging.info("complete: %s ok, %s failed", ok, len(results) - ok)
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
