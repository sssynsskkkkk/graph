#!/usr/bin/env bash
# Wait for the running text_edc experiment, then run decomp_edc, both entity-canonicalization variants and the comparison.
set -uo pipefail
cd "$(dirname "$0")/.."
export CUDA_VISIBLE_DEVICES=""
while pgrep -f "[r]un_experiment.py --exp text_edc" > /dev/null; do sleep 30; done
python run_experiment.py --exp decomp_edc      --input sentences --stage all
python run_experiment.py --exp decomp_edc_ec   --from-exp decomp_edc --entity-canon kggen         --stage all
python run_experiment.py --exp decomp_edc_ec_g --from-exp decomp_edc --entity-canon kggen_guarded --stage all
python scripts/compare_experiments.py text_edc decomp_edc decomp_edc_ec decomp_edc_ec_g
echo "REST_DONE"
