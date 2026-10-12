#!/usr/bin/env bash
# Start the local vLLM OpenAI-compatible server used by config.yaml (llm.base_url / llm.model).
# Usage: bash scripts/serve_vllm.sh            (env: MODEL, SERVED_NAME, PORT, MAX_LEN, GPU_UTIL, MAX_SEQS)
set -euo pipefail
export VLLM_NO_USAGE_STATS=1   # avoid writing to ~/.config (not writable on this machine)
# Default: Qwen3-4B-Instruct-2507 (fits next to other GPU jobs). With a free 24GB GPU use e.g.
#   MODEL=Qwen/Qwen2.5-7B-Instruct GPU_UTIL=0.85 bash scripts/serve_vllm.sh
# The served name stays "drugkg-llm" so config.yaml does not need to change when swapping models.
MODEL="${MODEL:-Qwen/Qwen3-4B-Instruct-2507}"
SERVED_NAME="${SERVED_NAME:-drugkg-llm}"
PORT="${PORT:-8000}"
exec vllm serve "$MODEL" \
  --served-model-name "$SERVED_NAME" \
  --dtype bfloat16 \
  --max-model-len "${MAX_LEN:-6144}" \
  --gpu-memory-utilization "${GPU_UTIL:-0.5}" \
  --max-num-seqs "${MAX_SEQS:-24}" \
  --port "$PORT"
