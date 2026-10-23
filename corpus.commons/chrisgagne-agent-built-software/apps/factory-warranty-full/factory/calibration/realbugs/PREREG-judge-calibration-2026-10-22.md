# Pre-registration: a judge that runs on the Claude Code CLI

Dated 2026-10-22, before any trial. The Anthropic API credit this harness judged with is spent, and we are not
topping it up. The question is whether ReviewBench's judge, driven through the `claude` CLI instead of the
Anthropic API, scores the same findings the same way. If it does, the remaining runs can be judged; if it does not,
CLI-judged numbers must not be put beside the API-judged ones.

## What changes

ReviewBench's matcher and classifier each open a session through the pi SDK, which needs an API key. A local
adapter (`scripts/eval/claude-cli-session.ts`, turned on by `REVIEW_BENCH_CLAUDE_CLI=1`) exposes the same session
surface and drives `claude -p` instead. The API path stays the default and is unchanged.

Three differences are known in advance and cannot be removed:

1. The CLI appends the judge's system prompt to Claude Code's own; the SDK session carries only the judge's.
2. Effort stands in for the SDK's thinking level: `low` for the matcher, `medium` for the classifier.
3. The classifier's `read`, `grep`, `find` and `ls` tools become Claude Code's Read, Grep and Glob. It gets no shell,
   as before.

Everything else is held: same judge model (`claude-sonnet-5`), same prompts, same chunking, same scorer, same
findings files. The CLI runs with `--safe-mode`, `--setting-sources ""` and `--strict-mcp-config`, so no CLAUDE.md,
skill, hook, agent or MCP server from this machine or from a reviewed repo reaches the judge.

## The test

Re-judge 5 of the 23 pull requests in v9's `opus-plain` arm (the folder `v7-opus-own`: Claude Code with a plain
prompt), which the API judge already scored. The five are **rd01 to rd05 by file name**, fixed here before their
per-pull-request scores were read: CommunityToolkit/Maui#3181, ComposioHQ/agent-orchestrator#1277, EdV4H/usketch#534,
FreeRTOS/FreeRTOS-Kernel#1379 and Mirkiux/featkit#17, 45 findings between them.

The comparison is against the API judge's own numbers for those same five pull requests, recomputed from its
`per_pr` block as the mean of the five (the same per-pull-request averaging the headline figures use).

**The rule.** The CLI-backed judge may stand in for the API judge if its grounded precision and its grounded recall
are each within 5 points of the API judge's on these five pull requests. Five points is the threshold the
head-to-head rule already uses to call a difference real, so a judge that drifts further than that could invent or
erase a result on its own.

Also recorded, as the thing that decides whether the full set is affordable: the run's reported cost, its
wall-clock time, and the weekly subscription allowance before and after.

## Limits

Five pull requests, one arm, one trial, and the judge is a Claude model judging Claude's findings either way. A pass
says the two judges agree on these five, not that they agree everywhere.
