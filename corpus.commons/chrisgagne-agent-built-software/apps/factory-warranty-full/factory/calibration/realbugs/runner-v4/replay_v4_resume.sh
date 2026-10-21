#!/bin/zsh
# Resume the round-two replay under PREREG-v4 Amendment 2: wait for Codex before each batch, and re-run repeat outages.
REPO="<repos>"
PY="$REPO/factory/.venv/bin/python"
OUT="$REPO/factory/calibration/realbugs/results"
CASES="$REPO/factory/calibration/realbugs/v4-cases.json"
S=<scratch>
REPOS=$S/realbugs/repos
CODEX=/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex
APP="$REPO/grounded-forge/.claude/worktrees/factory-distro/corpus.commons/chrisgagne-agent-built-software/apps/factory-warranty"
export FACTORY_AXIS_INDEX="$APP/distillations/warranting-agent-built-software/WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md"
typeset -A CHECKOUT; CHECKOUT[v3]="$REPO/factory-v3-pinned"; CHECKOUT[v4]="$REPO/factory-v4-pinned"
wait_codex() {
  local d=$(mktemp -d) r
  while true; do
    r=$(cd $d && "$CODEX" exec --skip-git-repo-check -m gpt-6.1-sol "Reply with the single word OK." 2>&1 | tail -5)
    if print -r -- "$r" | grep -q "usage limit"; then echo "$(date +%H:%M) codex at its usage limit; waiting"; sleep 600
    elif print -r -- "$r" | grep -qx "OK"; then echo "$(date +%H:%M) codex answers"; break
    else echo "$(date +%H:%M) codex probe failed; waiting"; sleep 300; fi
  done
  rm -rf $d
}
run_arm() {  # $1 batch, $2 arm
  (cd "${CHECKOUT[$2]}" && PYTHONPATH="${CHECKOUT[$2]}" "$PY" -m factory.cli replay run --cases "$CASES" --repos "$REPOS" \
     --out "$OUT/v4-arm-$2" --trials 2 --jobs 2 --only "$1" --grounding distillations)
}
for batch in w01,w02,w03,w04,w05 w06,w07,w08,w09,w10 w11,w12,w13,w14,w15 w16,w17,w18,w19,w20; do
  for arm in v3 v4; do
    echo "== batch $batch: $arm"
    for attempt in 0 1 2 3; do
      if [ $attempt -gt 0 ]; then
        n=$(cd "${CHECKOUT[$arm]}" && PYTHONPATH="${CHECKOUT[$arm]}" "$PY" $S/repeat_outages.py "$OUT/v4-arm-$arm")
        [ "$n" = "0" ] && break
        echo "repeat outages moved: $n (repeat $attempt)"
      fi
      wait_codex
      run_arm $batch $arm
    done
  done
done
date "+%Y-%m-%dT%H:%M:%S" > "$OUT/v4.finished"
for arm in v3 v4; do
  echo "== grade $arm"
  for pass in 1 2 3; do  # a grade the grader couldn't produce (an outage) is dropped and asked again
    "$PY" -c "import json,sys,pathlib; [p.unlink() for p in pathlib.Path(sys.argv[1]).glob('*.json') if json.loads(p.read_text()).get('grader_ok') is False]" "$OUT/v4-arm-$arm/grades" 2>/dev/null
    wait_codex
    "$REPO/factory/.venv/bin/factory" replay grade --cases "$CASES" --repos "$REPOS" --out "$OUT/v4-arm-$arm" --jobs 2
  done
  "$REPO/factory/.venv/bin/factory" replay report --cases "$CASES" --out "$OUT/v4-arm-$arm" --pass-mark "$REPO/factory/calibration/realbugs/pass-mark-v2.yaml" --title "v4, arm: $arm (2 trials; pass^k read at k = 2)" > /dev/null
done
echo "exit $?"
