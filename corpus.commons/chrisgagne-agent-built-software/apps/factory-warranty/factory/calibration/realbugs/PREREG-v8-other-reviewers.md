# Pre-registration v8: does the factory's Claude reviewer beat brooks-lint and Claude Code's own `/code-review`?

**Status:** approved by Chris Gagné (2026-10-20: "I think 2 is kinda interesting?", choosing to run both tools on v6's
pull requests) and in effect from the commit that adds it, before any trial runs. Nothing below may change after that
commit; a later change is a dated amendment that judges only later runs.

## Why

v5 to v7 compared the factory with PR-Agent, OpenAI's `codex review` and Claude Code with a plain review prompt. Two
reviewers a reader will ask about were left out:

- **brooks-lint** (github.com/hyhmrright/brooks-lint, MIT, v1.8.0, commit `c85f65e`), the open-source reviewer closest
  to the factory's idea: Claude reviewing against a library of classic engineering books, with each finding citing its
  source. It had about 1,500 GitHub stars on 2026-10-20 (`prior-art-2026-10-20.md`).
- **Claude Code's own `/code-review`** (built into Claude Code 2.1.288), Anthropic's review command, which v5 to v7
  replaced with a plain prompt.

Both run on Claude, so this needs no Codex.

## Sample

v6's 20 pull requests (`v6-cases.json`, drawn by `pick_v6.py`). Neither tool has run on them, and nothing in either
tool's set-up below was chosen from them. They aren't fresh to the operator: v6's arms were judged on them, and the
factory's design since then (v7's fix for many locked files) touches nothing these arms run.

## Arms (one trial each, all Claude Opus 5.5, Claude Code's default model, recorded)

| Arm | What runs |
|---|---|
| `brooks` | New run. brooks-lint's Claude Code plugin at `c85f65e` (`--plugin-dir`), command `/brooks-lint:brooks-review Review this branch's changes against main (git diff main...HEAD).` Its report is parsed by brooks-lint's own `scripts/report-parse.mjs`; each finding's message is its title, Symptom, Source, Consequence and Remedy as written. |
| `cc-review` | New run. Claude Code's built-in `/code-review`, no arguments. Findings are what it hands its `ReportFindings` tool (the last call, if it calls more than once), each message its summary and failure scenario; if it never calls the tool, the JSON array or list in its final message. |
| `factory-claude` | No new run. The factory's own Claude reviewer from v6's `factory` trials (its brief and the open build's library): every finding with leg `claude`, before the sort. |
| `plain` | No new run. v6's `claude-again` trials: one Claude Code review with the plain prompt. |

v6 judged neither of the last two alone (v6 judged the pooled arms, and its per-leg split was set aside because the
judge credits the first of several matching findings). Here each arm is judged on its own.

**How the new arms run.** Each pull request is checked out as in v6, then branch `main` is set to the change's start
and the remote is removed, since both tools review `main...HEAD` when given no pull request. Neither tool takes the pull
request's title or description when run on a local branch; both see its commits and their messages. Isolation: no
session persistence, no MCP servers, no settings files at all (`--setting-sources ""`, so a reviewed repository's own
`.claude/settings.json` can't add permissions or hooks), hooks off, tools Read, Grep, Glob, Agent, ReportFindings and
Bash limited to `git`, permission mode `dontAsk`, 60 minutes. Each tool reads the repository's CLAUDE.md files itself
where its method says to. A finding with no file a parser can read gets the change's first changed file, line 1; how
many did is reported.

Same judge as v5 to v7: ReviewBench's own `npm run judge` at `12e9d1a` with Claude Sonnet 5, offline.

## What decides it (primary)

The same rule: an arm did better than another only if its grounded precision and grounded recall (the judge's
per-pull-request averages) are each at least as high and one is higher by at least 5 points. Otherwise "about the
same on these pull requests".

Primary: `factory-claude` against `brooks`, and `factory-claude` against `cc-review`. Every other pair is reported
under the same rule.

## Reported, not judged

High-severity golden findings found, per arm; findings per pull request; cost (Claude dollars, judge API credit);
`/code-review`'s self-reported effort level per pull request; how many findings were placed on a fallback file.

**Limits, stated before the run:** 20 pull requests, one trial, offline scores, and only 3 high-severity golden
findings in the sample; the judge is a Claude model and every arm is Claude; brooks-lint is built for maintainability
(its six decay risks) more than for bugs, and ReviewBench's answer key is mostly bugs, so a low score measures fit to
this benchmark, not the tool's worth; `/code-review` is built to flag only what it's sure of, which favours precision
over recall by design; the `factory-claude` and `plain` findings were produced on 2026-10-19, the new arms a day later
on a newer Claude Code.

## Amendment 1 (2026-10-20, before any valid trial): Bash in the sandbox, not limited to `git`

The first 11 `cc-review` trials (rc01 to rc12, rc08 unfinished) ran with Bash limited to commands starting with `git`.
`/code-review` gets its diff with pipelines such as `git diff main...HEAD --stat | tail -5`, which that rule refused,
so it reviewed without seeing the change (four times it reported nothing and said so; elsewhere it guessed from the
latest commit message). That is a harness error, not the tool's verdict. No `brooks` trial had run and nothing had been
judged.

From this amendment, Bash runs in Claude Code's own sandbox (`sandbox.enabled`, `autoAllowBashIfSandboxed`, no
unsandboxed commands): commands may write only inside the checkout and can't reach the network. Everything else is
unchanged. The 11 trials move to `results/v8-cc-review/superseded-runs/`, unjudged, and both arms run in full.
