# Signing off AI-written code without reading every line

> I'm a product manager and consultant, not a developer. I was curious what kind of software factory could be built
> from open sources (public domain, MIT, Creative Commons and the like) on what good-quality, AI-built software looks
> like. This is what I came up with. I directed it, and I signed off its one real change from the sign-off sheet,
> without reading the code.
>
> *Chris Gagné*

**An experiment, built by AI and open for critique.** Claude (Anthropic) wrote nearly all of it, with OpenAI's Codex
reviewing, grading and picking test cases. It asks whether whoever signs off a change can rely on evidence instead of
reading every line, and every test of it was written down before it ran.

## The short version

- **Its AI review hasn't beaten the labs' own tools.** On GitHub's open benchmark, the factory's default review found
  less than OpenAI's `codex review` and Claude Code with a plain review prompt, run together; with its Claude reviewer
  plus those two as its reviewers, it came out level with them. It found two to three times as much as PR-Agent, an open-source reviewer.
- **With one model, its brief and library helped OpenAI's model and not Anthropic's.** Neither model found more serious
  bugs with them.
- **What it adds is the rest of the gate:** locked tests, sandboxed checks, a sign-off sheet for someone who doesn't
  read code, and a log.
- **Several stops on "good" changes were real changes in behaviour** that upstream had accepted. Making each stop
  quick for a non-coder to judge is the open problem.

## What it does

1. **Tests come first and get locked.** An AI turns the request into numbered acceptance criteria and a test for each.
   The factory checks the project's tests pass before the new ones are added and fail once they are, then locks them
   so the AI building the change can't edit them.
2. **The usual checks run:** the project's tests and commands, sandboxed, plus secret, dependency and code scanners. A
   test command passes on its exit code; the factory doesn't check which tests actually ran.
3. **AI reviewers from Anthropic and OpenAI review separately**, each in a fresh session told to stay blind to the
   others (Codex can still read the disk, so its blindness rests on the instruction). By default they get the factory's brief
   and, optionally, its library; Claude Code with a plain prompt and `codex review` can be added. A further AI sorts
   the findings and can't wave through a serious one.
4. **You get a sign-off sheet** in plain words: what was asked for, which checks passed, what you must decide, what's
   left over. You sign, or send it back in your own words. The factory never signs for you.

Every step lands on a tamper-evident log. [DESIGN.md](helpers/factory-warranty/DESIGN.md) says what it guarantees and
what it can't, such as whether the tests check the right behaviour.

## How its review compares

Three tests on [ReviewBench](https://github.com/review-bench/ReviewBench), GitHub's open benchmark of real pull
requests, scored offline by its own judge. *Recall* is how much of the answer key a reviewer found; *precision* is, of
its findings that match the key, the share that match a real issue (both averaged over pull requests). An arm counts as
better only if neither is lower and one is at least 5 points higher.

**On the 25-pull-request test set** ([results](helpers/factory-warranty/calibration/realbugs/results/v5-RESULTS.md)):

| | Precision | Recall | Serious found (of 36)\* |
|---|---|---|---|
| `codex review` + Claude Code with a plain prompt | 87.2% | 50.8% | 25 |
| The factory's default two reviewers, with its brief and library | 85.5% | 35.5% | 19 |
| PR-Agent | 81.5% | 14.4% | 8 |

\*Counted after the fact.

**On 20 fresh pull requests**, with the vendors' review modes added to the factory
([results](helpers/factory-warranty/calibration/realbugs/results/v6-RESULTS.md)):

| | Precision | Recall |
|---|---|---|
| The factory's three reviewers, every original finding pooled | 80.6% | 64.1% |
| Claude Code with a plain prompt twice, plus `codex review` | 80.2% | 62.1% |
| Claude Code with a plain prompt, plus `codex review` | 81.3% | 56.9% |
| PR-Agent | 83.3% | 19.0% |

No arm beat another by the rule. A third review of any kind added a few points of recall and nearly doubled what
someone has to read. The sample held only 3 serious findings, all found by every arm.

**With one model**, on 23 fresh pull requests chosen because they contain serious findings
([results](helpers/factory-warranty/calibration/realbugs/results/v7-RESULTS.md)):

| Model | Reviewing with | Precision | Recall | Serious found |
|---|---|---|---|---|
| Sol | the factory's brief and library | 86.8% | 19.8% | 21 |
| Sol | `codex review` | 84.9% | 14.7% | 22 |
| Opus | the factory's brief and library | 87.2% | 45.1% | 28 |
| Opus | Claude Code with a plain prompt | 87.2% | 49.6% | 29 |

On Sol the factory's version did better; on Opus, about the same. Two factory runs had failed on an unrelated bug and
were re-run under a dated amendment; as first judged, Sol was about the same and Claude Code found 3 more serious bugs.

**For a team:** run `codex review` and Claude Code, and keep everything both say; that did as well as anything we
built, for well under a dollar of Claude per pull request plus Codex. With OpenAI's model alone, a brief and library
like the factory's got more out of it.

**Limits:** one try per reviewer and 20 to 25 pull requests per test (none over 2,000 changed lines in the fresh
samples); an answer key mostly raised by AI reviewers and a Claude judge; PR-Agent in its diff-only local mode; and
Claude Code's own review command untested, only our plain prompt.

## Showing, not arguing

In one test, every stop on a good change came from a jsdiff change where a reviewer named an input that would now
break, and the input worked fine. Someone who doesn't read code can't tell a right argument from a wrong one, so we
built a step where an AI writes a check and the factory runs it before and after the change. On 70 blocking findings
from earlier runs (cases already seen), 58 of the 61 that caught real bugs came out "shown", and so did 7 of the 9 that
stopped good changes, from four changes run repeatedly: for example, a decimal.js build left disagreeing with its source, or a
node-semver file missing from the published package
([results](helpers/factory-warranty/calibration/realbugs/results/REPRO-RESULTS.md)).

The factory judges "shown" from exit codes; that a check tests what the finding names is the checking AI's account,
and where that AI says the code is new, failing after the change alone counts. The
step was meant to clear false stops and failed its rule (it cleared 2 of 10), so it ships as an optional display
instead (`review.reproduce`): the sheet shows each blocking finding's outcome, and blocking doesn't change. Whether that
helps a signer decide faster hasn't been tested.

## Earlier tests

**Does the standards library help?** On 17 real bugs reversed back into eight JavaScript and TypeScript libraries,
reviewers with the library caught 16 on both tries against 11 without, which met the bar we'd set
([results](helpers/factory-warranty/calibration/realbugs/results/v3-RESULTS.md)). Three of the five gains came where
OpenAI's reviewer ran out of time without it; counting only finished reviews it's 16 against 14 (a count that favours
the side without). It cost 2.4 times the Claude review spend, and a third company's model, TypeSafe's Jev, re-graded
the findings to the same totals.

**How often it stops good changes.** In that test, 38% and 44% of runs on good changes ended in a stop, against our bar
of 20%; on fresh cases both the old and a revised factory stopped 2 of 24
([results](helpers/factory-warranty/calibration/realbugs/results/v4-RESULTS.md)), so the rate depends heavily on which
changes you test. If you run AI review in anger, what share of good changes does it stop, and how fast can a signer
tell a wanted change from a bug?

**One change, start to finish.** The factory built one of its own features, a scanner rule. Chris sent it back twice
("Don't claim more than it catches") and signed the third version, which lists what it still misses
([showcase](helpers/factory-warranty/calibration/showcase-2026-10-14/), about $9 of Claude; one config file was edited
afterwards, so its recorded fingerprint no longer matches).

## Limits and proposals

Its rules (what blocks, the 20% false-stop bar) are marked PROPOSED in
[`policy.yaml`](helpers/factory-warranty/factory/policy.yaml), and [conformance/](helpers/factory-warranty/conformance/)
maps it to each standard. Not yet shown: that a non-coder can safely sign from the sheet (one showcase change), and
that the gates catch what reviewers miss (every replay switched the projects' test suites off). It runs on macOS only;
someone with the operator's access could rewrite the log without it showing; a signature is a record, not cryptography; and the commits
showing each test was written first are in the factory's unpublished repository.

Prior art: [`codex-plugin-cc`](https://github.com/openai/codex-plugin-cc) and
[PAL MCP](https://github.com/BeehiveInnovations/pal-mcp-server) have other models review Claude Code's work;
[TDD Guard](https://github.com/nizos/tdd-guard) enforces tests first; [in-toto](https://github.com/in-toto/in-toto)
and [Sigstore](https://github.com/sigstore/cosign) keep signed records of how software was made, with real cryptography.

## The library

Eighteen open sources, each read in full, written up and checked line by line against its source by a Claude agent and
by OpenAI's model: standards and threat lists from NIST, CISA and OWASP; research on AI-assisted development, including
METR's productivity trial, SWE-bench and Google's DORA report; and practice guidance from Cucumber, Microsoft, OpenSSF
and the UK government. It names 29 places where they disagree.

The app ships 17 of them, all licensed for commercial use; the DORA report (CC BY-NC-SA) ships only in
[`apps/factory-warranty-full/`](apps/factory-warranty-full/), for non-commercial use.

## Try it

Needs macOS, Python 3.12+, [uv](https://docs.astral.sh/uv/), Claude Code, the Codex CLI, `gitleaks`, `osv-scanner`
and `semgrep`.

```bash
cd corpus.commons/chrisgagne-agent-built-software/apps/factory-warranty
claude .                                   # ask it what evidence a change needs before you sign it off
uv tool install --editable ./factory       # the harness: `factory run STORY.md --repo PATH`
```

[The factory's README](helpers/factory-warranty/README.md) covers the config: `review.legs` picks the reviewers,
`review.grounding: distillations` gives them the library, and `review.reproduce` (with `review.reproduce_setup` to
install dependencies) adds the check for each blocking finding.

## What's in this folder

| Folder | What it is |
|---|---|
| [`helpers/factory-warranty/`](helpers/factory-warranty/) | The factory, and every test's pre-registration, results and records ([calibration/](helpers/factory-warranty/calibration/)) |
| [`distillations/`](distillations/warranting-agent-built-software/), [`references/`](references/), [`sources/`](sources/) | The library: one write-up per source, the index the reviewers read, and each source's full write-up and licence |
| [`apps/`](apps/) | The factory and library as an app: `factory-warranty` for any use, `factory-warranty-full` (with DORA) non-commercial |

It's a corpus in [grounded-forge](../../README.md), which builds assistants that answer from a fixed set of sources.

## Licence

The code is MIT. Each write-up keeps its source's licence (see [`LICENSE-CONTENT`](../../LICENSE-CONTENT)); DORA's CC
BY-NC-SA makes `factory-warranty-full` non-commercial.
