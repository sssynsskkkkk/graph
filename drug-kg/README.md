# Drug Knowledge Graph from Drugs.com with EDC (Extract–Define–Canonicalize)

지식기반시스템 Term Project 1. [Drugs.com](https://www.drugs.com/) 의 상위 50개 약(미국 처방량 기준, ClinCalc DrugStats ∩ Drugs.com) 페이지에서
**EDC 프레임워크** (Zhang & Soh, *Extract, Define, Canonicalize: An LLM-based Framework for Knowledge Graph Construction*, EMNLP 2024)
로 트리플을 추출해 지식그래프(KG)를 구축하는 end-to-end 파이프라인입니다. 로컬 vLLM(Qwen2.5-7B-Instruct)으로 동작하며, OpenAI 호환 API라면 무엇이든 교체 가능합니다.

```
drugs.com HTML ──(scrape)──▶ data/raw_html ──(parse)──▶ data/parsed/*.json, data/chunks/*.jsonl
      │                                                            │
      │ 구조화 메타데이터(generic/brand/class/dosage form/related)   │ 섹션별 텍스트 청크
      ▼                                                            ▼
 structured triples                      EDC: Extract(OIE) ─▶ Define(관계 정의) ─▶ Canonicalize(임베딩 검색 + LLM 검증, 스키마 확장)
      └──────────────────────────────┬────────────────────────────────┘
                                     ▼
            postprocess(엔티티 정규화·타입 부여·중복 제거) ─▶ output/kg/ (JSONL/CSV, Neo4j, Turtle, GraphML, stats)
```

## 1. 설치

```bash
conda create -n drugkg python=3.11 -y && conda activate drugkg
pip install -r requirements.txt
pip install vllm                    # GPU 서버용 (RTX 3090 Ti 24GB에서 Qwen2.5-7B-Instruct bf16 동작 확인)
```

## 2. LLM 서버 띄우기 (터미널 1)

```bash
conda activate drugkg
bash scripts/serve_vllm.sh          # 기본: Qwen/Qwen3-4B-Instruct-2507, GPU 메모리 50%, http://localhost:8000/v1, served name "drugkg-llm"
# GPU가 비어 있으면 더 큰 모델 권장 (served name은 그대로라 config.yaml 수정 불필요):
MODEL=Qwen/Qwen2.5-7B-Instruct GPU_UTIL=0.85 MAX_LEN=8192 bash scripts/serve_vllm.sh
```

> 개발 당시 RTX 3090 Ti(24GB)를 다른 작업과 공유하고 있어 4B 모델을 사용했습니다. 모델을 바꾸면 LLM 캐시(`output/cache/llm`)는
> 모델명 기준으로 분리되므로 `--force` 로 다시 추출하면 됩니다.

OpenAI/Anthropic 등 호스팅 API를 쓰려면 `config.yaml`의 `llm.base_url`, `llm.model`, `llm.api_key`(또는 환경변수
`DRUGKG_LLM_BASE_URL / DRUGKG_LLM_MODEL / DRUGKG_LLM_API_KEY`)만 바꾸면 됩니다.

## 3. 파이프라인 실행 (터미널 2)

```bash
conda activate drugkg
python run_pipeline.py --stage fetch                 # 50개 약 URL 확인 + HTML 캐시 (6~10초 간격, Akamai 차단 시 자동 대기)
python run_pipeline.py --stage parse --dry-run       # 섹션/청크 통계만 확인
python run_pipeline.py --stage extract --drugs 2 --max-chunks 3   # 파일럿 (약 2개 × 청크 3개)
python run_pipeline.py --stage extract               # 전체 EDC 추출 (약별 output/edc/<slug>.json, 스키마 output/schema/schema.csv)
python run_pipeline.py --stage consolidate           # 확장된 관계 중 중복 병합 (output/schema/relation_merge_map.json)
python run_pipeline.py --stage export                # 최종 KG 내보내기 (output/kg/)
python run_pipeline.py --stage all                   # 위 전부
bash scripts/run_all.sh                              # 동일 (fetch→parse→extract→consolidate→export)
python scripts/query_examples.py                     # 산출된 KG로 예시 질의 (pandas/networkx)
```

* 모든 LLM 호출은 `output/cache/llm/`에 캐시되어 재실행 시 비용/시간이 들지 않습니다. 약 단위로 재개(resume)되며 `--force`로 다시 추출합니다.
* `--iterations 1` 로 EDC+R(엔티티 추출 + 스키마 리트리버 힌트를 이용한 정제 추출)을 켤 수 있습니다 (호출 수 약 2배).

## 4. EDC 구현이 논문과 대응되는 지점

| 논문 단계 | 구현 | 파일 |
|---|---|---|
| Open Information Extraction | 약 이름/섹션 컨텍스트를 넣은 few-shot 프롬프트로 `[S, R, O]` JSON 추출 | `prompts/oie_*.txt`, `drugkg/edc/framework.py` |
| Schema Definition | 청크별로 등장한 관계마다 자연어 정의 생성 | `prompts/sd_*.txt` |
| Schema Canonicalization | 관계 **정의**를 `BAAI/bge-base-en-v1.5`로 임베딩 → 시드 스키마에서 top-k 후보 검색 → LLM 다지선다 검증("None of the above" 포함) | `drugkg/edc/canonicalize.py`, `drugkg/edc/schema.py` |
| Self-canonicalization (schema enrichment) | 매핑 실패 관계는 정의와 함께 스키마에 추가(같은 배치 내 신규 관계와 중복 검사), subject/object 타입을 LLM이 부여 | `canonicalize.py` (`enrich_schema: true`) |
| Schema Retriever + Refinement (EDC+R) | 엔티티 추출/병합 + 텍스트→관계 임베딩 검색 힌트로 재추출 | `drugkg/edc/retriever.py`, `framework.refinement_hints` |
| (추가) Schema consolidation | 추출 종료 후 확장 관계끼리 유사도 ≥ 0.88 이면 LLM yes/no로 병합 | `drugkg/edc/consolidate.py` |
| (추가) 구조화 트리플 | 페이지 메타데이터(generic/brand name, drug class, dosage form/strength, related drugs, FDA 승인연도, 처방 구분)를 고정밀 트리플로 추가 | `drugkg/postprocess.py` |

시드 스키마(관계 40개 + 도메인/레인지 타입)는 `schemas/drug_seed_schema.csv` 에 있으며 자유롭게 수정할 수 있습니다.
소형 모델(4B)을 쓰는 경우 OIE 프롬프트에 "관계명은 일반적인 2~4단어, 구체 내용은 object에" 지침을 넣어 스키마 폭발을 줄였습니다
(`prompts/oie_template.txt`). 그래도 남는 중복 관계는 `consolidate` 단계가 병합합니다.

## 5. 산출물 (`output/kg/`)

| 파일 | 내용 |
|---|---|
| `triples.jsonl` / `triples.csv` | (subject, relation, object) + 타입, 출처 약, 섹션/청크 provenance, 등장 횟수 |
| `entities.csv` | 엔티티 id, 표시명, 타입(Drug/Condition/SideEffect/...), 언급 횟수 |
| `schema.csv` | 실제 사용된 관계와 정의, 타입, 출처(seed/enriched), 트리플 수 |
| `neo4j/nodes.csv`, `neo4j/relationships.csv`, `neo4j/import.cypher` | Neo4j 적재용 |
| `kg.ttl` | RDF Turtle (`http://drugkg.example.org/`) |
| `kg.graphml` | networkx/Gephi 용 |
| `stats.json` | 통계 요약 |

중간 산출물: `output/edc/<slug>.json` (청크별 OIE → 정의 → 정규화 결과와 후보/응답 전부 기록), `output/schema/schema.csv` (확장된 스키마).

## 6. 설정 (`config.yaml`)

`scrape.pages` 에 `sfx`, `dosage` 를 추가하면 부작용/용량 서브페이지도 함께 추출합니다. `chunking.*` 로 청크 크기와 섹션 포함/제외,
`edc.*` 로 top-k, 자동 매핑 임계값, 스키마 확장 여부, 정제 반복 횟수, 병합 임계값을 조정합니다.

## 8. 현재 결과 (2026-10-06, Qwen3-4B-Instruct-2507, 메인 페이지만, refinement 0회)

| 항목 | 값 |
|---|---|
| 약 | 50 (ClinCalc 상위 50, Drugs.com 메인 페이지 824 청크) |
| 트리플 | 약 11,000 (EDC 약 10,400 + 구조화 메타데이터 약 970) |
| 엔티티 | 약 6,500 (Condition, SideEffect, Instruction, Warning, Substance, Drug 순) |
| 관계 | 약 147 (시드 40 + 확장 107, 1회만 쓰인 확장 관계 제외) |
| LLM 호출 | 약 2,600회 (추출+정의+정규화), 약 1개당 15~45초 |

상위 관계: has side effect, interacts with, has warning, has administration instruction, has serious side effect, treats, similar to, contraindicated in ...

**알려진 한계 / 개선 포인트**
- 4B 모델이라 정규화 검증에서 "None of the above"를 자주 택해 확장 관계가 많고(107개), 일부 트리플은 주어가 약이 아니거나 관계 선택이 어색합니다 (예: `Metformin lowers level of acne`). GPU가 비면 `MODEL=Qwen/Qwen2.5-7B-Instruct ... bash scripts/serve_vllm.sh` 후 `--stage extract --force` 로 재추출을 권장합니다.
- 브랜드명 표기 변형(`Adderall` / `Adderall XR`)이 별도 노드로 남습니다. `postprocess.relation_merges` 처럼 엔티티 별칭 병합 규칙을 추가하는 것이 다음 단계입니다.
- `consolidate` 는 명백한 동의어만 병합하며(4B 기준 0건), 수동 병합은 `config.yaml`의 `postprocess.relation_merges` 로 지정합니다.
- `--iterations 1` (EDC+R) 은 구현되어 있으나 비용 때문에 기본 실행에서는 끄여 있습니다.

## 9. 실험 (입력 전처리 · 엔티티 정규화)

`run_experiment.py`로 입력 소스와 정규화 방식을 바꿔 가며 실험합니다 (`scripts/run_experiments.sh` 가 네 실험을 순서대로 실행).
`--input text` (data/text), `--input sentences` (문장 분해 파일), `--entity-canon kggen|kggen_guarded` (KGGen 엔티티 정규화, `drugkg/entity_canon.py`).
결과와 해석은 `output/report/261007-experiments.md`, 수치 비교는 `output/report/experiments_comparison.md` 를 보세요.

## 10. 시각화

```bash
python scripts/visualize_kg.py --kg output/kg                       # -> output/viz/main/
python scripts/visualize_kg.py --kg output/experiments/decomp_edc/kg --drug Metformin --drug Apixaban
python scripts/visualize_kg.py --all                                # 모든 KG(메인 + 실험별 kg / kg_canon) + 실험 비교 그림
```

- `kg_explorer.html`: 브라우저에서 바로 여는 대화형 탐색기. 엔티티 검색 → 1~2 hop 이웃, 관계·타입·등장 횟수 필터, 50개 약 개요, 공유 부작용 보기, 엣지 클릭 시 근거 문장과 출처, 현재 화면 CSV 내보내기. (vis-network를 CDN에서 불러오므로 인터넷 연결 필요)
- `fig_*.png`: 발표용 정적 그림. 관계 상위 20, 엔티티 타입 분포, 약별 트리플 수, 공유 부작용, 약 1개의 1-hop 네트워크(`--drug`), 실험별 KG 크기 비교(`--all`).

## 7. 데이터 출처/이용

텍스트는 Drugs.com 소비자용 약 정보 페이지(각 트리플에 URL 기록). 수업 과제용 비상업적 사용이며 요청 간격을 두고 수집합니다.
