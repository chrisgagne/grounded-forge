# Verbatim mode against Gemini Notebook, round 2: the same comparison with a stricter rubric

**Status: run 2 November 2026.** Three questions, each over one corpus only. Gemini asked twice fresh, six claims passes, twelve single-answer judges, all on Opus; every judge scored every claim. Under the stricter rubric the forge answer's quotations stay near exact, and its claims hold up better on the two aarbuddy questions. On the demo question Gemini's claims were more often supported as delivered, because a third of the forge answer's attributed sentences carry no pointer. Round 1's effort gap closes: a passage the answer shows now costs nothing to read, and Gemini shows one for every marker. A Sol re-grade, one judge per answer, agrees with the Opus judges on 85% of delivered calls and holds the first two questions' readings, but on the demo question it puts the forge answer ahead on both measures, because it counted a source named in the sentence as that sentence's pointer.

[Round 1](../2026-11-02-verbatim-vs-gemini/) asked one question. Both blind judges preferred the forge answer: every quotation was exact, and its claims took a half to a third of the judge operations to check. Sol's review of that design found six weaknesses that only a different rubric can fix. Round 2 is that rubric, run on the pandemic question again (both answers reused) and on two questions the generator was never tuned on, one per corpus.

## What changed from round 1, and why

| Round 1 | Round 2 | Why |
|---|---|---|
| Each judge drew its own claim boundaries, and uncited prose went unscored | One pass ([`claims-brief.md`](claims-brief.md)) splits each answer into atomic claims, uncited ones included, and labels each one. Every judge scores the same list | Exact quotations could surround an unsupported recommendation that escaped scoring. Judges could also split compound sentences differently |
| Each judge read both answers | Each judge sees one answer only, in a fresh session. Each answer gets two judges | A passage found for one answer made the other cheaper to check |
| One support score per claim | Two: support as delivered (the answer's own pointer or shown passage) and support as recovered (the judge's own search) | A judge's search could quietly rescue a bad citation |
| `partly` covered every near miss | `partly` is split into reworded, narrower and overstated, and `no` into absent and contradicted | Different failures got the same score |
| No limit on searching | 6 judge operations per claim, then `not found` | Without a stopping rule, effort figures depend on each judge's patience |
| Library parity rested on the forge arm's five sources being in the notebook | A source manifest for both arms, and the notebook's one source outside the corpus (Chris's *Come Prepared to Die*) unticked | Gemini cited a source the forge arm could not have used |

The forge package changed too. Each fix came from a defect the round-1 judges found:

- **Built in the same step as the page.** `render.py` now writes `answer.md` through [`flatten.py`](../../../../scripts/verbatim/flatten.py), from the same data as the page. In round 1 the package was built before the data was replaced, and one pointer named an endnotes page.
- **Highlight drawn into the image.** The hit page's PNG now carries the highlight itself, so it shows wherever the image is opened. Before, only the report page drew it.
- **Paragraph context restored.** Some PDF conversions dropped the blank lines between paragraphs. The resolver now finds the paragraph ends those conversions lost, so a span's paragraph is a paragraph again, not a 2,000-word block.

## Design

- **Questions.** Each runs over one corpus only, against the notebook that holds it.

  | # | Question | Corpus and notebook | Forge answer | Gemini answer |
  |---|---|---|---|---|
  | 1 | How can NZ better prepare itself for the next pandemic? | `aarbuddy`, the AARBuddy notebook | round 1's, reused | round 1's, reused |
  | 2 | The non-duality question, word for word as in `verbatim-reports/non-duality/question.txt` | `aarbuddy`, the AARBuddy notebook | `verbatim-reports/non-duality/` | asked fresh |
  | 3 | Please draw some interesting parallels between US Marines war-fighting doctrine and modern "textbook" business administration. | `demo`, the demo notebook | `verbatim-reports/marines-business/` | asked fresh |

  Question 1 is the control: the same two answers as round 1, under the stricter rubric. If round 1's verdict holds there, a different result on questions 2 and 3 comes from the question, not the rubric. All three forge reports were re-rendered at `785acff6` with no new model call.

  Question 2 was written for Gemini and asks for a chat memo; the forge arm answers it as a report page. Judging is by claim, so the form does not enter the scores, but the write-up says so. Gemini's saved 31 October answer to it ran under a custom chat style, so it is asked again at Default.
- **The two arms' libraries.**
  - Forge: the `aarbuddy` corpus for questions 1 and 2, the `demo` corpus for question 3.
  - Gemini: the AARBuddy notebook, with *Come Prepared to Die* unticked, and the demo notebook. Before the first question, export each notebook's source list and match it against its corpus's `slug-table.json` into `manifest.md`, listing what is in one and not the other.
- **Gemini arm.** Each question is asked once, in a cleared chat, at Default style and length. Restore the notebook's custom chat setting afterwards. Capture every citation popup in full, without picking among them.
- **Forge arm.** `generate.py --model opus --joins both`. The evaluated deliverable is `answer.md` as `render.py` writes it, with its paths rewritten to the judges' neutral path (`flatten.py --base`).
- **Identity masking.** Judges reach the files through a neutral symlink, and nothing names either tool. The two arms still differ in form: pointer blocks and page images against citation popups. Judges record a guess at which tool made the answer, after scoring.
- **Judges' library.** The original of every source either answer cites, or converted text where no original is held. A source with neither is scored from the passage the answer shows, and marked as such.

## Procedure, per question

1. **Claims.** One Opus agent runs [`claims-brief.md`](claims-brief.md) on each answer separately and writes `claims-A.md` and `claims-B.md`. Chris or the orchestrating session spot-checks the split before judging.
2. **Judges.** Four fresh Opus agents, each running [`judge-brief.md`](judge-brief.md) on one answer and its claim list. Two judge answer A and two judge answer B.
3. **Results.** For each answer, report:
   - quotation fidelity, with its denominator;
   - support for substantive claims, delivered and recovered, each with its denominator;
   - the uncited claims, by type;
   - judge operations per claim, separately for claims checked and claims not found;
   - the completion rate;
   - where the two judges of the same answer disagree.

   Steps are judge operations under the brief's counting rule, not human effort.

**Related.** The [case-citations round](../2026-11-case-citations/) is the larger study of the same comparison: 30 answers and about 1,500 citations, graded by two model families. It graded every citation on whether its chunk or source carries the claim, and found 19% of Gemini's markers do, against 83% of `answer-from-corpus`'s credits. That round's figures and this one's don't compare: it scores each marker, this round each claim. [Round 3](../2026-11-02-verbatim-case-citations/) puts verbatim mode on that round's cases and rubric.

## Results

These hold for these six answers to these three questions. The forge deliverable judged is `answer.md` as `render.py` writes it, paths rewritten to the judges' neutral path. "Operations" are judge operations under the brief's counting rule, not human effort.

### How the Gemini arm ran

- **Libraries.** [`manifest.md`](manifest.md) gives both arms' source counts. The AARBuddy notebook holds all but eight of the `aarbuddy` corpus's sources, low hundreds in all. Of the eight, four uploads failed, two were ingested after it was built, two were never uploaded. Four notebook files are not corpus sources: *Come Prepared to Die* (unticked for question 2), a synthetic incident case and two lens specs. The demo notebook holds all 31 demo sources and nothing else.
- **Question 2.** Asked once, word for word, at Default style and length, in a cleared chat, with *Come Prepared to Die* unticked. Saving the Default setting sent the notebook's own suggested prompt, as in round 1; the chat was cleared again before the question. Afterwards the custom chat setting was restored, the chat cleared and the source re-ticked. Gemini answered with a memo of about 1,500 words, 65 distinct citations (115 markers). Its header read "FROM: Gemini Notebook"; the judges' copy redacts that one line.
- **Question 3.** Asked once in the demo notebook, already at Default. Its chat held one earlier exchange, saved before clearing (`gemini-notebook-arm/demo-notebook-chat-2026-11-01.md`). The answer, about 700 words, has 38 distinct citations (69 markers) to six sources.
- **Capture.** Every popup was captured in full and moved to disk through the clipboard, so the passages are byte-exact. Question 1 reuses round 1's capture.
- **Judges' library.** Originals of every source either answer cites, converted text for the six with none. Four of the files Gemini cites are one course's session notes, rebuilt from its session PDFs as uploaded, one bookmark per session; the upload-time files are gone. Question 1's *Come Prepared to Die* citations were scored from the shown passages.

### Claims

| | Q1 forge | Q1 Gemini | Q2 forge | Q2 Gemini | Q3 forge | Q3 Gemini |
|---|---|---|---|---|---|---|
| Quotations | 14 | 0 (one quoted phrase) | 14 | 12 | 14 | 1 |
| Attributed | 16 | 9 | 33 | 43 | 40 | 38 |
| Applications (marked / unmarked) | 9 / 0 | 0 / 19 | 18 / 7 | 0 / 23 | 11 / 0 | 0 / 4 |
| Uncited facts | 14 | 0 | 13 | 1 | 5 | 0 |
| Uncited recommendations | 1 | 0 | 1 | 1 | 1 | 0 |
| Framing (not scored) | 6 | 7 | 8 | 19 | 10 | 8 |

The forge answers state at the start what the corpus can't answer and what to ingest; those sentences are most of their uncited facts. The rest are short lead-ins that paraphrase the next quotation's source without carrying its pointer, which the claims brief types as uncited because the sentence itself cites nothing. Gemini's applications to the question carry citations but never mark the step as the answer's own; the forge answers mark theirs, except seven in question 2.

### Support and effort, per answer, judge 1 / judge 2

Quotation fidelity counts exact quotations over all quotations. "Delivered" covers quotations and attributed claims, scored from the answer's own pointer or shown passage; "recovered" is the judge's own search on the claims not `yes` on delivery.

| | Quotations exact | Delivered `yes` | Delivered, the rest | Recovered `yes` | Not found | Applications: source says it |
|---|---|---|---|---|---|---|
| **Q1 forge** (control) | 14/14, 14/14 | 26/30, 26/30 | 3 narrower, 1 overstated (both) | 2/4, 3/4 | 0 | 8/9, 8/9 |
| **Q1 Gemini** (control) | 1/1 phrase | 5/9, 5/9 | 4 overstated (both) | 1/4, 1/4 | 0 | 15/19, 15/19 |
| **Q2 forge** | 12/14, 14/14 | 27/47, 31/47 | 8 absent (both; no pointer), 7–8 narrower, 1–2 overstated, 2 reworded (judge 1) | 16/20, 15/16 | 0 | 15/25, 19/25 |
| **Q2 Gemini** | 8/12, 8/12 against the shown passage; 11/12 against the full source | 21/55, 23/55 | 12–16 overstated, 9–11 narrower, 5 absent, 3 reworded, 1 contradicted | 11/34, 12/32 | 8, 1 | 5/23, 1/23 |
| **Q3 forge** | 14/14, 13/14 | 31/54, 28/54 | 20–25 absent (22 with no pointer), 1–2 overstated, 1 narrower | 17/23, 21/26 | 2, 0 | 6/11, 11/11 |
| **Q3 Gemini** | 1/1, 1/1 | 24/39, 24/39 | 7–12 overstated, 1–6 narrower, 2 absent | 7/15, 6/15 | 5, 5 | 2/4, 2/4 |

Operations per claim, judge 1 / judge 2:

| | Delivered `yes` | Recovered | Not found |
|---|---|---|---|
| Q1 forge | 0.58 / 0.54 | 1.0 / 2.0 | none |
| Q1 Gemini | 0 / 1.75 | 2.0 / 2.9 | none |
| Q2 forge | 0.44 / 0.38 | 2.0 / 1.4 | none |
| Q2 Gemini | 0 / 0.33 | 1.1 / 1.1 | 1.5 / 1.5 |
| Q3 forge | 0.86 / 1.0 | 2.0 / 2.2 | 2.0 / none |
| Q3 Gemini | 0 / 0.04 | 2.5 / 1.5 | 2.6 / 1.6 |

Completion was 100%: all twelve judges scored every claim in their list. Judge 2 on Q1 Gemini confirmed each shown passage against its source with a search, which is why its delivered figure is not zero; the others took the shown passage as read, as the brief allows.

### What the scores are made of

- **Quotation fidelity.** The forge answers' 42 quotations are word for word with the converted text in every reading. Three carry what the converter left in the text: table pipes inside a Parsons quotation, pandoc's `:::` and `>` markers inside a Heifetz one (question 2), and an OCR'd heading, "AID" for "AND", inside an MCDP 1 one (question 3). One judge of each pair scored them `reworded`, the other exact with a note. The resolver places what the converted text holds; it doesn't strip converter markup or catch OCR slips. Gemini's question-2 memo puts twelve phrases in quotation marks: four don't match the passage shown, and one ("adaptive diagnosis", credited to Heifetz) is in neither the passage nor the book. It also names Tony Parsons as "Richard Parsons".
- **Gemini's support gap** is the round-1 pattern, now with its own labels. Claims firm up or add to their passages (`overstated`: far-UVC, "uniquely positioned", "significantly"), or rest on a passage beside the point (`absent`, `narrower`). One question-2 claim says the opposite of its Heifetz passage. On question 2 most of its 23 applications step from contemplative practice to corporate leadership without marking the step, and both judges scored all but a few `overstated` or `absent`. Its passages themselves were genuine wherever a judge checked.
- **The forge answers' gap** is pointers, not wording. Every quotation has a converted line that resolves exactly, plus its paragraph, so a quotation and the paraphrase around it check in about one operation. But attributed sentences written between the placed quotations carry no pointer: 8 of 47 in question 2 and 22 of 54 in question 3. On delivery those score `absent`. On recovery 15–21 of them were found in the source, so the claims are mostly sound, but the reader must search for them. This is what puts the forge answer below Gemini on delivered support for question 3 (52–57% against 62%), while it stays ahead once recovered (89–91% of its quotations and attributed claims, against 77–79%).
- **Effort.** Under round 1's counting, the forge answer took a half to a third of the operations. Under this brief, a passage the answer shows costs nothing, and Gemini shows one for every marker, so its supported claims cost nothing to check. The forge answer's cost an open per quotation, under one operation per claim. Recovery costs about the same for both, one to three operations. The forge answer's real saving is on claims that don't hold: a line pointer lets a judge find the right place in one step. Gemini names the book only, so a judge searches the whole file.

### Where the two judges of one answer disagree

- **Q1, both answers:** no disagreement. Both judges gave every claim the same delivered score.
- **Q3 Gemini:** five splits, all `narrower` against `overstated`; the same claims fell short.
- **Q3 forge:** six splits on attributed claims, all about whether a pointer's passage bears on the claim (`yes` or `overstated` against `absent`), plus the OCR quotation.
- **Q2 forge:** eight splits on attributed claims and the two markup quotations; on applications, judge 1 judged 15 of 25 `yes` and judge 2 19.
- **Q2 Gemini:** 14 splits over 78, mostly `overstated` against `narrower`, and on applications judge 1 found 5 `yes` against judge 2's 1. On `yes` against everything else they agreed on 70 of 78.

### Is round 1's verdict holding?

- **On question 1, the control, the direction holds and the gap narrows.** The forge answer: 26 of 30 cited claims and 8 of 9 applications supported as delivered. Gemini: 5 of 9 attributed claims and 15 of 19 applications. Round 1's judges gave Gemini 12 of 23 `yes`. With one answer per judge, a shared claim list, and `overstated` kept apart from narrower or reworded quotations, Gemini scores higher than it did, and the forge answer about the same.
- **On question 2, a new question over the same corpus, it holds.** Forge 57–66% of quotations and attributed claims supported as delivered against Gemini's 38–42%. On recovery the forge answer reaches 91–98% and Gemini 58–64%.
- **On question 3, over the demo corpus, it splits by measure.** Gemini is ahead on delivered support (62% against 52–57%), the forge answer once recovered (89–91% against 77–79%). Its quotations stay exact, and its applications are marked as its own.
- **Identity masking was thin.** All six Gemini judges guessed a NotebookLM-style tool. All six forge judges guessed a quote-locating pipeline with an LLM writer.

### Sol re-grade

Six Sol judges (`gpt-6.1-sol`, Codex `exec`, read-only sandbox), one per answer, a model family that wrote neither answer. Each got the Opus judges' brief, claim list, answer and library, through the same neutral paths, changed only to return its result as its final message. All six scored every claim. Figures cover quotations and attributed claims, as in the table above; Opus is judge 1 / judge 2.

| | Delivered `yes`, Opus | Delivered `yes`, Sol | Supported once recovered, Opus | Supported once recovered, Sol | Sol agrees with each Opus judge on `yes` / not `yes` | The two Opus judges agree |
|---|---|---|---|---|---|---|
| **Q1 forge** | 26/30, 26/30 | 29/30 | 28/30, 29/30 | 29/30 | 27/30, 27/30 | 30/30 |
| **Q1 Gemini** | 5/9, 5/9 | 4/9 | 6/9, 6/9 | 5/9 | 8/9, 8/9 | 9/9 |
| **Q2 forge** | 27/47, 31/47 | 30/47 | 43/47, 46/47 | 41/47 | 40/47, 40/47 | 41/47 |
| **Q2 Gemini** | 21/55, 23/55 | 26/55 | 32/55, 35/55 | 38/55 | 44/55, 46/55 | 51/55 |
| **Q3 forge** | 31/54, 28/54 | 37/54 | 48/54, 49/54 | 48/54 | 46/54, 43/54 | 51/54 |
| **Q3 Gemini** | 24/39, 24/39 | 25/39 | 31/39, 30/39 | 28/39 | 34/39, 34/39 | 39/39 |

Sol agrees with an Opus judge on 397 of 468 delivered calls (85%); the two Opus judges agree with each other on 221 of 234 (94%).

- **Question 1 holds, and the gap widens.** Sol gives the forge answer 29 of 30 and Gemini 4 of 9. Its three splits on the forge answer are claims the Opus judges called narrower or overstated and Sol called supported. Its one split on Gemini goes the other way.
- **Question 2 holds, by a smaller margin.** Forge 64% against Gemini 47% as delivered, 87% against 69% once recovered. Sol is milder than Opus on Gemini's overstatement (7 `overstated`, against 12–16) and stricter on its quotations: 5 of 12 exact against the shown passage, counting two hyphenation differences, and 9 of 12 against the full source. The forge answer's quotations are 14 of 14 again.
- **Question 3's split does not hold under Sol.** Sol puts the forge answer ahead on both measures: 69% against 64% as delivered, 89% against 72% once recovered. The difference is how the judges read "pointer". Of the forge answer's 22 attributed sentences with no pointer, Opus scored all but a few `absent` on delivery. Sol scored 8 of them `yes`, taking the source the sentence names, or the passage shown beside it, as what the answer gives. Under the Opus reading Gemini leads on delivered support; under Sol's, the forge answer does. Question 3's delivered lead sits inside that ambiguity. The brief should say whether a source named in the sentence counts as a pointer, and the forge answer should carry pointers on those sentences either way.
- **Effort is not comparable across the families.** Sol charged opening a file and searching it as two operations, so its recovery costs (3 to 5 operations per claim) run above the Opus judges' (1 to 3) for both answers.
- **Identity.** Sol's three forge judges guessed a corpus-retrieval tool with file and line pointers; its three Gemini judges guessed a document-retrieval chatbot. None named a product.

### Files

Copyrighted text stays under `corpus.local/aarbuddy/projects/verbatim-reports/`:

- `{nz-pandemic,non-duality,marines-business}/r2/`: `answer-A.md`, `answer-B.md`, both `claims-*.md` and their briefs, `originals/`, `converted-only/`, `judges/{A1,A2,B1,B2}/` (brief and result), and `judges/sol-{A,B}/` (brief, result and Codex log).
- `{non-duality,marines-business}/judge/gemini-answer.md`: the Gemini captures, with every passage.
- `{each}/judge/r2-key.md`: which arm is A and which B, and the library list.
- The judges reached these files through the symlinks `corpus.local/aarbuddy/projects/r2-q{1,2,3}`.

## What this round still cannot show

- Two or three questions are still a handful. They can show whether round 1's result repeats, not how often it holds.
- Judges are Opus with shell tools. A person with a PDF reader would find different steps cheap.
- The pandemic question is a development example: the resolver and renderer were fixed on its run.
