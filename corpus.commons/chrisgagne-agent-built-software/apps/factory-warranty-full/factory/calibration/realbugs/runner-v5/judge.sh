#!/bin/zsh
# Judge one arm's part A findings with ReviewBench's own judge (commit 12e9d1a) and the leaderboard's judge model,
# Claude Sonnet 5, through the Anthropic API. The key is read from ANTHROPIC_ENV and never printed.
#   judge.sh factory|vendors|pr-agent        (v5 part A)
#   judge.sh v6-factory|v6-vendors|v6-control|v6-pr-agent, or any v7-* or v8-* arm
set -e
ARM=$1; HERE=${0:A:h}; REPOS=${HERE:h:h:h:h}
RB=${RB_ROOT:-$REPOS/ReviewBench}; ENVF=${ANTHROPIC_ENV:-$REPOS/grounded-forge/_evals/anthropic.env}
case $ARM in v6-*|v7-*|v8-*) RUN=$HERE/../results/$ARM ;; *) RUN=$HERE/../results/v5-a-$ARM ;; esac
export ANTHROPIC_API_KEY="$(sed -n 's/^[[:space:]]*\(export[[:space:]]*\)\{0,1\}ANTHROPIC_API_KEY[[:space:]]*=[[:space:]]*//p' "$ENVF" | head -1 | tr -d "\"'")"
export REVIEW_BENCH_JUDGE_TIMEOUT_MS=${REVIEW_BENCH_JUDGE_TIMEOUT_MS:-1800000}
mkdir -p "$RUN/scoring"
cd "$RB" && PI_CODING_AGENT_DIR=$RB/.judge npm run judge -- --candidate "$RUN/findings" \
  --provider anthropic --model claude-sonnet-5 --output "$RUN/scoring/results.json" --concurrency 4
