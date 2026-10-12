"""Prompt builders for each EDC stage (templates live in prompts/)."""
from __future__ import annotations
import json
import pathlib

from .parsing import normalize_relation
from .schema import ENTITY_TYPES

PROMPT_DIR = pathlib.Path(__file__).resolve().parents[2] / "prompts"


def _read(name: str) -> str:
    return (PROMPT_DIR / name).read_text(encoding="utf-8")


class Prompts:
    def __init__(self):
        self.oie = _read("oie_template.txt")
        self.oie_fs = _read("oie_few_shot.txt").strip()
        self.oie_r = _read("oie_r_template.txt")
        self.oie_r_fs = _read("oie_r_few_shot.txt").strip()
        self.sd = _read("sd_template.txt")
        self.sd_fs = _read("sd_few_shot.txt").strip()
        self.sc = _read("sc_template.txt")
        self.ee = _read("ee_template.txt")
        self.ee_fs = _read("ee_few_shot.txt").strip()
        self.em = _read("em_template.txt")
        self.type = _read("type_template.txt")
        self.merge = _read("merge_template.txt")

    # ---- Extract
    def oie_prompt(self, chunk: dict) -> str:
        return self.oie.format(drug=chunk["drug"], section=chunk["section_heading"], few_shot_examples=self.oie_fs,
                               input_text=chunk["text"])

    def oie_refine_prompt(self, chunk: dict, entities_hint: list[str], relations_hint: str) -> str:
        return self.oie_r.format(drug=chunk["drug"], section=chunk["section_heading"], few_shot_examples=self.oie_r_fs,
                                 input_text=chunk["text"], entities_hint=json.dumps(entities_hint, ensure_ascii=False),
                                 relations_hint=relations_hint or "(none)")

    # ---- Define
    def sd_prompt(self, chunk: dict, triplets: list[list[str]]) -> str:
        relations = sorted({normalize_relation(t[1]) for t in triplets})
        return self.sd.format(few_shot_examples=self.sd_fs, text=chunk["text"],
                              triples=json.dumps(triplets, ensure_ascii=False),
                              relations=json.dumps(relations, ensure_ascii=False))

    # ---- Canonicalize
    def sc_prompt(self, text: str, triplet: list[str], definition: str, candidates: list[tuple[str, str]]) -> tuple[str, list[str]]:
        """candidates: [(relation, definition)]. Returns (prompt, letters) where the last letter is 'None of the above'."""
        letters, choices = [], ""
        for i, (rel, d) in enumerate(candidates):
            letter = chr(ord("A") + i)
            letters.append(letter)
            choices += f"{letter}. '{rel}': {d}\n"
        none_letter = chr(ord("A") + len(candidates))
        choices += f"{none_letter}. None of the above.\n"
        prompt = self.sc.format(input_text=text, query_triplet=json.dumps(triplet, ensure_ascii=False),
                                query_relation=triplet[1], query_relation_definition=definition, choices=choices)
        return prompt, letters

    # ---- Entity extraction / merging (refinement)
    def ee_prompt(self, chunk: dict) -> str:
        return self.ee.format(drug=chunk["drug"], few_shot_examples=self.ee_fs, input_text=chunk["text"])

    def em_prompt(self, chunk: dict, list1: list[str], list2: list[str]) -> str:
        return self.em.format(input_text=chunk["text"], entity_list_1=json.dumps(list1, ensure_ascii=False),
                              entity_list_2=json.dumps(list2, ensure_ascii=False))

    # ---- helpers for schema maintenance
    def type_prompt(self, relation: str, definition: str, example) -> str:
        return self.type.format(relation=relation, definition=definition, example=json.dumps(example, ensure_ascii=False),
                                types=", ".join(ENTITY_TYPES))

    def merge_prompt(self, rel_a: str, def_a: str, ex_a, rel_b: str, def_b: str, ex_b) -> str:
        return self.merge.format(relation_a=rel_a, definition_a=def_a, example_a=json.dumps(ex_a, ensure_ascii=False),
                                 relation_b=rel_b, definition_b=def_b, example_b=json.dumps(ex_b, ensure_ascii=False))
