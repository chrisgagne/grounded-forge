# Pre-registration v5: how does the factory compare with open prior art?

**Status:** approved by Chris Gagné (2026-10-19: the plan, about 45% of a week's Codex allowance, and ReviewBench as
the main comparison) and in effect from the commit that adds it, before any ReviewBench pull request is reviewed,
before Sol picks any project or case, and before any trial runs. Nothing below may change after that commit; a later
change is a dated amendment that judges only later runs.

## Why

The factory has only been compared with itself (with and without its library; v3 against round two). A startup
choosing a starting point would compare it with what it could use instead. A prior-art survey (2026-10-19) found no
open tool doing the factory's whole pipeline, and two credible things to compare against: the model vendors' own
reviewers, used bare, which a startup already pays for; and PR-Agent, the most used open-source AI reviewer (MIT).

Two questions, two parts:

- **A. Does it find what a good reviewer would find?** On a benchmark nobody here chose: the 25-pull-request test set of
  ReviewBench (GitHub, MIT), scored by its own judge against its human-reviewed golden findings.
- **B. Does it leave good changes alone?** ReviewBench can't say: every pull request in it has findings. So 15 good
  changes from real project history, picked by Sol, and whether each arm would stop them.

## Arms (both parts)

| Arm | What runs | Models | What counts as a stop (part B) |
|---|---|---|---|
| `factory` | The factory as in v3 and v4 (the project's own tests switched off), at the commit recorded in `results/v5-factory.commit` before the first trial, grounded in the open (17-source, no-DORA) build of the library | Claude + Sol, as configured | Its own gate: any blocking finding or gate failure |
| `vendors` | OpenAI's `codex review` and Claude Code, each reviewing the same checkout separately, findings pooled | Sol + Claude Code's default model (recorded) | Any Codex finding at P0 or P1, or any Claude finding at its top severity |
| `pr-agent` | PR-Agent `v0.48.0`, `review` tool, plain-diff mode, default configuration except the model | Claude via the Anthropic API (model recorded) | Any "key issue to review" or security concern |

Before the first trial the operator commits in `runner-v5/` the exact command, version and configuration for each arm,
and the converter from each arm's output to ReviewBench's findings format (file, start and end line, message). Every
arm gets the same inputs: the checkout at the change's head, the diff from its base, and for ReviewBench the pull
request's title and body (which ReviewBench gives every reviewer). In part B the story is the neutral "A contributor's
change to <project>. Review it before it merges." If an arm can't be made to run headless, that is recorded and it is
reported without; no other arm changes.

Every arm reports all its findings to ReviewBench, at every severity. The factory runs as it would ship: two changes
are in development (a reproduction step for blocking findings, and a review brief that also reports maintainability,
performance, documentation, accessibility and API-design findings, never as blocking). Each goes in only if its own
check, written down before it runs, passes; the factory commit is then fixed before the first trial here.

## Part A: ReviewBench

- **Pull requests:** the 25 in `corpus/test/test.json` at ReviewBench commit `12e9d1a`, checked out from the
  review-bench mirrors at each pull request's head.
- **Trials:** 2 per arm, unless the cost probe below projects the `factory` arm's two trials at more than 25% of a
  week's Codex allowance; then 1 per arm, for every arm.
- **Cost probe:** before any test-set pull request runs, the `factory` arm reviews one pull request from the full set
  that is not in the test set, chosen as the first full-set pull request over 1,000 changed lines in manifest order.
  Development only; never scored.
- **Judging:** ReviewBench's own `npm run judge`, at commit `12e9d1a`, with the leaderboard's judge model, Claude Sonnet
  5, through the Anthropic API. These are offline scores: ReviewBench says they can't be published as leaderboard
  scores, and they're reported as offline scores.
- **Measures:** grounded precision and grounded recall per arm (ReviewBench's definitions), the mean of the trials,
  plus recall on high-severity golden findings and the review time per pull request.

## Part B: good changes

- **Cases:** picked by Sol (gpt-6.1-sol) in two steps, with briefs committed before each: `pick-v5-projects.md` (four
  JavaScript or TypeScript libraries not used before), then `pick-v5.md` (15 CONTROL cases: at most 2 from any one of
  the twelve projects, at least 5 from the four new ones, none of the commits in `used-commits-v5.txt`, same rules for a
  clean change as v4). The operator clones the four projects and checks only that each case applies.
- **Trials:** 2 per arm. **Measure:** good-change trials stopped (of 30), by each arm's stop rule.
- Outages: Amendments 1 and 2 of v4 apply.

## What's reported (primary)

A table per part, as measured. The README may say one arm did better than another only where:

- **A:** its grounded precision and its grounded recall are each at least as high, one of them higher by at least 5
  points, in every trial;
- **B:** it stopped at least 4 fewer of the 30 good-change trials.

Otherwise it says "about the same on these pull requests" or "these changes".

**Limits, stated before the run:** 25 pull requests and 15 good changes are small samples. ReviewBench's golden
findings were mostly first raised by AI reviewers and labelled with a Claude classifier, and its judge is a Claude
model; Sol picks part B's cases and is a model in two arms. The other arms have no pass/fail gate of their own, so part
B's stop rules for them are our reading of their output; their findings are also reported without the rule.

## Reported, not judged

- Cost per arm: Claude dollars (API credit for `pr-agent` and for judging), Codex tokens with and without cached input,
  minutes per review.
- Findings per pull request and per change, and their severity mix, per arm.
- Review legs that ran out of time, per arm.

## Amendment 1, 2026-10-19, after the cost probe, before any part A or part B trial

Codex is on a smaller plan than when this was written (Plus, not Pro). The cost probe (`results/v5-probe/`) put one
large pull request at about 0.9% of a week, so part A runs 1 trial per arm, as the rule above already says. To keep the
whole comparison near 45% of a week, **part B also runs 1 trial per arm**: good-change trials stopped are counted of
15, not 30, and the bar for saying one arm stopped fewer becomes at least 3 fewer of the 15. Cases, arms and part A are
unchanged. No trial of either part had run.
