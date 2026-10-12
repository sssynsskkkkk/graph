#!/usr/bin/env bash
# Re-run the two entity-canonicalization experiments with the fixed KGGen port (LLM calls are cached), then compare.
set -uo pipefail
cd "$(dirname "$0")/.."
export CUDA_VISIBLE_DEVICES=""
while pgrep -f "[r]un_rest.sh" > /dev/null; do sleep 10; done
python run_experiment.py --exp decomp_edc_ec   --entity-canon kggen         --stage canon_entities
python run_experiment.py --exp decomp_edc_ec   --stage audit
python run_experiment.py --exp decomp_edc_ec_g --from-exp decomp_edc --entity-canon kggen_guarded --stage all
python scripts/compare_experiments.py text_edc decomp_edc decomp_edc_ec decomp_edc_ec_g
echo "CANON_RERUN_DONE"
