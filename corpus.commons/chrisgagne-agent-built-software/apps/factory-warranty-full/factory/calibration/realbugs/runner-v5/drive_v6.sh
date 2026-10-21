#!/bin/zsh
# PREREG-v6, start to finish: the four arms on the v6 sample, the control, judging, scoring. Waits out Codex's usage
# limit before each Codex step; outage trials are re-run (PREREG-v4 Amendments 1 and 2).
#   drive_v6.sh            (FACTORY_AXIS_INDEX must point at the open build's distillation index)
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
mkdir -p $R/v6-factory; git rev-parse HEAD > $R/v6-factory.commit
echo "== factory"
export FACTORY_REVIEW_LEGS=claude,claude-plain,codex-review V5_REPORT=members
for attempt in 0 1 2 3; do
  if [ $attempt -gt 0 ]; then
    n=$($PY $HERE/repeat_outages.py $R/v6-factory)
    [ "$n" = "0" ] && break
    echo "repeat outages moved: $n (repeat $attempt)"
  fi
  wait_codex
  $PY $HERE/run_v5.py c factory
done
$PY $HERE/run_v5.py c factory --to-rb
for a in vendors claude-again pr-agent; do
  echo "== $a"
  while true; do
    [ $a = vendors ] && wait_codex
    $PY $HERE/run_v5.py c $a && break
    [ $? -eq 3 ] || { echo "$a arm failed"; break; }
  done
done
$PY $FACTORY/calibration/realbugs/compare_v6.py --build-control
for a in factory vendors control pr-agent; do
  echo "== judge $a"
  for try in 1 2 3; do
    $HERE/judge.sh v6-$a > $R/v6-$a.judge.log 2>&1 && break
    echo "judge $a: try $try failed; retrying in 2 min"; sleep 120
  done
done
$PY $FACTORY/calibration/realbugs/compare_v6.py > $R/v6-compare.txt 2>&1
tail -6 $R/v6-compare.txt
$HERE/meter.sh
echo "exit"
