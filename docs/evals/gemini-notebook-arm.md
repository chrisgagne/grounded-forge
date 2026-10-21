# The Gemini Notebook arm (N)

Google's Gemini Notebook (NotebookLM until its rename on 16 July 2026) is the market's default source-grounded tool: upload sources, ask, and get an answer whose claims carry passage-level citations. None of the arms in [`methodology.md`](methodology.md) is a grounded product of this kind, and its citations offer per-claim auditability, the property the matrix claims as its edge. Method N loads Gemini Notebook with the demo corpus's converted sources and puts the same prompts to it as to the matrix (D) and to Claude with the sources (C).

**Question.** Over the same sources, does the matrix produce more faithful source-grounded claims, fewer hard errors, or better coverage of the distinctions that matter than Gemini Notebook does? And if it does, is the edge confined to material where the corpus disagrees with the canonical view?

**What N measures.** A product, not a method. Gemini Notebook's model is not Claude, and the [producer head-to-head](rounds/2026-08-08-producer-head-to-head/) found the hard-error rate dominated by the producer model, not the protocol. N vs D therefore confounds model with method, and this round can't separate them. Results are reported as a product comparison.

## Sources

All 31 converted sources in `corpus.commons/demo/sources/converted/`: every `.md` file there except `IMAGES-README.md`. Leave out `IMAGE-INDEX.yaml`, `extraction-manifest.json` and the `*-images/` folders. These are the files Pass C reads and Method C attaches; every one is `open` or `open-nc` in `reference-index.json`, so nothing above the demo profiles' `open-nc` ceiling leaves the repo. Private corpora are never uploaded under this protocol.

They fit the free tier (limits from Google's NotebookLM help page, checked 19 October 2026):

| Limit (free tier) | Cap | The 31 sources |
|---|---|---|
| Sources per notebook | 50 | 31 |
| Words per source | 500,000 | largest is `openstax-economics-3e.md`: 471,386 by `wc -w`, 472,684 counting alphanumeric tokens, about 5.5% under the cap |
| Size per file | 200 MB | largest is 2.8 MB; 28 MB in all |
| File type | Markdown accepted | all `.md` |

Google's word count may differ from either local count, so the operator checks economics-3e for truncation after upload: its converted text ends on the index line `Zero elasticity 115`. If the source viewer doesn't reach that line, or any upload shows an error, the arm is partial; stop and label the run partial rather than carrying on (source-integrity rule).

Upload under the original filenames. The readable `{author}-{topic}` slugs work as keys into the model's training prior (README, finding 3), and C and D see the same names. Images don't travel; Gemini Notebook gets the same text, alt text and image links that C gets.

## Prompts

Two existing prompts, chosen for the contrast the README's findings predict:

| Prompt | Why | D runs in | Rubric |
|---|---|---|---|
| [`p01-decision-cognitive-process`](harness/prompts/p01-decision-cognitive-process.md) | Canonical material: OpenStax *Organizational Behavior* Ch 6, dense in training data. README finding 4 reports no answer-quality gain for the matrix on such material, so the expected result is no difference. | `apps/decision` | `default` |
| [`e10-aar-process`](harness/prompts/e10-aar-process.md) | Curator vs canonical. The consultant's default is root-cause analysis; the corpus's learning-review guide holds that "Cause isn't something investigators 'find' or 'discover'" (`lfuo-learning-review-guide-2024`), while its own Open Practice Library still carries Five Whys ([`tasks/aar.md`](../../corpus.commons/demo/tasks/aar.md)). README finding 1 names this kind of load-bearing disagreement as where the matrix is necessary. | `apps/aar-mode` | `essay` |

Two prompts, because the claim audit's cost scales with claims and e10 asks for about 3,500 words.

**No synthetic AAR incident exists in the repo.** e10's own worked example is the nearest thing. A prompt built on a supplied fictional incident would test applying the corpus to a case rather than recalling it; it is a follow-up, written and locked before any arm sees it.

**Not tested:** README finding 1's strongest case, non-public corpora that the training prior can't route. The demo corpus is public by construction, and private material doesn't go to Google here.

## Arms and capture

- **N:** the operator, in their own Google account (see the [checklist](gemini-notebook-checklist.md)). One notebook with all 31 sources selected, no web or Discover sources, no custom chat instructions (the default product is what's under test), response length Default for p01 and Longer for e10. Chat history is deleted before each prompt, so the second answer isn't conditioned on the first.
- **D:** captured fresh by Claude, headless, in the built app (`claude -p` from inside `apps/decision` or `apps/aar-mode`), at the same commit for both prompts. Older captures predate the corpus repair and the rebuilt apps, so they aren't reused.
- **C:** Claude Code opened bare in `sources/converted/` with the same prompt. It separates "a grounded product" from "Claude with the same files". Recommended, not required.
- **A** (no tools) is optional, as a floor.

Record the Claude model and the repo commit for C and D, and the date, plan tier and any model name Gemini Notebook shows for N.

**Citations.** The copy button under a Gemini Notebook answer keeps the `[n]` markers but drops what they point to. The operator therefore saves, for each number, the source name and the opening words of the highlighted passage (clicking a number opens the source with that passage highlighted). Third-party Chrome extensions that export citations exist; they read the signed-in Google session, so this protocol doesn't use them unless the operator vets one.

**Files** (all under `_evals/manual-gemini/`, gitignored):

| Path | What | Who |
|---|---|---|
| `raw/{stem}-N.md` | the answer as copied, unedited | operator |
| `raw/{stem}-N.citations.md` | one line per citation: `[n] \| source name \| first ~15 words of the passage, verbatim` | operator |
| `raw/{stem}-N-01.png`… | full-answer screenshots, backup only | operator |
| `raw/{stem}-N.meta.md` | date and time, tier, settings, wall time, model if shown, any quota or error message | operator |
| `raw/{stem}-{C,D}.md` | C and D answers with their trace footers | Claude |
| `judge/{stem}-{A,C,D,N}.md` | arm-neutral copies: trace footers and arm tells stripped; N's `[n]` replaced mechanically by the cited source's filename stem, so every arm cites by source name | Claude |

## Scoring

Three layers. The claim audit leads, because the blind judge scores against its own training prior and so can't see what the matrix is for ([methodology, known limitations](methodology.md#known-limitations-of-this-rubric)).

### 1. Claim audit against the source text

The same discipline as Pass I and the head-to-head ([`method.md`](rounds/2026-08-08-producer-head-to-head/method.md); brief shape from [`scripts/pass_i/briefs/blind.md`](../../scripts/pass_i/briefs/blind.md)):

1. **Packet per answer.** `answer.md` (the judge copy), the 31 converted sources read-only, the rubric. No arm label, no hint that a comparison exists, no distillations: every arm is checked against the converted sources, so D's distillations give it no home advantage.
2. **Extract** (a fresh agent). Split the answer into atomic claims and tag each **S**, when it attributes content to a source, author, framework or finding, explicitly or by naming it, or **A**, the answerer's own advice or synthesis. Advice presented as what the research says is S.
3. **Audit** (a second fresh agent, never the extractor). Grade each S claim FAITHFUL, MINOR-DRIFT, UNSUPPORTED or CONTRADICTED: strict, grade down on doubt, targeted search in several phrasings plus a read of the matching region. Quoted text must match the source word for word, allowing smart-quote normalisation. The test is "which passage says it?", not "is it true?". The primed hunt list from the head-to-head applies: attributions the source doesn't make, enumeration miscounts, dropped qualifiers, dated-fact drift. A person or framework named in none of the 31 sources is UNSUPPORTED however true (training-data leakage). Close with an over-flag guard: what was considered and judged clean, and why.
4. **Citation check** (same agent). For each S claim with a pointer, does the cited source carry it, and for N, does the cited passage? A right claim with a wrong citation is counted apart from claim faithfulness.

**Auditor family.** A third family, neither Gemini nor Claude: `gpt-5.6-sol` through `codex exec`, as the Pass I second leg runs. A fresh Claude auditor re-audits one prompt's answers as the judge-variance control, reported beside the main audit and never merged into it.

**Per-answer counts:** S claims audited; hard errors (UNSUPPORTED + CONTRADICTED) as a count and a rate; FAITHFUL S claims (coverage); citation precision; leakage count; the A-claim count, which is the share of the answer no source check can reach.

### 2. Anchor recall

Before anyone reads an arm's answer, Claude writes six to ten anchors per prompt: passages a strong answer should carry, each quoted from the converted source with its line, checked word for word, and committed so they're fixed before scoring. For p01 they come from the prompt's own strength claim (dual-system processing, the six-step process, the barriers including escalation of commitment, OB Ch 6.2–6.5). For e10, at least one anchor is the corpus's disagreement over root cause. Each answer scores present, distorted or absent per anchor. Anchors are agent-authored and non-exhaustive, not ground truth; other valid evidence counts.

### 3. Blind judge

`eval.py` on the judge copies, `--methods` set to the arms captured (`A,C,D,N` at most), `--rubric default` for p01 and `--rubric essay` for e10, seeds 1 to 3. Reported, and read through the known limit above.

### Reading the result

Stated before any answer is read:

- **N matches D** on hard errors and anchor recall on both prompts: on public material the matrix earns nothing in answer quality over the market default. Its remaining case is what Gemini Notebook doesn't offer (files that run in Claude Code, over MCP or offline; lenses; published audit receipts; token cost), and the README says so.
- **D leads on e10 only:** consistent with README finding 1 on curator-vs-canonical material, on one prompt.
- **N leads:** the README says so.

Two prompts and one run per arm support a direction, not a decimal; no equivalence or superiority claim is made. A second N run per prompt (a fresh chat) is cheap and shows run-to-run variance; take it if quota allows.

The round is published as `rounds/{date}-gemini-notebook/`: README, anchors, the judge copies, audit receipts and judge JSON. Derived text inherits the sources' licences (NC for the open-nc sources), as in the head-to-head.
