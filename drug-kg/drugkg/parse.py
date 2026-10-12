"""Parse Drugs.com drug pages into a structured record (metadata + ordered text sections)."""
from __future__ import annotations
import json
import re
from bs4 import BeautifulSoup, NavigableString, Tag

SKIP_CLASS = re.compile(r"(ddc-box|ddc-mgb|ddc-related|ddc-carousel|ddc-ad|ddc-status|noprint|ddc-reviewed|ddc-sponsor|"
                        r"ddc-video|ddc-toc|ddc-breadcrumb|ddc-share|ddc-pagination|ddc-card|ddc-notice|ddc-author)")
SKIP_TAGS = {"script", "style", "nav", "aside", "figure", "img", "svg", "form", "button", "iframe", "noscript", "input"}
EXCLUDE_HEADINGS = re.compile(r"^(more about|further information|references|related/similar drugs|see also|popular faq|"
                              r"frequently asked questions|images|more faq|professional resources|patient resources|"
                              r"related treatment guides)", re.I)


def clean(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:)])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    return text


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def element_lines(el) -> list[str]:
    """Flatten an element into text lines: paragraphs, list items, dl pairs, table rows, sub-headings."""
    if isinstance(el, NavigableString):
        t = clean(str(el))
        return [t] if len(t) > 1 else []
    if not isinstance(el, Tag) or el.name in SKIP_TAGS:
        return []
    cls = " ".join(el.get("class") or [])
    if SKIP_CLASS.search(cls) or el.get("data-ad-injection-skip") is not None and el.name == "div" and "carousel" in cls:
        return []
    if el.name == "p":
        t = clean(el.get_text(" "))
        return [t] if t else []
    if el.name in ("ul", "ol"):
        out = []
        for li in el.find_all("li", recursive=False):
            t = clean(li.get_text(" "))
            if t:
                out.append("- " + t)
        return out
    if el.name in ("h3", "h4", "h5"):
        t = clean(el.get_text(" "))
        return [t.rstrip(":") + ":"] if t else []
    if el.name == "dl":
        out, dt = [], None
        for child in el.find_all(["dt", "dd"], recursive=False):
            if child.name == "dt":
                dt = clean(child.get_text(" "))
            else:
                dd = clean(child.get_text(" "))
                out.append(f"{dt}: {dd}" if dt else dd)
        return out
    if el.name == "table":
        out = []
        for row in el.find_all("tr"):
            cells = [clean(c.get_text(" ")) for c in row.find_all(["td", "th"])]
            cells = [c for c in cells if c]
            if cells:
                out.append(" | ".join(cells))
        return out
    if el.name == "details":
        out = []
        for child in el.children:
            if isinstance(child, Tag) and child.name == "summary":
                t = clean(child.get_text(" "))
                if t:
                    out.append(t.rstrip(":") + ":")
            else:
                out.extend(element_lines(child))
        return out
    if el.name in ("div", "section", "article", "blockquote", "span", "li"):
        out = []
        for child in el.children:
            out.extend(element_lines(child))
        return out
    t = clean(el.get_text(" "))
    return [t] if t and el.name in ("b", "strong", "em", "i", "a") and len(t) > 2 else []


def parse_sections(soup: BeautifulSoup, page: str = "main") -> list[dict]:
    main = soup.find("main") or soup
    sections = []
    for h2 in main.find_all("h2"):
        heading = clean(h2.get_text(" "))
        if not heading or EXCLUDE_HEADINGS.search(heading):
            continue
        sid = h2.get("id") or slugify(heading)
        lines: list[str] = []
        for sib in h2.find_next_siblings():
            if sib.name == "h2":
                break
            lines.extend(element_lines(sib))
        lines = [l for l in lines if l]
        if not lines:
            continue
        sections.append({"id": sid if page == "main" else f"{page}:{sid}", "page": page, "heading": heading,
                         "lines": lines, "text": "\n".join(lines)})
    return sections


def parse_subtitle(p: Tag) -> dict:
    fields: dict[str, str] = {}
    current, buf = None, []

    def flush():
        if current is not None:
            fields[current] = clean(" ".join(buf))

    for node in p.children:
        if isinstance(node, Tag) and node.name == "b":
            flush()
            label = clean(node.get_text(" ")).rstrip(":").lower()
            current, buf = label, []
        elif isinstance(node, Tag) and node.name == "br":
            continue
        else:
            buf.append(node.get_text(" ") if isinstance(node, Tag) else str(node))
    flush()
    out: dict = {}
    for label, value in fields.items():
        if "generic name" in label:
            m = re.match(r"(.*?)\s*\[\s*(.*?)\s*\]", value)
            out["generic_name"] = clean(m.group(1)) if m else value
            if m:
                out["pronunciation"] = m.group(2)
        elif "brand name" in label:
            value = re.sub(r"^.*?\binclude:?\s*", "", value)  # "Other brand names of X include: A, B"
            names = [clean(x) for x in re.split(r"[,.]", value) if clean(x)]
            out["brand_names"] = [re.sub(r"\s*\(discontinued\)", "", n) for n in names]
            out["discontinued_brands"] = [re.sub(r"\s*\(discontinued\)", "", n) for n in names if "discontinued" in n]
        elif "dosage form" in label:
            forms = []
            for m in re.finditer(r"([^,()]+?)\s*\(([^)]*)\)", value):
                forms.append({"form": clean(m.group(1)), "strengths": [clean(s) for s in m.group(2).split(";") if clean(s)]})
            if not forms:
                forms = [{"form": clean(f), "strengths": []} for f in value.split(",") if clean(f)]
            out["dosage_forms"] = forms
        elif "drug class" in label:
            out["drug_classes"] = [{"name": clean(a.get_text(" ")), "slug": a.get("href", "").split("/")[-1].replace(".html", "")}
                                   for a in p.find_all("a") if "/drug-class/" in a.get("href", "")]
            if not out["drug_classes"]:
                out["drug_classes"] = [{"name": clean(x), "slug": slugify(x)} for x in value.split(",") if clean(x)]
    return out


def parse_jsonld(soup: BeautifulSoup) -> dict:
    out: dict = {"faq": []}
    for sc in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(sc.string or "")
        except Exception:
            continue
        for item in (data if isinstance(data, list) else [data]):
            t = item.get("@type")
            if t == "MedicalWebPage":
                out["description"] = item.get("description")
                out["date_modified"] = item.get("dateModified")
                rb = item.get("reviewedBy") or {}
                out["reviewed_by"] = rb.get("name")
            elif t == "FAQPage":
                for q in item.get("mainEntity", []) or []:
                    ans = (q.get("acceptedAnswer") or {}).get("text", "")
                    out["faq"].append({"q": clean(q.get("name", "")), "a": clean(BeautifulSoup(ans, "lxml").get_text(" "))})
    return out


def parse_info_box(soup: BeautifulSoup) -> dict:
    out: dict = {}
    for item in soup.select(".ddc-status-info-item"):
        b = item.find("b")
        sub = item.select_one(".ddc-status-info-item-subtitle")
        if not b:
            continue
        key = clean(b.get_text(" ")).lower()
        val = clean(sub.get_text(" ")) if sub else ""
        if key.startswith("availability"):
            out["availability"] = val
        elif key.startswith("csa"):
            out["csa_schedule"] = val
        elif key.startswith("approval"):
            m = re.search(r"(19|20)\d{2}", val)
            out["fda_approval_year"] = m.group(0) if m else None
        elif key.startswith("pregnancy"):
            out["pregnancy"] = val
    return out


def parse_related(soup: BeautifulSoup) -> list[dict]:
    out = []
    h2 = soup.find("h2", id="related-drugs")
    if not h2:
        return out
    for sib in h2.find_next_siblings():
        if sib.name == "h2":
            break
        for h3 in sib.find_all("h3"):
            a = h3.find("a")
            if not a:
                continue
            p = h3.find_next_sibling("p")
            out.append({"name": clean(a.get_text(" ")), "slug": a.get("href", "").strip("/").replace(".html", ""),
                        "blurb": clean(p.get_text(" ")) if p else ""})
    return out


def parse_main_page(html: str, url: str, name: str | None = None, slug: str | None = None) -> dict:
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main") or soup
    h1 = main.find("h1")
    record: dict = {"name": name, "slug": slug, "url": url, "title": clean(h1.get_text(" ")) if h1 else name,
                    "page_title": clean(soup.title.get_text()) if soup.title else ""}
    sub = main.find("p", class_="drug-subtitle")
    if sub:
        record.update(parse_subtitle(sub))
    rev = main.find("p", class_="ddc-reviewed-by")
    if rev:
        record["reviewed_line"] = clean(rev.get_text(" "))
    record.update(parse_jsonld(soup))
    record.update(parse_info_box(soup))
    record["related_drugs"] = parse_related(soup)
    record["sections"] = parse_sections(soup, "main")
    if record.get("faq"):
        record["sections"].append({"id": "faq", "page": "main", "heading": "Popular FAQ",
                                   "lines": [f"Q: {f['q']} A: {f['a']}" for f in record["faq"]],
                                   "text": "\n".join(f"Q: {f['q']} A: {f['a']}" for f in record["faq"])})
    return record


def parse_subpage(html: str, page: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    return parse_sections(soup, page)
