#!/bin/zsh
# PREREG-v9, start to finish: Sol with the plain prompt (default and high effort) and /code-review at three levels on
# v7's sample, judging, scoring. The Sol and Claude arms run side by side; Codex outages wait and re-run.
#   drive_v9.sh
HERE=${0:A:h}; FACTORY=${HERE:h:h:h}; PY=$FACTORY/.venv/bin/python; R=$FACTORY/calibration/realbugs/results
cd $FACTORY
claude --version > $R/v9-claude-code.version
"${CODEX_BIN:-/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex}" --version > $R/v9-codex.version 2>&1
$HERE/meter.sh > $R/v9-meter-before.txt 2>&1
sol() {
  for a in sol-plain sol-plain-high; do
    echo "== $a"
    for attempt in 1 2 3 4 5 6; do
      $PY $HERE/run_v5.py f $a && break
      [ $? -eq 3 ] || { echo "$a arm failed"; break; }
      echo "$(date +%H:%M) codex usage limit; waiting 30 min"; sleep 1800
    done
  done
}
cc() {
  for a in cc-review cc-review-high cc-review-xhigh; do
    echo "== $a"
    $PY $HERE/run_v5.py f $a || echo "$a arm failed"
  done
}
sol > $R/v9-sol.log 2>&1 &
cc > $R/v9-cc.log 2>&1 &
wait
$HERE/meter.sh > $R/v9-meter-after.txt 2>&1
for a in sol-plain sol-plain-high cc-review cc-review-high cc-review-xhigh; do
  echo "== judge $a"
  for try in 1 2 3; do
    REVIEW_BENCH_JUDGE_TIMEOUT_MS=10800000 $HERE/judge.sh v9-$a > $R/v9-$a.judge.log 2>&1 && break
    echo "judge $a: try $try failed; retrying in 2 min"; sleep 120
  done
done
$PY $FACTORY/calibration/realbugs/compare_v9.py > $R/v9-compare.txt 2>&1
tail -12 $R/v9-compare.txt
echo "exit"
