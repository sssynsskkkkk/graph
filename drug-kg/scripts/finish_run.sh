#!/usr/bin/env bash
# Finish the run: wait for any other pipeline process to end, then fetch missing pages, parse, extract (resume), consolidate, export.
set -uo pipefail
cd "$(dirname "$0")/.."
export CUDA_VISIBLE_DEVICES=""
while pgrep -f "[r]un_pipeline.py" > /dev/null; do echo "waiting for another run_pipeline.py process..."; sleep 15; done
python run_pipeline.py --stage fetch
python run_pipeline.py --stage parse
python run_pipeline.py --stage extract
python run_pipeline.py --stage consolidate
python run_pipeline.py --stage export
echo "FINISH_RUN_DONE"
