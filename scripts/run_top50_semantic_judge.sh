#!/usr/bin/env bash
set -euo pipefail

# Run one resumable shard on a selected GPU. Models are loaded from local cache only.
EVAL_GPU="${1:?GPU index required}"
EVAL_SHARD="${2:?Shard index required}"
EVAL_ROOT="/home/heesun/graph"
EVAL_OUTPUT="${EVAL_ROOT}/data/gt_graph_semantic_comparison_top50"

cd "${EVAL_ROOT}"
CUDA_VISIBLE_DEVICES="${EVAL_GPU}" HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false \
  /home/heesun/anaconda3/envs/otw_qwen/bin/python -u \
  scripts/compare_gt_graph_semantics.py judge \
  --output-dir "${EVAL_OUTPUT}" --shard "${EVAL_SHARD}" --shards 2 --batch-size 4 \
  > "${EVAL_OUTPUT}/judge_${EVAL_SHARD}.log" 2>&1
