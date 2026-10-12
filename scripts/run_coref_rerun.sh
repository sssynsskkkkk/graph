#!/usr/bin/env bash
# Second EDC run on the SAME pronoun-resolved + decomposed sentences (run-to-run variance check), then the same
# recall / precision evaluation as run_precision_recall_eval.sh, and a combined report with both runs.
# Only difference from run 1: an empty LLM cache (otherwise every call would be answered from run 1's cache).
set -euo pipefail
G=/home/heesun/graph
DK=$G/drug-kg
EVAL=$G/data/kg_eval
EXP=coref_decomp_edc_r2
FINAL=$G/data/text-only/coref_pipeline/3_final_sentences/final_sentences_keep_incomplete.jsonl
PY=$G/.venv-drugkg/bin/python
PY_EVAL=$HOME/anaconda3/envs/otw_qwen/bin/python
VLLM_ENV=$HOME/anaconda3/envs/qwen-vllm312/bin
mkdir -p "$EVAL"
exec > >(tee -a "$EVAL/rerun.log") 2>&1
step() { echo; echo "===== [$(date '+%F %T')] $*"; }
wait_server() {  # port pid name
  until curl -s -m 3 "localhost:$1/v1/models" | grep -q "$3"; do
    kill -0 "$2" 2>/dev/null || { echo "server $3 died"; exit 1; }
    sleep 10
  done
}
cd "$G"

step "0. config copy with an empty LLM cache (output/cache/llm_$EXP); everything else identical to run 1"
CFG=$EVAL/config_$EXP.yaml
"$PY" - "$DK/config.yaml" "$CFG" "$DK/output/cache/llm_$EXP" <<'PYEOF'
import sys, yaml
cfg = yaml.safe_load(open(sys.argv[1]))
cfg["llm"]["cache_dir"] = sys.argv[3]
yaml.safe_dump(cfg, open(sys.argv[2], "w"), allow_unicode=True, sort_keys=False)
PYEOF
grep -n "cache_dir" "$CFG"

step "1. EDC run 2 with Qwen3-14B-AWQ (GPU0, :8002)"
PATH=$VLLM_ENV:$PATH CUDA_VISIBLE_DEVICES=0 VLLM_NO_USAGE_STATS=1 vllm serve Qwen/Qwen3-14B-AWQ --served-model-name drugkg-llm \
  --dtype bfloat16 --max-model-len 16384 --gpu-memory-utilization 0.9 --max-num-seqs 48 --port 8002 > "$EVAL/vllm_edc_14b_r2.log" 2>&1 &
VPID=$!
wait_server 8002 $VPID drugkg-llm
cd "$DK"
DRUGKG_LLM_BASE_URL=http://localhost:8002/v1 "$PY" run_experiment.py --exp "$EXP" --config "$CFG" --input sentences \
  --sentences-file "$FINAL" --stage all
cp "$G/data/text-only/coref_pipeline/4_trace/trace.jsonl" "output/experiments/$EXP/trace.jsonl"
kill $VPID; wait $VPID 2>/dev/null || true
step "2. explorer -> drug-kg/output/viz/$EXP"
"$PY" scripts/visualize_kg.py --kg "output/experiments/$EXP/kg" --drug Metformin --drug Carvedilol
cd "$G"
until [ "$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | awk '{s+=$1} END {print s}')" -lt 2000 ]; do sleep 5; done

OUT=$EVAL/recall_$EXP
step "3. recall [$EXP]: prepare + judge (Qwen3.5-9B, 2 shards) + summarize"
[ -f "$OUT/candidates.jsonl" ] || CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false "$PY_EVAL" -u \
  scripts/compare_gt_graph_semantics.py prepare --gt-file data/gt_top50_review/gold_triplets_draft.jsonl \
  --graph-file "$DK/output/viz/$EXP/kg_explorer.html" --output-dir "$OUT"
PIDS=""
for S in 0 1; do
  CUDA_VISIBLE_DEVICES=$S HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false "$PY_EVAL" -u scripts/compare_gt_graph_semantics.py judge \
    --output-dir "$OUT" --shard $S --shards 2 --batch-size 4 >> "$OUT/judge_$S.log" 2>&1 &
  PIDS="$PIDS $!"
done
wait $PIDS
"$PY" scripts/repair_judge_json.py --output-dir "$OUT"
"$PY_EVAL" scripts/compare_gt_graph_semantics.py summarize --output-dir "$OUT" | tail -2
grep -E '"match_percent"|"match_or_partial_percent"' "$OUT/summary.json" | head -2

step "4. precision [$EXP]: Qwen3.5-27B-GPTQ-Int4 judge (TP=2, :8003), same sampling and prompt as run 1"
PATH=$VLLM_ENV:$PATH CUDA_VISIBLE_DEVICES=0,1 VLLM_NO_USAGE_STATS=1 vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --served-model-name judge-llm \
  --language-model-only --tensor-parallel-size 2 --max-model-len 16384 --gpu-memory-utilization 0.9 --max-num-seqs 32 \
  --port 8003 > "$EVAL/vllm_judge_27b_r2.log" 2>&1 &
VPID=$!
wait_server 8003 $VPID judge-llm
P=$EVAL/precision_r2
"$PY" scripts/precision_judge.py prepare --output-dir "$P" --graph "$EXP=$DK/output/viz/$EXP/kg_explorer.html"
"$PY" scripts/precision_judge.py judge --output-dir "$P" --base-url http://localhost:8003/v1 --model judge-llm
"$PY" scripts/precision_judge.py summarize --output-dir "$P" | tail -25
kill $VPID; wait $VPID 2>/dev/null || true

step "5. run-to-run overlap of extracted triples (EDC triples, normalized subject|relation|object)"
"$PY" - "$DK/output/viz" <<'PYEOF'
import json, re, sys, itertools
def triples(name):
    h = open(f"{sys.argv[1]}/{name}/kg_explorer.html", encoding="utf-8").read()
    D = json.loads(re.search(r'<script\b[^>]*\bid=["\']kg-data["\'][^>]*>(.*?)</script>', h, re.S).group(1))
    lab = {n["id"]: n["l"].lower() for n in D["nodes"]}
    return {(lab[e["s"]], e["r"], lab[e["o"]]) for e in D["edges"] if "edc" in e["src"]}
T = {n: triples(n) for n in ["text_edc", "decomp_edc", "coref_decomp_edc", "coref_decomp_edc_r2"]}
for a, b in itertools.combinations(T, 2):
    i = len(T[a] & T[b])
    print(f"{a} vs {b}: shared {i}, jaccard {i / len(T[a] | T[b]):.3f}")
PYEOF

step "6. combined report -> drug-kg/output/report/precision_recall_comparison.md"
"$PY" scripts/precision_recall_report.py --precision-dir "$EVAL/precision" --precision-dir "$P" \
  --recall text_edc=$EVAL/recall_text_edc --recall decomp_edc=$EVAL/recall_decomp_edc \
  --recall coref_decomp_edc=$EVAL/recall_coref_decomp_edc --recall "$EXP=$OUT" \
  --recall kggen_canon=$G/data/gt_graph_semantic_comparison_top50 \
  --out $DK/output/report/precision_recall_comparison.md
step "RERUN_DONE"
