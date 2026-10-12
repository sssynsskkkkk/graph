#!/usr/bin/env bash
# Progress of run_precision_recall_eval.sh (tmux session kg_eval). Usage: bash scripts/eval_status.sh
E=/home/heesun/graph/data/kg_eval
echo "now: $(date '+%F %T')"
echo "current step: $(grep '^=====' $E/eval.log | tail -1)"
for KG in text_edc decomp_edc coref_decomp_edc; do
  d=$E/recall_$KG
  if [ -f $d/summary.json ]; then
    echo "recall  $KG: done  ($(grep -o '"match_or_partial_percent": [0-9.]*' $d/summary.json | head -1))"
  elif ls $d/judge_*.log >/dev/null 2>&1; then
    n=0; for f in $d/judge_*.log; do k=$(grep -o 'judged=[0-9]*' $f | tail -1 | cut -d= -f2); n=$((n + ${k:-0})); done
    echo "recall  $KG: judging $n / 1894"
  else
    echo "recall  $KG: waiting"
  fi
done
if [ -f $E/precision/summary.json ]; then echo "precision: done"
elif [ -f $E/precision/judgments.jsonl ]; then echo "precision: judging $(wc -l < $E/precision/judgments.jsonl) / 1500"
else echo "precision: waiting"; fi
grep -q EVAL_DONE $E/eval.log && echo "ALL DONE -> drug-kg/output/report/precision_recall_comparison.md"
awk "/restarted after/{buf=\"\"} {buf=buf \$0 \"\\n\"} END{printf \"%s\", buf}" $E/eval.log | grep -E "Traceback|Error" | head -3 | sed "s/^/ERROR (since last restart): /"
