"""Polite fetcher for Drugs.com pages with on-disk caching and slug resolution."""
from __future__ import annotations
import json
import logging
import pathlib
import random
import re
import time

import requests

log = logging.getLogger(__name__)

BASE = "https://www.drugs.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Windows"', "Connection": "keep-alive",
}
PAGE_PATHS = {
    "main": "/{slug}.html",
    "sfx": "/sfx/{slug}-side-effects.html",
    "dosage": "/dosage/{slug}.html",
}


class BlockedError(RuntimeError):
    pass


def _title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    return (m.group(1).strip() if m else "")


def page_ok(status: int, html: str) -> bool:
    t = _title(html)
    return status == 200 and "Access Denied" not in t and "Page Not Found" not in t and len(html) > 5000


class PoliteFetcher:
    def __init__(self, raw_dir: pathlib.Path, delay_range=(6, 10), max_retries: int = 4):
        self.raw_dir = pathlib.Path(raw_dir)
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.delay_range = tuple(delay_range)
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self._warm = False
        self._last = 0.0

    def _warm_up(self, fresh: bool = False) -> None:
        if fresh:  # drop cookies flagged by the bot manager and start a new session
            self.session = requests.Session()
            self.session.headers.update(HEADERS)
        try:
            self.session.get(BASE + "/", timeout=30)
        except requests.RequestException as e:  # pragma: no cover
            log.warning("warm-up failed: %s", e)
        self._warm = True
        self._last = time.time()

    def _wayback(self, path: str) -> str | None:
        """Fallback: fetch the most recent Internet Archive snapshot of the page."""
        url = f"https://web.archive.org/web/2026id_/{BASE}{path}"
        for attempt in range(3):
            try:
                r = requests.get(url, headers={"User-Agent": HEADERS["User-Agent"]}, timeout=60)
            except requests.RequestException as e:
                log.warning("wayback error %s: %s", url, e)
                time.sleep(20)
                continue
            if r.status_code == 200 and len(r.text) > 5000:
                log.info("fetched Wayback snapshot for %s (%s)", path, r.url)
                return r.text
            if r.status_code == 429:
                time.sleep(60 * (attempt + 1))
                continue
            log.warning("wayback %s for %s", r.status_code, url)
            return None
        return None

    def _sleep(self) -> None:
        wait = random.uniform(*self.delay_range) - (time.time() - self._last)
        if wait > 0:
            time.sleep(wait)

    @staticmethod
    def cache_name(path: str) -> str:
        return path.strip("/").replace("/", "__")

    def get(self, path: str, use_cache: bool = True) -> str | None:
        """Return the HTML for a Drugs.com path (e.g. '/lipitor.html'), or None when it does not exist."""
        cache = self.raw_dir / self.cache_name(path)
        if use_cache and cache.exists():
            html = cache.read_text(encoding="utf-8")
            if page_ok(200, html):
                return html
        if not self._warm:
            self._warm_up()
        url = BASE + path
        for attempt in range(self.max_retries + 1):
            self._sleep()
            try:
                r = self.session.get(url, timeout=45)
            except requests.RequestException as e:
                log.warning("request error %s (%s); retrying", url, e)
                time.sleep(15)
                continue
            self._last = time.time()
            title = _title(r.text)
            if r.status_code == 404 or "Page Not Found" in title:
                log.info("404 %s", url)
                return None
            if r.status_code in (403, 429) or "Access Denied" in title:
                backoff = 45 * (attempt + 1)
                log.warning("blocked (%s) on %s; backing off %ds (attempt %d/%d)", r.status_code, url, backoff,
                            attempt + 1, self.max_retries)
                time.sleep(backoff)
                self._warm_up(fresh=True)
                continue
            if page_ok(r.status_code, r.text):
                cache.write_text(r.text, encoding="utf-8")
                log.info("fetched %s (%d bytes)", url, len(r.text))
                return r.text
            log.warning("unexpected response %s for %s", r.status_code, url)
        html = self._wayback(path)
        if html and page_ok(200, html):
            cache.write_text(html, encoding="utf-8")
            return html
        raise BlockedError(f"gave up fetching {url}")


def default_candidates(name: str) -> list[str]:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return [slug]


def resolve_drug_urls(drugs: list[dict], fetcher: PoliteFetcher, url_map_path: pathlib.Path) -> dict[str, dict]:
    """Map each drug name to a Drugs.com slug (trying candidates in order) and persist the mapping."""
    url_map: dict[str, dict] = {}
    if url_map_path.exists():
        url_map = json.loads(url_map_path.read_text(encoding="utf-8"))
    for d in drugs:
        name = d["name"]
        if name in url_map and url_map[name].get("slug"):
            continue
        candidates = [d["slug"]] if d.get("slug") else list(d.get("candidates") or default_candidates(name))
        found = None
        for slug in candidates:
            html = fetcher.get(PAGE_PATHS["main"].format(slug=slug))
            if html:
                found = {"slug": slug, "url": BASE + PAGE_PATHS["main"].format(slug=slug), "title": _title(html)}
                break
        url_map[name] = found or {"slug": None, "tried": candidates}
        url_map_path.parent.mkdir(parents=True, exist_ok=True)
        url_map_path.write_text(json.dumps(url_map, indent=2, ensure_ascii=False), encoding="utf-8")
        if not found:
            log.error("could not resolve a Drugs.com page for %s (tried %s)", name, candidates)
    return url_map


def fetch_drug_pages(slug: str, pages: list[str], fetcher: PoliteFetcher) -> dict[str, str]:
    out = {}
    for page in pages:
        html = fetcher.get(PAGE_PATHS[page].format(slug=slug))
        if html:
            out[page] = html
    return out
