#!/usr/bin/env bash
# Run the whole pipeline (requires the vLLM server from scripts/serve_vllm.sh to be up).
# Usage: bash scripts/run_all.sh            # all 50 drugs
#        bash scripts/run_all.sh 5          # first 5 drugs (pilot)
set -euo pipefail
cd "$(dirname "$0")/.."
DRUGS="${1:-all}"
export CUDA_VISIBLE_DEVICES=""          # keep the embedder on CPU; the GPU belongs to vLLM
python run_pipeline.py --stage fetch --drugs "$DRUGS"
python run_pipeline.py --stage parse --drugs "$DRUGS"
python run_pipeline.py --stage extract --drugs "$DRUGS"
python run_pipeline.py --stage consolidate
python run_pipeline.py --stage export --drugs "$DRUGS"
echo "done -> output/kg/"
