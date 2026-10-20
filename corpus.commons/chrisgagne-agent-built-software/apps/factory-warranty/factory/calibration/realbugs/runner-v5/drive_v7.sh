#!/bin/zsh
# PREREG-v7, start to finish: the factory (default legs) and the vendors arm on the v7 sample, split into four
# single-model arms, judged and scored. Waits out Codex's usage
# limit before each Codex step; outage trials are re-run (PREREG-v4 Amendments 1 and 2).
#   drive_v7.sh            (FACTORY_AXIS_INDEX must point at the open build's distillation index)
HERE=${0:A:h}; FACTORY=${HERE:h:h:h}; PY=$FACTORY/.venv/bin/python; R=$FACTORY/calibration/realbugs/results
CODEX=${CODEX_BIN:-/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex}
wait_codex() {
  local d=$(mktemp -d) r
  while true; do
    r=$(cd $d && "$CODEX" exec --skip-git-repo-check --ephemeral -m gpt-6.1-sol "Reply with the single word OK." < /dev/null 2>&1 | tail -5)
    if print -r -- "$r" | grep -q "usage limit"; then echo "$(date +%H:%M) codex at its usage limit; waiting"; sleep 600
    elif print -r -- "$r" | grep -qx "OK"; then echo "$(date +%H:%M) codex answers"; break
    else echo "$(date +%H:%M) codex check failed; waiting"; sleep 300; fi
  done
  rm -rf $d
}
cd $FACTORY
mkdir -p $R/v7-factory; git rev-parse HEAD > $R/v7-factory.commit
echo "== factory"
export FACTORY_REVIEW_LEGS=claude,codex V5_REPORT=members
for attempt in 0 1 2 3; do
  if [ $attempt -gt 0 ]; then
    n=$($PY $HERE/repeat_outages.py $R/v7-factory)
    [ "$n" = "0" ] && break
    echo "repeat outages moved: $n (repeat $attempt)"
  fi
  wait_codex
  $PY $HERE/run_v5.py d factory
done
$PY $HERE/run_v5.py d factory --to-rb
for a in vendors; do
  echo "== $a"
  while true; do
    [ $a = vendors ] && wait_codex
    $PY $HERE/run_v5.py d $a && break
    [ $? -eq 3 ] || { echo "$a arm failed"; break; }
  done
done
$PY $FACTORY/calibration/realbugs/compare_v7.py --build
for a in opus-factory opus-own sol-factory sol-own; do
  echo "== judge $a"
  for try in 1 2 3; do
    REVIEW_BENCH_JUDGE_TIMEOUT_MS=10800000 $HERE/judge.sh v7-$a > $R/v7-$a.judge.log 2>&1 && break
    echo "judge $a: try $try failed; retrying in 2 min"; sleep 120
  done
done
$PY $FACTORY/calibration/realbugs/compare_v7.py > $R/v7-compare.txt 2>&1
tail -6 $R/v7-compare.txt
$HERE/meter.sh
echo "exit"
