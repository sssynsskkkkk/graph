#!/usr/bin/env python
"""Visualize an exported KG: an interactive explorer (HTML) plus static figures (PNG) for slides.

Usage
  python scripts/visualize_kg.py --kg output/kg                                   # -> output/viz/main/
  python scripts/visualize_kg.py --kg output/experiments/decomp_edc/kg            # -> output/viz/decomp_edc/
  python scripts/visualize_kg.py --kg output/experiments/decomp_edc_ec_g/kg_canon --name decomp_edc_ec_g_canon --drug Metformin
  python scripts/visualize_kg.py --all                                            # every KG under output/ (main + experiments)

Outputs (per KG)
  kg_explorer.html         interactive explorer: search an entity, 1-2 hops, filter by relation/type/count, drug overview,
                           shared-side-effect view, evidence sentence per edge, CSV export (needs internet for vis-network CDN)
  fig_relations.png        top-20 relations (bar)
  fig_entity_types.png     entities by type group (bar)
  fig_triples_per_drug.png top-15 drugs by number of triples (bar)
  fig_shared_side_effects.png  side effects shared by the most drugs (bar)
  fig_ego_<drug>.png       1-hop neighbourhood of one drug (network), one per --drug
  fig_experiments.png      (with --all) entities / triples / relations per experiment, small multiples
"""
from __future__ import annotations
import argparse
import os
os.environ.setdefault("MPLCONFIGDIR", os.path.expanduser("~/.cache/matplotlib"))  # ~/.config is not writable on this machine
import collections
import csv
import html
import json
import math
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

# ---- type groups (<= 7 categorical classes) and the validated reference palette (fixed slot order, never cycled)
GROUPS = [("Drug", ["Drug"]),
          ("Condition", ["Condition", "Symptom"]),
          ("Side effect", ["SideEffect"]),
          ("Substance / class", ["Substance", "Ingredient", "DrugClass"]),
          ("Dosing", ["Dose", "Strength", "DosageForm", "Route", "Schedule"]),
          ("Instruction / warning", ["Instruction", "Warning"]),
          ("Other", [])]
GROUP_OF = {t: gi for gi, (_, ts) in enumerate(GROUPS) for t in ts}
LIGHT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#898781"]  # slots 1-6 + muted gray for Other
DARK = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#898781"]
SHAPES = ["diamond", "dot", "dot", "triangle", "hexagon", "square", "dot"]  # secondary encoding (shape) per group; labels stay outside
INK = {"light": {"surface": "#fcfcfb", "page": "#f9f9f7", "text": "#0b0b0b", "text2": "#52514e", "muted": "#898781",
                 "grid": "#e1e0d9", "axis": "#c3c2b7"},
       "dark": {"surface": "#1a1a19", "page": "#0d0d0d", "text": "#ffffff", "text2": "#c3c2b7", "muted": "#898781",
                "grid": "#2c2c2a", "axis": "#383835"}}
VIS_JS = "https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/dist/vis-network.min.js"


def group_index(etype: str) -> int:
    return GROUP_OF.get(etype, len(GROUPS) - 1)


# ----------------------------------------------------------------------------- loading
def load_kg(kg_dir: pathlib.Path) -> dict:
    ents = {e["id"]: e for e in csv.DictReader(open(kg_dir / "entities.csv", encoding="utf-8"))}
    triples = [json.loads(l) for l in (kg_dir / "triples.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    schema = {r["relation"]: r for r in csv.DictReader(open(kg_dir / "schema.csv", encoding="utf-8"))} if (kg_dir / "schema.csv").exists() else {}
    stats = json.loads((kg_dir / "stats.json").read_text(encoding="utf-8")) if (kg_dir / "stats.json").exists() else {}
    return {"entities": ents, "triples": triples, "schema": schema, "stats": stats}


def find_chunks_dir(kg_dir: pathlib.Path) -> pathlib.Path | None:
    for cand in (kg_dir.parent / "chunks", ROOT / "data" / "chunks"):
        if cand.exists():
            return cand
    return None


def load_chunk_texts(chunks_dir: pathlib.Path | None, wanted: set[str]) -> tuple[dict[str, str], dict[str, list]]:
    """chunk_id -> text, and (sentence inputs only) chunk_id -> [[decomposed sentence, decomposer input, raw page sentence], ...]."""
    out, sents = {}, {}
    if not chunks_dir:
        return out, sents
    for f in chunks_dir.glob("*.jsonl"):
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            c = json.loads(line)
            if c["chunk_id"] in wanted:
                out[c["chunk_id"]] = c["text"]
                if c.get("sentences"):
                    sents[c["chunk_id"]] = [[s["sentence"], s.get("decomposer_input") or "", s.get("raw_sentence") or ""]
                                            for s in c["sentences"]]
    return out, sents


def load_trace(path: pathlib.Path) -> dict[str, dict]:
    """trace.jsonl of scripts/build_trace.py -> {file stem: {drug, rows: [[section, line, raw, coref, edits, label, status,
    [[output_index, sentence], ...], record_id], ...]}} for the 'Source trace' tab."""
    if not path.exists():
        return {}
    out: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        t = json.loads(line)
        d = out.setdefault(pathlib.Path(t["source_file"]).stem, {"drug": t["drug"], "rows": []})
        d["rows"].append([t["section_title"] or "", t["line_number"], t["raw_sentence"], t["coref_sentence"], t["coref_edits"],
                          t["label"], t["status"], [[x["output_index"], x["sentence"]] for x in t["decomposed"]], t["record_id"]])
    return out


_STOP = {"the", "and", "for", "with", "you", "your", "are", "may", "can", "not", "this", "that", "has", "have", "from",
         "into", "use", "used", "using", "take", "taking", "any", "all", "other", "medicine", "medicines"}


def _words(text: str) -> set[str]:
    """Content words cut to 5 characters (a crude stem: allergy/allergic, interact/interaction)."""
    return {w[:5] for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 2 and w not in _STOP}


def best_sentences(sentences: list[list[str]], subj: str, obj: str, top: int = 2) -> list[int]:
    """Indices of the decomposed sentences that best support (subj, obj): object words weigh twice the subject words.
    Words present in most sentences of the chunk (typically the drug name) do not discriminate and are ignored."""
    words = [_words(sent) for sent, *_rest in sentences]
    df = collections.Counter(w for ws in words for w in ws)
    common = {w for w, n in df.items() if len(sentences) > 2 and n > len(sentences) / 2}
    sw, ow = _words(subj) - common or _words(subj), _words(obj) - common or _words(obj)
    scored = []
    for i, w in enumerate(words):
        score = 2 * len(ow & w) / max(1, len(ow)) + len(sw & w) / max(1, len(sw))
        scored.append((score, i))
    best = max((s for s, _ in scored), default=0)
    return [i for s, i in sorted(scored, reverse=True) if s == best and s > 0][:top]


def core_drugs(kg: dict) -> list[str]:
    ids = [t["subject_id"] for t in kg["triples"] if "structured" in t["sources"] and t["relation"] == "has availability"]
    if not ids:
        deg = collections.Counter()
        for t in kg["triples"]:
            deg[t["subject_id"]] += 1
        ids = [i for i, _ in deg.most_common(60) if kg["entities"].get(i, {}).get("type") == "Drug"][:50]
    return sorted(set(ids), key=lambda i: kg["entities"][i]["label"].lower())


# ----------------------------------------------------------------------------- explorer (HTML)
def build_explorer(kg: dict, name: str, out: pathlib.Path) -> None:
    ents, triples = kg["entities"], kg["triples"]
    deg = collections.Counter()
    for t in triples:
        deg[t["subject_id"]] += 1
        deg[t["object_id"]] += 1
    nodes = [{"id": i, "l": e["label"], "t": e["type"], "g": group_index(e["type"]), "m": int(e["mentions"] or 0), "d": deg[i]}
             for i, e in ents.items() if deg[i] > 0]
    wanted = {t["provenance"][0]["chunk_id"] for t in triples if t.get("provenance") and t["provenance"][0].get("chunk_id")}
    chunk_text, chunk_sents = load_chunk_texts(find_chunks_dir(pathlib.Path(kg["dir"])), wanted)
    edges = []
    for t in triples:
        p = (t.get("provenance") or [{}])[0]
        e = {"s": t["subject_id"], "r": t["relation"], "o": t["object_id"], "c": int(t["count"]), "dr": t["drugs"],
             "src": t["sources"], "ch": p.get("chunk_id"), "sec": p.get("section"), "raw": p.get("raw_relation"),
             "url": p.get("url")}
        if e["ch"] in chunk_sents:
            e["ev"] = best_sentences(chunk_sents[e["ch"]], t["subject"], t["object"])
        edges.append(e)
    trace, sent2edges = load_trace(pathlib.Path(kg["dir"]).parent / "trace.jsonl"), {}
    if trace:
        # chunk sentence index -> "record_id|output_index", so the trace tab can list the triples of each decomposed sentence
        keys = {}
        chunks_dir = find_chunks_dir(pathlib.Path(kg["dir"]))
        for f in (chunks_dir.glob("*.jsonl") if chunks_dir else []):
            for line in f.read_text(encoding="utf-8").splitlines():
                c = json.loads(line) if line.strip() else {}
                if c.get("chunk_id") in chunk_sents:
                    keys[c["chunk_id"]] = [f"{x.get('record_id')}|{x.get('output_index')}" for x in c["sentences"]]
        for i, e in enumerate(edges):
            for k in e.get("ev", []):
                if e["ch"] in keys:
                    sent2edges.setdefault(keys[e["ch"]][k], []).append(i)
    rel_counts = collections.Counter(t["relation"] for t in triples)
    data = {"name": name, "nodes": nodes, "edges": edges, "chunks": chunk_text, "sents": chunk_sents,
            "trace": trace, "sent2edges": sent2edges,
            "relations": [{"r": r, "n": n, "def": kg["schema"].get(r, {}).get("definition", "")} for r, n in rel_counts.most_common()],
            "core": core_drugs(kg), "groups": [g for g, _ in GROUPS], "light": LIGHT, "dark": DARK, "shapes": SHAPES,
            "stats": {k: kg["stats"].get(k) for k in ("n_entities", "n_triples", "n_relations_used", "n_drugs")}}
    page = HTML_TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")) \
        .replace("__NAME__", html.escape(name)).replace("__VIS_JS__", VIS_JS)
    (out / "kg_explorer.html").write_text(page, encoding="utf-8")


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Drug KG explorer: __NAME__</title>
<script src="__VIS_JS__"></script>
<style>
:root{color-scheme:light;--surface:#fcfcfb;--page:#f9f9f7;--text:#0b0b0b;--text2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;--border:rgba(11,11,11,.10);--accent:#2a78d6}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--surface:#1a1a19;--page:#0d0d0d;--text:#fff;--text2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--accent:#3987e5}}
:root[data-theme=dark]{color-scheme:dark;--surface:#1a1a19;--page:#0d0d0d;--text:#fff;--text2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--accent:#3987e5}
[hidden]{display:none!important}*{box-sizing:border-box}body{margin:0;background:var(--page);color:var(--text);font:14px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
header{padding:12px 16px;border-bottom:1px solid var(--border);display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
header h1{font-size:18px;margin:0}header .stats{color:var(--text2);font-size:13px}
.filters{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;padding:10px 16px;border-bottom:1px solid var(--border);background:var(--surface)}
.filters label{display:flex;flex-direction:column;gap:3px;font-size:12px;color:var(--text2)}
.filters input,.filters select,.filters button{font:inherit;padding:5px 8px;border:1px solid var(--axis);border-radius:6px;background:var(--surface);color:var(--text)}
.filters button{cursor:pointer}.filters button.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
details.dd{position:relative}details.dd summary{list-style:none;cursor:pointer;padding:5px 8px;border:1px solid var(--axis);border-radius:6px;background:var(--surface)}
details.dd .menu{position:absolute;z-index:5;top:100%;left:0;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:8px;max-height:320px;overflow:auto;min-width:300px;box-shadow:0 4px 16px rgba(0,0,0,.12)}
details.dd .menu label{flex-direction:row;align-items:center;gap:6px;color:var(--text);font-size:13px;white-space:nowrap}
.legend{display:flex;gap:12px;flex-wrap:wrap;padding:6px 16px;font-size:12px;color:var(--text2);background:var(--surface);border-bottom:1px solid var(--border)}
.legend label{display:flex;align-items:center;gap:5px;cursor:pointer}.sw{width:12px;height:12px;border-radius:3px;display:inline-block}
main{display:grid;grid-template-columns:minmax(0,1fr) 420px;grid-template-rows:minmax(0,1fr);height:calc(100vh - 150px);min-height:480px}
#graph{min-height:0;height:100%;background:var(--surface);border-right:1px solid var(--border)}
aside{min-height:0;overflow:auto;padding:10px 12px;background:var(--page)}
aside h2{font-size:13px;margin:8px 0 6px;color:var(--text2);text-transform:uppercase;letter-spacing:.04em}
table{border-collapse:collapse;width:100%;font-size:12px}td,th{padding:4px 6px;border-bottom:1px solid var(--grid);text-align:left;vertical-align:top}th{color:var(--text2);font-weight:600}
td.n{text-align:right;font-variant-numeric:tabular-nums}tr:hover{background:var(--surface)}
.evidence{font-size:12px;color:var(--text2);background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:8px;margin-bottom:8px;white-space:pre-wrap}
.hint{color:var(--muted);font-size:12px}
.tabs{display:flex;gap:4px}.tabs button{font:inherit;font-size:13px;padding:5px 10px;border:1px solid var(--axis);border-radius:6px;background:var(--surface);color:var(--text2);cursor:pointer}
.tabs button.on{background:var(--accent);border-color:var(--accent);color:#fff}
#traceview{padding:12px 16px;max-width:1100px}#traceview .bar{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;margin-bottom:10px}
#traceview .bar label{display:flex;flex-direction:column;gap:3px;font-size:12px;color:var(--text2)}#traceview .bar label.ck{flex-direction:row;align-items:center;gap:6px}
#traceview select,#traceview input[type=search]{font:inherit;padding:5px 8px;border:1px solid var(--axis);border-radius:6px;background:var(--surface);color:var(--text)}
.tsec{font-size:13px;margin:18px 0 6px;color:var(--text2);text-transform:uppercase;letter-spacing:.04em}
.tcard{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:8px 10px;margin-bottom:8px;font-size:13px}
.tcard .meta{font-size:11px;color:var(--muted);margin-bottom:4px}.tcard .row{display:grid;grid-template-columns:120px minmax(0,1fr);gap:8px;padding:2px 0}
.tcard .k{color:var(--text2);font-size:12px}.tcard mark{background:rgba(42,120,214,.18);color:inherit;border-radius:3px;padding:0 2px}
.tcard del{color:var(--muted)}.tcard ol{margin:2px 0 0 0;padding-left:20px}.tcard li{margin:2px 0}
.trip{font-size:11px;color:var(--text2);margin:1px 0 0 0}.trip span{display:inline-block;margin:1px 6px 1px 0;padding:0 5px;border:1px solid var(--grid);border-radius:4px;cursor:pointer}
@media (max-width:900px){main{grid-template-columns:1fr;grid-template-rows:60vh auto;height:auto}#graph{height:60vh}aside{max-height:60vh}}
</style></head><body>
<header><h1>Drug KG explorer <span style="color:var(--text2);font-weight:400">__NAME__</span></h1><div class="stats" id="stats"></div>
<nav class="tabs" id="tabs"><button data-tab="graph" class="on">Graph</button><button data-tab="trace">Source trace (original → pronoun resolved → decomposed)</button></nav>
<div style="margin-left:auto"><button id="theme" class="hint" style="background:none;border:1px solid var(--axis);border-radius:6px;color:var(--text2);cursor:pointer">theme</button></div></header>
<div class="filters">
  <label>Entity (search) <input id="q" list="ents" placeholder="e.g. Metformin, nausea" style="min-width:240px"><datalist id="ents"></datalist></label>
  <label>Hops <select id="hops"><option value="1">1</option><option value="2">2</option></select></label>
  <label>Min count <input id="minc" type="number" min="1" value="1" style="width:70px"></label>
  <label>Max nodes <input id="maxn" type="number" min="20" max="600" value="120" style="width:80px"></label>
  <label>Relations <details class="dd"><summary id="relsum">all relations</summary><div class="menu" id="relmenu"></div></details></label>
  <button id="show" class="primary">Show neighbourhood</button>
  <button id="overview">Drug overview (50 drugs, drug–drug edges)</button>
  <label>Shared side effects: min drugs <input id="minshare" type="number" min="2" value="8" style="width:60px"></label><button id="shared">Shared side effects</button>
  <button id="csv">Export CSV</button>
</div>
<div class="legend" id="legend"></div>
<section id="traceview" hidden></section>
<main id="graphview"><div id="graph"></div><aside>
  <div class="hint">Click a node to expand it, double-click to focus on it, hover an edge for the evidence sentence.</div>
  <h2>Selected edge</h2><div class="evidence" id="evidence">—</div>
  <h2>Triples in view (<span id="ntrip">0</span>)</h2><div id="table"></div>
</aside></main>
<script id="kg-data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('kg-data').textContent);
const byId=new Map(D.nodes.map(n=>[n.id,n])); const adj=new Map(); D.edges.forEach((e,i)=>{(adj.get(e.s)||adj.set(e.s,[]).get(e.s)).push(i);(adj.get(e.o)||adj.set(e.o,[]).get(e.o)).push(i);});
const labelToId=new Map(D.nodes.map(n=>[n.l.toLowerCase(),n.id]));
const isDark=()=>document.documentElement.dataset.theme? document.documentElement.dataset.theme==='dark' : matchMedia('(prefers-color-scheme: dark)').matches;
const pal=()=>isDark()?D.dark:D.light; const ink=()=>isDark()?{text:'#fff',text2:'#c3c2b7',edge:'#898781',surface:'#1a1a19'}:{text:'#0b0b0b',text2:'#52514e',edge:'#c3c2b7',surface:'#fcfcfb'};
document.getElementById('stats').textContent=`${D.stats.n_entities} entities · ${D.stats.n_triples} triples · ${D.stats.n_relations_used} relations · ${D.stats.n_drugs||D.core.length} drugs`;
const dl=document.getElementById('ents'); D.nodes.slice().sort((a,b)=>b.d-a.d).slice(0,4000).forEach(n=>{const o=document.createElement('option');o.value=n.l;dl.appendChild(o);});
const groupOn=D.groups.map(()=>true);
function drawLegend(){const L=document.getElementById('legend');L.innerHTML='';D.groups.forEach((g,i)=>{const lab=document.createElement('label');lab.innerHTML=`<input type="checkbox" ${groupOn[i]?'checked':''}> <span class="sw" style="background:${pal()[i]}"></span>${g}`;lab.querySelector('input').onchange=ev=>{groupOn[i]=ev.target.checked;render();};L.appendChild(lab);});}
const relOn=new Map(D.relations.map(r=>[r.r,true]));
(function(){const m=document.getElementById('relmenu');const all=document.createElement('div');all.innerHTML='<button id="relall">all</button> <button id="relnone">none</button>';m.appendChild(all);
D.relations.forEach(r=>{const lab=document.createElement('label');lab.title=r.def;lab.innerHTML=`<input type="checkbox" checked> ${r.r} <span class="hint">(${r.n})</span>`;lab.querySelector('input').onchange=ev=>{relOn.set(r.r,ev.target.checked);relSummary();};m.appendChild(lab);});
m.querySelector('#relall').onclick=()=>{m.querySelectorAll('input').forEach(i=>{i.checked=true});D.relations.forEach(r=>relOn.set(r.r,true));relSummary();};
m.querySelector('#relnone').onclick=()=>{m.querySelectorAll('input').forEach(i=>{i.checked=false});D.relations.forEach(r=>relOn.set(r.r,false));relSummary();};})();
function relSummary(){const n=[...relOn.values()].filter(Boolean).length;document.getElementById('relsum').textContent=n===D.relations.length?'all relations':`${n} of ${D.relations.length} relations`;}
let seeds=[], mode='ego', viewEdges=[], network=null;
function edgeOk(e){const minc=+document.getElementById('minc').value||1;return e.c>=minc&&relOn.get(e.r)&&groupOn[byId.get(e.s).g]&&groupOn[byId.get(e.o).g];}
function subgraph(){const hops=mode==='overview'?0:+document.getElementById('hops').value, maxn=+document.getElementById('maxn').value; const nodes=new Set(seeds), picked=new Set(); let frontier=[...seeds];
 for(let h=0;h<hops&&frontier.length;h++){const next=[]; const cand=[]; frontier.forEach(id=>(adj.get(id)||[]).forEach(i=>{const e=D.edges[i]; if(edgeOk(e)) cand.push(i);}));
  cand.sort((a,b)=>D.edges[b].c-D.edges[a].c||byId.get(D.edges[b].o).d-byId.get(D.edges[a].o).d);
  for(const i of cand){const e=D.edges[i]; const other=nodes.has(e.s)?e.o:e.s; if(!nodes.has(other)){ if(nodes.size>=maxn) continue; nodes.add(other); next.push(other);} picked.add(i);} frontier=next;}
 if(mode==='overview'){D.edges.forEach((e,i)=>{if(nodes.has(e.s)&&nodes.has(e.o)&&edgeOk(e)) picked.add(i);});}
 D.edges.forEach((e,i)=>{if(nodes.has(e.s)&&nodes.has(e.o)&&edgeOk(e)) picked.add(i);});
 return {nodes:[...nodes], edges:[...picked]};}
function sharedSideEffects(){const k=+document.getElementById('minshare').value||5; const core=new Set(D.core); const count=new Map();
 D.edges.forEach((e,i)=>{if((e.r==='has side effect'||e.r==='has serious side effect')&&core.has(e.s)){(count.get(e.o)||count.set(e.o,new Set()).get(e.o)).add(e.s);}});
 const se=[...count.entries()].filter(([o,s])=>s.size>=k).map(([o])=>o); const nodes=new Set(se); const picked=[];
 D.edges.forEach((e,i)=>{if((e.r==='has side effect'||e.r==='has serious side effect')&&core.has(e.s)&&nodes.has(e.o)){picked.push(i);nodes.add(e.s);}});
 return {nodes:[...nodes],edges:picked};}
function render(){const sg=mode==='shared'?sharedSideEffects():subgraph(); viewEdges=sg.edges; const P=pal(), I=ink();
 const vn=sg.nodes.map(id=>{const n=byId.get(id); return {id, label:n.l.length>34?n.l.slice(0,32)+'…':n.l, shape:D.shapes[n.g], color:{background:P[n.g],border:P[n.g],highlight:{background:P[n.g],border:I.text}}, size:Math.min(24,6+2.6*Math.log2(1+n.d)), font:{color:I.text,size:12,face:'system-ui'}, title:`${n.l}\n${n.t} · ${n.d} edges · ${n.m} mentions`};});
 const showLabels=sg.edges.length<=160;
 const ve=sg.edges.map(i=>{const e=D.edges[i]; return {id:i, from:e.s, to:e.o, label:showLabels?e.r:undefined, arrows:'to', width:1+Math.min(3,Math.log2(e.c)), color:{color:I.edge,highlight:I.text}, font:{color:I.text2,size:10,strokeWidth:0,align:'middle'}, smooth:{type:'continuous'}};});
 const container=document.getElementById('graph'); if(network) network.destroy();
 network=new vis.Network(container,{nodes:new vis.DataSet(vn),edges:new vis.DataSet(ve)},{physics:{solver:'forceAtlas2Based',forceAtlas2Based:{gravitationalConstant:-40,springLength:110,avoidOverlap:0.6},stabilization:{iterations:150}},interaction:{hover:true,tooltipDelay:120},nodes:{borderWidth:1}});
 network.on('click',p=>{if(p.edges.length&&!p.nodes.length){showEvidence(D.edges[p.edges[0]]);} if(p.nodes.length){const id=p.nodes[0]; if(!seeds.includes(id)){seeds.push(id); render();}}});
 network.on('doubleClick',p=>{if(p.nodes.length){seeds=[p.nodes[0]]; mode='ego'; document.getElementById('q').value=byId.get(p.nodes[0]).l; render();}});
 network.on('hoverEdge',p=>showEvidence(D.edges[p.edge]));
 drawTable(sg.edges); document.getElementById('ntrip').textContent=sg.edges.length;}
function evidenceSentences(e){const S=D.sents&&e.ch?D.sents[e.ch]:null; if(!S||!e.ev||!e.ev.length) return '';
 const seen=new Set(); return e.ev.map(i=>{const [dec,inp,raw]=S[i]; let t=`▶ Decomposed sentence:\n  ${dec}\n▶ Original sentence (page):\n  ${raw||inp}`;
  if(inp&&raw&&inp!==raw) t+=`\n▶ After pronoun resolution (decomposer input):\n  ${inp}`; if(seen.has(t)) return ''; seen.add(t); return t;}).filter(Boolean).join('\n\n')+'\n\n';}
function showEvidence(e){const s=byId.get(e.s).l,o=byId.get(e.o).l; const ev=e.ch&&D.chunks[e.ch]?D.chunks[e.ch]:'(no evidence text: structured metadata triple)';
 const sent=evidenceSentences(e);
 document.getElementById('evidence').textContent=`${s}  —[${e.r}]→  ${o}\ncount ${e.c} · drugs: ${e.dr.join(', ')} · source: ${e.src.join('/')}${e.raw&&e.raw!==e.r?` · raw relation: "${e.raw}"`:''}\nsection: ${e.sec||'-'}  ${e.url||''}\n\n${sent}${sent?'── Full chunk given to the extractor ──\n':''}${ev}`;}
function drawTable(idx){const rows=idx.map(i=>D.edges[i]).sort((a,b)=>b.c-a.c).slice(0,400);
 document.getElementById('table').innerHTML='<table><tr><th>subject</th><th>relation</th><th>object</th><th>n</th></tr>'+rows.map(e=>`<tr><td>${esc(byId.get(e.s).l)}</td><td>${esc(e.r)}</td><td>${esc(byId.get(e.o).l)}</td><td class="n">${e.c}</td></tr>`).join('')+'</table>'+(idx.length>400?`<div class="hint">showing 400 of ${idx.length}</div>`:'');}
function esc(s){return String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
document.getElementById('show').onclick=()=>{const q=document.getElementById('q').value.trim().toLowerCase(); const id=labelToId.get(q)||[...labelToId.entries()].find(([l])=>l.includes(q))?.[1]; if(!id){alert('entity not found');return;} seeds=[id]; mode='ego'; render();};
document.getElementById('q').addEventListener('keydown',ev=>{if(ev.key==='Enter')document.getElementById('show').click();});
document.getElementById('overview').onclick=()=>{seeds=[...D.core]; mode='overview'; render();};
document.getElementById('shared').onclick=()=>{mode='shared'; render();};
document.getElementById('csv').onclick=()=>{const ev1=(e,k)=>{const S=D.sents&&e.ch?D.sents[e.ch]:null; if(!S||!e.ev||!e.ev.length) return ''; const r=S[e.ev[0]]; return k===2?(r[2]||r[1]):r[k];};
 const lines=['subject,relation,object,count,drugs,decomposed_sentence,original_sentence'].concat(viewEdges.map(i=>{const e=D.edges[i];return [byId.get(e.s).l,e.r,byId.get(e.o).l,e.c,e.dr.join(';'),ev1(e,0),ev1(e,2)].map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(',');})); const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([lines.join('\n')],{type:'text/csv'})); a.download='kg_view.csv'; a.click();};
document.getElementById('theme').onclick=()=>{document.documentElement.dataset.theme=isDark()?'light':'dark'; drawLegend(); render();};
drawLegend(); relSummary(); seeds=[...D.core]; mode='overview'; render();
// ---------------------------------------------------------------- Source trace tab
const TR=D.trace||{}; const traceKeys=Object.keys(TR).sort((a,b)=>TR[a].drug.localeCompare(TR[b].drug));
function showTab(name){document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===name));
 const g=name==='graph'; document.getElementById('graphview').hidden=!g; document.querySelector('.filters').hidden=!g; document.getElementById('legend').hidden=!g;
 document.getElementById('traceview').hidden=g; if(!g&&!document.getElementById('tdrug')) buildTrace(); if(g&&network) network.redraw();}
document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>showTab(b.dataset.tab));
function marked(raw,coref,edits){ // highlight the words pronoun resolution replaced
 let r=esc(raw), c=esc(coref); edits.forEach(([a,b])=>{ if(a) r=r.split(esc(a)).join(`<del>${esc(a)}</del>`); if(b) c=c.split(esc(b)).join(`<mark>${esc(b)}</mark>`);}); return [r,c];}
function buildTrace(){const V=document.getElementById('traceview');
 if(!traceKeys.length){V.innerHTML='<p class="hint">This KG was not built from decomposed sentences, so there is no sentence trace (needs trace.jsonl next to the kg folder).</p>';return;}
 V.innerHTML=`<div class="bar"><label>Drug <select id="tdrug">${traceKeys.map(k=>`<option value="${k}">${esc(TR[k].drug)}</option>`).join('')}</select></label>
  <label>Search <input id="tq" type="search" placeholder="word in any version" style="min-width:220px"></label>
  <label class="ck"><input type="checkbox" id="tchanged"> only sentences changed by pronoun resolution</label>
  <label class="ck"><input type="checkbox" id="tdec"> only decomposed sentences</label><span class="hint" id="tcount"></span></div><div id="tlist"></div>`;
 ['tdrug','tq','tchanged','tdec'].forEach(id=>document.getElementById(id).addEventListener('input',drawTrace)); drawTrace();}
function drawTrace(){const k=document.getElementById('tdrug').value, q=document.getElementById('tq').value.toLowerCase();
 const onlyC=document.getElementById('tchanged').checked, onlyD=document.getElementById('tdec').checked; let sec=null, html='', n=0, nT=0;
 TR[k].rows.forEach(([section,line,raw,coref,edits,label,status,dec,rid])=>{
  if(onlyC&&!edits.length) return; if(onlyD&&status!=='decomposed') return;
  if(q&&!(raw+' '+coref+' '+dec.map(d=>d[1]).join(' ')).toLowerCase().includes(q)) return; n++;
  if(section!==sec){sec=section; html+=`<div class="tsec">${esc(section)}</div>`;}
  const [r,c]=marked(raw,coref,edits);
  const decHtml=dec.map(([oi,sent])=>{const es=(D.sent2edges||{})[rid+'|'+oi]||[]; nT+=es.length;
    const trips=es.map(i=>{const e=D.edges[i]; return `<span data-e="${i}" title="show in graph">${esc(byId.get(e.s).l)} —[${esc(e.r)}]→ ${esc(byId.get(e.o).l)}</span>`;}).join('');
    return `<li>${esc(sent)}${trips?`<div class="trip">${trips}</div>`:''}</li>`;}).join('');
  html+=`<div class="tcard"><div class="meta">line ${line} · ${esc(label)} → ${esc(status)}${edits.length?` · ${edits.length} pronoun edit(s)`:''}</div>
   <div class="row"><span class="k">Original</span><span>${r}</span></div>
   ${edits.length?`<div class="row"><span class="k">Pronoun resolved</span><span>${c}</span></div>`:''}
   <div class="row"><span class="k">${status==='decomposed'?'Decomposed':'Sent to EDC as is'}</span><span>${dec.length?`<ol>${decHtml}</ol>`:'<span class="hint">(no output)</span>'}</span></div></div>`;});
 const L=document.getElementById('tlist'); L.innerHTML=html||'<p class="hint">No sentence matches.</p>';
 document.getElementById('tcount').textContent=`${n} sentences · ${nT} linked triples`;
 L.querySelectorAll('.trip span').forEach(sp=>sp.onclick=()=>{const e=D.edges[+sp.dataset.e]; showTab('graph'); seeds=[e.s]; mode='ego'; document.getElementById('q').value=byId.get(e.s).l; render(); showEvidence(e);});}
</script></body></html>
"""


# ----------------------------------------------------------------------------- static figures
def _style(ax, mode="light"):
    c = INK[mode]
    ax.set_facecolor(c["surface"])
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(c["axis"])
        ax.spines[sp].set_linewidth(0.8)
    ax.tick_params(colors=c["muted"], labelsize=9, length=0)
    ax.grid(axis="x", color=c["grid"], linewidth=0.6)
    ax.set_axisbelow(True)
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_color(c["text2"])


def _barh(labels, values, title, path, color=None, colors=None, xlabel="", label_top=3, note=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    c = INK["light"]
    fig_h = max(2.6, 0.34 * len(labels) + 1.2)
    fig, ax = plt.subplots(figsize=(8, fig_h), dpi=160)
    fig.patch.set_facecolor(c["surface"])
    _style(ax)
    y = list(range(len(labels)))[::-1]
    ax.barh(y, values, height=0.62, color=colors or color or LIGHT[0], edgecolor=c["surface"], linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels([l if len(l) <= 42 else l[:40] + "…" for l in labels])
    ax.set_xlabel(xlabel, color=c["text2"], fontsize=9)
    ax.set_title(title, loc="left", fontsize=12, color=c["text"], pad=10)
    xmax = max(values) if values else 1
    for i, (yy, v) in enumerate(zip(y, values)):
        if i < label_top:
            ax.text(v + xmax * 0.01, yy, f"{v:,}", va="center", ha="left", fontsize=9, color=c["text2"])
    ax.set_xlim(0, xmax * 1.12)
    if note:
        fig.text(0.01, 0.005, note, fontsize=8, color=c["muted"])
    fig.tight_layout()
    fig.savefig(path, facecolor=fig.get_facecolor())
    plt.close(fig)


def fig_relations(kg, out):
    rel = collections.Counter(t["relation"] for t in kg["triples"]).most_common(20)
    _barh([r for r, _ in rel], [n for _, n in rel], "Top 20 relations by number of triples", out / "fig_relations.png", xlabel="triples")


def fig_entity_types(kg, out):
    deg = collections.Counter()
    for t in kg["triples"]:
        deg[t["subject_id"]] += 1
        deg[t["object_id"]] += 1
    cnt = collections.Counter(group_index(e["type"]) for i, e in kg["entities"].items() if deg[i] > 0)
    labels = [GROUPS[g][0] for g in range(len(GROUPS))]
    vals = [cnt[g] for g in range(len(GROUPS))]
    _barh(labels, vals, "Entities by type group", out / "fig_entity_types.png", colors=LIGHT, xlabel="entities", label_top=7,
          note="Colors match the node colors in kg_explorer.html")


def fig_triples_per_drug(kg, out):
    per = collections.Counter()
    for t in kg["triples"]:
        for d in t["drugs"]:
            per[d] += 1
    top = per.most_common(15)
    _barh([d for d, _ in top], [n for _, n in top], "Top 15 drugs by number of triples", out / "fig_triples_per_drug.png", xlabel="triples")


def fig_shared_side_effects(kg, out):
    core = set(core_drugs(kg))
    share = collections.defaultdict(set)
    for t in kg["triples"]:
        if t["relation"] in ("has side effect", "has serious side effect") and t["subject_id"] in core:
            share[t["object"]].add(t["subject_id"])
    top = sorted(share.items(), key=lambda kv: -len(kv[1]))[:15]
    if top:
        _barh([o for o, _ in top], [len(s) for _, s in top], "Side effects shared by the most drugs", out / "fig_shared_side_effects.png",
              xlabel="number of drugs (of the 50)")


def fig_ego(kg, out, drug: str, max_nodes: int = 36):
    """Radial 1-hop neighbourhood: the drug in the centre, neighbours on a ring grouped by relation, labels pointing outward."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    ents = kg["entities"]
    did = next((i for i, e in ents.items() if e["label"].lower() == drug.lower()), None)
    if did is None:
        print(f"  ego: entity '{drug}' not found")
        return
    skip_groups = {GROUPS.index(("Instruction / warning", ["Instruction", "Warning"]))}  # sentence-like nodes clutter the ring
    edges = [t for t in kg["triples"] if did in (t["subject_id"], t["object_id"]) and t["relation"] != "similar to"
             and group_index(ents[t["object_id"] if t["subject_id"] == did else t["subject_id"]]["type"]) not in skip_groups]
    # round-robin over relations (most frequent first, at most `per_rel` neighbours each) so the ring shows the variety
    rel_rank = collections.Counter(t["relation"] for t in edges)
    by_rel: dict[str, list] = collections.defaultdict(list)
    for t in sorted(edges, key=lambda t: (-t["count"], len(t["object"]))):
        by_rel[t["relation"]].append(t)
    per_rel, seen, ring = 5, set(), []
    for rel, _ in rel_rank.most_common():
        for t in by_rel[rel][:per_rel]:
            other = t["object_id"] if t["subject_id"] == did else t["subject_id"]
            if other in seen or other == did:
                continue
            seen.add(other)
            ring.append((other, rel, t["subject_id"] == did))
    ring = ring[:max_nodes]
    ring.sort(key=lambda x: (-rel_rank[x[1]], x[1]))  # group by relation around the ring
    c = INK["light"]
    fig, ax = plt.subplots(figsize=(13, 10.5), dpi=160)
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])
    ax.axis("off")
    ax.set_xlim(-2.9, 2.9)
    ax.set_ylim(-2.25, 2.25)
    ax.set_aspect("equal")
    n = max(1, len(ring))
    R = 1.0
    for k, (nid, rel, outgoing) in enumerate(ring):
        th = 2 * math.pi * k / n + math.pi / 2
        x, y = R * math.cos(th), R * math.sin(th)
        ax.annotate("", xy=(x * 0.93, y * 0.93) if outgoing else (0.09 * math.cos(th), 0.09 * math.sin(th)),
                    xytext=(0.09 * math.cos(th), 0.09 * math.sin(th)) if outgoing else (x * 0.93, y * 0.93),
                    arrowprops=dict(arrowstyle="-|>", color=c["axis"], lw=0.9, shrinkA=0, shrinkB=0))
        g = group_index(ents[nid]["type"])
        ax.scatter([x], [y], s=110, color=LIGHT[g], edgecolors=c["surface"], linewidths=1.2, zorder=3)
        lab = ents[nid]["label"]
        lab = lab if len(lab) <= 30 else lab[:28] + "…"
        deg = math.degrees(th)
        left = 90 < (deg % 360) < 270
        ax.text((R + 0.07) * math.cos(th), (R + 0.07) * math.sin(th), f"{lab}  ·  {rel}", fontsize=7, color=c["text"],
                rotation=deg + 180 if left else deg, rotation_mode="anchor", ha="right" if left else "left", va="center")
    ax.scatter([0], [0], s=700, color=LIGHT[0], edgecolors=c["surface"], linewidths=2, zorder=4, marker="D")
    ax.text(0, -0.13, ents[did]["label"], fontsize=10, color=c["text"], ha="center", va="top", zorder=5, fontweight="bold")
    used = sorted({group_index(ents[nid]["type"]) for nid, _, _ in ring} | {0})
    ax.legend(handles=[Patch(color=LIGHT[g], label=GROUPS[g][0]) for g in used], loc="lower left", fontsize=8, frameon=False)
    total = len({(t["object_id"] if t["subject_id"] == did else t["subject_id"]) for t in edges})
    fig.suptitle(f"{ents[did]['label']}: 1-hop neighbourhood, {len(ring)} of {total} concept neighbours "
                 f"(up to {per_rel} per relation; instructions/warnings and 'similar to' omitted)", x=0.01, y=0.995, ha="left",
                 fontsize=11, color=c["text"])
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(out / f"fig_ego_{re.sub(r'[^a-z0-9]+', '_', drug.lower())}.png", facecolor=fig.get_facecolor())
    plt.close(fig)


def fig_experiments(out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rows = []
    for kg_dir, label in experiment_kgs():
        st = kg_dir / "stats.json"
        if st.exists():
            s = json.loads(st.read_text(encoding="utf-8"))
            rows.append((label, s["n_entities"], s["n_triples"], s["n_relations_used"]))
    if len(rows) < 2:
        return
    c = INK["light"]
    fig, axes = plt.subplots(1, 3, figsize=(12, max(2.8, 0.42 * len(rows) + 1.2)), dpi=160, sharey=True)
    fig.patch.set_facecolor(c["surface"])
    for ax, (title, idx) in zip(axes, (("Entities", 1), ("Triples", 2), ("Relations", 3))):
        _style(ax)
        y = list(range(len(rows)))[::-1]
        vals = [r[idx] for r in rows]
        ax.barh(y, vals, height=0.6, color=LIGHT[0], edgecolor=c["surface"], linewidth=1)
        ax.set_yticks(y)
        ax.set_yticklabels([r[0] for r in rows])
        ax.set_title(title, loc="left", fontsize=11, color=c["text"])
        for yy, v in zip(y, vals):
            ax.text(v + max(vals) * 0.01, yy, f"{v:,}", va="center", fontsize=8, color=c["text2"])
        ax.set_xlim(0, max(vals) * 1.18)
    fig.suptitle("KG size per experiment (same 50 drugs)", x=0.01, ha="left", fontsize=12, color=c["text"])
    fig.tight_layout()
    fig.savefig(out / "fig_experiments.png", facecolor=fig.get_facecolor())
    plt.close(fig)


def experiment_kgs():
    found = []
    if (ROOT / "output" / "kg" / "stats.json").exists():
        found.append((ROOT / "output" / "kg", "main (4B)"))
    for d in sorted((ROOT / "output" / "experiments").glob("*")):
        if d.name == "smoke":
            continue
        stages = json.loads((d / "stages.json").read_text(encoding="utf-8")) if (d / "stages.json").exists() else {}
        copied = "copy_from" in stages  # the pre-canonicalization KG of a copied experiment duplicates its source
        for sub, suffix in (("kg", ""), ("kg_canon", " (canon)")):
            if (d / sub / "stats.json").exists() and not (copied and sub == "kg"):
                found.append((d / sub, d.name + suffix))
    return found


# ----------------------------------------------------------------------------- main
def run_one(kg_dir: pathlib.Path, name: str, drugs: list[str]) -> pathlib.Path:
    out = ROOT / "output" / "viz" / name
    out.mkdir(parents=True, exist_ok=True)
    kg = load_kg(kg_dir)
    kg["dir"] = str(kg_dir)
    build_explorer(kg, name, out)
    fig_relations(kg, out)
    fig_entity_types(kg, out)
    fig_triples_per_drug(kg, out)
    fig_shared_side_effects(kg, out)
    for d in drugs:
        fig_ego(kg, out, d)
    print(f"{name}: {kg['stats'].get('n_entities')} entities, {kg['stats'].get('n_triples')} triples -> {out}")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kg", default=None, help="KG directory with entities.csv / triples.jsonl / schema.csv / stats.json")
    ap.add_argument("--name", default=None, help="output folder name under output/viz/ (default: derived from --kg)")
    ap.add_argument("--drug", action="append", default=None, help="drug(s) for static ego-network figures (repeatable)")
    ap.add_argument("--all", action="store_true", help="visualize every KG under output/ and draw the experiment comparison")
    args = ap.parse_args()
    drugs = args.drug or ["Metformin", "Sertraline"]
    if args.all:
        for kg_dir, label in experiment_kgs():
            run_one(kg_dir, re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_"), drugs)
        viz = ROOT / "output" / "viz"
        fig_experiments(viz)
        print(f"experiment comparison figure -> {viz / 'fig_experiments.png'}")
        return
    kg_dir = pathlib.Path(args.kg or (ROOT / "output" / "kg"))
    if not kg_dir.is_absolute():
        kg_dir = ROOT / kg_dir
    name = args.name or ("main" if kg_dir == ROOT / "output" / "kg" else f"{kg_dir.parent.name}{'_canon' if kg_dir.name == 'kg_canon' else ''}")
    run_one(kg_dir, name, drugs)


if __name__ == "__main__":
    sys.exit(main())
