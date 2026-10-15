# Factory Warranty: a software factory grounded in open standards

**An experiment, built by AI and open for critique.** Claude (Anthropic) wrote nearly all of this, the code, the
corpus and these docs, with OpenAI's Codex as an independent reviewer and grader, under the direction of Chris Gagné.
It asks one question: when coding agents write software faster than anyone can read it, how can the person
accountable for it still stand behind each change?

The answer tried here: move the warranty from reading the code to reading the evidence. A change goes through a
harness that writes down what "correct" means before the build, locks tests the builder can't touch, runs
deterministic gates, has two AI reviewers from different companies read it blind, and records every step on a
tamper-evident ledger. The accountable person gets a one-page decision written for someone who doesn't read code, and
signs it or sends it back in their own words. The harness never signs.

The reviewers don't work from their training alone. They work from distillations of 18 open sources (NIST, OWASP,
CISA, UK government assurance guidance, and research on AI-assisted development) projected onto the eight stages of a
change's life. A pre-registered test, set up so it could have killed that idea, says the corpus helps. The same test
shows a problem we haven't solved. Both are below.

## What's here

| Folder | What it is |
|---|---|
| [`helpers/factory-warranty/`](helpers/factory-warranty/) | The factory: the harness's code, its tests, its design ([DESIGN.md](helpers/factory-warranty/DESIGN.md)), its standards mapping ([conformance/](helpers/factory-warranty/conformance/)) and every measurement ([calibration/](helpers/factory-warranty/calibration/)) |
| [`tasks/`](tasks/warranting-agent-built-software.md) | The task axis: the job ("warranting agent-built software"), its eight stages and the practitioner questions it answers |
| [`distillations/`](distillations/warranting-agent-built-software/) | One distillation per source, and the index the reviewers read: 271 trigger→response rows and 29 named disagreements between sources |
| [`references/`](references/), [`sources/`](sources/) | Each source's deep and light reference, its converted text, its source card and licence, and its audit log |
| [`apps/factory-warranty/`](apps/factory-warranty/), [`distros/`](distros/) | The built app (the distillations, the indexes and the factory together) and its packaged tarball |

## How a change goes through

1. **Spec.** An AI turns the story into numbered behaviours, each naming the test that will check it.
2. **Triage.** Rules sort the change by what it touches: sign-in, personal data, money, migrations, AI features.
3. **Tests first.** An AI writes the tests; the factory checks they fail before the build, then locks them.
4. **Build.** An AI builds the change in a sandbox; it may run only the factory's own check.
5. **Gate.** The locked tests, the project's own commands, secret, dependency and code scanners, and a check that
   nothing the builder shouldn't touch was touched.
6. **Review.** Claude and Codex review blind, each from its own copy, grounded in the distillations; a third AI sorts
   their findings, and can't clear a reviewer's serious finding on its own.
7. **Warranty.** Code, not a model, assembles the pack from the ledger: a decision page first, then the evidence.
8. **Sign or return.** The accountable person signs at a terminal, or sends it back in their own words; a send-back
   goes through spec and tests again before the rebuild.

[`helpers/factory-warranty/README.md`](helpers/factory-warranty/README.md) has the commands.

## What we measured

### The test we set ourselves

The axis spec says, in advance: if reviewers who consult the corpus don't catch more defects than the same reviewers
without it, the corpus is shelf material and the gates carry the warranty on their own.

The first try couldn't answer that. On 10 planted defects (2026-10-11), the reviewers caught all 10 with no corpus,
with the axis spec's seed rows, and with an earlier version of the distillations: a ceiling, too easy to tell anything
apart.

So we wrote a harder test down first ([pre-registration](helpers/factory-warranty/calibration/realbugs/PREREG-v3-grounding.md),
committed before anything ran): 25 real changes from the history of eight open-source projects, 17 that brought back
a real bug and 8 clean ones, picked by Codex (Sol) rather than by the builder. Each was reviewed twice with the
corpus and twice without, the two interleaved, and Sol graded the reviews blind against each bug's real fix. The
corpus would count as helping only if it caught at least 3 more of the 17 bugs on both tries, while stopping at most
one more clean change.

| | Without the corpus | With the corpus |
|---|---|---|
| Real bugs caught on both tries | 11 of 17 | **16 of 17** |
| Clean changes wrongly stopped | 3 of 8 | 4 of 8 |
| Confirmed findings that cite a standard or source | 0 of 64 | 56 of 82 (68%) |
| Review cost | $13 Claude, 1.2M Codex tokens | $32 Claude, 2.1M Codex tokens |

**The test was met:** 5 more bugs caught reliably, and one more clean change stopped, which the rule allowed (that
one was the gate, not the reviewers). Full results: [v3-RESULTS.md](helpers/factory-warranty/calibration/realbugs/results/v3-RESULTS.md).

What that doesn't show: 17 bugs is a small sample, so a gap of 5 could still be partly luck; two tries per change is an
easier bar than three; and the corpus costs about 2.4 times as much to review with.

### The problem we haven't solved

**About four clean changes in ten were stopped, with or without the corpus.** Our own bar is two in ten. The same
three changes were flagged in both arms, so this is the reviewers, not the corpus. Some of the flags are arguably
right (one change updated a library's source but not its committed minified build), but they were picked as clean
changes, so they count against us. For a builder, every false stop is time spent reading a decision page and clearing
it. If you've solved false alarms in AI code review without letting real bugs through, that's the conversation we'd
most like to have.

The gate also gave different answers on two runs of the same change once, most likely because its scanner downloads
its rules fresh each run; pinning them is on the list.

### One real change, start to finish

The factory built one of its own features: a scanner rule that stops code from running text built at run time
(`eval` and its relatives). The accountable person read each decision page, sent the change back twice in plain
words ("Don't claim more than it catches"), and signed the third version. Along the way the run exposed three bugs in
the factory itself, each fixed with a test. The ledger, the signed pack and the cost (about $9 of Claude and 214k
Codex tokens over five runs) are in [the showcase](helpers/factory-warranty/calibration/showcase-2026-10-14/).

## What is still a proposal

The factory's rules (when a finding blocks, when a second person is needed, the replay's pass mark) are in
[`policy.yaml`](helpers/factory-warranty/factory/policy.yaml), and every one is marked PROPOSED, with who set it.
One rests on a source (NIST SP 800-218A: no AI model alone in the path of a significant security decision); the
others are design choices. All are the operator's to confirm. The standards mapping
([conformance/](helpers/factory-warranty/conformance/)) says row by row what is shown by a test, what is only
asserted, and what is a gap.

Other limits, plainly: it runs on macOS only (it sandboxes with `sandbox-exec`); the ledger is tamper-evident, not
tamper-proof, against someone with the operator's own access; and a signature is a record, not a cryptographic
signature. DESIGN.md has the full list.

## The sources

Eighteen open sources, each read in full and processed through grounded-forge's 9-pass ingestion protocol, then
audited by a fresh Claude agent and a blind Codex reviewer working separately, with their disagreements sorted and
fixed against the source text. Two (the Microsoft playbook and the Cucumber docs) are labelled subsets.

- **Standards and threat lists:** NIST SSDF 1.1 and SP 800-218A, the CISA secure software attestation form, OWASP
  ASVS 5.0, the OWASP Top 10 for LLM applications and for agentic applications (2026), and OWASP's agentic threats and
  mitigations.
- **Research on AI-assisted development:** METR's productivity trial, the Cursor velocity and complexity study,
  SWE-bench, *Why Language Models Hallucinate*, Google's DORA report on AI-assisted development (2025), and
  TestSuiteBench (a 2026 preprint).
- **Practice and assurance guidance:** the Cucumber BDD and Gherkin docs, Microsoft's Code-With Engineering Playbook,
  the UK government's *Quality assurance of code for analysis and research* and *AQuA Book*, and OpenSSF's guide to
  finding and fixing vulnerabilities with AI.

The sources disagree with each other in 29 places the index names, for example whether a manager can trust code they
don't read (the Duck Book) or whether verification has to read the source (ASVS). The reviewers are told to say so
when it matters.

## Try it

Needs macOS, Python 3.12+, [uv](https://docs.astral.sh/uv/), Claude Code, the Codex CLI, `gitleaks`, `osv-scanner`
and `semgrep`.

```bash
tar -xzf distros/factory-warranty-v0.4.0-open-nc.tar.gz
cd factory-warranty
claude .                                   # the knowledge layer: ask it what evidence a change needs
uv tool install --editable ./factory       # the harness: `factory run STORY.md --repo PATH`
```

## Licence

The code is MIT. Each reference and distillation inherits its source's licence (public domain, OGL, CC BY, CC BY-SA,
MIT, and CC BY-NC-SA for the DORA report, which makes the packaged app non-commercial as a whole); see
[`LICENSE-CONTENT`](../../LICENSE-CONTENT) for the table.
