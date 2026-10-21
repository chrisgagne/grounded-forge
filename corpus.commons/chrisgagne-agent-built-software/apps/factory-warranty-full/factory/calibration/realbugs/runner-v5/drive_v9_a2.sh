#!/bin/zsh
# PREREG-v9 Amendment 2: the factory's brief at higher effort (one reviewer per run) and Claude Code's plain prompt at
# --effort xhigh, on v7's sample; judging; scoring. FACTORY_AXIS_INDEX must point at the open build's index.
HERE=${0:A:h}; FACTORY=${HERE:h:h:h}; PY=$FACTORY/.venv/bin/python; R=$FACTORY/calibration/realbugs/results
cd $FACTORY
$HERE/meter.sh > $R/v9-meter-before-a2.txt 2>&1
export V5_REPORT=members
sol() {
  git rev-parse HEAD > $R/v9-sol-factory-high.commit
  for attempt in 1 2 3 4 5 6; do
    if [ $attempt -gt 1 ]; then
      n=$($PY $HERE/repeat_outages.py $R/v9-sol-factory-high)
      [ "$n" = "0" ] && break
      echo "$(date +%H:%M) repeat outages moved: $n; waiting 30 min"; sleep 1800
    fi
    RUN_OUT=v9-sol-factory-high FACTORY_REVIEW_LEGS=codex FACTORY_REVIEW_CODEX_EFFORT=high $PY $HERE/run_v5.py f factory
  done
  RUN_OUT=v9-sol-factory-high $PY $HERE/run_v5.py f factory --to-rb
}
opus() {
  git rev-parse HEAD > $R/v9-opus-factory-xhigh.commit
  RUN_OUT=v9-opus-factory-xhigh FACTORY_REVIEW_LEGS=claude FACTORY_REVIEW_CLAUDE_EFFORT=xhigh $PY $HERE/run_v5.py f factory
  RUN_OUT=v9-opus-factory-xhigh $PY $HERE/run_v5.py f factory --to-rb
  RUN_OUT=v9-opus-plain-xhigh $PY $HERE/run_v5.py f plain-xhigh
}
sol > $R/v9-a2-sol.log 2>&1 &
opus > $R/v9-a2-opus.log 2>&1 &
wait
$HERE/meter.sh > $R/v9-meter-after-a2.txt 2>&1
for a in sol-factory-high opus-factory-xhigh opus-plain-xhigh; do
  for try in 1 2 3; do
    REVIEW_BENCH_JUDGE_TIMEOUT_MS=10800000 $HERE/judge.sh v9-$a > $R/v9-$a.judge.log 2>&1 && break
    sleep 120
  done
done
$PY $FACTORY/calibration/realbugs/compare_v9.py > $R/v9-compare.txt 2>&1
tail -14 $R/v9-compare.txt
echo exit
