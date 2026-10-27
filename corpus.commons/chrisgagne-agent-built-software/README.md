# Signing off AI-written code without reading every line

> I'm a tech-savvy product manager and consultant, but I've rarely been held responsible for warranting software the
> way a professional developer is. I wanted to see what software factory could be built from open sources (public
> domain, MIT, Creative Commons and the like) on what good AI-built software looks like. I directed this one, and
> signed off its one real change from the sign-off sheet without reading the code. A naïve junior developer like me
> can now build review tooling that beats PR-Agent (the most-starred open-source AI reviewer we found) and brooks-lint.
> It also beats the labs' own review commands at their default settings, though turned up to higher effort they catch
> up. On either model, a plain "review this as a careful senior engineer" prompt does as well. What it adds is the
> rest: locked tests, a sheet I could sign from, and a record of what was and wasn't shown.
>
> *Chris Gagné*

**An experiment, built by AI and open for critique.** Claude wrote nearly all of it, with OpenAI's Codex reviewing,
grading and picking test cases. Every test was written down before it ran.

## The short version

- **Its review hasn't beaten `codex review` and Claude Code with a plain prompt, pooled.** With those two added as
  its reviewers, it came out level.
- **It beat PR-Agent, brooks-lint (Claude reviewing against twelve engineering books), and both labs' review commands
  at their default levels,** with 1.3 to 3.5 times their recall. Turned up to higher effort, the labs' commands caught
  up.
- **Its brief and library don't beat a plain prompt on either model, at any effort we tried.** Its wins are over tools
  that hold the model back. Effort mattered more: Claude Code with a plain prompt at `xhigh` and `/code-review xhigh`
  found the most serious bugs of anything we tried.
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

## How it differs from other software factories

Most tools called software factories run the work: a ticket goes in, agents plan, build, test and review it, and a
merged pull request comes out. They're built for throughput, and the human checks the result on staging or in a
review. This one is built for the person who signs, and it doesn't try to build faster:

- **What the sheet calls shown, the factory ran.** Each command is listed with its exit code and an output hash. The
  builder's own account sits apart, under "Asserted, not evidence".
- **Its checks run things rather than look for a file.** A rollback has to name a command, and the gate runs it.
- **Every commit names who wrote it.** Trailers give the change and the leg, model and log entry behind the work, so
  a line traced back from production leads to the evidence.

None of this makes the review smarter. The point is that the person who signs can see what was shown and what was
only claimed.

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
([v7](helpers/factory-warranty/calibration/realbugs/results/v7-RESULTS.md),
[v9](helpers/factory-warranty/calibration/realbugs/results/v9-RESULTS.md)):

| Model | Reviewing with | Precision | Recall | Serious found (of 48)\* |
|---|---|---|---|---|
| Sol | the factory's brief and library | 86.8% | 19.8% | 20 |
| Sol | a plain prompt | 85.4% | 22.1% | 26 |
| Sol | a plain prompt, reasoning effort "high" | 86.0% | 28.4% | 30 |
| Sol | `codex review` | 84.9% | 14.7% | 22 |
| Sol | `codex review`, reasoning effort "high" | 89.8% | 22.1% | 27 |
| Sol | the factory's brief and library, reasoning effort "high" | 87.5% | 27.0% | 27 |
| Opus | the factory's brief and library | 87.2% | 45.1% | 28 |
| Opus | Claude Code with a plain prompt | 87.2% | 49.6% | 30 |
| Opus | Claude Code's `/code-review` | 84.7% | 26.6% | 25 |
| Opus | `/code-review high` | 87.8% | 46.2% | 28 |
| Opus | `/code-review xhigh` | 82.7% | 55.9% | 34 |
| Opus | the factory's brief and library, `--effort xhigh` | 79.8% | 51.3% | 27 |
| Opus | Claude Code with a plain prompt, `--effort xhigh` | 88.6% | 52.3% | 34 |

\*v7 counted 1 more for the first Sol arm and 1 fewer for the Opus plain prompt.

At the defaults, the brief came out about the same as a plain prompt on both models. Both labs' review commands hold
the model back at their defaults: turned up, `codex review` drew level with the brief and `/code-review` with the plain
prompt. Turning the brief up didn't pull it ahead: on Sol it stayed level with the plain prompt, and on Opus the plain
prompt did better, as the brief's precision fell. A plain prompt at `xhigh` found as many serious bugs as
`/code-review xhigh` at higher precision and lower cost. Sol ran at its CLI's default reasoning effort ("none") except
in the "high" rows. Two factory runs that failed on an unrelated bug were re-run under a dated amendment, and the rows
at "high" or `xhigh` other than `/code-review`'s were added after the rest were judged.

**Against other Claude reviewers**, on v6's pull requests, each judged alone
([v8](helpers/factory-warranty/calibration/realbugs/results/v8-RESULTS.md)):

| | Precision | Recall |
|---|---|---|
| Claude Code with a plain prompt | 81.3% | 56.2% |
| The factory's Claude reviewer, with its brief and library | 78.2% | 47.5% |
| Claude Code's built-in `/code-review` | 74.5% | 18.7% |
| [brooks-lint](https://github.com/hyhmrright/brooks-lint) 1.8.0 `/brooks-review` | 72.2% | 13.7% |

The factory's reviewer beat both tools (`/code-review` at its default), and the plain prompt beat it. Neither tool aims at an answer key of mostly
bugs: `/code-review` reports only what it's sure of, and brooks-lint looks for maintainability risks. A third of
brooks-lint's findings named no file and went on each change's first file; at best its recall would have been 30.6%.

**Limits:** one try per reviewer; 20 to 25 pull requests per test, none over 2,000 changed lines in the fresh
samples; an answer key mostly raised by AI reviewers, and a Claude judge; PR-Agent in its diff-only local mode; v8
reused v6's pull requests and v9 reused v7's.

Every number above was scored through the Anthropic API. The same judge driven through the Claude Code CLI instead,
re-scoring five of these pull requests, agreed on 42 of 45 findings but came out 8.3 points lower on precision, so a
new arm has to be judged the same way as the arm it is set beside
([cal](helpers/factory-warranty/calibration/realbugs/results/cal-RESULTS.md)).

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

The closest prior art is AWS Labs' [AI-DLC](https://github.com/awslabs/aidlc-workflows), and it's far larger: it
steers a whole build, from requirements to operations, in seven coding tools, and asks a person to approve the plan
before any code is written, which the factory doesn't. On the checks that matter to whoever signs a change, though,
the factory enforces in code what AI-DLC mostly leaves to instructions, advisory checks or the coding tool's
permissions: tests locked before the build, scanners run in a sandbox, blind reviewers from two model families, a
hash-chained log and a decision page in plain words
([comparison](helpers/factory-warranty/calibration/realbugs/prior-art-aidlc-2026-10-21.md), from each one's docs and
code; neither was run, and AI-DLC was read in part).

[`codex-plugin-cc`](https://github.com/openai/codex-plugin-cc) and
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
