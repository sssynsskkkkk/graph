# 정확도·재현율 비교 (자동 판정)

- **재현율**: GT 초안 1,894개(50개 약, 사람 미검수·비완전 주석) 중 KG가 담은 비율. 팀원 스크립트 `compare_gt_graph_semantics.py`를 그대로 사용(Qwen3-Embedding 후보 검색 + Qwen3.5-9B 판정). 엄격 = match, 관대 = match + partial.
- **정확도**: KG마다 EDC 트리플을 약별 10개씩 무작위 추출(500개)해, 해당 트리플이 나온 **원래 페이지 섹션 원문**과 대조. Qwen3.5-27B가 KG 출처를 모른 채 섞어서 판정. 엄격 = correct, 관대 = correct + partial. 괄호는 95% 신뢰구간.
- F1은 같은 기준(엄격끼리, 관대끼리)의 정확도와 재현율로 계산한 참고값입니다.

| KG | 트리플 | 정확도 엄격 | 정확도 관대 | 재현율 엄격 | 재현율 관대 | F1 엄격 | F1 관대 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 원문 입력 + EDC | 12233 | 48.0 (44–52) | 88.4 (85–91) | 28.6 | 77.7 | 35.8 | 82.7 |
| 문장 분해 + EDC | 13198 | 47.8 (44–52) | 87.0 (84–90) | 28.6 | 77.1 | 35.8 | 81.8 |
| 대명사 치환 + 문장 분해 + EDC | 13244 | 40.6 (36–45) | 81.4 (78–85) | 27.5 | 75.3 | 32.8 | 78.2 |
| 대명사 치환 + 문장 분해 + EDC (2차 실행) | 13202 | 44.8 (40–49) | 87.4 (84–90) | 28.0 | 76.5 | 34.5 | 81.6 |
| 문장 분해 + EDC + KGGen 정규화 (팀원) | 11746 | – | – | 15.9 | 50.5 | – | – |

## 정확도: 틀린 트리플의 오류 유형 (500개 중 개수)

| 오류 유형 | 원문 입력 + EDC | 문장 분해 + EDC | 대명사 치환 + 문장 분해 + EDC | 대명사 치환 + 문장 분해 + EDC (2차 실행) |
|---|---:|---:|---:|---:|
| not_in_text | 4 | 2 | 2 | 2 |
| uninformative | 1 | 0 | 4 | 2 |
| wrong_direction | 4 | 7 | 4 | 0 |
| wrong_entity | 6 | 4 | 7 | 6 |
| wrong_relation | 43 | 52 | 75 | 53 |

## 재현율: 약별 (관대 기준 %, match+partial)

| 약 | GT | 원문 입력 + EDC | 문장 분해 + EDC | 대명사 치환 + 문장 분해 + EDC | 대명사 치환 + 문장 분해 + EDC (2차 실행) | 문장 분해 + EDC + KGGen 정규화 (팀원) |
|---|---:|---:|---:|---:|---:|---:|
| Atorvastatin | 36 | 92 | 97 | 94 | 94 | 69 |
| Levothyroxine | 29 | 83 | 59 | 52 | 86 | 52 |
| Metformin | 35 | 69 | 71 | 66 | 71 | 57 |
| Amlodipine | 30 | 83 | 77 | 80 | 77 | 77 |
| Lisinopril | 34 | 85 | 71 | 79 | 71 | 56 |
| Albuterol | 35 | 57 | 57 | 57 | 66 | 37 |
| Losartan | 32 | 75 | 88 | 91 | 91 | 66 |
| Metoprolol | 34 | 79 | 91 | 85 | 88 | 62 |
| Rosuvastatin | 31 | 71 | 77 | 68 | 65 | 61 |
| Omeprazole | 39 | 87 | 92 | 92 | 90 | 56 |
| Gabapentin | 33 | 82 | 79 | 58 | 61 | 45 |
| Sertraline | 31 | 84 | 94 | 87 | 81 | 55 |
| Escitalopram | 35 | 89 | 94 | 86 | 91 | 54 |
| Semaglutide | 22 | 82 | 82 | 77 | 86 | 64 |
| Dextroamphetamine + Amphetamine salts | 29 | 86 | 79 | 83 | 83 | 55 |
| Pantoprazole | 32 | 84 | 91 | 78 | 94 | 75 |
| Bupropion | 48 | 54 | 60 | 65 | 60 | 52 |
| Hydrochlorothiazide | 32 | 88 | 84 | 75 | 72 | 66 |
| Fluoxetine | 33 | 73 | 82 | 79 | 82 | 85 |
| Trazodone | 40 | 65 | 75 | 75 | 72 | 52 |
| Montelukast | 37 | 84 | 65 | 59 | 59 | 49 |
| Amoxicillin | 31 | 71 | 84 | 58 | 45 | 55 |
| Fluticasone | 38 | 84 | 84 | 87 | 87 | 53 |
| Tamsulosin | 40 | 92 | 90 | 78 | 88 | 48 |
| Apixaban | 34 | 82 | 76 | 82 | 82 | 65 |
| Simvastatin | 50 | 70 | 70 | 70 | 72 | 80 |
| Insulin Glargine | 33 | 85 | 85 | 85 | 88 | 39 |
| Empagliflozin | 26 | 77 | 73 | 77 | 77 | 46 |
| Furosemide | 30 | 77 | 67 | 73 | 67 | 47 |
| Meloxicam | 30 | 90 | 80 | 90 | 93 | 57 |
| Acetaminophen + Hydrocodone | 41 | 73 | 78 | 78 | 83 | 32 |
| Tirzepatide | 43 | 79 | 79 | 79 | 86 | 51 |
| Methylphenidate | 47 | 77 | 79 | 79 | 81 | 64 |
| Duloxetine | 40 | 80 | 88 | 80 | 75 | 42 |
| Prednisone | 53 | 92 | 87 | 91 | 85 | 58 |
| Carvedilol | 29 | 93 | 93 | 90 | 90 | 3 |
| Famotidine | 32 | 75 | 72 | 69 | 75 | 47 |
| Ibuprofen | 43 | 77 | 67 | 65 | 65 | 47 |
| Buspirone | 35 | 60 | 60 | 54 | 60 | 46 |
| Venlafaxine | 64 | 81 | 77 | 80 | 77 | 56 |
| Tramadol | 48 | 75 | 79 | 79 | 79 | 42 |
| Potassium Chloride | 36 | 81 | 75 | 75 | 67 | 67 |
| Hydroxyzine | 53 | 68 | 58 | 66 | 66 | 32 |
| Allopurinol | 37 | 76 | 70 | 73 | 73 | 46 |
| Clopidogrel | 36 | 67 | 44 | 47 | 56 | 42 |
| Ergocalciferol | 41 | 46 | 61 | 66 | 66 | 29 |
| Cetirizine | 40 | 72 | 75 | 75 | 78 | 2 |
| Ondansetron | 35 | 89 | 74 | 74 | 86 | 26 |
| Cyclobenzaprine | 61 | 79 | 82 | 75 | 69 | 49 |
| Spironolactone | 61 | 82 | 89 | 82 | 84 | 34 |

## 한계

- GT는 사람이 검수하지 않은 AI 초안이고, 문서의 일부 관계만 주석했습니다. 재현율은 'GT 초안 커버리지'입니다.
- 두 판정 모두 LLM 자동 판정이며 오류가 있습니다. 재현율 판정 모델(Qwen3.5-9B)은 문장 분해에도 쓰였습니다.
- 정확도는 KG당 500개 표본 추정이라 신뢰구간 안의 차이는 우연일 수 있습니다.
- 판정 원자료: `/home/heesun/graph/data/kg_eval/precision/judged_triples.csv`, `/home/heesun/graph/data/kg_eval/precision_r2/judged_triples.csv`, 재현율은 각 디렉터리의 `semantic_comparison.csv`.
