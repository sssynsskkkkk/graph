"""Relation schema with definition embeddings (used for canonicalization and the schema retriever)."""
from __future__ import annotations
import csv
import json
import logging
import pathlib
import threading

import numpy as np

log = logging.getLogger(__name__)

ENTITY_TYPES = ["Drug", "DrugClass", "Ingredient", "Condition", "SideEffect", "Symptom", "Substance", "Therapy",
                "Mechanism", "Warning", "Population", "DosageForm", "Strength", "Route", "Dose", "LabTest",
                "Schedule", "Organization", "Year", "Instruction", "Availability", "Other"]


class Embedder:
    def __init__(self, model_name: str, device: str = "cpu"):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name, device=device)
        self.model_name = model_name
        self._cache: dict[str, np.ndarray] = {}
        self._lock = threading.Lock()

    def encode(self, texts: list[str]) -> np.ndarray:
        missing = [t for t in texts if t not in self._cache]
        if missing:
            vecs = self.model.encode(missing, normalize_embeddings=True, batch_size=64, show_progress_bar=False)
            with self._lock:
                for t, v in zip(missing, vecs):
                    self._cache[t] = np.asarray(v, dtype=np.float32)
        return np.stack([self._cache[t] for t in texts]) if texts else np.zeros((0, 1), dtype=np.float32)

    def encode_one(self, text: str) -> np.ndarray:
        return self.encode([text])[0]


class Schema:
    """Ordered mapping relation -> {definition, subject_type, object_type, origin, count, example}."""

    def __init__(self, embedder: Embedder):
        self.embedder = embedder
        self.relations: dict[str, dict] = {}
        self._names: list[str] = []
        self._emb: np.ndarray | None = None
        self._lock = threading.Lock()

    def __contains__(self, name: str) -> bool:
        return name in self.relations

    def __len__(self) -> int:
        return len(self.relations)

    def add(self, name: str, definition: str, subject_type: str = "Drug", object_type: str = "Other",
            origin: str = "enriched", example=None, count: int = 0) -> None:
        with self._lock:
            if name in self.relations:
                return
            self.relations[name] = {"definition": definition, "subject_type": subject_type, "object_type": object_type,
                                    "origin": origin, "count": count, "example": example}
            self._names.append(name)
            vec = self.embedder.encode_one(definition)[None, :]
            self._emb = vec if self._emb is None else np.vstack([self._emb, vec])

    def bump(self, name: str, n: int = 1) -> None:
        if name in self.relations:
            self.relations[name]["count"] += n

    def retrieve(self, definition: str, top_k: int = 5, restrict_to: set[str] | None = None,
                 exclude: set[str] | None = None) -> list[tuple[str, float]]:
        if self._emb is None or not self._names:
            return []
        q = self.embedder.encode_one(definition)
        scores = self._emb @ q
        order = np.argsort(-scores)
        out = []
        for idx in order:
            name = self._names[idx]
            if restrict_to is not None and name not in restrict_to:
                continue
            if exclude and name in exclude:
                continue
            out.append((name, float(scores[idx])))
            if len(out) >= top_k:
                break
        return out

    def definition(self, name: str) -> str:
        return self.relations[name]["definition"]

    # ------------------------------------------------------------ persistence
    def save(self, path: pathlib.Path) -> None:
        path = pathlib.Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["relation", "definition", "subject_type", "object_type", "origin", "count", "example"])
            for name in self._names:
                r = self.relations[name]
                w.writerow([name, r["definition"], r["subject_type"], r["object_type"], r["origin"], r["count"],
                            json.dumps(r.get("example"), ensure_ascii=False) if r.get("example") else ""])

    @classmethod
    def load(cls, path: pathlib.Path, embedder: Embedder, default_origin: str = "seed") -> "Schema":
        schema = cls(embedder)
        with open(path, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        definitions = [r["definition"] for r in rows]
        embedder.encode(definitions)  # batch-embed once
        for r in rows:
            example = None
            if r.get("example"):
                try:
                    example = json.loads(r["example"])
                except Exception:
                    example = None
            schema.add(r["relation"].strip(), r["definition"].strip(), r.get("subject_type") or "Drug",
                       r.get("object_type") or "Other", r.get("origin") or default_origin, example,
                       int(r.get("count") or 0))
        log.info("schema loaded from %s: %d relations", path, len(schema))
        return schema
