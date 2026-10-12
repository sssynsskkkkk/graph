"""OpenAI-compatible chat client with a disk cache and bounded concurrency.

Works against the local vLLM server (scripts/serve_vllm.sh) or any OpenAI-compatible endpoint.
"""
from __future__ import annotations
import hashlib
import json
import logging
import os
import pathlib
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable, Sequence

from openai import OpenAI, APIConnectionError, APIStatusError, APITimeoutError, RateLimitError
from tqdm import tqdm

log = logging.getLogger(__name__)

SYSTEM_PROMPT = "You are a precise biomedical information extraction assistant. Follow the requested output format exactly and never add explanations."


class LLMClient:
    def __init__(self, base_url: str, api_key: str, model: str, temperature: float = 0.0, max_tokens: int = 1024,
                 concurrency: int = 8, timeout: float = 300, cache_dir: str | os.PathLike | None = None,
                 system_prompt: str = SYSTEM_PROMPT, extra_body: dict | None = None):
        self.client = OpenAI(base_url=base_url, api_key=api_key or "EMPTY", timeout=timeout, max_retries=0)
        self.model = model
        self.extra_body = dict(extra_body or {})
        # The served name may be a model-agnostic alias (e.g. "drugkg-llm"); resolve the real model id so that the
        # disk cache never returns completions produced by a different model.
        self.model_id = model
        try:
            for m in self.client.models.list().data:
                if m.id == model:
                    self.model_id = getattr(m, "root", None) or model
                    break
        except Exception:
            pass
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.concurrency = max(1, int(concurrency))
        self.system_prompt = system_prompt
        self.cache_dir = pathlib.Path(cache_dir) if cache_dir else None
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self.stats = {"calls": 0, "cache_hits": 0, "prompt_tokens": 0, "completion_tokens": 0, "errors": 0}

    # ------------------------------------------------------------------ cache
    def _key(self, messages: list[dict], max_tokens: int, stop: Sequence[str] | None) -> str:
        payload = json.dumps({"m": self.model_id, "t": self.temperature, "mt": max_tokens, "stop": list(stop or []),
                              "extra": self.extra_body, "msgs": messages}, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def _cache_path(self, key: str) -> pathlib.Path:
        return self.cache_dir / key[:2] / f"{key}.json"

    def _cache_get(self, key: str) -> str | None:
        if not self.cache_dir:
            return None
        p = self._cache_path(key)
        if p.exists():
            try:
                return json.loads(p.read_text(encoding="utf-8"))["completion"]
            except Exception:
                return None
        return None

    def _cache_put(self, key: str, messages: list[dict], completion: str) -> None:
        if not self.cache_dir:
            return
        p = self._cache_path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        # unique temp name per writer: identical prompts can be in flight on several threads at once
        tmp = p.with_name(f"{p.stem}.{threading.get_ident()}.tmp")
        tmp.write_text(json.dumps({"model": self.model_id, "messages": messages, "completion": completion},
                                  ensure_ascii=False), encoding="utf-8")
        try:
            os.replace(tmp, p)
        except FileNotFoundError:  # another thread already wrote the same entry
            pass

    # ------------------------------------------------------------------ calls
    def chat(self, prompt: str, max_tokens: int | None = None, stop: Sequence[str] | None = None,
             system: str | None = None, retries: int = 6) -> str:
        max_tokens = max_tokens or self.max_tokens
        messages = [{"role": "system", "content": system or self.system_prompt}, {"role": "user", "content": prompt}]
        key = self._key(messages, max_tokens, stop)
        cached = self._cache_get(key)
        if cached is not None:
            with self._lock:
                self.stats["cache_hits"] += 1
            return cached
        delay = 2.0
        for attempt in range(retries):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model, messages=messages, temperature=self.temperature,
                    max_tokens=max_tokens, stop=list(stop) if stop else None,
                    extra_body=self.extra_body or None)
                text = (resp.choices[0].message.content or "").strip()
                with self._lock:
                    self.stats["calls"] += 1
                    if resp.usage:
                        self.stats["prompt_tokens"] += resp.usage.prompt_tokens or 0
                        self.stats["completion_tokens"] += resp.usage.completion_tokens or 0
                self._cache_put(key, messages, text)
                return text
            except (APIConnectionError, APITimeoutError, RateLimitError) as e:
                err = e
            except APIStatusError as e:
                err = e
                if e.status_code < 500:
                    raise
            with self._lock:
                self.stats["errors"] += 1
            log.warning("LLM call failed (%s), retry %d/%d in %.0fs", err.__class__.__name__, attempt + 1, retries, delay)
            time.sleep(delay)
            delay = min(delay * 2, 60)
        raise RuntimeError(f"LLM call failed after {retries} retries: {err}")

    def chat_many(self, prompts: Iterable[str], max_tokens: int | None = None, stop: Sequence[str] | None = None,
                  desc: str = "llm") -> list[str]:
        prompts = list(prompts)
        results: list[str | None] = [None] * len(prompts)
        if not prompts:
            return []
        with ThreadPoolExecutor(max_workers=self.concurrency) as ex:
            futures = {ex.submit(self.chat, p, max_tokens, stop): i for i, p in enumerate(prompts)}
            for fut in tqdm(futures, total=len(futures), desc=desc, leave=False):
                pass
            for fut, i in futures.items():
                results[i] = fut.result()
        return results  # type: ignore[return-value]

    def ping(self) -> bool:
        try:
            self.client.models.list()
            return True
        except Exception as e:  # pragma: no cover
            log.error("LLM server not reachable at %s: %s", self.client.base_url, e)
            return False


def build_llm(cfg) -> LLMClient:
    llm_cfg = cfg.section("llm")
    cache_dir = cfg.path("llm.cache_dir") if llm_cfg.get("cache_dir") else None
    api_key = os.environ.get("DRUGKG_LLM_API_KEY") or llm_cfg.get("api_key") or "EMPTY"
    return LLMClient(base_url=os.environ.get("DRUGKG_LLM_BASE_URL", llm_cfg.get("base_url")), api_key=api_key,
                     model=os.environ.get("DRUGKG_LLM_MODEL", llm_cfg.get("model")),
                     temperature=float(llm_cfg.get("temperature", 0.0)), max_tokens=int(llm_cfg.get("max_tokens", 1024)),
                     concurrency=int(llm_cfg.get("concurrency", 8)), timeout=float(llm_cfg.get("timeout", 300)),
                     cache_dir=cache_dir, extra_body=llm_cfg.get("extra_body"))
