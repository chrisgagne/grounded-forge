# Pilot: Methodical's work review as a ReviewBench arm (3 pull requests)

**Status:** approved by Chris Gagné (2026-10-22, relayed from the main thread: "go on the 3-PR Methodical pilot") and
in effect from the commit that adds it, before any pilot run. A pilot, not a test: it finds out whether Methodical's
review can run faithfully as a benchmark arm, what it costs and what has to be decided with its author before a full
run. Nothing here is judged; ReviewBench's judge needs API credit, which is exhausted.

**Added 2026-10-22, after the pilot ran:** the three runs were judged after all, by ReviewBench's judge driven
through the Claude Code CLI (`judge-cli/`), against v9's plain-prompt arm on the same three pull requests judged the
same way. That judge misses its own calibration rule against the API judge (`results/cal-RESULTS.md`), so the
pilot's scores read against each other and against nothing else. Results: `results/pilot-methodical-RESULTS.md`.

## What runs

[Methodical](https://github.com/BigLeverVentures/methodical-gated-engineering) 0.11.0 at
`d2c1b3cd48aada915fa2d4fc3cd5d820cbc4667b` (MIT, Christopher B. Myers), its Claude Code plugin loaded for the run with
`--plugin-dir plugins/methodical`, so its own hooks print the routing table and route each seat.

Its `work-review` skill, invoked as `/methodical:work-review`, on a checkout where `main` is the pull request's base and
HEAD its head (as v8's `/code-review` arm), with this request:

> Review this branch (base: main; the change is `git diff main...HEAD`). The plan is waived. The user's request,
> verbatim: «{title and body of the pull request}». This is a review-only run for an offline benchmark: run the review
> round once, with every seat the seat selection calls for; don't run the project's tests (its dependencies aren't
> installed), and don't fix, commit, push or go on to compound. When the round is done, print the seat lines, then end
> with ONLY a JSON array of every finding the seats raised, material or not, one object per finding:
> {"file", "start_line", "end_line", "severity", "seat", "message"}.

**Where that departs from Methodical as designed, and why:**

- **No tests first.** Its step 3 runs every project test before any seat; the benchmark checkouts have no
  dependencies installed. (v5–v9 ran every arm without tests.)
- **One round, no fixes.** Its review is a correction cycle that fixes material findings and re-reviews; a benchmark
  reviews a fixed change, so the first round's findings are what's scored.
- **No North Star.** The brief names the plan's North Star; these repositories have none and the plan is waived, so the
  North Star seat has only the pull request's description to judge against.
- **Escalation `none`.** A waived plan reads as `none` (seat-selection.md), so no backstop review runs.
- **The JSON list at the end** is ours, so the findings can be scored.

**Effort, stated:** the parent session runs at Claude Code's default effort, as v7's plain Claude Code arm did.
Methodical's hooks route the seats by role; its documented baseline is Opus at medium for the deciding seats
(code-grounded, rigor, each stack's correctness seat) and Sonnet at medium for the worker and census seats (simplicity,
North Star). The pilot records what each seat actually ran on.

**Isolation (v8's recipe, one change):** `--setting-sources ""` (the reviewed repository's own `.claude/settings.json`
and hooks don't load), `--strict-mcp-config`, `--no-session-persistence`, permission mode `dontAsk`, Bash only inside
Claude Code's sandbox. The change: hooks are **not** disabled, because Methodical's routing runs in its plugin hooks;
with project settings excluded, the plugin's are the only hooks that load. Tools: Read, Grep, Glob, Bash, Agent, Skill.

## Sample

The first three pull requests of v7's sample (`v7-cases.json`, chosen for serious golden findings, already reviewed by
v7's and v9's arms): rd01 (CommunityToolkit/Maui, C#), rd02 (ComposioHQ/agent-orchestrator, TypeScript), rd03
(EdV4H/usketch, TypeScript).

## What's reported

For each pull request: whether the run completed, the seat lines (seats, models, efforts), whether the routing hook
fired, findings and findings per seat, Claude cost and minutes from the run's own result, and every harness problem.
Nothing is judged and no comparison is claimed; the full run's comparison would be against v7's plain Claude Code arm
on all 23 pull requests at the same stated efforts.

## Result, 2026-10-22 (not judged)

All three runs completed, with no timeouts, no unreadable output and every finding naming a file. Methodical's own
routing hook loaded and printed its table (session Sonnet high pinned as its recommendation; decider Opus medium;
worker and census Sonnet medium; backstop Fable high); the parent session ran on Claude Code's default, Opus.

| | rd01 (C#) | rd02 (TypeScript) | rd03 (TypeScript) |
|---|---|---|---|
| Seats (as its seat lines report) | North Star (Sonnet medium), code-grounded, rigor, generic correctness "no C# lens" (Opus medium), simplicity (Sonnet medium) | the same, with typescript-correctness | the same, with typescript-correctness |
| Findings | 54 | 29 | 33 |
| Claude cost, minutes | $3.85, 6.6 | $2.02, 2.9 | $2.05, 2.9 |
| v7's plain Claude Code on the same PR: findings, cost | 14, $0.70 | 6, $0.41 | 8, $0.47 |

About 4–5 times the findings and the cost of a plain Claude Code review; whether they're better findings needs the
judge. Full 23-pull-request run: about $60 of Claude at this rate, no Codex.

Harness notes: seats labelled their severities in two vocabularies (low/medium/high on rd01 and rd03; Methodical's
material/minor/nit on rd02); ReviewBench doesn't score severity, but a full run's report should map them. The seat
lines' models and efforts are what the orchestrator printed and the Agent calls requested; Claude Code's result
reports models and cost but not each seat's effort.
