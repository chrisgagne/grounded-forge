# Signing off AI-written code without reading every line

> I'm a product manager and consultant, not a developer. I was curious what kind of software factory could be built
> from open sources (public domain, MIT, Creative Commons and the like) on what good-quality, AI-built software looks
> like. This is what I came up with. I directed it, and I signed off its one real change from the sign-off sheet,
> without reading the code.
>
> *Chris Gagné*

**An experiment, built by AI and open for critique.** Claude (Anthropic) wrote nearly all of it: the code, these docs
and the library behind it, with OpenAI's Codex as a second reviewer and as the grader.

When AI agents write code faster than a team can review it, code review becomes the queue. This project asks whether
the person who signs off a change can rely on evidence instead of reading every line, and measures how far that gets.

## What it does

A change goes through a harness (we call it the factory) before anyone signs it off:

1. **Tests come first and get locked.** An AI turns the request into numbered acceptance criteria and writes a test
   for each. The factory checks the project's tests pass before the new ones are added and fail once they are, then
   locks them so the AI building the change can't edit them.
2. **The usual checks run.** The project's own tests and commands, sandboxed, plus secret, dependency and code
   scanners.
3. **Two AI reviewers from different companies review it separately.** Claude and OpenAI's model each get their own
   copy of the change in a fresh session. When it's configured to, as in the comparison below, they work from a library
   of 18 open standards and studies on secure software and AI-assisted development (NIST, OWASP, CISA, UK government
   guidance on quality assurance of code, and research).
   A third AI sorts their findings, and can't wave through a serious finding either reviewer raised.
4. **You get a sign-off sheet**, written for someone who doesn't read code, with the evidence after it: what was asked
   for, which checks passed, what you must decide, what's left over. You sign, or send it back in your own words; a send-back goes
   through the tests-first step again before the rebuild. The factory never signs for you.

Every step lands on a tamper-evident log. What it can't promise: that the tests check the right behaviour, or that the
reviewers weren't fooled. [DESIGN.md](helpers/factory-warranty/DESIGN.md) lists what it does and doesn't guarantee.

## One change, start to finish

The factory built one of its own features: a scanner rule that blocks added lines matching listed JavaScript,
TypeScript and Python patterns that run text built at run time (`eval` and its relatives). Chris read each sign-off sheet as a non-coder would. The first
version flagged harmless code, so he sent it back: "It flags fixed text it shouldn't." The second version claimed to
catch `eval` "however reached"; a reviewer showed it didn't, so he sent it back again: "Don't claim more than it
catches." The third version listed what it doesn't catch, and he signed it. The rule's own list still misses two
forms, which the signed sheet records. Along the way the run exposed three bugs in the factory itself, each fixed
with a test. Cost: about $9 of Claude and 214,000 Codex tokens over five runs. The log and the signed sheet are in
[the showcase](helpers/factory-warranty/calibration/showcase-2026-10-14/). It ran before this library existed, with
the lighter summary as the reviewers' grounding, and its config was edited afterwards to point here, so the hash the
log recorded for that one file no longer matches; the log's chain and the signature still check out.

## Does the standards library help the reviewers?

We set ourselves a test that could have killed the idea: if reviewers with the library don't catch more bugs than the
same reviewers without it, the library is shelf material.

The first try was too easy to tell anything. On 10 planted bugs, the review caught 10 without the library, 9 with an
early summary of it and 10 with an earlier version of the full library.

So we wrote a harder test down before running it ([the pre-registration](helpers/factory-warranty/calibration/realbugs/PREREG-v3-grounding.md)):
25 real changes from eight JavaScript and TypeScript libraries' history, 17 of them small bug fixes reversed to bring
the bug back and 8 good changes. OpenAI's model picked them, not us. Each was reviewed twice with the library and twice
without. OpenAI's model matched each bug review's findings against the bug's real fix, without knowing which side it
came from; stops on the good changes were counted mechanically.
The library would count as helping only if it caught at least 3 more of the 17 bugs on both tries, while stopping at
most one more good change.

| | Without the library | With the library |
|---|---|---|
| Real bugs caught on both tries | 11 of 17 | **16 of 17** |
| Good changes stopped at least once | 3 of 8 | 4 of 8 |
| Confirmed findings that name a standard, a source or a library row | 0 of 64 | 56 of 82 (68%) |
| Review cost per review (one of the two per change; review only; Codex tokens exclude cached input) | about $0.27 of Claude and 25,000 Codex tokens | about $0.64 of Claude and 42,000 Codex tokens |

**The test was met as written:** 5 more bugs caught on both tries, and one more good change stopped, which the rule
allowed (that stop came from a scanner, not the reviewers).

**But it's weaker than that headline.** In three of those five, the review without the library caught the bug once,
and on the other try OpenAI's reviewer ran past its 30-minute time limit and was stopped, so the factory stopped the
change without naming the bug. Without the library that reviewer hit the limit five times in 50 reviews; with it, once.
Without the library it read around the code base for longer, which may be the library's real effect here: focus,
showing up as finishing in time. Counting only reviews that finished, it's 16 against 14,
a gap of 2, under the bar we set. (That count isn't the rule we registered: it lets three cases count on one finished
review where the library side needed two.) Whether a longer time limit would close that gap, these 100 reviews can't
tell.

Other limits: 17 bugs is a small sample, and two tries per change is an easier bar than three. The project's own test
suites were switched off, so this measures the review step, not the whole factory. No human has checked the AI
grader, which also picked the cases and is one of the two reviewers; a model from a third company, TypeSafe's
Jev, graded every finding again and agreed on every count in the table. A finding that names a standard may still name
the wrong one. And the timestamps showing the test was written before it ran sit in the factory's history from before
it was published, not in this repository. Full results:
[v3-RESULTS.md](helpers/factory-warranty/calibration/realbugs/results/v3-RESULTS.md).

## How often it stops good changes

**We don't know yet, and it's the question we'd most like help with.** In the test above, 38% and 44% of the runs on
good changes (6 and 7 of 16, without and with the library) ended in a stop, against our own bar of 20%. Six of the
stops on each side came from review, mostly reviewers' findings and, in three runs across both sides, a reviewer that
hit its time limit; the seventh with the library came from a scanner. Some flags were arguably right (one change
updated a library's source but not its committed minified build), but those changes were picked as good, so they count
against us. For whoever signs off, every false stop is time spent reading a sheet and clearing it.

So we changed the factory: reviewers get more time and one retry, a serious finding must name the input that now goes
wrong, a stale generated file counts as minor, and a scanner check that errors is measured again. Then we tested the old and new versions on 20 changes neither
had seen, 12 good and 8 bugs, with the rule written down first
([the pre-registration](helpers/factory-warranty/calibration/realbugs/PREREG-v4-false-stops.md)).

**Round two's changes didn't measurably cut false stops without costing catches.** There was little to cut: each
version stopped 2 of 24 runs on the good changes (8%), both on the same change, and both caught the same 7 of 8 bugs on
both tries. So the stop rate depends on which changes you test more than our small samples can pin down. Full results:
[v4-RESULTS.md](helpers/factory-warranty/calibration/realbugs/results/v4-RESULTS.md).

All four stops were one change to the jsdiff library, titled "Remove dead code". Each time a reviewer called it
critical and named the input that would now break. We ran that input through the code before and after the change:
it works the same, because jsdiff's parser adjusts the line number before the deleted code would matter; only a
patch object built by hand reaches the difference. Asking
reviewers to name the trigger made the finding look evidenced without making it right.

If you run AI code review in anger: what share of good changes does it stop, and what brought that down without
letting real bugs through? That's the conversation we'd most like to have.

The scanner also gave different answers on two runs of the same change once, most likely because it downloads its
rules fresh each run. Pinning them is on the list.

## What's still a proposal

The factory's rules (when a finding blocks, when the sheet recommends a qualified second person, and the targets a
replay is reported against, such as the 20% false-stop bar) are in
[`policy.yaml`](helpers/factory-warranty/factory/policy.yaml), each marked PROPOSED with who set it. The library
comparison's own rule is in its pre-registration. Several draw on the sources (for example NIST SP 800-218A: no AI model alone in the path of a
significant security decision); the thresholds and categories are design choices. The second-person rule is advice
on the sheet; the factory doesn't check that the second review happened. [conformance/](helpers/factory-warranty/conformance/)
says, standard by standard, what is shown by a test, what is only asserted, and what is a gap.

Other limits: macOS only (it sandboxes with `sandbox-exec`); Codex's separation from the other reviewer is by
procedure, since its read-only sandbox can still read the disk; the log shows tampering by the agents or by accident, but
someone with the operator's own access could rewrite it and its anchor together; and a signature is a record, not a
cryptographic signature.

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

The sources don't always agree, and the library names 29 places where they disagree, pull against each other or speak
to different roles. One direct disagreement: the Duck Book calls hallucination in language models inevitable, while
*Why Language Models Hallucinate* argues it persists because evaluations reward guessing, which can change. The
assistant in the app is told to say so when a disagreement matters; the factory's reviewers aren't yet.

## Try it

Needs macOS, Python 3.12+, [uv](https://docs.astral.sh/uv/), Claude Code, the Codex CLI, `gitleaks`, `osv-scanner`
and `semgrep`.

```bash
tar -xzf distros/factory-warranty-v0.4.0-open-nc.tar.gz
cd factory-warranty
claude .                                   # ask it what evidence a change needs before you sign it off
uv tool install --editable ./factory       # the harness: `factory run STORY.md --repo PATH`
```

To review with the library, as in the test above, set `review.grounding: distillations` and point `axis_index` at the
library's index (the example config uses a lighter summary). [The factory's README](helpers/factory-warranty/README.md)
has the commands and the config.

## What's in this folder

| Folder | What it is |
|---|---|
| [`helpers/factory-warranty/`](helpers/factory-warranty/) | The factory: code, tests, design, the standards mapping ([conformance/](helpers/factory-warranty/conformance/)) and the measurement reports ([calibration/](helpers/factory-warranty/calibration/); per-review records for the test above) |
| [`tasks/`](tasks/warranting-agent-built-software.md) | The job the library is organised around, "warranting agent-built software", in eight stages of a change's life |
| [`distillations/`](distillations/warranting-agent-built-software/) | One write-up per source, aimed at that job, and the index the reviewers read: 271 trigger-and-response rows and the 29 disagreements |
| [`references/`](references/), [`sources/`](sources/) | Each source's full write-up, its converted text, its licence and its check log |
| [`apps/factory-warranty/`](apps/factory-warranty/), [`distros/`](distros/) | The write-ups, the indexes and the factory built into one app, and its download |

This folder is a corpus in [grounded-forge](../../README.md), which builds assistants that answer from a fixed set of
sources rather than from memory. In its terms: a *corpus* is the set of sources; a *distillation* is one source
written up for one job; the job is a *task axis*; and *grounding* is which part of the library a reviewer is given.

## Licence

The code is MIT. Each write-up inherits its source's licence (public domain, OGL, CC BY, CC BY-SA, MIT, and CC
BY-NC-SA for the DORA report, which makes the packaged app non-commercial as a whole); see
[`LICENSE-CONTENT`](../../LICENSE-CONTENT) for the table.
