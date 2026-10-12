from __future__ import annotations
import pathlib
from dataclasses import dataclass, field
from typing import Any
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]


@dataclass
class Config:
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def load(cls, path: str | pathlib.Path = ROOT / "config.yaml") -> "Config":
        with open(path, "r", encoding="utf-8") as f:
            return cls(yaml.safe_load(f) or {})

    def get(self, dotted: str, default: Any = None) -> Any:
        cur: Any = self.raw
        for part in dotted.split("."):
            if not isinstance(cur, dict) or part not in cur:
                return default
            cur = cur[part]
        return cur

    def path(self, dotted: str, default: str | None = None) -> pathlib.Path:
        value = self.get(dotted, default)
        if value is None:
            raise KeyError(dotted)
        p = pathlib.Path(value)
        return p if p.is_absolute() else ROOT / p

    def section(self, name: str) -> dict[str, Any]:
        return dict(self.raw.get(name, {}) or {})
