#!/bin/zsh
# Judge one arm's findings with ReviewBench's judge (commit 12e9d1a) driven through the Claude Code CLI instead of
# the Anthropic API, per PREREG-judge-calibration-2026-10-22.md. No API key is read or set.
#   judge_cli.sh <results-folder-name>
set -e
ARM=$1; HERE=${0:A:h}; REPOS=${HERE:h:h:h:h}
RB=${RB_ROOT:-$REPOS/ReviewBench}
RUN=$HERE/../results/$ARM
export REVIEW_BENCH_CLAUDE_CLI=1
export REVIEW_BENCH_JUDGE_TIMEOUT_MS=${REVIEW_BENCH_JUDGE_TIMEOUT_MS:-1800000}
mkdir -p "$RUN/scoring"
export REVIEW_BENCH_CLI_COST_LOG=${REVIEW_BENCH_CLI_COST_LOG:-$RUN/scoring/cli-cost.jsonl}
cd "$RB" && PI_CODING_AGENT_DIR=$RB/.judge npm run judge -- --candidate "$RUN/findings" \
  --provider anthropic --model claude-sonnet-5 --output "$RUN/scoring/results.json" --concurrency "${CONC:-2}"
