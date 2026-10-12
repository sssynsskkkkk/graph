# Top-25 관계 추출 GT 검토 초안

`data/top50.yaml`의 rank 1~25와 `data/text-only/text-only/*.txt`를 기준으로 작성했습니다.
학습/분해 모델의 출력을 정답으로 복사하지 않고, Codex가 선택한 원문 구간을 읽어
관계 주석을 작성했습니다. Qwen 추론이나 외부 의료 지식을 이용한 자동 보충은 하지 않았습니다.

**이 데이터는 사람이 검수한 gold가 아닙니다.** 모든 관계의 `review_status`는
`pending_human_review`입니다. 팀원의 독립 검토와 필요한 수정 이후에 정답셋으로 확정하세요.
원문에 명시된 사실의 추출 정답 후보이며, 최신 의료 지식의 진위를 검증한 데이터는 아닙니다.

## 범위

25개 약물 모두 포함하지만, 전체 문서의 모든 관계를 빠짐없이 주석한 exhaustive GT는 아닙니다.
용도, 작용기전, 일부 부작용, 주의/금기, 제형, 용량, 상호작용, 복약 정보 중 명확한 사실을
선택해 주석했습니다. FAQ 전체, 모든 복약 지시, 모든 목록 항목을 완전 주석하지 않았습니다.
문장 분류에서 Incomplete였다는 이유로 원문 관계를 제외하지 않았습니다.

정확한 개수와 약물별 파일 연결은 `summary.json`을 참고하세요. 원래 50개 TXT에서 추출한
8,028개 텍스트 단위 중, rank 1~25의 입력은 4,308개입니다.
`source_passages.jsonl`은 주석한 근거 구간을 기록하며 각 구간의 `fully_annotated`도 `false`입니다.
그 구간 안에서도 모든 가능한 관계를 주석했다고 가정하지 마세요.

## 파일

- `gold_triplets_draft.jsonl`: 한 줄에 한 관계. 원문, 줄 번호, 조건, 출처, 검토 상태 포함.
- `gold_triplets_review.csv`: Excel 등에서 검토 가능한 UTF-8 BOM CSV.
  수정용 `corrected_entity_1`, `corrected_relationship`, `corrected_entity_2`,
  `reviewer`, `review_notes` 컬럼이 있으며 비어 있습니다.
- `by_drug/01_atorvastatin.json` 등: 약물별 JSON 25개.
- `codekg_format_draft.json`: `Entity 1`, `Relationship`, `Entity 2` 형식의 약물별 묶음.
  조건을 평가할 때는 이 파일의 `qualifiers`도 반드시 확인하세요.
- `source_passages.jsonl`: 근거 구간과 연결된 GT ID.
- `relation_schema.json`: 정규화된 관계 ID와 영어 관계 표현의 대응.
- `annotation_spec.json`: 사람이 수정하기 쉬운 원문 줄 번호별 주석 명세.
- `summary.json`: 전체/약물별 통계와 원본 파일 SHA-256.

## 주석 원칙

1. 관계의 방향과 부정/가능성 표현을 보존했습니다.
   `may cause`는 `causes`와 다르고, `is not approved for`는 금기와 다릅니다.
2. 질환/부작용 나열은 가능한 한 하나의 object씩 분리했습니다.
3. 연령, 질환, 제형, 병용약, 투여 단계, 용량/단위/횟수 등 중요한 조건은 `qualifiers`에
   보존했습니다. 세 필드만으로 조건부 사실을 무조건적인 사실처럼 사용하면 안 됩니다.
4. "의사에게 알려야 할 병력/병용약"은 `requires medication review with` 등으로 기록했습니다.
   이런 문구를 금기나 확정 상호작용으로 바꾸지 않았습니다.
5. 제품을 구별했습니다. rank 15는 `adderall.txt`의 Adderall이고,
   rank 23은 `flonase.txt`의 Flonase 제품입니다. Flonase Sensimist와 Flonase Allergy Relief의
   성분/연령, metoprolol 염/제형, gabapentin enacarbil, semaglutide 브랜드별 용도를 합치지 않았습니다.
6. 약물 이름, 질환 동의어와 약어는 의미를 유지하면서 일부 표준화했습니다.
   `MDD`, `OCD`, `DVT`, `PE` 등의 풀네임은 해당 문서에서 확인할 수 있습니다.
7. 문맥상 대명사/"this medicine"은 문서 약물로 연결했습니다. 숫자 토큰 ID를 임상 수치로
   해석하지 않았습니다. 원문 철자 오타와 비정상 줄바꿈은 근거에 그대로 남겼습니다.
8. 데이터 작성자가 생성한 관계 후보입니다. 모델/사람의 신뢰도 확률이나 임의 RMSE는 넣지 않았습니다.

## 기존 파이프라인 결과와 연결

`source_record_ids`는 기존 문장 분류/분해 결과의 `record_id` 및 최종 문장 파일의
`source_record_id`와 연결됩니다. 하나의 근거 문단/목록이 여러 입력 문장을 포함하면 여러 ID가
들어 있습니다. 이 목록은 줄 번호 기반의 문맥 연결이며 정확한 개체 span은 아닙니다.

`evidence_char_start`/`evidence_char_end`는 UTF-8을 디코딩한 원문에서 사용하는 Python 문자 offset입니다.
종료 offset은 exclusive이며 byte offset이 아닙니다. `source_sha256`으로 문서 버전도 확인할 수 있습니다.

## 평가 시 주의

- 현재 초안에 없는 모델 트리플을 곧바로 false positive로 계산하지 마세요.
  주석 누락과 진짜 모델 오류를 원문을 보고 구별해야 합니다.
- 완전한 문서 단위 Precision/Recall/F1을 구하려면 평가 범위를 먼저 정하고 그 범위의 모든
  유효 관계와 "관계 없음" 사례를 사람이 완전 주석해야 합니다.
- 검수한 후보를 기준으로 관계 회수율을 확인하는 소규모 분석은 가능하지만,
  이 값을 전체 문서의 recall/F1이라고 발표하지 마세요.
- CoDe-KG는 관계 표현이 자유롭습니다. 단순 문자열 exact match만 사용하면
  `used to treat`와 `treats`, `hypertension`과 `high blood pressure` 등을 오답 처리할 수 있습니다.
  entity/관계 표준화 또는 사전에 정한 의미적 매칭 기준이 필요합니다.
- 가능한 한 동일한 원본 근거 구간에서 두 파이프라인을 비교하고, 목록·부정·용량 조건을
  의미적으로 보존했는지도 별도로 평가하세요. 트리플 개수만으로 품질이 더 좋다고 판단하지 마세요.

## 재생성

명세를 수정한 뒤 프로젝트 루트에서 실행합니다. 출력 검토 CSV를 덮어쓰므로,
사람이 검수한 CSV는 먼저 별도의 이름으로 보관하세요.

```bash
python scripts/build_top25_gt_draft.py
```
