# GT 초안과 팀원 그래프의 의미 비교

우리 GT의 약물 문서 25개는 팀원 그래프에 모두 포함됩니다. 그래프 전체는 50개 문서, 11,746개 관계이며 비교 대상 25개 문서에 연결된 고유 관계는 6,323개입니다.

문서의 존재와 노드 이름의 일치는 구별했습니다. 약물 문서 키(`dr`)로 범위를 제한했으며, Amlodipine/Amlodipine besylate 같은 동의 표현은 허용했습니다. Bupropion/Wellbutrin XL, Adderall/Adderall XR, Sertraline/sertraline oral solution은 제형·제품 범위를 그대로 동일하다고 가정하지 않았습니다.

## 전체 결과

| 자동 판정 | GT 수 | 비율 |
|---|---:|---:|
| 일치 후보 | 157 | 18.5% |
| 부분 일치 후보 | 340 | 40.0% |
| 대응 후보 미확인 | 353 | 41.5% |

일치와 부분 일치를 합하면 **497 / 850 (58.5%)**입니다.

이 비율은 GT 초안에서 선택한 관계의 의미 겹침에 대한 자동 추정입니다. 전체 그래프 Precision/Recall/F1이나 확정된 정확도가 아닙니다.

## 판정 기준

- 일치 후보: 개체·관계·방향의 의미가 대응하고 별도 조건 확인이 요구되지 않은 자동 판정.
- 부분 일치 후보: 핵심 사실이 대응하지만 연령·병용약·제형·초기/최대 용량·가능성·허가 여부 등을 확인해야 함. 보수적인 규칙에서는 조건이 있는 GT를 부분 일치로 분류하므로, 실제로 조건이 보존된 사례도 여기에 포함될 수 있음.
- 대응 후보 미확인: 명시적 동의어 규칙으로 같은 문서 전체 관계를 찾지 못하고, 임베딩으로 검색한 후보에서도 LLM이 대응을 찾지 못함. 전체 그래프에 절대 없다는 증명은 아님.

## 약물별 결과

| 순위 | 약물 | GT | 일치 | 부분 일치 | 미확인 | 일치+부분 |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Atorvastatin | 36 | 17 | 8 | 11 | 69.4% |
| 2 | Levothyroxine | 29 | 4 | 11 | 14 | 51.7% |
| 3 | Metformin | 35 | 6 | 14 | 15 | 57.1% |
| 4 | Amlodipine | 30 | 8 | 15 | 7 | 76.7% |
| 5 | Lisinopril | 34 | 7 | 14 | 13 | 61.8% |
| 6 | Albuterol | 35 | 4 | 9 | 22 | 37.1% |
| 7 | Losartan | 32 | 4 | 17 | 11 | 65.6% |
| 8 | Metoprolol | 34 | 9 | 12 | 13 | 61.8% |
| 9 | Rosuvastatin | 31 | 2 | 17 | 12 | 61.3% |
| 10 | Omeprazole | 39 | 18 | 4 | 17 | 56.4% |
| 11 | Gabapentin | 33 | 1 | 14 | 18 | 45.5% |
| 12 | Sertraline | 31 | 0 | 17 | 14 | 54.8% |
| 13 | Escitalopram | 35 | 2 | 17 | 16 | 54.3% |
| 14 | Semaglutide | 22 | 7 | 7 | 8 | 63.6% |
| 15 | Dextroamphetamine + Amphetamine salts | 29 | 0 | 16 | 13 | 55.2% |
| 16 | Pantoprazole | 32 | 8 | 16 | 8 | 75.0% |
| 17 | Bupropion | 48 | 2 | 23 | 23 | 52.1% |
| 18 | Hydrochlorothiazide | 32 | 9 | 13 | 10 | 68.8% |
| 19 | Fluoxetine | 33 | 9 | 19 | 5 | 84.8% |
| 20 | Trazodone | 40 | 6 | 15 | 19 | 52.5% |
| 21 | Montelukast | 37 | 4 | 14 | 19 | 48.6% |
| 22 | Amoxicillin | 31 | 8 | 9 | 14 | 54.8% |
| 23 | Fluticasone | 38 | 8 | 12 | 18 | 52.6% |
| 24 | Tamsulosin | 40 | 6 | 13 | 21 | 47.5% |
| 25 | Apixaban | 34 | 8 | 14 | 12 | 64.7% |

## 방법 및 한계

1. HTML의 `kg-data` JSON을 추출했습니다. 화면 표시나 브라우저 자바스크립트 실행은 사용하지 않았습니다.
2. GT 원본 파일명과 그래프 관계의 문서 출처(`dr`)를 연결했습니다.
3. 로컬 Qwen3-Embedding-0.6B로 GT별 같은 문서의 상위 7개 관계를 찾고, object 문자열이 정확히 일치하는 후보를 최대 2개 추가했습니다.
4. Qwen3.5-9B가 canonical subject/relation/object를 비교했습니다. 사전 명시한 동의어·관계 대응 규칙을 같은 문서의 모든 관계에 추가 적용했습니다.
5. 조건, 수치, 제형의 누락을 보수적으로 처리했습니다. 모든 판정은 사람이 확인할 수 있도록 CSV에 남겼습니다.

GT 850개 자체가 사람이 검수하지 않은 부분 주석 초안입니다. 임베딩 후보 검색과 LLM 판정에도 오류가 있을 수 있으며, Qwen3.5-9B는 앞선 문장 분해에도 사용된 모델이므로 평가기의 독립성을 보장하지 않습니다. 실험/논문의 확정 성능 수치로 사용하려면 GT와 비교 판정을 독립적으로 사람이 검수해야 합니다.

원래 관계(`raw_relationship`)나 근거 chunk가 맞더라도 canonical 그래프 관계가 다른 의미로 바뀌었다면 동일한 관계로 간주하지 않았습니다.

파일: `semantic_comparison.csv`, `semantic_comparison.jsonl`, `per_drug_summary.csv`, `summary.json`. 원본 그래프 파일과 GT 파일은 수정하지 않았습니다.

## 직접 확인한 정규화 문제 사례

- 그래프: `Atorvastatin → contraindicated in → allergy to Metformin`
  알레르기 대상 약물이 다릅니다. atorvastatin.txt 69행은 atorvastatin 알레르기를 말합니다.
- 그래프: `Atorvastatin → belongs to drug class → Zocor`
  atorvastatin.txt 7행의 약물 계열은 HMG-CoA reductase inhibitors/statins입니다. Zocor는 계열명으로 대응하지 않습니다.
- 그래프: `Adderall XR → administered via → breast milk in small amounts`
  adderall.txt 63행의 'passes into breast milk'가 투여 경로로 바뀌었습니다. 모유 이행과 모유를 통한 투여는 다른 의미입니다.
