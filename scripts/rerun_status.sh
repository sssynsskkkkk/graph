#!/usr/bin/env bash
# Progress of run_coref_rerun.sh (tmux session coref_rerun). Usage: bash scripts/rerun_status.sh
E=/home/heesun/graph/data/kg_eval; X=/home/heesun/graph/drug-kg/output/experiments/coref_decomp_edc_r2
echo "now: $(date '+%F %T')"
echo "current step: $(grep '^=====' $E/rerun.log 2>/dev/null | tail -1)"
echo "EDC drugs extracted: $(ls $X/edc 2>/dev/null | wc -l) / 50"
n=0; for f in $E/recall_coref_decomp_edc_r2/judge_*.log; do [ -f "$f" ] || continue; k=$(grep -o 'judged=[0-9]*' $f | tail -1 | cut -d= -f2); n=$((n + ${k:-0})); done
echo "recall judged: $n / 1894"
[ -f $E/precision_r2/judgments.jsonl ] && echo "precision judged: $(wc -l < $E/precision_r2/judgments.jsonl) / 500"
grep -q RERUN_DONE $E/rerun.log 2>/dev/null && echo "ALL DONE -> drug-kg/output/report/precision_recall_comparison.md"
grep -E "Traceback|Error|died" $E/rerun.log 2>/dev/null | head -3 | sed "s/^/ERROR: /"
