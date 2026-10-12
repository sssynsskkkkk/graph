#!/usr/bin/env bash
# Pronoun-resolved text -> BERT sentence classification -> CoDe-KG decomposition -> EDC KG -> explorer + report.
# Needs the two vLLM servers (tmux sessions vllm9b :8001 for decomposition, vllm14b :8002 for EDC).
# Env overrides: COREF_TEXT RAW_DIR WORK EXP DRUGS (DRUGS=all or e.g. carvedilol for a smoke test)
set -euo pipefail
G=/home/heesun/graph
DK=$G/drug-kg
COREF_TEXT=${COREF_TEXT:-$G/data/text-only/coref/text}
RAW_DIR=${RAW_DIR:-$G/data/text-only/text-only}
WORK=${WORK:-$G/data/text-only/coref_pipeline}
EXP=${EXP:-coref_decomp_edc}
DRUGS=${DRUGS:-all}
PY=$G/.venv-drugkg/bin/python                 # qwen-vllm stack + sentence-transformers (EDC, OpenAI client)
PY_BERT=$HOME/anaconda3/envs/heesun/bin/python  # transformers 4.41 env the CoDe-KG BERT classifier was trained with
FINAL=$WORK/3_final_sentences/final_sentences_keep_incomplete.jsonl

mkdir -p "$WORK"
exec > >(tee -a "$WORK/pipeline.log") 2>&1
step() { echo; echo "===== [$(date '+%F %T')] $*"; }
cd "$G"
step "0. settings: COREF_TEXT=$COREF_TEXT WORK=$WORK EXP=$EXP DRUGS=$DRUGS"
cat "$G/data/text-only/coref/summary.json" 2>/dev/null || true

step "1. BERT sentence classification of the pronoun-resolved text (CPU; both GPUs serve vLLM)"
CUDA_VISIBLE_DEVICES="" "$PY_BERT" scripts/classify_drugs_pilot_sentences.py --input-dir "$COREF_TEXT" \
  --output-dir "$WORK/1_classification"

step "2. CoDe-KG decomposition with Qwen3.5-9B (vllm9b :8001)"
"$PY" scripts/decompose_classified_sentences_vllm.py --input-jsonl "$WORK/1_classification/sentence_classification.jsonl" \
  --output-dir "$WORK/2_decomposition"

step "3. flatten (incomplete sentences kept, as in decomp_edc)"
"$PY" scripts/export_final_sentences_keep_incomplete.py --input-jsonl "$WORK/2_decomposition/decomposition.jsonl" \
  --output-dir "$WORK/3_final_sentences"

step "4. attach the original page sentence to every decomposed sentence"
"$PY" scripts/attach_raw_sentences.py --final-jsonl "$FINAL" --raw-dir "$RAW_DIR" --coref-dir "$COREF_TEXT"

step "5. sentence trace (original -> pronoun resolved -> label -> decomposed): $WORK/4_trace/{trace.jsonl,md/}"
"$PY" scripts/build_trace.py --decomposition-jsonl "$WORK/2_decomposition/decomposition.jsonl" --final-jsonl "$FINAL" \
  --raw-dir "$RAW_DIR" --coref-dir "$COREF_TEXT" --output-dir "$WORK/4_trace"

step "6. EDC with Qwen3-14B-AWQ (vllm14b :8002) -> drug-kg/output/experiments/$EXP"
cd "$DK"
DRUGKG_LLM_BASE_URL=http://localhost:8002/v1 "$PY" run_experiment.py --exp "$EXP" --input sentences \
  --sentences-file "$FINAL" --drugs "$DRUGS" --stage all
cp "$WORK/4_trace/trace.jsonl" "output/experiments/$EXP/trace.jsonl"

step "7. explorer (Graph + Source trace tabs) and figures -> drug-kg/output/viz/$EXP"
"$PY" scripts/visualize_kg.py --kg "output/experiments/$EXP/kg" --drug Metformin --drug Carvedilol

if [ "$DRUGS" = "all" ]; then
  step "8. per-drug quality vs text_edc / decomp_edc -> drug-kg/output/report/${EXP}_per_drug_quality.md"
  "$PY" scripts/per_drug_quality.py text_edc=output/experiments/text_edc/kg decomp_edc=output/experiments/decomp_edc/kg \
    "$EXP=output/experiments/$EXP/kg" --out "output/report/${EXP}_per_drug_quality.md"
fi
step "PIPELINE_DONE"
