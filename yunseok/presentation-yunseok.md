# Drug-KG 발표 정리 (EDC-only vs EDC + Code-KG)

- 작성일: 2026-10-12
- 대상 저장소: `/home/heesun/graph` (`drug-kg/` 파이프라인, `data/`·`scripts/` 평가 자료)
- 이 문서에서 쓰는 두 KG의 정의
  - **EDC-only** = `drug-kg/output/experiments/text_edc` (Drugs.com 원문 854 청크 → EDC, Qwen3-14B-AWQ). 사람 평가 시트·정확도/재현율 보고서에서 "원문 입력 + EDC" / "Model A"로 불리는 결과입니다.
  - **EDC + Code-KG** = `drug-kg/output/experiments/coref_decomp_edc_r2` (대명사 치환 → 문장 복잡도 분류 → 문장 분해 → EDC). 보고서의 "대명사 치환 + 문장 분해 + EDC (2차 실행)" / "Model B"입니다.
  - 참고로 `drug-kg/output/kg`는 10-06에 4B 모델로 만든 초기 EDC-only KG이며, 본 문서의 EDC-only 수치는 모두 14B `text_edc` 기준입니다.
- 주의: `text_edc`의 `kg/triples.jsonl`, `edc/*.json`, `schema/schema.csv`는 현재 디스크에 없습니다. 이 문서의 EDC-only 트리플/정규화 분석은 `output/viz/text_edc/kg_explorer.html`에 내장된 KG JSON(노드·엣지·raw relation·청크 텍스트)과 `output/report/experiments_comparison.json`, LLM 캐시(`output/cache/llm`)에서 복원한 것입니다.

## 이 폴더의 파일

| 파일 | 내용 |
|---|---|
| `presentation-yunseok.md` | 이 문서 |
| `carvedilol_kg.html` | 4절의 1-drug 시각화 (브라우저에서 열기, vis-network CDN 필요) |
| `build_carvedilol_viz.py` | 위 HTML과 아래 CSV를 다시 만드는 스크립트 (`--drug escitalopram` 등으로 다른 약도 생성 가능) |
| `canonicalization_mapping.csv` | EDC-only KG의 raw relation → canonical relation 매핑 전체 (768개 raw 이름, 엣지 수 포함) |
| `relations_edc_only.csv` | EDC-only KG의 최종 관계 149개: 출처(seed/enriched), 엣지 수, direct/mapped 수, 흡수한 raw 이름 수, 정의 |
| `edc_only_judged_500.csv` | 정확도 판정에 쓰인 EDC-only 트리플 500개와 판정(correct/partial/incorrect, 오류 유형, 사유) |
| `recall_status_changes_edc_vs_codekg.csv` | GT 1,894개 중 두 KG의 재현 판정이 달라진 383개 (EDC 실패 → Code-KG 성공 45건 포함) |

## 0. 한눈에 보기

| 항목 | EDC-only (`text_edc`) | EDC + Code-KG (`coref_decomp_edc_r2`) |
|---|---:|---:|
| 입력 | 원문 50페이지, 854 청크 (≤1,100자) | 분해 문장 12,306개를 같은 약·섹션 안에서 1,100자로 묶은 916 청크 |
| LLM | Qwen3-14B-AWQ (vLLM, thinking off, temp 0) | 동일 (+ 전처리에 같은 모델) |
| 추출 LLM 호출 / 시간 | 4,732회 / 25.1분 | 5,345회 / 29.6분 (+ coref·분류·분해 비용) |
| Open triplets (Extract 단계) | 12,113 | 13,180 (decomp_edc 기준) |
| 최종 트리플 / 엔티티 / 관계 | 12,233 / 7,529 / 149 (seed 40 + enriched 109) | 13,202 / 8,470 / 201 (seed 40 + enriched 161) |
| 정확도 엄격 / 관대 (500개 표본, Qwen3.5-27B 판정) | 48.0 / 88.4 | 44.8 / 87.4 |
| 재현율 엄격 / 관대 (GT 초안 1,894개) | 28.6 / 77.7 | 28.0 / 76.5 |
| 틀린 트리플 중 `wrong_relation` | 43 / 58 | 53 / 63 |

출처: `drug-kg/output/report/precision_recall_comparison.md`, `experiments_comparison.md`, `output/experiments/*/stages.json`.

---

## 1. EDC(-only) 결과: 성공 케이스와 실패 케이스

정확도 판정(`data/kg_eval/precision/judged_triples.csv`, 약별 10개씩 500개 무작위 표본, 출처 섹션 원문과 대조)에서 EDC-only는 **correct 240 / partial 202 / incorrect 58**이었습니다. 아래 예시는 모두 그 표본과 KG에서 가져온 실제 트리플입니다.

### 1.1 성공 케이스

| # | 트리플 (subject, relation, object) | 원문 / 판정 사유 | 왜 성공인가 |
|---|---|---|---|
| S1 | (Allopurinol, **reduces risk of**, gout attacks) | "Allopurinol is used to **prevent** gout attacks." raw relation은 `used to prevent` | 추출 + 정규화 성공. 열린 관계명 `used to prevent`가 정의 임베딩 검색과 LLM 검증을 거쳐 시드 관계 `reduces risk of`로 매핑됨 |
| S2 | (Albuterol Inhalation, has administration instruction, use 2 inhalations 15 to 30 minutes before exercise to prevent exercise-induced bronchospasm) | "To prevent exercise-induced bronchospasm, use 2 inhalations 15 to 30 minutes before you exercise." | 주어가 생략된 명령문을 프롬프트의 약 이름 컨텍스트로 약 주어 트리플로 복원 |
| S3 | (Amlodipine, has serious side effect, swelling of face, lips, tongue, or throat) | 판정 사유: 원문이 얼굴·입술·혀·목의 부기를 "응급 치료가 필요한 알레르기 반응의 징후"로 나열 | 섹션 맥락(응급 상황)을 반영해 일반 부작용이 아닌 `has serious side effect`로 분류 |
| S4 | (Allopurinol, interacts with, Coumadin) | "a blood thinner such as warfarin, Coumadin, Jantoven" | 목록·괄호 안 브랜드명까지 개별 엔티티로 전개 |
| S5 | (amoxicillin, has storage instruction, do not allow liquid medicine to freeze if stored in refrigerator) | "If stored in the refrigerator, do not allow it to freeze." | 'it'을 약으로 해석하고 조건절을 object에 보존 |
| S6 | (Famotidine, **belongs to drug class**, histamine-2 blocker) / (Ondansetron, **reduces risk of**, vomiting caused by radiation treatment) | raw: `has drug class` / `used to prevent` | 정규화 단계의 전형적 성공: 변형 관계명이 시드 관계로 수렴 |
| S7 | Atorvastatin "What is atorvastatin?" 청크 1개 → 11 트리플 | belongs to drug class(HMG-CoA reductase inhibitors), treats(high cholesterol), reduces risk of(stroke/heart attack/angina/need for heart surgery), has mechanism of action, administered via(oral), has administration instruction(once daily with or without food) | 짧은 설명 단락은 거의 완전하게 구조화됨 |

### 1.2 실패 케이스 (오류 유형별)

틀린 58개의 유형: `wrong_relation` 43, `wrong_entity` 6, `wrong_direction` 4, `not_in_text` 4, `uninformative` 1. `wrong_relation` 43개 중 **29개가 `has administration instruction`** 입니다.

**A. 관계 오선택 — `has administration instruction`이 만능 관계가 됨 (가장 큰 실패 유형)**

| 트리플 | 원문이 실제로 말하는 것 |
|---|---|
| (Atorvastatin, has administration instruction, call your doctor at once if you have urinating less) | 부작용 발생 시 행동 지침 (복용법 아님) |
| (Cetirizine, has administration instruction, tell your doctor about all prescription and over-the-counter medications) | 상호작용 관련 고지 지침 |
| (Trazodone, has administration instruction, report mood or behavior changes) | 모니터링/보고 지침 |
| (Methylphenidate, has administration instruction, treatment may also include counseling or other treatments) | 치료 계획 설명 |
| (metformin, has missed dose instruction, tell your doctor if side effects bother you a lot) | 부작용 상담 지침 |

→ 시드 스키마에 "부작용 발생 시 행동", "의사에게 알릴 것"을 받는 관계(`should inform doctor about`는 있으나 LLM이 거의 쓰지 않음, direct 0회)가 부족하고, 프롬프트가 "advice sentences는 *instruction* 관계로"라고 지시한 결과입니다.

**B. 관계 의미 불일치 (정의와 다른 뜻으로 사용)**

| 트리플 | 문제 |
|---|---|
| (Hydrochlorothiazide, has duration of treatment, up to 24 hours) | 약효 지속시간을 치료 기간 관계에 넣음 |
| (Empagliflozin, has overdose symptom, feeling jittery) / (…, has overdose symptom, stomach pain) | 저혈당·케톤산증 증상을 과용량 증상으로 분류 (`not_in_text`) |
| (Furoscix ReadyFlow, has duration of treatment, about 10 seconds) | 투여에 걸리는 시간 |

**C. 방향 오류 (`wrong_direction`)**

- (MAO inhibitors, belongs to drug class, isocarboxazid): "isocarboxazid is an MAO inhibitor"의 역방향. raw relation `includes`가 `belongs to drug class`로 매핑되면서 12개 엣지에서 같은 방향 오류 발생 (3절 참고).
- (hypoglycemia, treats, eat or drink hard candy): 치료 주체와 대상이 뒤바뀜.
- (spironolactone, affects, kidney function): 원문은 "신장 기능이 약물 배출에 영향"을 준다는 뜻.

**D. 주어 오류 / 비약물 주어 (`wrong_entity`)**

- (high uric acid levels, **reduces risk of**, gout attacks): 원문 "high uric acid levels may cause gout attacks". raw `may cause`가 정규화에서 `reduces risk of`로 잘못 매핑되어 **의미가 반전**됨. 같은 청크의 (high uric acid levels, reduces risk of, kidney stones)도 동일.
- (Famotidine, increases risk of, stomach damage): 원문은 알코올이 위 손상 위험을 높인다는 내용.
- (Fluoxetine, interacts with, mental illness): 상호작용 약물 목록의 "medicine to treat mental illness"에서 질환명을 상호작용 대상으로 추출.

**E. 상용구 / 무정보 객체**

- (Amlodipine, has warning, not a complete list of side effects), (Montelukast, has warning, this is not a complete list of side effects, and others may occur): 모든 페이지에 있는 면책 문구가 경고 트리플이 됨 (50개 약 전체에서 반복).
- (Empagliflozin, has serious side effect, not feeling well): 비특정 표현.

**F. 복합문·긴 목록이 한 덩어리 객체로 뭉침 (partial 202개의 주된 원인, 2절의 동기)**

| EDC-only 트리플 | 놓친 것 |
|---|---|
| (amoxicillin, has warning, other drugs may interact with it including prescription and over-the-counter medicines, vitamins, and herbal products) | `interacts with` ×4 (prescription medicines, OTC medicines, vitamins, herbal products) |
| (spironolactone, has administration instruction, regular blood tests to check potassium sodium kidney function uric acid and blood sugar) | `requires monitoring of` ×5 (GT에 있는 uric acid, blood sugar 등이 no_match 처리됨) |
| (Adderall, has boxed warning, abuse) | misuse, addiction까지 포함한 경고 범위 |
| (Adderall, has recommended dose, daily dose may be raised in 2.5 mg increments at weekly intervals …) | "3~5세 ADHD 소아" 한정 조건 누락 |
| (Trazodone, has effect, mood) | "It may help to improve your mood, appetite, and energy level …"에서 '개선'이라는 방향성이 `has effect`로 희석 |

---

## 2. Code-KG(문장 분해) 채택의 motivation이 되는 케이스

**EDC-only에서는 실패했지만 EDC + Code-KG에서 성공한 사례**를 GT 재현율 판정(`data/kg_eval/recall_*/semantic_comparison.csv`)과 문장 추적 파일(`data/text-only/coref_pipeline/4_trace/trace.jsonl`), 두 KG의 청크별 트리플에서 직접 대조했습니다. GT 1,894개 중 EDC-only `no_match` → Code-KG `match`가 **45개**, `no_match` → `partial`이 105개입니다 (전체 목록: `recall_status_changes_edc_vs_codekg.csv`).

### 2.1 관계절로 이어진 인과 연쇄 (Complex Sentence)

원문 (atorvastatin.txt:40, Warnings): *"Atorvastatin calcium can cause the breakdown of muscle tissue, **which** can lead to kidney failure."*

| | 입력 문장 | 결과 트리플 |
|---|---|---|
| EDC-only | 원문 그대로 (청크 안) | (Atorvastatin calcium, has serious side effect, muscle tissue breakdown) **뿐** — "근육 분해 → 신부전" 연쇄는 없음. GT01_0018 (breakdown of muscle tissue, may cause, kidney failure) = `no_match` |
| EDC + Code-KG | S1 "Atorvastatin calcium can cause the breakdown of muscle tissue." / S2 "The breakdown of muscle tissue can lead to kidney failure." | (Atorvastatin calcium, has serious side effect, breakdown of muscle tissue) + **(breakdown of muscle tissue, can cause, kidney failure)** → GT `match` |

같은 패턴: simvastatin.txt:11 (GT26_0010), gabapentin.txt:175 *"Morphine can increase gabapentin levels, which may increase drowsiness…"* → EDC-only는 (Gabapentin, interacts with, morphine)만, Code-KG는 **(morphine, increases level of, Gabapentin)** 추가 (GT11_0033 `match`).

### 2.2 세 개의 술어가 병렬된 문장 (Compound Sentence)

원문 (atorvastatin.txt:6): *"Atorvastatin helps lower LDL cholesterol ('bad cholesterol') and triglyceride levels, and increases HDL cholesterol ('good cholesterol') levels, to improve your overall lipid profile."*

| | 결과 트리플 |
|---|---|
| EDC-only | (Atorvastatin, has mechanism of action, lowering LDL cholesterol and triglyceride levels), (Atorvastatin, has mechanism of action, increasing HDL cholesterol levels) — 수치 변화가 '기전' 관계의 긴 object 안에 묻힘. GT01_0008 (Atorvastatin, raises, HDL cholesterol) = `no_match` |
| EDC + Code-KG | S1/S2/S3로 분해 → **(Atorvastatin, lowers level of, LDL cholesterol)**, **(Atorvastatin, lowers level of, triglyceride levels)**, **(Atorvastatin, increases level of, HDL cholesterol)**, (Atorvastatin, improves, overall lipid profile) → `match` |

같은 패턴: simvastatin.txt:6 (GT26_0003 lowers triglycerides, GT26_0004 raises HDL), rosuvastatin.txt:6 단락 (EDC-only 8 트리플 → Code-KG 18 트리플; "reduces cholesterol synthesis", "increases level of LDL receptors in liver", "reduces LDL and total cholesterol levels" 추가, GT09_0006/0007 `match`).

### 2.3 대명사 주어 (Coreference)

원문 (metoprolol.txt:22): *"**It** is not used to stop an attack that has already begun."*

| | 입력 문장 | 결과 |
|---|---|---|
| EDC-only | 원문 그대로 | 이 문장에서 트리플 없음 (청크 19개 트리플 중 해당 없음). GT08_0018 = `no_match` |
| EDC + Code-KG | coref: "**Metoprolol** is not used to stop an attack that has already begun." | **(Metoprolol, not used for, angina attack that has already begun)** → `match` |

원문 (trazodone.txt:7): *"**It** may help to improve your mood, appetite, and energy level as well as decrease anxiety and insomnia related to depression."* → EDC-only: (Trazodone, has effect, mood / appetite / energy level) (관계가 모호해 GT20_0004/0005 `no_match`); Code-KG: coref + 5문장 분해 → **(Trazodone, improves, mood)**, (improves, appetite), (improves, energy level) `match`.

### 2.4 괄호·열거 목록이 긴 문장

원문 (amoxicillin 부작용 섹션): *"Get emergency medical help if you have signs of an allergic reaction to amoxicillin (hives, difficult breathing, swelling in your face or throat) or a severe skin reaction (fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling)."*

| | 결과 |
|---|---|
| EDC-only (4개) | has serious side effect: allergic reaction, severe skin reaction; has side effect: rash; has administration instruction: call your doctor at once if … |
| EDC + Code-KG (11개) | 분해 결과 "Signs of an allergic reaction to amoxicillin include hives, difficult breathing, and swelling…" / "Signs of a severe skin reaction include fever, sore throat, …" → has serious side effect: **hives, difficulty breathing, swelling in face or throat, fever, sore throat, burning eyes, skin pain, red or purple skin rash with blistering and peeling** + allergic reaction, severe skin reaction |

같은 패턴:
- ibuprofen.txt:77 *"Other drugs may interact with ibuprofen, including prescription and over-the-counter medicines, vitamins, and herbal products."* → EDC-only: (ibuprofen, has warning, other drugs may interact with ibuprofen) 1개; Code-KG: (ibuprofen, interacts with, prescription medicines / over-the-counter medicines / vitamins / herbal products) 4개.
- trazodone.txt:41 *"You should not stop using this medicine suddenly, or you could have unpleasant symptoms (such as dizziness, vomiting, agitation, sweating, confusion, numbness, tingling, or electric shock feelings)."* → EDC-only: (Trazodone, has missed dose instruction, do not stop using this medicine suddenly) 1개(관계도 틀림); Code-KG: (Trazodone, has administration instruction, do not stop suddenly) + has side effect ×8 (dizziness, vomiting, agitation, sweating, confusion, numbness, tingling, electric shock feelings).

### 2.5 정량적 근거

| 지표 | EDC-only | EDC + Code-KG |
|---|---:|---:|
| 최종 트리플 / 엔티티 | 12,233 / 7,529 | 13,202 / 8,470 (+8% / +12%) |
| GT 1,894개 중 EDC-only만 놓친 사실 | — | 45 (no_match→match) + 105 (no_match→partial) |
| 사람 평가 v2 표본 105문장: 문장당 트리플 / 트리플 없는 문장 | 1.43 / 23 | 1.62 / 15 |
| Amoxicillin 한 페이지(82문장): 트리플 수 / 트리플 없는 문장 | 121 / 13 | 147 / 7 |
| 전처리가 실제로 바꾼 문장 비율 (8,028문장) | — | 분해 1,916 (24%), 대명사 치환 923 (11%), 나머지 65%는 그대로 |

### 2.6 발표 시 같이 말해야 할 한계 (반대 방향 사례)

전처리는 재현율을 올리지만 정밀도를 깎습니다 (엄격 정확도 48.0 → 44.8, `wrong_relation` 43 → 53; GT 기준 `match`→`no_match` 49건도 존재). 원인이 되는 실제 사례:

- **맥락 소실**: simvastatin.txt:11 *"In rare cases, simvastatin can cause a condition that results in the breakdown of skeletal muscle tissue, potentially leading to kidney failure."* → 분해 S1 "In rare cases, simvastatin can cause **a condition**." → **(Simvastatin, has side effect, condition)** (무정보). EDC-only는 (Simvastatin, has side effect, skeletal muscle tissue breakdown), (…, has serious side effect, kidney failure)를 바로 뽑았음.
- **열거 분해 후 주어 왜곡**: amoxicillin *"Do not use this medication if you are allergic to … any other penicillin antibiotic, such as ampicillin (Omnipen, Principen), …"* → 분해 "Examples of other penicillin antibiotics include ampicillin, …" / "Other penicillin antibiotics include brands such as Omnipen, …" → (penicillin antibiotic, belongs to drug class, ampicillin) 방향 오류 + (penicillin antibiotic, has brand name, Omnipen) 등 브랜드 트리플 12개가 엉뚱한 주어로 생성. EDC-only는 (amoxicillin, contraindicated in, allergy to ampicillin/dicloxacillin/oxacillin/penicillin) 5개로 깔끔.
- **coref 오류 전파**: *"This may happen while you are taking amoxicillin…"* → "Antibiotic medicines may happen within a few months after you stop taking amoxicillin." → (amoxicillin, has side effect, diarrhea within a few months after stopping) 식의 왜곡.

따라서 motivation 슬라이드는 "복합문·병렬문·대명사 문장(전체의 약 1/3)에서는 분해가 recall을 올린다"로 한정하고, 분해를 **문장 유형에 따라 선택 적용**하거나 분해 후 주어가 약이 아닌 문장을 걸러내는 보완이 필요하다는 식으로 마무리하는 것이 안전합니다 (상세: `drug-kg/output/report/why_preprocessing_did_not_help_en.md`).

---

## 3. EDC-only Canonicalization 분석

### 3.1 파이프라인과 관계 수의 변화

```
Extract (OIE)          Define                 Canonicalize                         Consolidate        Export
12,113 open triplets   관계마다 정의 생성      시드 40개 + 정의 임베딩 top-5 검색     enriched 관계끼리   enriched 관계 중
860개 raw 관계명  ───▶  (chunk 단위)   ───▶   + LLM 다지선다(+None of the above)  ───▶ cos≥0.80 → LLM  ───▶ 2회 미만 사용 제거
                                              스키마 40 → 206 (enriched 166)       yes/no: 0건 병합    149 (seed 40 + enriched 109)
```

| 단계 | 관계 수 | 비고 |
|---|---:|---|
| 추출 직후 raw 관계명 (open triplets 12,113개 기준) | **860** | 4B 모델 때는 1,409개 (README) |
| 시드 스키마 | 40 | `schemas/drug_seed_schema.csv` |
| Canonicalize 종료 후 스키마 | **206** | seed 40 + enriched 166 |
| Consolidate (enriched 간 병합) | 206 | 496회 LLM yes/no 판정, 병합 0건 |
| Export 후 최종 KG | **149** | 사용 1회뿐인 enriched 57개 제거 (`min_enriched_relation_count: 2`) + 수동 병합 1건 (`has instruction` → `has administration instruction`) |
| 최종 KG EDC 엣지의 raw 관계명 | 768 | 중복 제거된 엣지 11,352개 기준 |

### 3.2 트리플이 어떤 경로로 정규화되었나

Open triplet 단위 status (`experiments_comparison.json`):

| status | 의미 | 개수 | 비율 |
|---|---|---:|---:|
| `direct` | 추출된 관계명이 이미 스키마에 있음 (LLM 검증 불필요) | 9,426 | 77.8% |
| `mapped` | 임베딩 top-5 후보 중 LLM이 하나를 선택 | 2,468 | 20.4% |
| `enriched` | LLM이 "None of the above" → 새 관계로 스키마에 추가 | 166 | 1.4% |
| `mapped_new` | 같은 배치에서 새로 추가된 관계와 병합 | 41 | 0.3% |
| `auto` | 정의 유사도 ≥0.97 + 이름 동일로 자동 수락 | 12 | 0.1% |

최종 KG의 EDC 엣지 11,352개 기준 (`canonicalization_mapping.csv`):

| 분류 | 엣지 수 | 비율 |
|---|---:|---:|
| raw = canonical, 시드 관계 (direct) | 8,373 | 73.8% |
| raw ≠ canonical, 시드 관계로 매핑 | 1,682 | 14.8% |
| raw ≠ canonical, enriched 관계로 매핑 | 765 | 6.7% |
| raw = canonical, enriched 관계 (새 관계가 그대로 남음) | 530 | 4.7% |
| 수동 병합 | 2 | — |

즉 **최종 엣지의 88.6%가 시드 40개 관계**에 들어갔고, enriched 109개 관계는 1,296개(11.4%)를 차지합니다. 참고로 4B 모델에서는 direct 비율이 62%였고 14B에서 78%로 올라 LLM 검증 호출이 4,000여 회에서 2,468회로 줄었습니다.

### 3.3 어떤 raw 관계들이 어디로 통합되었나 (상위)

| canonical (출처) | 흡수한 raw 이름 수 | 매핑된 엣지 | 대표 raw 관계 (엣지 수) |
|---|---:|---:|---|
| has side effect (seed) | 35 | 278 | has side effect symptom 67, has symptom of side effect 29, has symptom of low magnesium 18, has symptom of kidney problems 16, has symptom of bleeding 14, has symptom to report 14 |
| has serious side effect (seed) | 14 | 201 | has serious side effect symptom 144, has symptom of allergic reaction 11, has medical emergency symptom 11 |
| treats (seed) | 27 | 106 | used for 40, used in treatment of 14, is approved for 7, approved for 7, used to treat 4, **does not treat 3** |
| should be avoided with (seed) | 6 | 86 | contraindicated with 62, has contraindication 20 |
| interacts with (seed) | 11 | 80 | has drug interaction warning 23, has interaction warning 18, has interaction with 10, may interact with 8 |
| contains ingredient (seed) | 15 | 74 | contains 29, has inactive ingredient 20, has active ingredient 7 |
| include (enriched) | 5 | 64 | includes 48, has example 8, contains 4 |
| has recommended dose (seed) | 25 | 62 | has recommended dose for 8, has starting dose 7, has usual range 6, has maintenance dose 4, has initial dose 4 |
| should inform doctor about (seed) | 12 | 61 | requires patient history of 16, requires disclosure of 15, has symptom to report 13 |
| used in population (seed) | 23 | 60 | approved for 9, fda approved for 7, has approved age range 6, has age restriction 5 |
| has effect (enriched) | 26 | 58 | improves 9, has effect on 9, has weight loss result 8, affects 3 |
| has increased risk in (enriched) | 11 | 56 | has risk factor 19, increased risk in 15, has risk during pregnancy 6 |
| increases risk of (seed) | 16 | 53 | increased risk in 15, increases risk in 8, has risk factor 4 |
| belongs to drug class (seed) | 9 | 49 | has drug class 15, **includes 12**, is a 3 |
| contraindicated in (seed) | 9 | 49 | has contraindication 24, has contraindicated in 10, not recommended in 5 |
| requires adjustment of (enriched) | 12 | 48 | requires dose adjustment with 28 |
| has warning (seed) | 15 | 46 | has note 11, has pregnancy warning 6, has side effect warning 5 |
| may cause (enriched) | 10 | 42 | causes 18, can cause 7, can cause damage to 5 |

### 3.4 시드 관계 40개의 사용 양상

| 시드 관계 | 최종 엣지 | direct | 매핑 유입 | 흡수 raw 이름 수 |
|---|---:|---:|---:|---:|
| has administration instruction | 2,297 | 2,273 | 24 | 16 |
| has side effect | 1,603 | 1,325 | 278 | 36 |
| interacts with | 1,023 | 943 | 80 | 12 |
| has serious side effect | 842 | 641 | 201 | 15 |
| contraindicated in | 397 | 348 | 49 | 10 |
| has warning | 385 | 339 | 46 | 16 |
| treats | 381 | 275 | 106 | 28 |
| use with caution in | 364 | 343 | 21 | 11 |
| has overdose symptom | 291 | 291 | 0 | 1 |
| has recommended dose | 278 | 216 | 62 | 26 |
| should be avoided with | 221 | 135 | 86 | 7 |
| has missed dose instruction | 171 | 170 | 1 | 2 |
| has dosage form | 168 | 122 | 46 | 18 |
| has strength | 167 | 117 | 50 | 11 |
| has storage instruction | 141 | 137 | 4 | 4 |
| has mechanism of action | 113 | 108 | 5 | 5 |
| has overdose instruction | 112 | 112 | 0 | 1 |
| has brand name | 102 | 41 | 61 | 10 |
| reduces risk of | 97 | 65 | 32 | 9 |
| has pregnancy or breastfeeding warning | 93 | 76 | 17 | 7 |
| increases risk of | 88 | 35 | 53 | 17 |
| requires monitoring of | 87 | 61 | 26 | 18 |
| belongs to drug class | 76 | 27 | 49 | 10 |
| contains ingredient | 74 | **0** | 74 | 15 |
| not approved for | 72 | 44 | 28 | 15 |
| used in population | 65 | 5 | 60 | 24 |
| used in combination with | 63 | 43 | 20 | 11 |
| should inform doctor about | 61 | **0** | 61 | 12 |
| administered via | 46 | 32 | 14 | 9 |
| manufactured by | 26 | 13 | 13 | 10 |
| has generic name | 24 | 23 | 1 | 2 |
| has duration of treatment | 24 | 1 | 23 | 10 |
| increases level of | 22 | **0** | 22 | 7 |
| has onset of effect | 20 | **0** | 20 | 11 |
| lowers level of | 19 | **0** | 19 | 8 |
| similar to | 15 | **0** | 15 | 13 |
| fda approval year | 10 | 2 | 8 | 4 |
| has boxed warning | 7 | 7 | 0 | 1 |
| has availability | 6 | 1 | 5 | 5 |
| has controlled substance schedule | 5 | 2 | 3 | 3 |

(여기서 엣지 수는 EDC 엣지만. `similar to` 500개, `has brand name`·`has strength`·`has dosage form` 등의 나머지는 구조화 메타데이터 트리플 969개에서 옵니다.)

해석 포인트:
- 상위 5개 시드 관계(has administration instruction, has side effect, interacts with, has serious side effect, contraindicated in)가 EDC 엣지의 **54%**를 차지. 특히 `has administration instruction`(2,297)은 프롬프트에서 예시로 명시한 관계라 LLM이 그대로 쓰지만, 1절 A처럼 과잉 사용됨.
- `contains ingredient`, `should inform doctor about`, `increases level of`, `lowers level of`, `has onset of effect`, `similar to`는 **LLM이 그 이름을 한 번도 직접 쓰지 않았고** 전부 정규화(매핑)로만 채워짐 → 시드 관계명이 LLM의 자연스러운 표현과 다를 때는 정규화가 실제로 일을 합니다. 반대로 `has overdose symptom`, `has overdose instruction`, `has missed dose instruction`, `has storage instruction`은 거의 100% direct (섹션 제목과 프롬프트 지시가 그대로 반영).

### 3.5 LLM 검증(다지선다) 결정의 복원 (캐시 표본)

`output/cache/llm`에 남아 있는 14B 캐시 중 text_edc 청크 텍스트와 일치하는 검증 프롬프트 **677건**을 복원했습니다 (전체 2,468+166건 중 일부만 캐시에 남아 있음).

| 결과 | 건수 | 비율 |
|---|---:|---:|
| 후보 중 하나 선택 | 594 | 87.7% |
| None of the above (→ enriched) | 83 | 12.3% |
| 선택 위치: 임베딩 1위 / 2위 / 3위 / 4위 / 5위 | 357 / 115 / 58 / 39 / 25 | 1위가 60% |

- 검증된 raw 관계명 331개 중 262개는 항상 매핑, 55개는 항상 None, 14개만 혼합 → 결정은 대체로 일관적.
- 임베딩 top-1이 60%만 선택됨 → 임베딩 검색만으로 자동 매핑하면 40%는 다른 후보로 갔을 것. LLM 검증 단계가 필요함을 보여주는 수치.

### 3.6 Enriched(새로 생긴) 관계의 성격

최종 KG에 남은 enriched 109개(1,296 엣지) 중 상위:

| enriched 관계 | 엣지 | 정의 (요약) | 평가 |
|---|---:|---|---|
| used in | 98 | 약이 쓰이는 임상 맥락/절차 | `treats`·`used in population`과 중복 (정의 cos 0.93) |
| has effect | 92 | 약이 내는 치료/생리 효과 | 방향성(improves/reduces)을 잃는 모호 관계 |
| include | 82 | 주어가 포함하는 구성요소 | 범용 관계, 약물 지식이 아님 |
| has symptom | 65 | 질환의 증상 | 주어가 약이 아님 (Condition → Symptom); 시드에 없는 유형이라 필요했던 관계 |
| has increased risk in | 58 | 특정 집단에서 위험 증가 | `increases risk of`(Drug→Condition)와 방향이 다른 Drug→Population 관계; 실질적으로 유용 |
| has side effect frequency | 55 | 부작용 + 빈도 | 시드에 빈도 수식어 자리가 없어서 생김 |
| may cause | 50 | 비약물 주어의 인과 | 2절의 "breakdown → kidney failure" 같은 2차 인과 표현 |
| requires adjustment of | 50 | 용량 조절 필요 | 유용 (시드 보강 후보) |
| has maximum dose | 49 | 최대 용량 | 유용 (시드 보강 후보) |
| helps reduce / has study result / has approved use / has off label use | 34 / 27 / 25 / 21 | | 일부 유용, 일부 `treats`와 중복 |

→ enriched 관계는 (a) 시드에 빠진 유형(`has maximum dose`, `has increased risk in`, `has withdrawal symptom`, `has symptom`)을 메우는 **스키마 보강**과 (b) 시드와 뜻이 겹치는 **중복/모호 관계**(`used in`, `has effect`, `include`)가 섞여 있습니다. 관계 정의 임베딩 기준으로 text_edc 149개 관계 중 115개가 cos ≥0.85인 이웃을 가지고 있고(쌍 562개), 그런 관계들이 트리플의 97%를 차지합니다 (`output/report/relation_redundancy.md`).

### 3.7 정규화 실패 유형 (발표용)

| 유형 | 사례 (raw → canonical) | 결과 |
|---|---|---|
| 부정 소실 | `does not treat` → `treats` (3), `not compared to` → `compared with` | (amoxicillin, treats, common cold / flu / viral infection) 처럼 **사실 반전** (원문: "Amoxicillin will not treat a viral infection such as the common cold or flu") |
| 인과 방향 반전 | `may cause` → `reduces risk of` (2) | (high uric acid levels, reduces risk of, kidney stones) |
| 역방향 관계 흡수 | `includes` → `belongs to drug class` (12), `is ingredient in` → `contains ingredient` | (MAO inhibitors, belongs to drug class, isocarboxazid) |
| 한정어 소실 | `has symptom of low magnesium` → `has side effect` (18), `has symptom of kidney problems` → `has side effect` (16) | 저마그네슘혈증의 *증상*이 약의 직접 부작용으로 승격 |
| 같은 raw가 다른 곳으로 | `has serious side effect symptom` → has serious side effect 144 / has side effect 4, `has risk factor` → has increased risk in 6 / increases risk of 2 | 일관성 저하 |
| 병합 누락 | consolidate 0건: `no dose change needed in` vs `no dose adjustment needed with` (cos 0.96) 등도 미병합 | 14B가 merge 프롬프트에 매우 보수적 (yes 0/496) |

---

## 4. 잘 만들어진 1-drug KG: Carvedilol (시각화 `carvedilol_kg.html`)

### 4.1 선정 기준과 후보

EDC-only KG의 약별 품질 지표(`output/report/coref_decomp_edc_per_drug_quality.md`의 text_edc 열, 재현율 보고서, 그리고 kg_explorer 데이터에서 다시 계산한 값):

| 약 | EDC 트리플 | 시드 관계 비율 | 주어=약 비율 | 짧은 object(≤6단어) | 자동 품질 점수 | GT 재현 (match+partial) |
|---|---:|---:|---:|---:|---:|---:|
| **Carvedilol** | 139 | 97.1% | 100% | 70.5% | 89.2 | **93.1%** (50개 중 1위) |
| Escitalopram | 216 | 97.7% | 100% | 80.1% | 91.0 | 88.6% |
| Simvastatin | 149 | 98.0% | 100% | 76.5% | 92.1 | 70.0% |
| Montelukast | 124 | 99.2% | 100% | 74.2% | 89.7 | 83.8% |
| Tamsulosin | 148 | 91.9% | 100% | 70.3% | 86.0 | 92.5% |
| Atorvastatin | 247 | 96.0% | 98.4% | 69.6% | 86.7 | 91.7% |

Carvedilol을 고른 이유: 재현율 1위이면서 자동 품질 점수도 상위권이고, 트리플 150개·노드 147개로 한 화면에 들어가는 크기입니다. (Escitalopram은 품질 점수가 더 높지만 부작용 64개 등 노드가 많아 발표 그림으로는 덜 읽힙니다. `python yunseok/build_carvedilol_viz.py --drug escitalopram`으로 같은 HTML을 만들 수 있습니다.)

### 4.2 Carvedilol KG 구성

- 150 트리플 = EDC 139 + 구조화 메타데이터 14 (3개 겹침), 노드 147, 관계 24개 (시드 관계가 97%)
- 정규화 상태: direct 111, mapped 24 (예: `has serious side effect symptom` → has serious side effect, `has drug class` → belongs to drug class, `treatment program includes` → used in combination with, `has pregnancy category` → has pregnancy or breastfeeding warning), enriched 4, structured 11
- EDC 트리플의 주어는 2개(`beta blocker → has effect → heart / circulation`)를 빼고 전부 Carvedilol

| 관계 | 수 | 내용 |
|---|---:|---|
| has administration instruction | 37 | 복용법·주의 행동 (Coreg CR 알코올 2시간 간격, 서서히 일어나기, 음식과 함께 등) |
| has serious side effect | 27 | 알레르기 반응, 느리거나 불규칙한 심박, 호흡곤란, 고혈당 징후 등 |
| has side effect | 12 | dizziness, tired feeling, weight gain, dry eyes … |
| similar to (structured) | 10 | Metoprolol, Lisinopril, Losartan, Amlodipine … |
| contraindicated in | 9 | asthma, bronchitis, emphysema, heart block, sick sinus syndrome, slow heart rate, severe liver disease … |
| use with caution in | 9 | diabetes, kidney/liver disease, thyroid disorder, pheochromocytoma, Raynaud's … |
| has overdose symptom | 7 | fainting, seizure, shortness of breath, uneven heartbeats … |
| treats | 6 | heart failure, hypertension, high blood pressure, angina, left ventricular dysfunction, atrial fibrillation |
| interacts with / should be avoided with | 5 / 2 | alcohol, OTC/prescription medicines, vitamins, herbal products |
| has pregnancy or breastfeeding warning | 4 | may harm an unborn baby, unknown if passes into breast milk … |
| has missed dose / overdose / storage instruction | 3 / 2 / 1 | |
| used in combination with | 3 | diet, exercise, weight control |
| belongs to drug class, has brand name, has availability 등 | 2 / 2 / 1 | beta blocker, Non-cardioselective beta blockers; Coreg, Coreg CR; Prescription only |

### 4.3 남아 있는 약점 (그림에서 짚을 것)

- `has administration instruction` 37개 중 일부는 경고에 가깝습니다: "alcohol may cause the carvedilol in Coreg CR to be released too quickly into the body", "can affect your pupils during cataract surgery".
- `has serious side effect`에 고혈당의 *징후*(dry mouth, fruity breath odor, increased thirst, increased urination)가 개별 부작용으로 들어갔습니다 (3.7의 한정어 소실 유형).
- (Carvedilol, has pregnancy or breastfeeding warning, C)는 임신 카테고리 문자만 남아 무정보. (Carvedilol, has side effect, stopping suddenly may cause chest pain or a heart attack)는 경고 문장.
- `treats`에 "high blood pressure"와 "hypertension"이 별도 노드 → 엔티티 정규화가 없다는 EDC의 한계.

### 4.4 HTML 사용법

`carvedilol_kg.html`을 브라우저로 열면 (vis-network를 CDN에서 받으므로 인터넷 필요):
- 가운데 큰 마름모가 Carvedilol, 이웃 노드 색은 타입 그룹(Drug / Condition / Side effect / Substance·class / Dosing / Instruction·warning / Other), 범례의 체크박스로 켜고 끔
- 관계 칩을 클릭해 관계별로 필터 (실선 테두리 = 시드 관계, 점선 = enriched 관계), 점선 엣지 = 구조화 메타데이터 트리플
- 엣지를 클릭하면 오른쪽에 **추출기에 입력된 청크 원문**(object 하이라이트)과 raw relation → canonical relation, 정규화 status, 섹션, URL이 표시됨
- 오른쪽 표는 관계별 트리플 목록, 행 클릭으로 같은 근거 확인. `theme` 버튼으로 다크 모드.

---

## 5. Drug 도메인을 위한 EDC 적응 (원 EDC와의 차이)

원 EDC(Zhang & Soh, EMNLP 2024)는 일반 도메인 문장(WebNLG·REBEL·Wiki-NRE)에 대해 Extract(OIE) → Define → Canonicalize(정의 임베딩 검색 + LLM 검증, 선택적 target schema, self-canonicalization) + EDC+R(schema retriever)로 구성됩니다. 본 구현(`drug-kg/drugkg/edc/`)이 바꾼 지점은 아래와 같습니다.

### 5.1 입력 단위: 문장 → 섹션 기반 청크

- Drugs.com HTML을 섹션(h2) 단위로 파싱해 **약 이름·섹션 제목·URL을 보존한 ≤1,100자 청크**로 만듭니다 (`drugkg/chunk.py`). 관련 약·FAQ·참고문헌 섹션은 제외.
- 청크 단위 추출이라 한 번의 호출로 10~20개 트리플을 얻고, 섹션 제목(예: "What happens if I overdose?")이 관계 선택의 힌트가 됩니다 → `has overdose symptom` 291개 100% direct.

### 5.2 Extract(OIE) 프롬프트 (`prompts/oie_template.txt`, `oie_few_shot.txt`)

원 EDC의 일반 few-shot 대신 다음을 넣었습니다.

| 항목 | 내용 |
|---|---|
| 약 이름 + 섹션 컨텍스트 | `The text comes from the Drugs.com page about the drug "{drug}" (section: {section}).` |
| 대명사 처리 지시 | `Expressions such as "this medicine", "this medication", "this drug" or "it" refer to {drug}; always use "{drug}" as the entity name for the drug itself.` (coref 전처리를 프롬프트로 대체) |
| 관계명 규칙 | 2~4단어의 일반적 소문자 구문만 허용, "put all specifics (doses, populations, conditions, instructions) into the object entity, never into the relationship name" → 스키마 폭발 억제 (raw 관계명: 4B 모델 1,409개, 14B 모델 860개; 규칙은 4B 실험에서 폭발을 줄이려고 도입) |
| 추천 관계명 예시 | treats, has side effect, interacts with, contraindicated in, has recommended dose, has administration instruction, has missed dose / overdose / storage instruction |
| 완전성 지시 | `Extract every fact stated in the text, including side effects, conditions, interactions, dosing, warnings and patient instructions` |
| 도메인 few-shot 5개 | Lipitor(statin·기전·위험 감소), metformin(금기·주의·중증 부작용·비승인 연령), sertraline(부작용·투여경로·용량·모니터링), tramadol(상호작용·회피·규제 등급·브랜드·제조사·승인연도), amlodipine(제형·함량·과용량·임신·보관) — 시드 관계 40개 중 30개 이상을 예시로 노출 |

### 5.3 Define 프롬프트 (`sd_template.txt`, `sd_few_shot.txt`)

- 정의를 항상 "The subject drug … specified by the object entity." 꼴로 쓰게 하는 도메인 few-shot을 제공해, 시드 관계 정의와 **같은 문체**로 임베딩되도록 맞췄습니다 (검색 품질에 직접 영향).
- 청크마다 등장한 관계 전체를 한 번에 정의 (호출 수 절감).

### 5.4 사전 정의 관계 40개 + 타입 (`schemas/drug_seed_schema.csv`)

| 범주 | 관계 (subject → object 타입) |
|---|---|
| 식별/분류 | has generic name, has brand name (Drug→Drug), belongs to drug class (→DrugClass), contains ingredient (→Ingredient), similar to (→Drug), manufactured by (→Organization), fda approval year (→Year), has availability (→Availability), has controlled substance schedule (→Schedule) |
| 적응증/효과 | treats, reduces risk of (→Condition), used in combination with (→Therapy), has mechanism of action (→Mechanism), lowers level of, increases level of (→Substance), has onset of effect, has duration of treatment (→Instruction), used in population (→Population) |
| 안전성 | has side effect, has serious side effect (→SideEffect), increases risk of, contraindicated in, use with caution in, should inform doctor about (→Condition), has boxed warning, has warning, has pregnancy or breastfeeding warning (→Warning), not approved for (→Population), has overdose symptom (→Symptom), requires monitoring of (→LabTest) |
| 상호작용 | interacts with, should be avoided with (→Substance) |
| 용법/제형 | has dosage form (→DosageForm), has strength (→Strength), administered via (→Route), has recommended dose (→Dose), has administration instruction, has missed dose instruction, has overdose instruction, has storage instruction (→Instruction) |

- 엔티티 타입 22종(`ENTITY_TYPES`)을 관계의 domain/range로 두고, 최종 엔티티 타입은 그 엔티티가 참여한 관계들의 타입 투표로 결정합니다 (`postprocess.py`).
- 원 EDC의 target schema는 "있으면 쓰는" 선택 사항이지만, 여기서는 **시드 40개를 항상 후보 풀의 기반**으로 두고(hybrid: `enrich_schema: true`) 못 맞는 관계만 추가합니다.

### 5.5 Canonicalize 단계의 변경 (`drugkg/edc/canonicalize.py`, `sc_template.txt`)

| 항목 | 구현 |
|---|---|
| 후보 검색 | 관계 **정의**를 `BAAI/bge-base-en-v1.5`로 임베딩, 코사인 top-5 |
| 자동 수락 | 유사도 ≥0.97이고 이름이 느슨하게 같으면(has/is 접두사·공백 무시) LLM 생략 (`auto`) |
| LLM 검증 프롬프트 | 청크 원문 + 트리플 + 관계 정의 + 후보 A~E + "None of the above". 도메인 적응: `Choose a relation whose meaning and subject/object direction match the triplet even if the wording differs; choose 'None of the above' only if no candidate fits.` (4B 모델이 None을 남발하던 문제 대응) |
| Enrichment | None 선택 시 새 관계를 스키마에 추가하되, (1) 같은 배치에서 방금 추가된 관계와 정의 유사도 ≥0.80이면 다시 LLM 검증(`mapped_new`), (2) `type_template.txt`로 subject/object 타입을 LLM이 부여 |
| 배치/병렬 | 약 단위로 모든 청크의 검증 프롬프트를 모아 vLLM에 16 동시 요청 |

### 5.6 추가한 후처리 단계 (원 EDC에 없음)

| 단계 | 내용 | 효과 |
|---|---|---|
| Schema consolidation (`consolidate.py`) | 추출 종료 후 enriched 관계끼리 정의 cos ≥0.80이면 `merge_template.txt`로 yes/no | 4B·14B 모두 0건 (프롬프트가 "모든 트리플에서 교체 가능한가"를 묻기 때문에 보수적) |
| Export 필터 | 2회 미만 사용된 enriched 관계 제거, 수동 merge map (`has instruction` → `has administration instruction`) | 206 → 149 관계 |
| 약 별칭 정규화 (`postprocess.py`) | 페이지 제목·generic/brand·slug·괄호 약어(HCTZ)·"this medicine" 류 대명사를 모두 페이지 약 노드로 통합, 관사·따옴표 제거, 120자 초과 엔티티 제거 | 50개 약 노드가 허브로 유지 |
| 구조화 메타데이터 트리플 | 페이지 info box에서 generic/brand name, drug class, dosage form·strength, related drugs(`similar to`), FDA 승인연도, CSA schedule, availability를 고정밀 트리플로 추가 | 969개 (전체의 8%) |
| Provenance | 모든 트리플에 약·섹션·청크 id·raw relation·status·URL 저장 | 근거 추적·시각화·사람 평가 시트 생성에 사용 |

### 5.7 EDC+R(refinement)

- 엔티티 추출(`ee_template.txt`) → 이전 라운드 엔티티와 병합(`em_template.txt`) → 스키마 리트리버 힌트와 함께 재추출(`oie_r_template.txt`)까지 구현되어 있으나, 호출 수가 2배라 모든 실험에서 `refinement_iterations: 0`으로 꺼 두었습니다.

### 5.8 요약 슬라이드용 한 줄

> "EDC의 세 단계는 유지하되, (1) 입력을 약·섹션 컨텍스트가 붙은 청크로 바꾸고, (2) 추출·정의 프롬프트를 약물 도메인 few-shot과 관계명 규칙으로 바꾸고, (3) 40개 시드 관계 + 22개 타입을 정규화의 기준 스키마로 고정한 뒤 못 맞는 관계만 LLM이 타입을 붙여 추가하며, (4) 약 별칭 통합·구조화 메타데이터·희귀 관계 제거를 후처리로 더했다."

---

## 부록: 재현 커맨드

```bash
# 1-drug 시각화와 정규화 CSV 재생성
python yunseok/build_carvedilol_viz.py                          # carvedilol_kg.html + *.csv
python yunseok/build_carvedilol_viz.py --drug escitalopram --out yunseok/escitalopram_kg.html

# 원본 분석 자료
drug-kg/output/report/precision_recall_comparison.md            # 정확도·재현율
drug-kg/output/report/experiments_comparison.md                 # 실험별 추출 통계 (direct/mapped/enriched)
drug-kg/output/report/relation_redundancy.md                    # 관계 정의 유사도
drug-kg/output/report/why_preprocessing_did_not_help_en.md      # 전처리 한계 분석
data/kg_eval/precision/judged_triples.csv                       # 트리플 정확도 판정 원자료
data/kg_eval/recall_text_edc/, recall_coref_decomp_edc_r2/      # GT 재현 판정 원자료
data/text-only/coref_pipeline/4_trace/trace.jsonl               # 원문 → coref → 분해 추적
```
