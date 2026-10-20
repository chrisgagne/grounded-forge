# Signing off AI-written code without reading every line

> I'm a product manager and consultant, not a developer. I was curious what kind of software factory could be built
> from open sources (public domain, MIT, Creative Commons and the like) on what good-quality, AI-built software looks
> like. This is what I came up with. I directed it, and I signed off its one real change from the sign-off sheet,
> without reading the code.
>
> *Chris Gagné*

**An experiment, built by AI and open for critique.** Claude (Anthropic) wrote nearly all of it: the code, these docs
and the library behind it, with OpenAI's Codex as a second reviewer, as a grader and as the picker of test cases.

When agents write code faster than a team can review it, can the person who signs off a change rely on evidence
instead of reading every line? This project builds a harness for that (we call it the factory) and measures it, with
each test's rule written down before it ran.

## The short version

- **Its AI review hasn't beaten the labs' own tools.** On GitHub's open benchmark of real pull requests, the factory's
  default review found less than OpenAI's `codex review` and Claude Code with a plain review prompt, run together. With
  both of those added as reviewers, it came out level with them by the rule we set. It found two to three times as
  much as PR-Agent, a widely used open-source AI reviewer.
- **With one model, the factory's brief and library helped OpenAI's model and not Anthropic's.** On Sol they did
  better than `codex review`; on Opus, about the same as Claude Code with a plain prompt. Neither model found more
  serious bugs with them.
- **What it adds is everything around the review:** tests written first and locked, sandboxed checks, a sign-off sheet
  written for someone who doesn't read code, and a log of every step; and, optionally, an attempt to show each
  blocking finding by running a check before and after the change.
- **Several stops on "good" changes pointed at real changes in behaviour** that upstream had accepted. Telling a wanted
  change from a bug stays the signer's call, and making that quick is the open problem.

## What it does

A change goes through the factory before anyone signs it off:

1. **Tests come first and get locked.** An AI turns the request into numbered acceptance criteria and writes a test
   for each. The factory checks the project's tests pass before the new ones are added and fail once they are, then
   locks them so the AI building the change can't edit them.
2. **The usual checks run.** The project's own tests and commands, sandboxed, plus secret, dependency and code
   scanners. A test command passes on its exit code; the factory doesn't check which tests the runner actually ran.
3. **AI reviewers from Anthropic and OpenAI review it separately**, each in a fresh session, told to stay blind to the
   others' work (Codex's read-only sandbox can still read the disk, so its blindness rests on following that
   instruction). The config picks the reviewers: by default, Claude and OpenAI's model each given the factory's review
   brief (optionally with the library of open standards and studies described below); also available, Claude Code
   with a plain review prompt and OpenAI's own `codex review`. A further AI sorts the findings and can't wave through a
   serious finding a reviewer raised.
4. **You get a sign-off sheet**, written for someone who doesn't read code, with the evidence after it: what was asked
   for, which checks passed, what you must decide, what's left over. You sign, or send it back in your own words; a
   send-back goes through the tests-first step again before the rebuild. The factory never signs for you.

Every step lands on a tamper-evident log. What it can't promise: that the tests check the right behaviour, or that the
reviewers weren't fooled. [DESIGN.md](helpers/factory-warranty/DESIGN.md) lists what it does and doesn't guarantee.

## How its review compares

Three tests, each written down before it ran, on [ReviewBench](https://github.com/review-bench/ReviewBench): GitHub's
open benchmark of real pull requests, scored against findings people checked, by ReviewBench's own judge and the
judge model its leaderboard uses. These are offline scores, not leaderboard entries. *Recall* is how much of the answer
key a reviewer found; *precision* is, of its findings that match something in the answer key, the share that match a
real issue (the key also lists claimed issues its checkers rejected). Both are averages over pull requests. One arm
counts as better than another only if neither measure is lower and one is at least 5 points higher; otherwise the
two are about the same.

**Against what a team could use instead** (ReviewBench's 25-pull-request test set,
[results](helpers/factory-warranty/calibration/realbugs/results/v5-RESULTS.md)):

| | Precision | Recall | Serious findings found (of 36)\* |
|---|---|---|---|
| `codex review` + Claude Code with a plain prompt, pooled | 87.2% | 50.8% | 25 |
| The factory as set by default (two reviewers with its brief and library, then its sort) | 85.5% | 35.5% | 19 |
| PR-Agent | 81.5% | 14.4% | 8 |

\*Counted after the fact. The pooled pair did better than the factory, and both did better than PR-Agent.

The factory's two reviewers, given the same brief, looked for the same things; the other pair's findings barely
overlap. So we added `codex review` and the plain Claude Code prompt as reviewers and tested again on 20 pull requests
nobody here had reviewed ([results](helpers/factory-warranty/calibration/realbugs/results/v6-RESULTS.md)):

| | Precision | Recall |
|---|---|---|
| The factory's three reviewers (its brief on Claude, the plain Claude Code prompt, `codex review`), every original finding pooled | 80.6% | 64.1% |
| The plain Claude Code prompt twice, plus `codex review` | 80.2% | 62.1% |
| The plain Claude Code prompt plus `codex review` | 81.3% | 56.9% |
| PR-Agent | 83.3% | 19.0% |

No arm did better than another by the rule, not even against PR-Agent, whose precision was highest. A third review of
any kind added a few points of recall and nearly doubled what someone has to read; the factory's brief added about
what a second plain review did. These pull requests held only 3 serious answer-key findings, all found by every arm,
so this test says nothing about serious bugs.

**With only one model** (23 fresh pull requests chosen because they contain serious findings,
[results](helpers/factory-warranty/calibration/realbugs/results/v7-RESULTS.md)):

| Model | Reviewing with | Precision | Recall | Serious found |
|---|---|---|---|---|
| OpenAI's Sol | the factory's brief and library | 86.8% | 19.8% | 21 |
| OpenAI's Sol | `codex review` | 84.9% | 14.7% | 22 |
| Claude Opus | the factory's brief and library | 87.2% | 45.1% | 28 |
| Claude Opus | Claude Code with a plain prompt | 87.2% | 49.6% | 29 |

On Sol the factory's brief and library did better; on Opus, about the same. Two of the factory's runs had failed on a
bug unrelated to the review (projects with thousands of test files); we fixed it and re-ran them under a dated
amendment. As first judged, before the re-runs, Sol was about the same, and Claude Code found more serious bugs than
the factory's Opus reviewer (29 against 26).

**What a team can take from this:** run OpenAI's `codex review` and Claude Code with a plain review prompt, and keep
everything both say; that did as well as anything we built, for well under a dollar of Claude per pull request plus
Codex. With OpenAI's model alone, a review brief and library like the factory's got more out of it than `codex review`.
And measure an open-source reviewer against the labs' own tools before adopting it.

**Limits of all three:** one try per reviewer and 20 to 25 pull requests per test; the two fresh samples leave out pull
requests over 2,000 changed lines; ReviewBench's answer key was mostly first raised by AI reviewers, and its judge is a
Claude model, grading findings mostly written by Claude models; PR-Agent ran in its local mode, which sees the diff but
not the repository; and Claude Code's own review command wasn't tested, only our plain prompt run through Claude Code.

## Showing, not arguing

In one test, every stop on a good change came from a single jsdiff change titled "Remove dead code": a reviewer called
it critical and named an input that would now break. That input worked fine; the reviewer had missed that the parser
adjusts the line number first. A person who doesn't read code can't tell a right argument from a wrong one.

So we built a step that makes each blocking finding show its work: a separate AI writes a check and the command to run
it, and the factory runs that command on the code before and after the change. We tried it on 70 blocking findings
from earlier runs ([results](helpers/factory-warranty/calibration/realbugs/results/REPRO-RESULTS.md)), cases already
seen, including the jsdiff change that prompted it:

- **58 of the 61 findings that caught real bugs came out "shown":** a check that passed before the change and failed
  after it. None came out "not shown"; for 3 the step gave no usable answer.
- **7 of the 9 findings that stopped good changes also came out "shown".** The checks found real changes in behaviour:
  a decimal.js change left the shipped minified build disagreeing with its source; a node-semver change left a new
  file out of the published package; a js-yaml change now returns nothing, silently, for a cut-off input. For jsdiff,
  the reviewer's named input was wrong, but two of four checks found that a patch object built by hand now lands a line
  at the end.

The factory decides "shown" from exit codes; whether a check exercises the problem the finding names is the checking
AI's account, recorded beside it; and where the checking AI says the code didn't exist before the change, a check that
fails after it also counts as shown. The
step was meant to clear false stops automatically and failed the rule we set for that (it cleared 2 of 10 stops), so
it didn't go in as designed. It's in the factory now as an optional display instead (`review.reproduce`): the sheet
shows each blocking finding's outcome, and blocking doesn't change. Whether that display helps a signer decide faster
hasn't been tested.

## How often it stops good changes

**We don't know yet, and it's the question we'd most like help with.** In the first library test (below), 38% and 44%
of the runs on good changes ended in a stop, against our own bar of 20%. We changed the factory (more time for
reviewers; reviewers instructed that a serious finding must name the input that now goes wrong, and that a stale
generated file counts as minor unless the project requires it to change with the code) and tested the old and new versions on 12 good changes neither had seen
([results](helpers/factory-warranty/calibration/realbugs/results/v4-RESULTS.md)): each stopped 2 of 24 runs, both on
the jsdiff change, so the changes didn't measurably help, and the rate depends heavily on which changes you test. On 15
more good changes, the factory stopped 2, the labs' own tools 4 and PR-Agent 7, by our reading of when each would block.

If you run AI code review in anger: what share of good changes does it stop, and how quickly can someone who signs off
tell a wanted change in behaviour from a bug? That's the conversation we'd most like to have.

## Does the standards library help the reviewers?

We set ourselves a test that could have killed the idea: if reviewers with the library don't catch more bugs than the
same reviewers without it, the library is shelf material
([pre-registration](helpers/factory-warranty/calibration/realbugs/PREREG-v3-grounding.md),
[results](helpers/factory-warranty/calibration/realbugs/results/v3-RESULTS.md)). On 25 real changes from eight
JavaScript and TypeScript libraries, 17 of them bug fixes reversed to bring the bug back, each reviewed twice with the
library and twice without, the library side caught 16 of the 17 bugs on both tries against 11, and stopped one more of
the 8 good changes (from a scanner, not the reviewers). That met the bar we set (3 more bugs, at most one more stop).
It cost more: about 2.4 times the Claude review spend and 1.7 times the recorded Codex tokens.

It's weaker than that headline. In three of the five extra catches, the review without the library caught the bug once
and on the other try OpenAI's reviewer ran out of time. Counting only reviews that finished, it's 16 against 14, under
the bar, though that count is lopsided: three cases without the library count on one finished review, where the
library side needed two. A model from a third company, TypeSafe's Jev, graded every bug-review finding again and its grades gave the
same totals; no human has checked the grader. 68% of the confirmed findings with the library named a standard, a
source or one of its rows, against none without it, though naming one doesn't mean naming the right one.

## One change, start to finish

The factory built one of its own features: a scanner rule that blocks added lines matching listed JavaScript,
TypeScript and Python patterns that run text built at run time (`eval` and its relatives). Chris read each sign-off
sheet as a non-coder would. The first version flagged harmless code, so he sent it back: "It flags fixed text it
shouldn't." The second claimed to catch `eval` "however reached"; a reviewer showed it didn't, so he sent it back
again: "Don't claim more than it catches." The third listed what it doesn't catch, and he signed it. The rule's own
list still misses two forms, which the signed sheet records. Along the way the run exposed three bugs in the factory
itself, each fixed with a test. Cost: about $9 of Claude and 214,000 recorded Codex tokens (excluding cached input)
over five runs.
[The showcase](helpers/factory-warranty/calibration/showcase-2026-10-14/) holds the log and the signed sheet. It ran
before this library existed, so its reviewers worked from a lighter summary. One config file was edited afterwards to
point at the library, so the fingerprint the log recorded for that file no longer matches; that affects only that
file, and the log's chain and the signature still check out.

## What came before

Most of the factory's pieces exist elsewhere, open and widely used; what we haven't found is them combined into one
gate and measured against each other on known bugs and good changes. The closest, from their repositories and docs
as of 2026-10-19:

- **A second vendor's reviewer from inside Claude Code:** OpenAI's [`codex-plugin-cc`](https://github.com/openai/codex-plugin-cc)
  (Apache-2.0) and [PAL MCP](https://github.com/BeehiveInnovations/pal-mcp-server) both have Codex or other models
  review Claude Code's work. Neither documents keeping the reviewers blind to each other or a further model sorting
  their findings.
- **AI review of a diff:** [PR-Agent](https://github.com/The-PR-Agent/pr-agent) (MIT, about 13,000 GitHub stars) is a
  widely used open-source AI reviewer, compared above, as was the Codex CLI's `codex review`. Claude Code has its own
  review command, which we didn't test.
- **Tests first:** [TDD Guard](https://github.com/nizos/tdd-guard) (MIT) blocks a coding agent from writing code
  without a failing test.
- **A tamper-evident record of how software was made:** [in-toto](https://github.com/in-toto/in-toto) and
  [Sigstore](https://github.com/sigstore/cosign) do this for supply chains, with real cryptographic signatures, which
  the factory's log doesn't have.
- **Measuring AI review:** [ReviewBench](https://github.com/review-bench/ReviewBench) (GitHub, MIT), used above.

## What's still a proposal, and other limits

The factory's rules (when a finding blocks, when the sheet recommends a qualified second person, and the targets a
replay is reported against, such as the 20% false-stop bar) are in
[`policy.yaml`](helpers/factory-warranty/factory/policy.yaml), each marked PROPOSED with who set it. Each comparison's
own rule is in its pre-registration. Several draw on the sources (for example NIST SP 800-218A: no AI model alone in
the path of a significant security decision); the thresholds and categories are design choices. The second-person rule
is advice on the sheet; the factory doesn't check that the second review happened.
[conformance/](helpers/factory-warranty/conformance/) says, standard by standard, what is shown by a test, what is
only asserted, and what is a gap.

Not yet shown: that a non-coder can safely sign from the sheet (one showcase change), and that the gates catch what
reviewers miss on real changes (every replay switched the projects' own test suites off). Other limits: macOS only (it
sandboxes with `sandbox-exec`); Codex's separation from the other reviewers is by procedure, since its read-only
sandbox can still read the disk; the log shows tampering by the agents or by accident, but someone with the operator's
own access could rewrite it and its anchor together; and a signature is a record, not a cryptographic signature. The
commits showing each test was written before it ran are in the factory's own repository, which isn't published; here
they are files.

## The library

Eighteen open sources, each read in full, written up, and checked line by line against its source by a Claude agent
and, separately, by OpenAI's model. Two are labelled subsets (the Microsoft playbook and the Cucumber docs).

- **Standards and threat lists:** NIST SSDF 1.1 and SP 800-218A, the CISA secure software attestation form, OWASP
  ASVS 5.0, the OWASP Top 10 for LLM applications and for agentic applications (2026), and OWASP's agentic threats and
  mitigations.
- **Research on AI-assisted development:** METR's productivity trial, the Cursor velocity and complexity study,
  SWE-bench, *Why Language Models Hallucinate*, Google's DORA report on AI-assisted development (2025), and
  TestSuiteBench (a 2026 preprint).
- **Practice and assurance guidance:** the Cucumber BDD and Gherkin docs, Microsoft's Code-With Engineering Playbook,
  the UK government's *Quality assurance of code for analysis and research* (the Duck Book) and *AQuA Book*, and
  OpenSSF's guide to finding and fixing vulnerabilities with AI.

The app ships 17 of them, all licensed for commercial use. The DORA report is CC BY-NC-SA, so it ships only in a
separate non-commercial build, [`apps/factory-warranty-full/`](apps/factory-warranty-full/). Its findings still appear,
in our words and cited to the published report, in the three disagreements it's part of.

The sources don't always agree, and the library names 29 places where they disagree, pull against each other or speak
to different roles. One direct disagreement: the Duck Book calls hallucination in language models inevitable, while
*Why Language Models Hallucinate* argues it persists because evaluations reward guessing, which can change. The
assistant in the app is told to say so when a disagreement matters; the factory's reviewers aren't yet.

## Try it

Needs macOS, Python 3.12+, [uv](https://docs.astral.sh/uv/), Claude Code, the Codex CLI, `gitleaks`, `osv-scanner`
and `semgrep`.

```bash
cd corpus.commons/chrisgagne-agent-built-software/apps/factory-warranty
claude .                                   # ask it what evidence a change needs before you sign it off
uv tool install --editable ./factory       # the harness: `factory run STORY.md --repo PATH`
```

Review settings, in `.factory/config.yaml`: `review.legs` picks the reviewers (`claude`, `codex`, `claude-plain`,
`codex-review`); `review.grounding: distillations` with `axis_index` pointing at the library's index gives the factory's
reviewers the library, as in the tests above (the example config uses a lighter summary); `review.reproduce: true` adds
the attempt to show each blocking finding, with `review.reproduce_setup` as the command that installs the project's
dependencies in each copy first (for example `npm ci --ignore-scripts`). [The factory's README](helpers/factory-warranty/README.md) has the commands and
the config.

## What's in this folder

| Folder | What it is |
|---|---|
| [`helpers/factory-warranty/`](helpers/factory-warranty/) | The factory: code, tests, design, the standards mapping ([conformance/](helpers/factory-warranty/conformance/)) and the measurements ([calibration/](helpers/factory-warranty/calibration/): every pre-registration, its results and its per-review records) |
| [`tasks/`](tasks/warranting-agent-built-software.md) | The job the library is organised around, "warranting agent-built software", in eight stages of a change's life |
| [`distillations/`](distillations/warranting-agent-built-software/) | One write-up per source, aimed at that job, and the index the reviewers read: 271 trigger-and-response rows and the 29 disagreements |
| [`references/`](references/), [`sources/`](sources/) | Each source's full write-up, its converted text, its licence and its check log |
| [`apps/factory-warranty/`](apps/factory-warranty/) | The write-ups, the indexes and the factory built into one app, for commercial or non-commercial use; [`apps/factory-warranty-full/`](apps/factory-warranty-full/) adds the DORA report, non-commercial only |

This folder is a corpus in [grounded-forge](../../README.md), which builds assistants that answer from a fixed set of
sources rather than from memory. In its terms: a *corpus* is the set of sources; a *distillation* is one source
written up for one job; the job is a *task axis*; and *grounding* is which part of the library a reviewer is given.

## Licence

The code is MIT. Each write-up inherits its source's licence: public domain, OGL, CC BY, CC BY-SA or MIT in the app,
so a company can use it, and CC BY-NC-SA for the DORA report, which makes `factory-warranty-full` non-commercial as a
whole. The four CC BY-SA write-ups stay CC BY-SA if you adapt them. See
[`LICENSE-CONTENT`](../../LICENSE-CONTENT) for the table.
