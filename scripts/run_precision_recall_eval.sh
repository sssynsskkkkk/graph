#!/usr/bin/env bash
# Precision (sampled, judged against the original page section) and GT-coverage recall for three EDC KGs.
# Stops the vllm9b / vllm14b tmux servers (GPUs are needed), then
#   recall   : teammate's compare_gt_graph_semantics.py (Qwen3-Embedding-0.6B + Qwen3.5-9B, 2 GPU shards) per KG
#   precision: scripts/precision_judge.py with Qwen3.5-27B-GPTQ-Int4 served by vLLM on both GPUs (TP=2, port 8003)
set -euo pipefail
G=/home/heesun/graph
V=$G/drug-kg/output/viz
EVAL=$G/data/kg_eval
PY_EVAL=$HOME/anaconda3/envs/otw_qwen/bin/python   # env used for the original GT comparison
PY=$G/.venv-drugkg/bin/python
KGS="text_edc decomp_edc coref_decomp_edc"
mkdir -p "$EVAL"
exec > >(tee -a "$EVAL/eval.log") 2>&1
step() { echo; echo "===== [$(date '+%F %T')] $*"; }
cd "$G"

step "0. stop vLLM servers to free both GPUs"
tmux kill-session -t vllm9b 2>/dev/null || true
tmux kill-session -t vllm14b 2>/dev/null || true
until [ "$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | awk '{s+=$1} END {print s}')" -lt 2000 ]; do sleep 5; done
nvidia-smi --query-gpu=index,memory.used --format=csv

for KG in $KGS; do
  OUT=$EVAL/recall_$KG
  if [ -f "$OUT/summary.json" ]; then step "1. recall [$KG]: already done, skipped"; continue; fi
  step "1. recall [$KG]: prepare candidates (Qwen3-Embedding-0.6B, GPU0)"
  [ -f "$OUT/candidates.jsonl" ] && echo "candidates exist, reusing" || CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false "$PY_EVAL" -u scripts/compare_gt_graph_semantics.py prepare \
    --gt-file data/gt_top50_review/gold_triplets_draft.jsonl --graph-file "$V/$KG/kg_explorer.html" --output-dir "$OUT"
  step "1. recall [$KG]: judge (Qwen3.5-9B, 2 shards on GPU0/GPU1)"
  PIDS=""
  for S in 0 1; do
    CUDA_VISIBLE_DEVICES=$S HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false "$PY_EVAL" -u scripts/compare_gt_graph_semantics.py judge \
      --output-dir "$OUT" --shard $S --shards 2 --batch-size 4 >> "$OUT/judge_$S.log" 2>&1 &
    PIDS="$PIDS $!"
  done
  wait $PIDS   # only the judge shards: a bare `wait` would also wait for the `tee` process substitution
  tail -n 2 "$OUT"/judge_*.log
  step "1. recall [$KG]: repair judgments whose JSON only lacks a closing quote/brace, then summarize"
  "$PY" scripts/repair_judge_json.py --output-dir "$OUT"
  "$PY_EVAL" scripts/compare_gt_graph_semantics.py summarize --output-dir "$OUT" | tail -3
  grep -E '"match_percent"|"match_or_partial_percent"' "$OUT/summary.json"
done

step "2. precision: start Qwen3.5-27B-GPTQ-Int4 judge (vLLM TP=2, :8003)"
PATH=$HOME/anaconda3/envs/qwen-vllm312/bin:$PATH CUDA_VISIBLE_DEVICES=0,1 VLLM_NO_USAGE_STATS=1 \
  vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --served-model-name judge-llm --language-model-only --tensor-parallel-size 2 \
  --max-model-len 16384 --gpu-memory-utilization 0.9 --max-num-seqs 32 --port 8003 > "$EVAL/vllm_judge_27b.log" 2>&1 &
VPID=$!
until curl -s -m 3 localhost:8003/v1/models | grep -q judge-llm; do
  kill -0 $VPID 2>/dev/null || { echo "judge server died"; tail -20 "$EVAL/vllm_judge_27b.log"; exit 1; }
  sleep 10
done
step "2. precision: sample 10 EDC triples per drug per KG, judge against the original page section"
P=$EVAL/precision
"$PY" scripts/precision_judge.py prepare --output-dir "$P" \
  --graph text_edc=$V/text_edc/kg_explorer.html --graph decomp_edc=$V/decomp_edc/kg_explorer.html \
  --graph coref_decomp_edc=$V/coref_decomp_edc/kg_explorer.html
"$PY" scripts/precision_judge.py judge --output-dir "$P" --base-url http://localhost:8003/v1 --model judge-llm
"$PY" scripts/precision_judge.py summarize --output-dir "$P" | tail -40
kill $VPID; wait $VPID 2>/dev/null || true

step "3. combined report -> drug-kg/output/report/precision_recall_comparison.md"
"$PY" scripts/precision_recall_report.py --precision-dir "$P" \
  --recall text_edc=$EVAL/recall_text_edc --recall decomp_edc=$EVAL/recall_decomp_edc \
  --recall coref_decomp_edc=$EVAL/recall_coref_decomp_edc \
  --recall kggen_canon=$G/data/gt_graph_semantic_comparison_top50 \
  --out $G/drug-kg/output/report/precision_recall_comparison.md
step "EVAL_DONE"
