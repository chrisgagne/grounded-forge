#!/usr/bin/env bash
# Run the four blind Sol judgments in parallel (read-only), then print each verdict.
V=<round>
C=codex
P='Read question.md and rubric.md in this folder, then answer-X.md and answer-Y.md in full. The folder distillations/ holds the source material both answers drew on: check the claims that carry each answer against it (search it with rg, and open the passages you need). Judge the two answers by the rubric. Reply with only a JSON object, no prose around it: {"read": "which files you read in full and which you searched", "scores": {"X": {"grounding": 1-5, "coverage": 1-5, "precision": 1-5, "usefulness": 1-5}, "Y": {"grounding": 1-5, "coverage": 1-5, "precision": 1-5, "usefulness": 1-5}}, "unsupported": {"X": ["claims you could not find support for"], "Y": []}, "better": "X or Y or tie", "reasons": "three to five sentences"}'
for q in Q1 Q2 Q3 Q4; do
  ( "$C" -p ingest exec -s read-only --skip-git-repo-check --ephemeral -C "$V/judge/$q" -o "$V/judge/$q/verdict.json" "$P" < /dev/null > "$V/judge/$q/run.log" 2>&1; echo "$q exit $?" ) &
done
wait
for q in Q1 Q2 Q3 Q4; do
  echo "== $q"
  python3 -c "import json; d=json.load(open('$V/judge/$q/verdict.json')); print('better:', d['better'], '| scores:', d['scores'])" 2>&1 | cut -c1-240
done
