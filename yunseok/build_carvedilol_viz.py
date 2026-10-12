#!/usr/bin/env python3
"""Build the 1-drug visualization (HTML) and the canonicalization analysis CSVs for presentation-yunseok.md.

Source KG = EDC-only run `text_edc` (Qwen3-14B-AWQ, raw page text input). Its triples/entities files are no longer on
disk, so the KG is read back from the JSON embedded in drug-kg/output/viz/text_edc/kg_explorer.html (nodes, edges with
raw relation + chunk provenance, chunk texts).

  python yunseok/build_carvedilol_viz.py            # -> yunseok/carvedilol_kg.html + yunseok/*.csv
  python yunseok/build_carvedilol_viz.py --drug escitalopram --out yunseok/escitalopram_kg.html
"""
from __future__ import annotations
import argparse, collections, csv, html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPLORER = ROOT / "drug-kg/output/viz/text_edc/kg_explorer.html"
SEED_CSV = ROOT / "drug-kg/schemas/drug_seed_schema.csv"
VIS_JS = "https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/dist/vis-network.min.js"

# same type groups / validated palette as drug-kg/scripts/visualize_kg.py (fixed slot order, never cycled)
GROUPS = [("Drug", ["Drug"]), ("Condition", ["Condition", "Symptom"]), ("Side effect", ["SideEffect"]),
          ("Substance / class", ["Substance", "Ingredient", "DrugClass"]),
          ("Dosing", ["Dose", "Strength", "DosageForm", "Route", "Schedule"]),
          ("Instruction / warning", ["Instruction", "Warning"]), ("Other", [])]
GROUP_OF = {t: gi for gi, (_, ts) in enumerate(GROUPS) for t in ts}
LIGHT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#898781"]
DARK = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#898781"]
SHAPES = ["diamond", "dot", "dot", "triangle", "hexagon", "square", "dot"]


def load_explorer() -> dict:
    page = EXPLORER.read_text(encoding="utf-8")
    m = re.search(r'<script\b[^>]*\bid=["\']kg-data["\'][^>]*>(.*?)</script>', page, re.S)
    return json.loads(m.group(1))


def seed_relations() -> list[str]:
    return [r["relation"] for r in csv.DictReader(open(SEED_CSV, encoding="utf-8"))]


def edge_status(e: dict, seed: set[str]) -> str:
    if "edc" not in e["src"]:
        return "structured"
    raw, r = e["raw"], e["r"]
    if raw == r:
        return "direct" if r in seed else "enriched"
    if raw == "has instruction":
        return "manual merge"
    return "mapped" if r in seed else "mapped_new"


# ----------------------------------------------------------------------------- canonicalization CSVs
def write_canon_csvs(D: dict, seed: list[str], out_dir: pathlib.Path) -> None:
    S = set(seed)
    E = [e for e in D["edges"] if "edc" in e["src"]]
    pair = collections.Counter((e["raw"], e["r"]) for e in E)
    with open(out_dir / "canonicalization_mapping.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["raw_relation", "canonical_relation", "canonical_origin", "status", "n_edges"])
        for (raw, r), n in sorted(pair.items(), key=lambda kv: (-kv[1], str(kv[0][1]))):
            st = "direct" if raw == r and r in S else "enriched" if raw == r else "manual merge" if raw == "has instruction" else "mapped" if r in S else "mapped_new"
            w.writerow([raw, r, "seed" if r in S else "enriched", st, n])
    rel_edges = collections.Counter(e["r"] for e in E)
    rel_direct = collections.Counter(e["r"] for e in E if e["raw"] == e["r"])
    rel_raws = collections.defaultdict(set)
    for e in E:
        rel_raws[e["r"]].add(e["raw"])
    defs = {r["r"]: r["def"] for r in D["relations"]}
    with open(out_dir / "relations_edc_only.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["relation", "origin", "n_edges_edc", "n_direct", "n_mapped_in", "n_distinct_raw_names", "definition"])
        for r in sorted(defs, key=lambda x: -rel_edges[x]):
            w.writerow([r, "seed" if r in S else "enriched", rel_edges[r], rel_direct[r], rel_edges[r] - rel_direct[r],
                        len(rel_raws[r]), defs[r]])


# ----------------------------------------------------------------------------- 1-drug HTML
def build_html(D: dict, seed: list[str], drug: str, out: pathlib.Path) -> dict:
    S = set(seed)
    by_id = {n["id"]: n for n in D["nodes"]}
    E = [e for e in D["edges"] if drug in e["dr"]]
    node_ids = {e["s"] for e in E} | {e["o"] for e in E}
    deg = collections.Counter()
    for e in E:
        deg[e["s"]] += 1
        deg[e["o"]] += 1
    nodes = [{"id": i, "l": by_id[i]["l"], "t": by_id[i]["t"], "g": GROUP_OF.get(by_id[i]["t"], len(GROUPS) - 1),
              "d": deg[i], "core": i == drug} for i in node_ids]
    edges = []
    for e in E:
        edges.append({"s": e["s"], "r": e["r"], "o": e["o"], "c": e["c"], "src": e["src"], "ch": e["ch"], "sec": e["sec"],
                      "raw": e["raw"], "url": e["url"], "st": edge_status(e, S), "seed": e["r"] in S})
    chunks = {e["ch"]: D["chunks"][e["ch"]] for e in E if e["ch"] and e["ch"] in D["chunks"]}
    defs = {r["r"]: r["def"] for r in D["relations"]}
    rels = collections.Counter(e["r"] for e in edges)
    label = by_id[drug]["l"]
    data = {"drug": drug, "label": label, "nodes": nodes, "edges": edges, "chunks": chunks,
            "relations": [{"r": r, "n": n, "seed": r in S, "def": defs.get(r, "")} for r, n in rels.most_common()],
            "groups": [g for g, _ in GROUPS], "light": LIGHT, "dark": DARK, "shapes": SHAPES,
            "stats": {"nodes": len(nodes), "edges": len(edges), "relations": len(rels),
                      "edc": sum("edc" in e["src"] for e in edges), "structured": sum("structured" in e["src"] for e in edges),
                      "status": dict(collections.Counter(e["st"] for e in edges))}}
    page = HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")) \
        .replace("__LABEL__", html.escape(label)).replace("__VIS_JS__", VIS_JS)
    out.write_text(page, encoding="utf-8")
    return data["stats"]


HTML = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>__LABEL__ KG (EDC-only)</title>
<script src="__VIS_JS__"></script>
<style>
:root{color-scheme:light;--surface:#fcfcfb;--page:#f9f9f7;--text:#0b0b0b;--text2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;--border:rgba(11,11,11,.10);--accent:#2a78d6}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--surface:#1a1a19;--page:#0d0d0d;--text:#fff;--text2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--accent:#3987e5}}
:root[data-theme=dark]{color-scheme:dark;--surface:#1a1a19;--page:#0d0d0d;--text:#fff;--text2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--accent:#3987e5}
*{box-sizing:border-box}body{margin:0;background:var(--page);color:var(--text);font:14px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
header{padding:12px 16px;border-bottom:1px solid var(--border);display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
header h1{font-size:18px;margin:0}header .stats{color:var(--text2);font-size:13px}
.bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;padding:8px 16px;border-bottom:1px solid var(--border);background:var(--surface);font-size:12px;color:var(--text2)}
.bar input,.bar select,.bar button{font:inherit;padding:4px 8px;border:1px solid var(--axis);border-radius:6px;background:var(--surface);color:var(--text)}
.bar button{cursor:pointer}.bar label{display:flex;align-items:center;gap:5px;cursor:pointer}
.sw{width:12px;height:12px;border-radius:3px;display:inline-block}
.chips{display:flex;gap:6px;flex-wrap:wrap}.chip{display:inline-flex;align-items:center;gap:4px;padding:2px 8px;border:1px solid var(--axis);border-radius:999px;cursor:pointer;color:var(--text);background:var(--surface);user-select:none}
.chip.off{opacity:.38}.chip .n{color:var(--muted)}.chip.enr{border-style:dashed}
main{display:grid;grid-template-columns:minmax(0,1fr) 440px;height:calc(100vh - 170px);min-height:480px}
#graph{min-height:0;height:100%;background:var(--surface);border-right:1px solid var(--border)}
aside{min-height:0;overflow:auto;padding:10px 12px;background:var(--page)}
aside h2{font-size:12px;margin:10px 0 6px;color:var(--text2);text-transform:uppercase;letter-spacing:.04em}
.evidence{font-size:12px;color:var(--text2);background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:8px;white-space:pre-wrap}
.evidence b{color:var(--text)}.evidence mark{background:rgba(42,120,214,.20);color:inherit;border-radius:3px;padding:0 2px}
table{border-collapse:collapse;width:100%;font-size:12px}td,th{padding:3px 6px;border-bottom:1px solid var(--grid);text-align:left;vertical-align:top}th{color:var(--text2);font-weight:600}
td.n{text-align:right;font-variant-numeric:tabular-nums}tr.sel{background:rgba(42,120,214,.12)}tr{cursor:pointer}tr:hover{background:var(--surface)}
.hint{color:var(--muted);font-size:12px}
@media (max-width:900px){main{grid-template-columns:1fr;grid-template-rows:60vh auto;height:auto}#graph{height:60vh}aside{max-height:60vh}}
</style></head><body>
<header><h1>__LABEL__ <span style="color:var(--text2);font-weight:400">· EDC-only KG (text_edc, Qwen3-14B-AWQ)</span></h1><div class="stats" id="stats"></div>
<div style="margin-left:auto;display:flex;gap:8px"><button id="fit" class="hint" style="background:none;border:1px solid var(--axis);border-radius:6px;color:var(--text2);cursor:pointer">fit</button><button id="theme" class="hint" style="background:none;border:1px solid var(--axis);border-radius:6px;color:var(--text2);cursor:pointer">theme</button></div></header>
<div class="bar" id="legend"></div>
<div class="bar"><span>관계 필터 (실선 = seed 관계, 점선 = enriched 관계; 클릭으로 켜고 끔)</span><button id="relall">all</button><button id="relnone">none</button><div class="chips" id="rels"></div></div>
<div class="bar"><label><input type="checkbox" id="labels" checked> 엣지에 관계명 표시</label><label><input type="checkbox" id="struct" checked> 구조화 메타데이터 트리플 포함(점선 엣지)</label><label>노드 검색 <input id="q" placeholder="e.g. heart failure" style="min-width:200px"></label><span class="hint" id="nview"></span></div>
<main><div id="graph"></div><aside>
  <div class="hint">엣지를 클릭하면 근거 청크(추출기에 입력된 원문)와 raw relation → canonical relation 매핑이 표시됩니다. 노드를 더블클릭하면 해당 노드로 포커스합니다.</div>
  <h2>선택한 트리플</h2><div class="evidence" id="evidence">—</div>
  <h2>관계별 트리플 (<span id="ntrip">0</span>)</h2><div id="table"></div>
</aside></main>
<script id="kg-data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('kg-data').textContent);
const byId=new Map(D.nodes.map(n=>[n.id,n]));
const isDark=()=>document.documentElement.dataset.theme? document.documentElement.dataset.theme==='dark' : matchMedia('(prefers-color-scheme: dark)').matches;
const pal=()=>isDark()?D.dark:D.light; const ink=()=>isDark()?{text:'#fff',text2:'#c3c2b7',edge:'#898781',surface:'#1a1a19'}:{text:'#0b0b0b',text2:'#52514e',edge:'#c3c2b7',surface:'#fcfcfb'};
const st=D.stats; document.getElementById('stats').textContent=`${st.nodes} nodes · ${st.edges} triples (EDC ${st.edc}, structured ${st.structured}) · ${st.relations} relations · status: direct ${st.status.direct||0}, mapped ${st.status.mapped||0}, enriched ${(st.status.enriched||0)+(st.status.mapped_new||0)}`;
const groupOn=D.groups.map(()=>true), relOn=new Map(D.relations.map(r=>[r.r,true]));
function drawLegend(){const L=document.getElementById('legend');L.innerHTML='<span>노드 타입</span>';D.groups.forEach((g,i)=>{const lab=document.createElement('label');lab.innerHTML=`<input type="checkbox" ${groupOn[i]?'checked':''}> <span class="sw" style="background:${pal()[i]}"></span>${g}`;lab.querySelector('input').onchange=ev=>{groupOn[i]=ev.target.checked;render();};L.appendChild(lab);});}
(function(){const m=document.getElementById('rels');D.relations.forEach(r=>{const c=document.createElement('span');c.className='chip'+(r.seed?'':' enr');c.title=r.def;c.innerHTML=`${r.r} <span class="n">${r.n}</span>`;c.onclick=()=>{relOn.set(r.r,!relOn.get(r.r));c.classList.toggle('off',!relOn.get(r.r));render();};m.appendChild(c);});
document.getElementById('relall').onclick=()=>{D.relations.forEach(r=>relOn.set(r.r,true));m.querySelectorAll('.chip').forEach(c=>c.classList.remove('off'));render();};
document.getElementById('relnone').onclick=()=>{D.relations.forEach(r=>relOn.set(r.r,false));m.querySelectorAll('.chip').forEach(c=>c.classList.add('off'));render();};})();
let network=null, selected=null;
function edgeOk(e){return relOn.get(e.r)&&groupOn[byId.get(e.s).g]&&groupOn[byId.get(e.o).g]&&(document.getElementById('struct').checked||e.src.includes('edc'));}
function render(){const P=pal(), I=ink(); const idx=[]; D.edges.forEach((e,i)=>{if(edgeOk(e)) idx.push(i);}); const ids=new Set([D.drug]); idx.forEach(i=>{ids.add(D.edges[i].s);ids.add(D.edges[i].o);});
 const q=document.getElementById('q').value.trim().toLowerCase();
 const vn=[...ids].map(id=>{const n=byId.get(id); const hit=q&&n.l.toLowerCase().includes(q); return {id, label:n.l.length>36?n.l.slice(0,34)+'…':n.l, shape:D.shapes[n.g], color:{background:P[n.g],border:hit?I.text:P[n.g],highlight:{background:P[n.g],border:I.text}}, borderWidth:hit?3:1, size:n.core?34:Math.min(22,7+2.4*Math.log2(1+n.d)), font:{color:I.text,size:n.core?16:12,face:'system-ui',bold:n.core?{color:I.text}:undefined}, title:`${n.l}\n${n.t} · ${n.d} edges`};});
 const showLabels=document.getElementById('labels').checked;
 const ve=idx.map(i=>{const e=D.edges[i]; const structOnly=!e.src.includes('edc'); return {id:i, from:e.s, to:e.o, label:showLabels?e.r:undefined, arrows:'to', dashes:structOnly?[6,4]:false, width:selected===i?3:1.2, color:{color:selected===i?I.text:I.edge,highlight:I.text,hover:I.text}, font:{color:I.text2,size:10,strokeWidth:0,align:'middle'}, smooth:{type:'continuous'}};});
 const container=document.getElementById('graph'); if(network) network.destroy();
 network=new vis.Network(container,{nodes:new vis.DataSet(vn),edges:new vis.DataSet(ve)},{physics:{solver:'forceAtlas2Based',forceAtlas2Based:{gravitationalConstant:-55,springLength:120,avoidOverlap:0.7},stabilization:{iterations:200}},interaction:{hover:true,tooltipDelay:120},nodes:{borderWidth:1}});
 network.on('click',p=>{if(p.edges.length&&!p.nodes.length){select(p.edges[0]);}});
 network.on('doubleClick',p=>{if(p.nodes.length){network.focus(p.nodes[0],{scale:1.4,animation:true});}});
 drawTable(idx); document.getElementById('ntrip').textContent=idx.length; document.getElementById('nview').textContent=`${ids.size} nodes · ${idx.length} edges in view`;}
function esc(s){return String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function hl(text,obj){const t=esc(text); const o=esc(obj); if(!o) return t; const i=t.toLowerCase().indexOf(o.toLowerCase()); if(i<0) return t; return t.slice(0,i)+'<mark>'+t.slice(i,i+o.length)+'</mark>'+t.slice(i+o.length);}
function select(i){selected=i; const e=D.edges[i]; const s=byId.get(e.s).l,o=byId.get(e.o).l; const chunk=e.ch&&D.chunks[e.ch]?D.chunks[e.ch]:null;
 let head=`<b>${esc(s)}</b>  —[${esc(e.r)}]→  <b>${esc(o)}</b>\nstatus: ${e.st}${e.raw&&e.raw!==e.r?`  (raw relation "${esc(e.raw)}" → canonical "${esc(e.r)}")`:''} · source: ${e.src.join('/')} · count ${e.c}\nsection: ${esc(e.sec||'-')}\n${esc(e.url||'')}\n\n`;
 document.getElementById('evidence').innerHTML=head+(chunk?`── 추출기에 입력된 청크 (${esc(e.ch)}) ──\n`+hl(chunk,o):'(근거 텍스트 없음: 페이지 메타데이터에서 만든 구조화 트리플)');
 document.querySelectorAll('#table tr').forEach(tr=>tr.classList.toggle('sel',tr.dataset.i==i)); if(network){network.selectEdges([i]);}}
function drawTable(idx){const rows=idx.map(i=>[i,D.edges[i]]).sort((a,b)=>a[1].r.localeCompare(b[1].r)||byId.get(a[1].o).l.localeCompare(byId.get(b[1].o).l));
 let h='<table><tr><th>relation</th><th>subject → object</th><th>status</th></tr>', last=null;
 rows.forEach(([i,e])=>{h+=`<tr data-i="${i}"><td>${e.r!==last?esc(e.r):''}</td><td>${esc(byId.get(e.s).l)} → ${esc(byId.get(e.o).l)}</td><td class="hint">${e.st}</td></tr>`; last=e.r;});
 const T=document.getElementById('table'); T.innerHTML=h+'</table>'; T.querySelectorAll('tr[data-i]').forEach(tr=>tr.onclick=()=>select(+tr.dataset.i));}
['labels','struct'].forEach(id=>document.getElementById(id).onchange=render); document.getElementById('q').addEventListener('input',render);
document.getElementById('theme').onclick=()=>{document.documentElement.dataset.theme=isDark()?'light':'dark'; drawLegend(); render();};
document.getElementById('fit').onclick=()=>network&&network.fit({animation:true});
drawLegend(); render();
</script></body></html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--drug", default="carvedilol")
    ap.add_argument("--out", type=pathlib.Path, default=None)
    ap.add_argument("--csv-dir", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent)
    args = ap.parse_args()
    D = load_explorer()
    seed = seed_relations()
    out = args.out or (pathlib.Path(__file__).resolve().parent / f"{args.drug}_kg.html")
    stats = build_html(D, seed, args.drug, out)
    write_canon_csvs(D, seed, args.csv_dir)
    print(f"wrote {out}: {stats}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
