# Top-50 약물 관계 추출 GT 검토 초안

`data/top50.yaml`의 1~50번 약물과 `data/text-only/text-only/*.txt`를 기준으로 만든
원문 근거 기반의 AI 주석 초안입니다. 기존 1~25번의 850개 관계는 변경 없이 유지하고,
26~50번의 1,044개 관계를 추가했습니다. 총 50개 약물, 1,894개 관계입니다.
팀원의 그래프나 문장 분해 모델의 출력을 정답으로 복사하지 않았습니다.

## 주의

이 파일은 **사람이 검수하여 확정한 gold가 아닙니다**. 모든 관계는
`review_status: pending_human_review`이며 독립적인 사람 검수가 필요합니다.
50개 약물은 모두 포함하지만, 전체 문서의 모든 관계를 빠짐없이 주석하지는 않았습니다.
근거 구간도 `fully_annotated: false`이므로 이 초안에 없는 모델 관계를 자동으로
false positive로 처리하거나 전체 문서의 Precision/Recall/F1을 계산하면 안 됩니다.

평가 범위를 먼저 확정한 뒤 그 범위의 관계를 완전 주석해야 합니다.
약물마다 문서 길이와 선택한 정보가 달라 관계 수와 범주 분포도 같지 않습니다.
새로운 26~50번과 기존 1~25번은 주석 회차도 다르므로 동일한 기준으로 함께 검수하세요.
원문에 적힌 내용을 추출한 후보이며 최신 의료 사실이나 허가 여부를 검증한 데이터는 아닙니다.
원문 내 충돌이나 검토가 필요한 일부 주장은 `qualifiers.review_note`에 표시했습니다.

## 파일

- `gold_triplets_draft.jsonl`: 50개 약물 통합 파일. 한 줄에 한 관계.
- `gold_triplets_review.csv`: 원문과 수정/검토 컬럼을 포함한 Excel용 CSV.
- `by_drug/`: 약물별 JSON 50개. 파일명 앞 두 자리 숫자는 약물 순위입니다.
- `codekg_format_draft.json`: `Entity 1`, `Relationship`, `Entity 2` 형식의 약물별 묶음.
- `annotation_spec.json`: 전체 1~50번의 근거 줄 번호 기반 주석 명세.
- `annotations_26_50.json`: 이번에 추가한 26~50번의 주석 명세만 포함.
- `source_passages.jsonl`: 주석 근거 구간과 GT ID 연결.
- `relation_schema.json`: 정규화된 관계 ID와 영어 관계 표현.
- `summary.json`: 전체 및 약물별 통계, 원본 파일 연결.
- `validation_report.json`: 구조, 출처, 문자 offset, 용량 수치 검사 결과.
- `extension_validation.json`: 기존 850개 유지 여부와 추가분 통계.

## JSONL 필드와 주석 원칙

관계는 `entity_1`, `relationship`, `entity_2`에 있습니다.
`rank`, `ranking_drug_name`으로 약물별로 분리할 수 있습니다.
`gt_id`는 `GT01_0001`과 같은 약물별 고유 ID입니다.

`qualifiers`의 연령, 제형, 투여 경로, 적응증, 병용약, 시점과 부정/가능성 표현을
함께 평가하세요. 예를 들어 일반형/서방형 트라마돌의 최대 용량이나
경구/주사 히드록시진의 용도를 합치면 원문의 의미가 달라집니다.
"의사에게 병용약을 알려라"라는 문구를 확정 상호작용이나 금기로 바꾸지 않았습니다.

각 관계에는 원문 `evidence_text`, `source_file`, `source_url`, `source_sha256`,
`line_start`, `line_end`, 필요한 `additional_context`를 기록했습니다.
`evidence_char_start`/`evidence_char_end`는 디코딩한 원문의 Python 문자 offset이며
종료 값은 exclusive입니다. Byte offset이 아닙니다.
`source_record_ids`는 줄 번호에 기반한 기존 문장 분류/분해 입력과의 연결이며,
정확한 개체 span을 뜻하지 않습니다.

자세한 기존 주석 기준은 `../gt_top25_review/README.md`를 참고하세요.
구조 검증 통과는 의료적/의미적 정확성에 대한 인증이 아닙니다.

## 재생성

아래 명령은 이 폴더의 출력 파일과 검토 CSV를 덮어씁니다.
사람이 수정한 검토 CSV가 있다면 먼저 별도로 보관하세요.

```bash
python scripts/build_top25_gt_draft.py \
  --spec data/gt_top25_review/annotation_spec.json \
  --extra-spec data/gt_top50_review/annotations_26_50.json \
  --rank-end 50 \
  --output-dir data/gt_top50_review
python scripts/validate_top25_gt_draft.py --data-dir data/gt_top50_review
```
