"""One-off probe: resolve the 50 generic drug names to drugs.com page slugs and cache the HTML."""
import json, random, time, re, sys, pathlib
import requests
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw_html"; RAW.mkdir(parents=True, exist_ok=True)
OUT = ROOT / "data" / "drug_urls.json"

DRUGS = ["Atorvastatin","Levothyroxine","Metformin","Amlodipine","Lisinopril","Albuterol","Losartan","Metoprolol",
 "Rosuvastatin","Omeprazole","Gabapentin","Sertraline","Escitalopram","Semaglutide","Dextroamphetamine + Amphetamine salts",
 "Pantoprazole","Bupropion","Hydrochlorothiazide","Fluoxetine","Trazodone","Montelukast","Amoxicillin","Fluticasone",
 "Tamsulosin","Apixaban","Simvastatin","Insulin Glargine","Empagliflozin","Furosemide","Meloxicam","Acetaminophen + Hydrocodone",
 "Tirzepatide","Methylphenidate","Duloxetine","Prednisone","Carvedilol","Famotidine","Ibuprofen","Buspirone","Venlafaxine",
 "Tramadol","Potassium Chloride","Hydroxyzine","Allopurinol","Clopidogrel","Ergocalciferol","Cetirizine","Ondansetron",
 "Cyclobenzaprine","Spironolactone"]
SPECIAL = {
 "Dextroamphetamine + Amphetamine salts": ["adderall","amphetamine-dextroamphetamine","mtm/amphetamine-and-dextroamphetamine","mtm/dextroamphetamine-and-amphetamine"],
 "Acetaminophen + Hydrocodone": ["hydrocodone-acetaminophen","acetaminophen-hydrocodone","mtm/acetaminophen-and-hydrocodone","mtm/hydrocodone-and-acetaminophen"],
 "Insulin Glargine": ["insulin-glargine","lantus"],
 "Fluticasone": ["fluticasone","fluticasone-nasal","flonase"],
 "Potassium Chloride": ["potassium-chloride"],
}
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
   "Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate, br",
   "Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"none","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1",
   "sec-ch-ua":'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',"sec-ch-ua-mobile":"?0","sec-ch-ua-platform":'"Windows"',"Connection":"keep-alive"}
s=requests.Session(); s.headers.update(H)
s.get("https://www.drugs.com/",timeout=30); time.sleep(4)
result = json.load(open(OUT)) if OUT.exists() else {}
for name in DRUGS:
    if name in result and result[name].get("url"): continue
    cands = SPECIAL.get(name, [name.lower().replace(" ","-")])
    found=None
    for slug in cands:
        url=f"https://www.drugs.com/{slug}.html"
        for attempt in range(2):
            r=s.get(url,timeout=30); title=re.search(r"<title>(.*?)</title>",r.text,re.S)
            title=title.group(1).strip() if title else ""
            if r.status_code==403 or "Access Denied" in title:
                print(f"[403] {url} attempt {attempt}; sleeping 60s", flush=True); time.sleep(60); continue
            break
        ok = r.status_code==200 and "Page Not Found" not in title and "Access Denied" not in title
        print(f"{r.status_code} {url} | {title[:70]}", flush=True)
        if ok:
            fn = RAW / (slug.replace("/","__")+".html"); fn.write_text(r.text)
            found={"url":r.url,"slug":slug,"title":title,"html":str(fn.relative_to(ROOT))}
            break
        time.sleep(random.uniform(4,7))
    result[name]=found or {"url":None,"tried":cands}
    json.dump(result, open(OUT,"w"), indent=2)
    time.sleep(random.uniform(5,8))
missing=[k for k,v in result.items() if not v.get("url")]
print("DONE. missing:", missing)
