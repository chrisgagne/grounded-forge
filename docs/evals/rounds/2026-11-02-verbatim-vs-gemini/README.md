# Verbatim mode against Gemini Notebook: can a reader check every claim?

**Status: run 2 November 2026.** Both arms answered the one question, and two blind Opus judges scored both answers, with the order swapped between them. Both judges would hand the forge package to a reader who must check every claim. Sol's design points that need a revised brief (listed under "Second opinion") are not addressed; whether to run a second judging round is Chris's call.

**Related.** The [case-citations round](../2026-11-case-citations/) is the larger study of the same comparison: 30 answers and about 1,500 citations, graded by two model families. It graded every citation on whether its chunk or source carries the claim, and found 19% of Gemini's markers do, against 83% of `answer-from-corpus`'s credits. That round's figures and this one's don't compare: it scores each marker, this round each claim. [Round 3](../2026-11-02-verbatim-case-citations/) puts verbatim mode on that round's cases and rubric.

## The question this round asks

[Verbatim mode](../../../architecture/verbatim-mode-proposal.md) moves quotation out of the model's hands: the model names a passage by an anchor copied from the converted source, and a deterministic resolver places the author's sentence there, with its line, section, page and a pre-rendered image of the page. The claim worth testing is the one Chris set as the standard: *it should be dead simple for the human to verify the quote in context*. Two things, per claim:

1. **Support.** Does the cited source say what the answer says it says?
2. **Verification effort.** Given only what the answer hands the reader, how many steps does it take to find the passage, and which pointer got them there?

Gemini Notebook is the comparison because it is what a reader would otherwise use over the same files, and because its citation markers open the passage they rest on, which is a strong pointer of its own.

## Design

- **One question:** "How can NZ better prepare itself for the next pandemic?" Neither corpus holds a public-health source or anything on New Zealand, so both arms answer obliquely. That makes it a test of honest grounding as much as of retrieval.
- **Same library.** The forge arm ran over the private `aarbuddy` corpus only. The Gemini arm is the AARBuddy notebook, which holds the same corpus as uploaded on 19 October 2026 (low hundreds of sources, all ticked). The five sources the forge report cites are all in the notebook (checked 2 November).
- **Same originals for the judge.** Each judge gets both answers and the original PDFs and EPUBs of every source either answer cites, plus converted text for any source with no original file.
- **Blind.** The arms are labelled A and B, the order swapped between the two judges, and nothing in either package or brief names the tool that made it.

## Arms

- **Forge (verbatim mode).** `scripts/verbatim/generate.py` at commit `d12d8225`, one Opus model step through `answer-from-corpus` in project mode, then the resolver and the renderer. For the judge the report is flattened to prose: every placed span in quotation marks with a number, and under each paragraph a pointer per span (source, section, printed page where the converter kept one, original file and the page within it, converted file and line, the span's own paragraph, the page images with the passage boxed). Builder: [`package_forge.py`](package_forge.py).
- **Gemini Notebook.** The bare question, asked once in a cleared chat, with default settings. The answer is captured with its citations, and each citation is clicked to capture the passage it shows.

## Rubric

The judges' brief is [`judge-brief.md`](judge-brief.md). Per claim: support (yes / partly / no, naming the passage found) and verification effort (the pointer used and the steps taken, counting each file opened, search run and page turned). Per answer: counts, mean steps for verified claims, and what made checking easy or hard.

## Forge arm: what the generator produced

| | |
|---|---|
| Model step | 342 s, 30 turns, about $2.41 of allowance |
| Spans | 14 placed of 14 on the first pass; no repair needed |
| Sources | 5 (Edmondson, Dörner, Suleyman, Hollnagel, Kim & Spear) |
| Page images | the hit page and two either side for all 14 spans, passage boxed |
| Authors' words | 91% of the page at `--joins minimal --verbatim 1`; 50% in the essay form |

Fixes the first generated run exposed, all in the resolver or renderer, none in the contract:

- A heading set as a bold all-caps line wrapped over two lines was not read as a heading, so two spans had no section. The locator now reads short all-caps lines as headings and joins a wrapped pair.
- A blockquote marker line (`> > >`) was taken for a heading. Locator lines now need letters.
- Originals keep their download names, so three sources had no original file to show. The resolver now matches the original by author surname and two title words, and records how it matched.
- Three spans found no page in the original, because the book set an apostrophe curly where the converter has it straight, or broke a hyphenated compound across lines. The page search now tries both apostrophes and starts a few words into the span.
- Sources whose sidecar carries no title showed their slug. Titles now fall back to `reference-index.json`.
- The resolver treated a number before a full stop as an abbreviation, so a sentence ending in a year never ended. A number now counts as an abbreviation only when a digit follows the stop.

## Results

**On this one question, the forge package's claims were better supported than Gemini Notebook's, and checking them took a half to a third of the judge operations.** All 14 of its quotations were exact, and 10 to 11 of its 12 other claims were fully supported, with none unsupported. Gemini's 23 claims scored 12 fully supported, 10 partly and 1 not, identically from both judges. Gemini's citations were honest: every passage they open that could be checked is genuine source text. The gap is in the claims, which often go further than the passages under them, and in the pointers, which name a book but no place in it.

These findings hold for these two answers to this one question. The forge deliverable the judges scored is the flattened package `package_forge.py` builds, not the report page a reader sees.

### How the Gemini arm ran

- **Asked once**, at 11:50 notebook time on 2 November, in a cleared chat, with every source ticked, including the five the forge report cites.
- **Chat settings.** The notebook's Configure Chat was not at its default. It was set to a Custom style ("Write content for CTO/CEOs reading LinkedIn") with Longer responses. It was switched to Default style and Default length for the question, then restored. The 31 October non-duality answer saved beside the forge reports ran under that custom setting.
- **One stray prompt.** Before the real question, a misplaced click sent the notebook's own suggested prompt (how the notebook can help with these sources). The chat was cleared again, so the round's question was asked in a clean chat.
- **What came back.** Five numbered strategies, about 580 words, with 28 distinct citations (49 markers, once six collapsed groups were expanded) to twelve sources. Four of them are also cited by the forge report: Edmondson, Hollnagel's *Safety-II in Practice*, Suleyman, and Kim & Spear. Gemini did not cite Dörner. The other eight:
  - McChrystal, *Team of Teams*;
  - Woods, Hollnagel and Leveson, *Resilience Engineering*;
  - Snowden and others, *Cynefin*;
  - Hubbard, *How to Measure Anything*;
  - Pfeffer and Sutton, *The Knowing-Doing Gap*;
  - Marquet, *Leadership Is Language*;
  - Schwartz, *No Bad Parts*;
  - Chris's own *Come Prepared to Die*, a Google Doc in the notebook that isn't in the corpus.
- **Form.** The prose is all paraphrase except one quoted phrase. Each marker opens a source chunk of 80 to 250 words with nothing marked inside it. Every popup was captured in full.
- **Judges' library.** The judges had the original of every cited source, or converted text for Marquet and Schwartz, which have no original in the corpus. *Come Prepared to Die* has neither, so its two citations could be judged only from the passages Gemini shows. Both claims that cite it also cite Hollnagel, which the judges checked.

### Support and effort

Both judges drew the same claim boundaries: 26 claims in the forge answer (14 quotations and 12 paraphrases or attributions) and 23 in Gemini's. "Judge operations" counts what an Opus judge with shell tools did: each file opened, search run or page image viewed. It is not a measure of human effort.

| | Forge, judge 1 | Forge, judge 2 | Gemini, judge 1 | Gemini, judge 2 |
|---|---|---|---|---|
| Quotations exact | 14 of 14 | 14 of 14 | 1 of 1 (a quoted phrase) | 1 of 1 |
| Cited passages genuine | | | 26 of 26 checkable (2 judged from the shown text) | 26 of 26 checkable |
| Other claims: yes / partly / no | 10 / 2 / 0 of 12 | 11 / 1 / 0 of 12 | 12 / 10 / 1 of 23 | 12 / 10 / 1 of 23 |
| Judge operations per claim, all claims | 1.15 | 1.08 | 2.30 | 3.35 |
| on claims scored yes | 1.08 | 1.08 | 2.58 | 3.92 |
| on claims scored partly or no | 2.0 | 1.0 | 2.0 | 2.73 |
| Claims where no passage was found | 0 | 0 | 0 | 0 |

No check failed outright: for every claim in both answers, the judges found the passage the claim rests on. A "partly" or "no" means the passage was found and doesn't carry the claim. Wrong turns before a find:

- **Forge:** one. Pointer [1]'s page image cost judge 1 an extra operation (see the package defects below).
- **Gemini:** four. Two searches by each judge missed at first, because the source text breaks lines or carries soft hyphens inside the phrase searched for.

Checks of Gemini's claims cost more because each one starts with converting a whole book and searching it. Claims with three or four markers took three to six operations. The two judges' Gemini totals differ (53 against 77 operations) because judge 2 charged two operations for the first check of every marker; their forge totals are within two operations of each other.

### What the support gap is made of

- **Gemini's partly and no scores** are claims that go further than their passages, in three ways. Judges 1 and 2 named the same ones.
  - Specifics the passages lack: far-UVC and airborne pathogens where the source has low-wavelength light that kills viruses, supply bottlenecks, manufacturing partnerships, frontline healthcare workers.
  - Passages put to work they don't do. Dutch flood management stands for pandemic planning. A postal service's own fleet stands for sovereign medical supply. A list of small countries where Cynefin has spread stands for New Zealand being suited to network governance, the one claim both judges scored "no".
  - A source softened: a proposed ban on the riskiest research becomes "governance, oversight".
- **The forge answer's partly scores** are its own framing sentences around exact quotations. One says Suleyman traces the gap to how governments plan, where he puts it down to how hard novel threats are. The other says detection comes first in Esvelt's scheme, where Suleyman ranks the three pillars equally.
- **Not scored.** Uncited joining prose was skipped in both answers, per the brief. That leaves out the forge answer's New Zealand applications, which it keeps apart from the attributed claims, and any uncited recommendation in Gemini's. Judge 1 credited the forge answer for stating at the start what the library can't answer (nothing on New Zealand's own response, no public-health sources). Neither judge scored that.

### Where the judges agree and where they don't

- **Agreed:** the same 49 claim boundaries, and the same score on 48 of the 49. Gemini's 23 claims scored identically, claim by claim. Both judges would hand the forge package to a reader who must check every claim.
- **Split:** one claim. On the forge answer's "detection comes first" lead-in, judge 1 scored partly, while judge 2 scored yes and noted the lead-in as the answer's own judgement.
- **Effort:** the same ranking, with different spreads. The forge answer cost 1.08 to 1.15 operations per claim for both judges; Gemini cost 2.30 for judge 1 and 3.35 for judge 2, a difference in how they counted, as above.

### Defects the judges found in the forge package

Both judges found the first two; judge 1 found the others. None changed a support score.

1. **Pointer [1]'s page image is an endnotes page.** The package names page 170 of the Edmondson EPUB; the passage is on page 58. The package was built at 10:23 from a bundle that a resolver re-run replaced at 10:35. Rebuilt from the current bundle, the package gives page 58 and the right images, and nothing else changes. The earlier page search had matched the endnote's tag line, which repeats the span's opening words. So the report page was right and the judged package was stale. Fix: build the package from the bundle in the same step as the render.
2. **"Boxed" is promised but not shown.** The resolver stores each passage's boxes as fractions of the page, and the report page draws them over the image. The PNGs carry none, so the package's "the passage is boxed on …" is false for anyone opening the image. Fix: burn the boxes into the PNGs, or drop the wording from the package.
3. **The "paragraph" field for the three Kim & Spear spans runs to 1,700–2,000 words.** The converted PDF text has no paragraph breaks around the passage, so the context runs to the section's edges. This is still in the current bundle.
4. **Two printed pages for one page.** Pointers [1] and [11] give printed pages 101 and 102 for passages on the same EPUB page.

### Files

The answers, the judges' briefs and results, and the judges' library quote copyrighted sources, so they stay in `corpus.local/aarbuddy/projects/verbatim-reports/nz-pandemic/judge/`:

- `gemini-answer.md`: the Gemini capture, with how it ran and every citation's passage.
- `forge-package.md`: the forge package as judged.
- `blind/judge-1/` and `blind/judge-2/`: each judge's `brief.md`, `answer-A.md`, `answer-B.md` and `result.md`. Judge 1: A is forge, B is Gemini. Judge 2: the reverse.
- `blind/originals/` and `blind/converted-only/`: the judges' library.

The judges read everything through `corpus.local/aarbuddy/projects/round-nz-pandemic`, a symlink to the report folder, so no path they saw names the tool. The non-duality chat that was cleared to run this arm is saved beside its report, with its citation markers, as `non-duality/gemini-answer-2026-10-31-citations.md`.

## What this round cannot show

- One question and one notebook. A single question can't separate the tool from the topic.
- The two arms read the same sources differently: the forge arm through the corpus's audited references and converted text, Gemini through its own ingestion of the original files. A claim Gemini supports from a passage the forge arm never read is a retrieval difference, not a grounding one.
- Verification effort is measured by an Opus judge with shell tools, not by a person with a PDF reader. Steps that are cheap for a judge with `grep` may be slow for a reader, and the reverse.

## Second opinion

Sol (`gpt-6.1-sol` through `codex exec`, read-only) reviewed the code in `scripts/verbatim/` and, separately, this round's design.

**The code review** raised 17 points on the resolver and the renderer. The cheap ones are fixed in commit `2f48a3c2`:

- the source and the anchor go through one normaliser, with true end offsets;
- matches sit on word boundaries, and every hit is counted;
- signs on numbers are kept;
- paragraph breaks are structural;
- page markers come only from explicit anchors, and a PDF's printed page from the folio on the page itself;
- a report's converted path must be the slug's own;
- duplicate span IDs, a failed model step, or quotation marks in the model's own prose stop the run.

Three are left as known: "etc." ending a sentence, locators on prose-like lines, and folio detection on PDF extracts that start mid-book.

**The design review** raised 13 points. They fall into three groups.

*Already handled by this run.*

- The judges read the answers through a neutral path (`round-nz-pandemic/…`), and nothing in either package names the tool that made it. Sol's point stands that this is identity-masking, not blinding. The repository name sits in every path, and the boxed page images and pointer blocks mark the forge arm by their form.
- Each judge has the originals of every source either answer cites, plus converted text where there is no original. A valid Gemini citation to a source the forge arm never read counts as support, not as a retrieval penalty. Missing evidence is "unassessable", not "unsupported".
- Gemini's citation popups were captured in full, without picking among them.

*Applied in how the results are reported.*

- "Steps" are judge operations with shell tools, not human effort.
- Quotation fidelity and the support for substantive assertions are reported separately, each with its denominator. Raw counts of supported claims are not a measure of answer quality: fourteen exact quotations can outweigh a few unsupported recommendations.
- Effort on failed checks is reported beside effort on successful ones.
- The evaluated forge deliverable is the flattened package `package_forge.py` builds, not the report page a reader sees.
- Findings hold for these two answers to this one question only. The resolver was repaired on this very run, so it is a development example, not a held-out test.

*Not addressed. They need a revised brief and a second judging run.*

- Each judge read both answers before scoring. A passage found for one answer can make the other cheaper to check, and swapping the order only partly cancels that. Fix: a fresh judge session per answer.
- Support as delivered isn't separated from support recovered by the judge's own search, so a search can quietly repair a bad citation.
- Uncited joining prose is skipped, so an unsupported recommendation that sits between exact quotations escapes scoring. Fix: inventory every substantive assertion.
- Claim boundaries aren't agreed up front, and "partly" lumps inexact quotation, narrower support and overstatement together.
- There is no common search budget per claim, and no stopping rule.
- Library parity rests on the five forge citations being in the notebook. A manifest of sources and versions would establish it.
