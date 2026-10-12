# 실험 보고서: 입력 전처리와 엔티티 정규화가 EDC 기반 KG에 미치는 영향 (2026-10-07)

- 모델: Qwen3-14B-AWQ (4-bit AWQ, vLLM, thinking 비활성화), 임베딩 BAAI/bge-base-en-v1.5
- 코드: `run_experiment.py`, `drugkg/inputs.py`, `drugkg/entity_canon.py`, `scripts/run_experiments.sh`, `scripts/compare_experiments.py`
- 산출물: `output/experiments/<실험명>/{kg, kg_canon, audit, audit_canon, entity_canon, stages.json}`, 비교표 `output/report/experiments_comparison.md`

## 1. 실험 구성

| 실험 | 입력 | 처리 | 청크 |
|---|---|---|---|
| `text_edc` | `data/text/*.txt` (섹션 구조 원문) | EDC | 854 |
| `decomp_edc` | `data/final_sentences_keep_incomplete.jsonl` (Code-KG 방식 문장 분해, 12,298문장) | EDC | 911 |
| `decomp_edc_ec` | `decomp_edc` 추출 결과 재사용 | + KGGen 엔티티·관계 정규화(논문 그대로) | 911 |
| `decomp_edc_ec_g` | 위와 동일 | + KGGen에 같은 타입 제약 + 엄격한 중복 정의 추가(변형) | 911 |

- 분해 문장은 같은 약·섹션 안에서 순서대로 1,100자까지 묶어 청크로 만들었습니다(원문 실험과 호출 수를 맞추기 위함). 문장 1개 = 청크 1개 설정은 `--sentence-level`로 가능합니다.
- 두 입력 모두 구조화 메타데이터 트리플(generic/brand/class/제형/관련 약 등 약 970개)을 동일하게 추가했습니다.
- 엔티티 정규화는 KGGen(Mo et al., 2025, arXiv:2502.09956)의 Resolution 단계를 공개 코드 기준으로 옮긴 것입니다: semhash(NFKC 정규화·단수화·유사도 0.95 병합) → k-means 128개 클러스터 → 클러스터마다 항목을 하나씩 꺼내 BM25+임베딩 융합 검색 상위 16개를 LLM에 보여 주고 "중복과 대표 이름"을 받아 병합 → 트리플 재작성. 원본과 다른 점은 (1) 숫자가 다른 문자열은 합치지 않는 안전장치(두 실험 공통), (2) 변형 실험에만 적용한 타입 제약과 지시문 강화입니다.

## 2. 소요 시간과 비용

| 단계 | text_edc | decomp_edc | decomp_edc_ec | decomp_edc_ec_g |
|---|---|---|---|---|
| 추출(Extract+Define+Canonicalize) | 25.1분 | 26.4분 | (재사용) | (재사용) |
| 관계 병합(consolidate) | 50초 | 70초 | – | – |
| 내보내기 | 12초 | 13초 | 22초 | 23초 |
| KGGen 정규화 | – | – | 8.8분 (LLM 5,471회) | 14.2분 (LLM 6,019회) |

14B-AWQ 모델은 4B 모델과 비슷한 속도(약 1개당 30초)로 동작했습니다. GPU를 전부 쓸 수 있어 동시 요청이 늘어난 덕입니다.

## 3. 결과 비교

### 3.1 추출·정규화 통계

| 지표 | text_edc | decomp_edc |
|---|---|---|
| open triplets | 12,113 | 13,180 |
| 관계 정규화: direct / mapped / enriched | 9,426 (78%) / 2,468 / 166 | 10,241 (78%) / 2,657 / 239 |
| 최종 KG 트리플 | 12,233 | 13,198 |
| 엔티티 | 7,529 | 8,466 |
| 관계 (시드 40 + 확장) | 149 (+109) | 210 (+170) |
| 엔티티 점검: 문제 있는 엔티티 | 4,323 | 4,984 |
| 중복 표기 그룹 / 문장형 개념 / 복합 엔티티 | 237 / 685 / 606 | 235 / 781 / 636 |

**4B → 14B 모델 효과 (text_edc vs 어제 결과):** 관계명이 시드 스키마에 바로 맞는 비율(direct)이 62% → 78%로 올라 LLM 검증 호출이 4,000여 회에서 2,500여 회로 줄었고, 트리플은 11,267 → 12,233개로 늘었습니다. 관계 분포도 더 치우쳤습니다(has administration instruction 2,297, has side effect 1,603, interacts with 1,023).

**문장 분해 전처리 효과 (decomp_edc vs text_edc):** 트리플 +8%, 엔티티 +12%로 재현율은 올랐지만, 확장 관계가 109 → 170개로 늘고 문장형 개념 엔티티도 685 → 781개로 늘었습니다. 분해된 짧은 문장은 주어가 생략되거나 맥락이 빠진 경우가 많아 LLM이 새로운 관계명을 더 자주 만들어 냈습니다. 관계 집중도(상위 10개 비중)는 66% → 61%로 낮아졌습니다. 즉 분해는 "더 많이" 뽑지만 "더 깔끔하게" 뽑지는 않았습니다.

### 3.2 KGGen 엔티티 정규화 결과

| 지표 | 정규화 전 (decomp_edc) | KGGen 원본 (`_ec`) | KGGen 변형 (`_ec_g`) |
|---|---|---|---|
| 엔티티 | 8,466 | 5,064 (−40%) | 5,669 (−33%) |
| 트리플 | 13,198 | 11,940 | 11,746 |
| 관계 | 210 | 143 | 130 |
| 병합된 엔티티 쌍 | – | 3,480 | 2,847 |
| 타입이 섞인 클러스터 | – | 641 | 11 |
| 부정·역방향 관계가 섞인 관계 클러스터 | – | 5 | 3 |
| 점검: 중복 표기 그룹 | 235 | 53 | 68 |
| 점검: 문장형 개념 / 복합 엔티티 | 781 / 636 | 463 / 294 | 523 / 366 |
| 점검: 관계-타입 불일치 엔티티 | 361 | 1,136 | 1,001 |
| 점검: 상용구 허브 노드 | 14 | 26 | 20 |

표기 중복은 크게 줄었지만(235 → 53/68 그룹), **사실을 바꾸는 과병합**이 다수 발생했습니다.

**원본 방식에서 확인한 과병합**
- 페이지 약 자체가 다른 약으로 병합: Atorvastatin → Lovastatin, Escitalopram → citalopram, Carvedilol → "Non-cardioselective beta blockers", Gabapentin → gabapentin enacarbil, Bupropion → "bupropion with naltrexone".
- 부위·정도가 다른 증상을 하나로: `swelling` 클러스터(27개)에 facial swelling, leg swelling, lump in neck; `vision changes`에 loss of vision, double vision.
- 관계 병합이 방향과 부정을 무시: `causes`에 `caused by`, `administered via`에 `not administered via`, `treats`에 `are being treated with`, `interacts with`·`should be avoided with`·`compared with`가 서로 섞임. 그 결과 `used in combination with`가 1,420개로 급증하는 등 관계 분포가 왜곡되었습니다.

**변형(타입 제약 + 엄격 지시문)에서도 남은 과병합**
- Carvedilol → Metoprolol, Cetirizine → Levocetirizine, Duloxetine → Cymbalta(브랜드), Bupropion → Wellbutrin XL.
- `low white blood cell count`에 hypoglycemia, low blood sugar, low calcium; `heart disease`에 heart block, QRS prolongation.
- 관계에서는 `has side effect`가 `has symptom`으로 대표되고, `not used for`에 `does not contain`, `is not`이 묶였습니다.

타입 혼합은 641 → 11개로 거의 사라졌지만, 같은 타입 안에서 "비슷한 주제"를 "같은 개념"으로 판단하는 문제는 그대로입니다. 점검 지표에서 관계-타입 불일치 엔티티가 361 → 1,000개 이상으로 늘어난 것도 잘못된 병합이 관계 의미를 흐린 결과입니다.

### 3.3 해석
1. KGGen의 LLM 중복 판정은 "시제·복수·대소문자·약어 변형"을 겨냥한 일반 도메인 설계입니다. 약물 KG처럼 한 글자 차이(citalopram/escitalopram)나 부위 차이가 다른 사실을 뜻하는 영역에서는 14B 모델이 "같은 의미"를 "같은 주제"로 넓게 해석했습니다.
2. 관계(edge) 정규화는 EDC가 정의 기반으로 이미 수행하므로, KGGen의 이름 기반 관계 병합을 덧붙이면 방향·부정 정보가 손상됩니다. 관계는 KGGen에서 제외하는 것이 맞습니다.
3. 가장 큰 가치는 1단계 semhash와 표기 변형 병합(단수·복수, 대소문자, 수식어 차이)에서 나왔습니다. 이 부분은 안전하고 효과가 큽니다.

## 4. 권장 사항 (다음 반복)
- **관계는 정규화 대상에서 제외**(`--no-canon-edges`)하고, 엔티티만 처리합니다.
- **보호 목록**: 50개 페이지 약 노드, 그리고 파싱한 generic/brand 이름은 LLM 병합 대상에서 제외하거나 "같은 성분"임이 메타데이터로 확인될 때만 합칩니다.
- **병합 승인 강화**: KGGen이 제안한 쌍마다 "두 항목이 동일한 실체인가? 다른 약·용량·부위·정도면 아니오"를 묻는 2차 검증을 넣고, 임베딩 유사도 하한(예: 0.85)을 둡니다. 현재 변형의 지시문 강화만으로는 부족했습니다.
- **상하위 관계 분리**: `severe swelling`처럼 더 구체적인 표현은 병합하지 말고 `broader` 엣지로 연결해 정보 손실 없이 연결성을 확보합니다.
- **정량 평가**: `entity_canon/merge_pairs_sample.csv`(실험별 120쌍)를 수동 채점하면 두 변형의 병합 정밀도를 바로 비교할 수 있습니다.
- 발표용 KG로는 당장은 `decomp_edc/kg` 또는 `text_edc/kg`(정규화 전)를 기준으로 삼고, 정규화는 위 보완을 거친 뒤 적용하는 것을 권합니다.

## 5. 재현 커맨드
```bash
conda activate drugkg && cd ~/drug-kg-edc
MODEL=Qwen/Qwen3-14B-AWQ GPU_UTIL=0.9 MAX_LEN=8192 MAX_SEQS=48 bash scripts/serve_vllm.sh   # 터미널 1
bash scripts/run_experiments.sh                                                               # 터미널 2 (4개 실험 + 비교표)
python scripts/audit_entities.py --kg output/experiments/decomp_edc_ec_g/kg_canon --out /tmp/audit   # 개별 점검
```
실행 중 발견한 버그(LLM이 같은 문자열을 중복 목록에 두 번 넣으면 삭제가 실패) 하나를 고쳐 정규화 두 실험은 재실행했습니다. 모든 LLM 응답은 모델별로 캐시되어 재실행 비용이 없습니다.
