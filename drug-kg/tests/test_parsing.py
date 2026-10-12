"""Smoke tests that need no LLM / network:  python -m pytest tests -q"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from drugkg.chunk import chunk_record
from drugkg.edc.parsing import parse_raw_entities, parse_raw_triplets, parse_relation_definition
from drugkg.parse import parse_main_page
from drugkg.postprocess import entity_id, entity_key

RAW = pathlib.Path(__file__).resolve().parents[1] / "data" / "raw_html" / "atorvastatin.html"


def test_parse_triplets_json_and_python_literals():
    assert parse_raw_triplets('[["Lipitor", "has_generic_name", "atorvastatin"]]') == [["Lipitor", "has generic name", "atorvastatin"]]
    out = parse_raw_triplets("Triplets: [['metformin', 'Treats', 'type 2 diabetes'], ['x', 'y', 'x']] trailing")
    assert out == [["metformin", "treats", "type 2 diabetes"]]  # self-loop dropped, relation normalized


def test_parse_definitions_and_entities():
    d = parse_relation_definition("treats: The subject drug is used to treat the condition.\nAnswer: ignored\nfoo")
    assert d == {"treats": "The subject drug is used to treat the condition."}
    assert parse_raw_entities('["a", "b", "a"]') == ["a", "b"]


def test_entity_normalisation():
    assert entity_key("The severe kidney disease.") == "severe kidney disease"
    assert entity_id("ldl cholesterol ('bad')") == "ldl_cholesterol_bad"


def test_parse_and_chunk_real_page():
    if not RAW.exists():
        return
    rec = parse_main_page(RAW.read_text(encoding="utf-8"), "https://www.drugs.com/atorvastatin.html", "Atorvastatin", "atorvastatin")
    assert rec["generic_name"] == "atorvastatin" and "Lipitor" in rec["brand_names"]
    assert any(s["id"] == "side-effects" for s in rec["sections"])
    chunks = chunk_record(rec, 1100, 150, None, True, ["related-drugs", "faq"])
    assert chunks and len({c["chunk_id"] for c in chunks}) == len(chunks)
    assert all(len(c["text"]) <= 1100 * 1.5 for c in chunks)
