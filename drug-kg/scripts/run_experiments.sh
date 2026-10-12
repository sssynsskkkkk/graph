#!/usr/bin/env bash
# Run the three experiments sequentially (needs the vLLM server: MODEL=Qwen/Qwen3-14B-AWQ GPU_UTIL=0.9 bash scripts/serve_vllm.sh)
#   1. text_edc      : EDC on data/text (section-structured raw text of the 50 drugs)
#   2. decomp_edc    : EDC on data/final_sentences_keep_incomplete.jsonl (Code-KG style sentence decomposition)
#   3. decomp_edc_ec   : decomp_edc + KGGen entity/edge canonicalization (as published)
#   4. decomp_edc_ec_g : same, with same-type restriction + stricter duplicate definition (guarded variant)
set -uo pipefail
cd "$(dirname "$0")/.."
export CUDA_VISIBLE_DEVICES=""
python run_experiment.py --exp text_edc      --input text      --stage all                 "$@"
python run_experiment.py --exp decomp_edc    --input sentences --stage all                 "$@"
python run_experiment.py --exp decomp_edc_ec    --from-exp decomp_edc --entity-canon kggen         --stage all
python run_experiment.py --exp decomp_edc_ec_g  --from-exp decomp_edc --entity-canon kggen_guarded --stage all
python scripts/compare_experiments.py text_edc decomp_edc decomp_edc_ec decomp_edc_ec_g
echo "EXPERIMENTS_DONE"
