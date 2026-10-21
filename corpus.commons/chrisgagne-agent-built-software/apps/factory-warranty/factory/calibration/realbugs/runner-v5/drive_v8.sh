#!/bin/zsh
# PREREG-v8, start to finish: brooks-lint and Claude Code's /code-review on v6's sample, the two arms built from v6's
# trials, judging, scoring. No Codex.
#   drive_v8.sh
HERE=${0:A:h}; FACTORY=${HERE:h:h:h}; PY=$FACTORY/.venv/bin/python; R=$FACTORY/calibration/realbugs/results
cd $FACTORY
claude --version > $R/v8-claude-code.version
for a in cc-review brooks; do
  echo "== $a"
  $PY $HERE/run_v5.py e $a || echo "$a arm failed"
done
$PY $FACTORY/calibration/realbugs/compare_v8.py --build
for a in factory-claude plain cc-review brooks; do
  echo "== judge $a"
  for try in 1 2 3; do
    REVIEW_BENCH_JUDGE_TIMEOUT_MS=10800000 $HERE/judge.sh v8-$a > $R/v8-$a.judge.log 2>&1 && break
    echo "judge $a: try $try failed; retrying in 2 min"; sleep 120
  done
done
$PY $FACTORY/calibration/realbugs/compare_v8.py > $R/v8-compare.txt 2>&1
tail -8 $R/v8-compare.txt
echo "exit"
