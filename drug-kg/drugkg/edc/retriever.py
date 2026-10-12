"""Schema retriever: fetch relations likely present in a text (used to build hints for refined extraction)."""
from __future__ import annotations
from .schema import Schema

QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


class SchemaRetriever:
    def __init__(self, schema: Schema, top_k: int = 10):
        self.schema = schema
        self.top_k = top_k

    def retrieve(self, text: str) -> list[str]:
        q = self.schema.embedder.encode_one(QUERY_PREFIX + text)
        if self.schema._emb is None:
            return []
        scores = self.schema._emb @ q
        order = scores.argsort()[::-1][: self.top_k]
        return [self.schema._names[i] for i in order]
