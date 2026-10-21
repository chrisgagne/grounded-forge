# Signing off AI-written code without reading every line

> I'm a tech-savvy product manager and consultant, but I've rarely been held responsible for warranting software the
> way a professional developer is. I wanted to see what software factory could be built from open sources (public
> domain, MIT, Creative Commons and the like) on what good AI-built software looks like. I directed this one, and
> signed off its one real change from the sign-off sheet without reading the code. A naïve junior developer like me
> can now build review tooling that beats PR-Agent (the most-starred open-source AI reviewer we found), brooks-lint and
> Claude Code's own `/code-review`. It adds little if you already ask Claude Code for a plain review and run
> `codex review` beside it, though on OpenAI's model alone it found more than `codex review`. What it adds is the rest:
> locked tests, a sheet I could sign from, and a record of what was and wasn't shown.
>
> *Chris Gagné*

**An experiment, built by AI and open for critique.** Claude wrote nearly all of it, with OpenAI's Codex reviewing,
grading and picking test cases. Every test was written down before it ran.

## The short version

- **Its review hasn't beaten `codex review` and Claude Code with a plain prompt, pooled.** With those two added as
  its reviewers, it came out level.
- **It beat the other reviewers we tried,** with two to three and a half times the recall of PR-Agent, brooks-lint
  (Claude reviewing against twelve engineering books) and `/code-review`.
- **On OpenAI's model its brief and library beat `codex review`; on Anthropic's, a plain prompt did as well or
  better.** We haven't yet tried a plain prompt on OpenAI's model. Neither model found more serious bugs with them.
- **Several stops on "good" changes were real changes in behaviour** that upstream had accepted. Making each stop
  quick for a non-coder to judge is the open problem.

## What it does

1. **Tests come first and get locked.** An AI turns the request into acceptance criteria and a test for each; the
   factory checks they fail before the change, then locks them so the AI building it can't edit them.
2. **The usual checks run**, sandboxed: the project's tests and commands, plus secret, dependency and code scanners. A
   test command passes on its exit code; the factory doesn't check which tests ran.
3. **Reviewers from Anthropic and OpenAI review separately**, each in a fresh session told to stay blind to the others
   (Codex can still read the disk, so its blindness rests on the instruction). They get the factory's brief and,
   optionally, its library; Claude Code with a plain prompt and `codex review` can be added. A further AI sorts the
   findings and can't wave through a serious one.
4. **You get a sign-off sheet** in plain words: what was asked, what passed, what you must decide. You sign or send
   it back; the factory never signs for you.

Every step lands on a tamper-evident log; [DESIGN.md](helpers/factory-warranty/DESIGN.md) says what it can and can't
guarantee.

## How its review compares

Four tests on [ReviewBench](https://github.com/review-bench/ReviewBench), GitHub's open benchmark of real pull
requests, scored offline by its own judge. *Recall* is how much of the answer key a reviewer found; *precision* is, of
its findings that match the key, the share that match a real issue (both averaged over pull requests). An arm counts as
better only if neither is lower and one is at least 5 points higher.

**On the 25-pull-request test set** ([v5](helpers/factory-warranty/calibration/realbugs/results/v5-RESULTS.md)):

| | Precision | Recall | Serious found (of 36)\* |
|---|---|---|---|
| `codex review` + Claude Code with a plain prompt | 87.2% | 50.8% | 25 |
| The factory's two reviewers, with its brief and library | 85.5% | 35.5% | 19 |
| PR-Agent | 81.5% | 14.4% | 8 |

\*Counted after the fact.

**On 20 fresh pull requests**, with the vendors' review modes added to the factory
([v6](helpers/factory-warranty/calibration/realbugs/results/v6-RESULTS.md)):

| | Precision | Recall |
|---|---|---|
| The factory's three reviewers, every finding pooled | 80.6% | 64.1% |
| Claude Code with a plain prompt twice, plus `codex review` | 80.2% | 62.1% |
| Claude Code with a plain prompt, plus `codex review` | 81.3% | 56.9% |
| PR-Agent | 83.3% | 19.0% |

No arm beat another; a third review of any kind added a little recall and nearly doubled the reading. All 3 serious
findings were found by every arm.

**With one model**, on 23 fresh pull requests chosen for their serious findings
([v7](helpers/factory-warranty/calibration/realbugs/results/v7-RESULTS.md)):

| Model | Reviewing with | Precision | Recall | Serious found |
|---|---|---|---|---|
| Sol | the factory's brief and library | 86.8% | 19.8% | 21 |
| Sol | `codex review` | 84.9% | 14.7% | 22 |
| Opus | the factory's brief and library | 87.2% | 45.1% | 28 |
| Opus | Claude Code with a plain prompt | 87.2% | 49.6% | 29 |

On Sol the factory's version did better; on Opus, about the same. Two factory runs that failed on an unrelated bug
were re-run under a dated amendment; as first judged, Claude Code found 3 more serious bugs.

**Against other Claude reviewers**, on v6's pull requests, each judged alone
([v8](helpers/factory-warranty/calibration/realbugs/results/v8-RESULTS.md)):

| | Precision | Recall |
|---|---|---|
| Claude Code with a plain prompt | 81.3% | 56.2% |
| The factory's Claude reviewer, with its brief and library | 78.2% | 47.5% |
| Claude Code's built-in `/code-review` | 74.5% | 18.7% |
| [brooks-lint](https://github.com/hyhmrright/brooks-lint) 1.8.0 `/brooks-review` | 72.2% | 13.7% |

The factory's reviewer beat both tools, and the plain prompt beat it. Neither tool aims at an answer key of mostly
bugs: `/code-review` reports only what it's sure of, and brooks-lint looks for maintainability risks. A third of
brooks-lint's findings named no file and went on each change's first file; at best its recall would have been 30.6%.

**Limits:** one try per reviewer; 20 to 25 pull requests per test, none over 2,000 changed lines in the fresh
samples; an answer key mostly raised by AI reviewers, and a Claude judge; PR-Agent in its diff-only local mode; v8
reused v6's pull requests.

## Showing, not arguing

In one test, every stop on a good change came from a reviewer naming an input that would now break, and it didn't. A
non-coder can't tell a right argument from a wrong one, so an AI now writes a check the factory runs before and after
the change. On 70 blocking findings from earlier runs (cases already seen),
58 of the 61 that caught real bugs came out "shown", and so did 7 of the 9 that stopped good changes, from four
changes run repeatedly ([results](helpers/factory-warranty/calibration/realbugs/results/REPRO-RESULTS.md)).

"Shown" is judged from exit codes; that a check tests what the finding names is the checking AI's account, and where
it says the code is new, failing after the change alone counts. The step was meant to clear false stops and cleared 2
of 10, failing its rule, so it ships as an optional display (`review.reproduce`) that leaves blocking unchanged.
Whether it helps a signer decide faster hasn't been tested.

## Earlier tests

**Does the library help?** On 17 real bugs reversed into eight JavaScript and TypeScript libraries, reviewers
with it caught 16 on both tries against 11 without
([v3](helpers/factory-warranty/calibration/realbugs/results/v3-RESULTS.md)). Three of the five gains came where
OpenAI's reviewer timed out without it; counting finished reviews only, it's 16 against 14. It cost 2.4 times the
Claude review spend.

**How often it stops good changes.** In that test, 38% and 44% of runs, against a bar of 20%; on fresh cases, 2 of 24
([v4](helpers/factory-warranty/calibration/realbugs/results/v4-RESULTS.md)). It depends heavily on the changes.

**One change, start to finish.** The factory built itself a scanner rule. Chris sent it back twice ("Don't claim
more than it catches") and signed the third
([showcase](helpers/factory-warranty/calibration/showcase-2026-10-14/), about $9 of Claude; one config file was edited
afterwards, so its recorded fingerprint no longer matches).

## Limits and prior art

Its rules (what blocks, the 20% bar) are marked PROPOSED in [`policy.yaml`](helpers/factory-warranty/factory/policy.yaml),
and [conformance/](helpers/factory-warranty/conformance/) maps it to each standard. Not yet shown: that a non-coder can
safely sign from the sheet (one showcase change), and that the gates catch what reviewers miss (every replay switched
the projects' test suites off). It runs on macOS only; someone with the operator's access could rewrite the log
unseen; a signature is a record, not cryptography; and the commits showing each test came first are in the factory's
unpublished repository.

AWS Labs' [AI-DLC](https://github.com/awslabs/aidlc-workflows) structures a whole build with approval gates, reviewer
agents and an audit trail; [`codex-plugin-cc`](https://github.com/openai/codex-plugin-cc) and
[PAL MCP](https://github.com/BeehiveInnovations/pal-mcp-server) have other models review Claude Code's work;
[TDD Guard](https://github.com/nizos/tdd-guard) enforces tests first; [in-toto](https://github.com/in-toto/in-toto)
and [Sigstore](https://github.com/sigstore/cosign) keep cryptographically signed records of how software was made.
[Reviewers' star counts, 2026-10-20](helpers/factory-warranty/calibration/realbugs/prior-art-2026-10-20.md).

## The library

Eighteen open sources, each read in full and checked line by line by Claude and OpenAI's model: NIST, CISA and OWASP
standards; research on AI-assisted development, including METR's trial and Google's DORA report; and guidance from
Microsoft, OpenSSF and the UK government. It names 29 places where they disagree. The app ships the 17 licensed for commercial use; DORA
(CC BY-NC-SA) ships only in [`apps/factory-warranty-full/`](apps/factory-warranty-full/).

## Try it

**Without installing anything:** add `https://review.groundedforge.com/mcp` to Claude or ChatGPT as a custom connector
and sign in with GitHub. Your own assistant reviews a change with the factory's brief and library and writes the
sign-off sheet ([how](https://review.groundedforge.com/)). That's the review stage only.

**The whole factory** needs macOS, Python 3.12+, [uv](https://docs.astral.sh/uv/), Claude Code, the Codex CLI, `gitleaks`, `osv-scanner`
and `semgrep`.

```bash
cd corpus.commons/chrisgagne-agent-built-software/apps/factory-warranty
claude .                                   # ask it what evidence a change needs before you sign it off
uv tool install --editable ./factory       # the harness: `factory run STORY.md --repo PATH`
```

[The factory's README](helpers/factory-warranty/README.md) covers the config.

## What's in this folder

- [`helpers/factory-warranty/`](helpers/factory-warranty/): the factory, and every test's pre-registration, results
  and records ([calibration/](helpers/factory-warranty/calibration/)).
- [`distillations/`](distillations/warranting-agent-built-software/), [`references/`](references/),
  [`sources/`](sources/): the library.
- [`apps/`](apps/): the factory and library as an app.

It's a [grounded-forge](../../README.md) corpus. The code is MIT; each write-up keeps its source's licence (see [`LICENSE-CONTENT`](../../LICENSE-CONTENT)).
