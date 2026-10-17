#!/bin/zsh
# Pre-registered replay v4 (factory calibration/realbugs/PREREG-v4-false-stops.md): the v3 factory against the round-two
# factory, both with the corpus, 2 trials, interleaved in batches of five cases. Each arm runs from its own pinned checkout.
REPO="<repos>"
PY="$REPO/factory/.venv/bin/python"
OUT="$REPO/factory/calibration/realbugs/results"
CASES="$REPO/factory/calibration/realbugs/v4-cases.json"
REPOS=<scratch>/realbugs/repos
APP="$REPO/grounded-forge/.claude/worktrees/factory-distro/corpus.commons/chrisgagne-agent-built-software/apps/factory-warranty"
export FACTORY_AXIS_INDEX="$APP/distillations/warranting-agent-built-software/WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md"
typeset -A CHECKOUT; CHECKOUT[v3]="$REPO/factory-v3-pinned"; CHECKOUT[v4]="$REPO/factory-v4-pinned"
for arm in v3 v4; do
  mkdir -p "$OUT/v4-arm-$arm"; git -C "${CHECKOUT[$arm]}" rev-parse HEAD > "$OUT/v4-arm-$arm.commit"
  git -C "$APP" rev-parse HEAD > "$OUT/v4-arm-$arm.grounded-forge.commit"
done
date "+%Y-%m-%dT%H:%M:%S" > "$OUT/v4.started"
for batch in w01,w02,w03,w04,w05 w06,w07,w08,w09,w10 w11,w12,w13,w14,w15 w16,w17,w18,w19,w20; do
  for arm in v3 v4; do
    echo "== batch $batch: $arm"
    (cd "${CHECKOUT[$arm]}" && PYTHONPATH="${CHECKOUT[$arm]}" "$PY" -m factory.cli replay run --cases "$CASES" --repos "$REPOS" \
       --out "$OUT/v4-arm-$arm" --trials 2 --jobs 2 --only "$batch" --grounding distillations)
  done
done
date "+%Y-%m-%dT%H:%M:%S" > "$OUT/v4.finished"
for arm in v3 v4; do
  echo "== grade $arm"; "$REPO/factory/.venv/bin/factory" replay grade --cases "$CASES" --repos "$REPOS" --out "$OUT/v4-arm-$arm" --jobs 2
  "$REPO/factory/.venv/bin/factory" replay grade --cases "$CASES" --repos "$REPOS" --out "$OUT/v4-arm-$arm" --jobs 2
  "$REPO/factory/.venv/bin/factory" replay report --cases "$CASES" --out "$OUT/v4-arm-$arm" --pass-mark "$REPO/factory/calibration/realbugs/pass-mark-v2.yaml" --title "v4, arm: $arm (2 trials; pass^k read at k = 2)" > /dev/null
done
echo "exit $?"
