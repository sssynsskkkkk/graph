# 50개 약물 GT 초안과 팀원 그래프 비교

대상은 `data/gt_top50_review/gold_triplets_draft.jsonl`의 1,894개 GT 후보와
`data/kg_explorer_edc_ec_g.html` 안의 canonical 그래프 관계입니다.
원본 파일은 변경하지 않습니다.

## 평가 단위와 기준

GT 한 관계를 기준으로 같은 약물 문서에서 나온 그래프 관계를 찾습니다.
`mtm__ergocalciferol.txt`는 그래프 출처 키 `mtm/ergocalciferol`에 연결합니다.
제품/제형은 무조건 성분명과 동일한 개체로 처리하지 않습니다.
Ergocalciferol 문서에서 브랜드로 명시된 Calciferol/Drisdol/Calcidol은 해당 성분의 별칭으로 허용합니다.
화면에 보이는 노드 개수나 단순 약물 이름의 중복률을 평가하는 것이 아닙니다.

Cosine similarity는 **후보 검색에만** 사용합니다.

1. 로컬 Qwen3-Embedding-0.6B로 `subject | relation | object`를 임베딩합니다.
2. 정규화 벡터의 내적으로 cosine similarity를 계산합니다.
3. 같은 문서의 상위 7개 관계와 object 문자열 일치 후보 최대 2개를 선택합니다.
   점수 기준 threshold는 없으며, 0.8 이상을 정답으로 처리하지 않습니다.
4. 로컬 Qwen3.5-9B에 GT/조건과 후보 canonical 관계/관계 정의를 제시해 의미를 판정합니다.
5. 같은 문서의 전체 관계에 명시적인 동의어·관계 대응 규칙을 적용하고,
   조건·수치·제형을 보수적으로 검사합니다.

범주:

- `match`: 개체·관계 방향·대상의 핵심 의미가 같고 추가 조건 확인이 필요하지 않은 일치 후보.
- `partial`: 핵심 의미는 대응하지만 연령·제형·시점·병용약·용량 역할·가능성·허가 등의
  조건이 빠졌거나 아직 확인되지 않은 부분 일치 후보.
- `no_match`: 규칙/검색 후보에서 같은 사실의 대응을 확인하지 못함.
  다른 약물, 다른 관계 방향, 부정 반전, 서로 다른 명시적 용량은 일치가 아닙니다.

GT에 `qualifiers`가 있으면 **항상 보수적으로 partial로 분류**합니다.
따라서 partial을 모두 "모델이 조건을 틀린 사례"로 해석하면 안 됩니다.
LLM에 원문 문단 전체를 제공하지 않으며, 의학 상식으로 그래프의 오류를 보충하지 않습니다.
원문이나 raw 관계가 맞아도 실제 canonical 관계가 틀렸다면 같은 사실로 취급하지 않습니다.

추가 검사에서는 같은 단위의 명시적 용량들이 서로 겹치지 않는 후보,
그리고 abuse/misuse/addiction을 서로 치환한 후보를 no_match로 보정합니다.
질량 단위 변환과 범위 끝점만 처리하는 제한적인 검사로, 완전한 용량 비교기는 아닙니다.
보정으로 다른 올바른 후보를 놓칠 가능성도 있어 검수가 필요합니다.
GT가 성인과 소아 모두를 포함하는데 후보가 한 집단만 포함하면 일치가 아닌 부분 일치로 처리합니다.

## 결과와 해석

완료된 통계는 `summary.json`과 `report_ko.md`를 참고하세요.

- `semantic_comparison.jsonl`: 각 GT의 판정, 근거, 그래프 관계, cosine 후보와 최종 판정 방법.
- `semantic_comparison.csv`: 검토용 통합 표. cosine 점수와 의미 판정은 별도 컬럼입니다.
- `per_drug_summary.csv`: 약물 50개별 GT 수와 일치/부분/미확인 수.
- `contradiction_guard_audit.jsonl`: 수치 등의 모순 검사로 보정한 LLM 판정.
- `validation_report.json`: 입력 동일성, 결과 수, 약물 범위, 후보 출처, 판정 연결 검사.
- `metadata.json`: 원본 파일 해시, 모델 위치, 후보 검색 설정.
- `candidates.jsonl`, `judgments_*.jsonl`: 재현/감사를 위한 중간 입력과 모델 출력.

`(match + partial) / 1894`는 선택한 GT 후보의 잠정적 핵심 의미 겹침 비율입니다.
각 GT가 독립적인 비교 단위이며 같은 그래프 관계가 여러 GT에 대응할 수도 있습니다.
약물 개수나 그래프 관계 11,746개의 정확도를 뜻하지 않습니다.
Micro 비율은 GT 관계 하나하나에 같은 가중치를 주고, macro 비율은 약물별 비율을 평균냅니다.

GT는 사람이 검수하지 않은 비완전 AI 초안이며 판정 모델에도 오류가 있습니다.
후보 검색을 못 한 경우 실제 그래프에 관계가 없는 것과 구분하기 어렵습니다.
Qwen3.5-9B는 기존 문장 분해에도 사용돼 평가기 독립성을 보장하지 않습니다.
이 결과는 확정된 정확도나 Precision/Recall/F1이 아닙니다.

기존 1~25번의 GT와 그래프 해시가 동일하므로 기존 모델 입력/판정 850개를 재사용했습니다.
새로운 26~50번 1,044개를 판정하고, 모순 검사는 전체 1,894개에 동일하게 적용합니다.
따라서 기존 25개 평가에서 일부 최종 범주는 달라질 수 있습니다.

## 재현

`prepare`는 중간 입력을 덮어씁니다. 사람 검수 CSV가 있다면 먼저 별도로 보관하세요.
모델은 로컬 캐시에서만 읽으며 네트워크 호출은 하지 않습니다.

```bash
/home/heesun/anaconda3/envs/otw_qwen/bin/python -u scripts/compare_gt_graph_semantics.py prepare \
  --gt-file data/gt_top50_review/gold_triplets_draft.jsonl \
  --output-dir data/gt_graph_semantic_comparison_top50 \
  --reuse-dir data/gt_graph_semantic_comparison
bash scripts/run_top50_semantic_judge.sh 0 0
bash scripts/run_top50_semantic_judge.sh 1 1
python scripts/compare_gt_graph_semantics.py summarize \
  --output-dir data/gt_graph_semantic_comparison_top50
```
