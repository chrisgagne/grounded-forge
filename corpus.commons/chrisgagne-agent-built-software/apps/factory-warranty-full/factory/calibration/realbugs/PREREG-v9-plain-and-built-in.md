# Pre-registration v9: does the factory's brief beat a plain prompt on Sol, and does `/code-review` catch up at higher effort?

**Status:** approved by Chris Gagné (2026-10-21: "knock yourself out", after asking whether the factory's review only
wins by not getting in the way) and in effect from the commit that adds it, before any trial runs. Nothing below may
change after that commit; a later change is a dated amendment that judges only later runs.

## Why

Two gaps in v7 and v8 leave a reader's sharpest question open: does the factory's brief add anything, or does it only
win where the other side gets in the model's way?

- **Sol has no plain-prompt arm.** On Opus, v7 and v8 compared the brief with a plain "review this as a careful
  senior engineer" prompt, and the plain prompt did as well or better. On Sol, v7 compared the brief only with
  `codex review`, OpenAI's sparse built-in mode (about 2 findings per pull request). The brief beat it, but that may
  say more about `codex review` than about the brief.
- **`/code-review` ran at its own level.** In v8, Claude Code's built-in review chose "low" on 14 of 20 pull requests
  and found far less than the plain prompt. It takes a level (`high`, `xhigh`), at which it's meant to report more.

A third gap was found while setting this up: every Sol run so far, the factory's leg and `codex review` alike, ran at
the Codex CLI's default reasoning effort, which its log reports as "none". One secondary arm runs Sol at "high".

## Sample

v7's 23 pull requests (`v7-cases.json`, drawn by `pick_v7.py`: those with at most 2,000 changed lines whose golden set
holds a true high-severity finding). Already used in v7; nothing in the new arms was chosen from them.

## Arms (one trial each)

New:

| Arm | What runs |
|---|---|
| `sol-plain` | Sol (`gpt-6.1-sol`) with the plain prompt v5 to v8 gave Claude Code (`CLAUDE_PROMPT` in `runner-v5/run_v5.py`), run as the factory runs its own Codex leg: `codex exec`, read-only, `--ignore-user-config`, a Codex home holding only the sign-in, no output schema (the Claude plain arm has none), the CLI's default reasoning effort. |
| `sol-plain-high` | As `sol-plain`, with `model_reasoning_effort="high"`. Secondary. |
| `cc-review` | Claude Code's built-in `/code-review`, no arguments, as in v8 (Amendment 1's sandbox). |
| `cc-review-high` | `/code-review high`, otherwise the same. |
| `cc-review-xhigh` | `/code-review xhigh`, otherwise the same. |

From v7, as judged there (no new run): `sol-factory` (Sol with the factory's brief and library), `sol-own` (`codex
review`), `opus-factory` (Opus with the brief and library) and `opus-plain` (Claude Code with the plain prompt; v7's
`opus-own`).

Same judge: ReviewBench's own `npm run judge` at `12e9d1a` with Claude Sonnet 5, offline.

## What decides it (primary)

The same rule: an arm did better than another only if its grounded precision and grounded recall (the judge's
per-pull-request averages) are each at least as high and one is higher by at least 5 points. Otherwise "about the
same on these pull requests".

1. `sol-factory` against `sol-plain`: does the brief beat a plain prompt on Sol?
2. `opus-plain` against each of `cc-review`, `cc-review-high` and `cc-review-xhigh`.

Every other pair is reported under the same rule, including `sol-plain-high` against `sol-factory` and `sol-plain`,
and `cc-review-xhigh` against `cc-review`.

## Reported, not judged

High-severity golden findings found per arm; findings per pull request; cost (Claude dollars, Codex tokens as
recorded, the Codex meter before and after); `/code-review`'s self-reported level per pull request; Sol's reported
reasoning effort per run.

**Limits, stated before the run:** 23 pull requests, already used in v7, one trial, offline scores; the judge is a
Claude model; the v7 arms ran a day earlier on earlier CLI versions; Claude Code's own effort for the plain arm and
`/code-review` is the CLI's default, not set here.

## Amendment 1 (2026-10-21, after v9's results, before this arm runs): `codex review` at "high"

v9 ran Claude Code's `/code-review` at three levels but OpenAI's `codex review` only at its default, so the grid
can't say whether `codex review` is held back by its default effort the way `/code-review` was. Chris approved
running it (2026-10-21).

One new arm on the same 23 pull requests: `codex-review-high`, OpenAI's `codex review` exactly as v7's `sol-own`
(same Codex home, same title, same parser) with `model_reasoning_effort="high"`. Judged the same way, it is compared
by the same rule against `sol-own` (`codex review` at its default), `sol-plain-high` (Sol, plain prompt, "high") and
`sol-factory` (Sol with the factory's brief). These comparisons were chosen after seeing v9's other results; they are
reported as such, and nothing already reported changes.
