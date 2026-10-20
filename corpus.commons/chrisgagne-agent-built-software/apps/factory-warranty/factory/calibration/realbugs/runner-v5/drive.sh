#!/bin/zsh
# Runs the arms that use Codex (factory, vendors) for one part, waiting out Codex's usage limit before each step and
# re-running outage trials under PREREG-v4's Amendments 1 and 2 (which PREREG-v5 adopts).
#   drive.sh a|b          (FACTORY_AXIS_INDEX must point at the open build's distillation index)
PART=$1; HERE=${0:A:h}; FACTORY=${HERE:h:h:h}; PY=$FACTORY/.venv/bin/python
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
git rev-parse HEAD > calibration/realbugs/results/v5-factory.commit
echo "== $PART factory"
for attempt in 0 1 2 3; do
  if [ $attempt -gt 0 ]; then
    n=$($PY $HERE/repeat_outages.py calibration/realbugs/results/v5-$PART-factory)
    [ "$n" = "0" ] && break
    echo "repeat outages moved: $n (repeat $attempt)"
  fi
  wait_codex
  $PY $HERE/run_v5.py $PART factory
done
[ $PART = a ] && $PY $HERE/run_v5.py a factory --to-rb
echo "== $PART vendors"
while true; do
  wait_codex
  $PY $HERE/run_v5.py $PART vendors && break
  [ $? -eq 3 ] || { echo "vendors arm failed"; break; }
done
$HERE/meter.sh
echo "exit"
