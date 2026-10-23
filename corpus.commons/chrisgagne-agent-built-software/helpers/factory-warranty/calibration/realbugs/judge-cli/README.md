# Judging on the Claude Code CLI

ReviewBench's judge talks to the Anthropic API through the pi SDK, which needs an API key. These two files run the
same judge through the `claude` CLI instead, so it can be driven by a Claude subscription. Pre-registered in
`../PREREG-judge-calibration-2026-10-22.md`; the calibration result is in `../results/cal-RESULTS.md`.

To apply, against ReviewBench at commit `12e9d1a`:

```sh
cp claude-cli-session.ts <reviewbench>/scripts/eval/claude-cli-session.ts
git -C <reviewbench> apply wire-in.patch
```

`wire-in.patch` moves each of the two SDK session set-ups into a helper of its own and adds the branch that picks
the adapter instead. With `REVIEW_BENCH_CLAUDE_CLI` unset, nothing changes: the API path is still the default.
Run it with `../runner-v5/judge_cli.sh <results-folder>`.

The adapter exposes the part of the SDK's session surface the matcher and the classifier use (`prompt`, `messages`,
`subscribe`, `abort`, `dispose`, `sessionFile`) and spawns one `claude -p` per turn, holding the conversation with
`--session-id` and then `--resume`. `--safe-mode`, `--setting-sources ""` and `--strict-mcp-config` keep this
machine's and the reviewed repo's CLAUDE.md, skills, hooks, agents and MCP servers out of the judge.

Three differences from the API judge are in the adapter's header comment and in the pre-registration. The one to
watch when reading the records: `total_cost_usd` is cumulative over a resumed session, so each turn reports the
difference from the last.
