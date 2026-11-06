# Gemini Notebook with a strict chat style: can a prompt fix the citations?

**Status: run 5 November 2026.** Ten Gemini answers under a one-paragraph custom chat style, four on the public notebook and six on the private one, graded by two model families with the method used on the same cases at Gemini's default style. The style roughly doubles how often a cited sentence is carried by its markers: from about 40% to about 72% across both notebooks. On the public notebook that is the pre-registered "helps"; on the private one both families put it above 70%, the "fixes" bar. Gemini gets there mostly by citing less: it moves its own reasoning into uncited sentences marked "My inference:".

The design was committed before the first run: [`DESIGN.md`](DESIGN.md), with the style text in [`style.txt`](style.txt). The private half was added after the public result, on the same design.

## The style

Custom chat style, response length Default, every source ticked:

> Attach a citation only to a sentence that says what the cited passage itself says. Do not add numbers, percentages, causes, examples, or applications to the user's situation that the passage does not contain, and do not make the passage's claim stronger or broader than it is. When you apply a source to the user's case, or draw your own conclusion, put that in a separate sentence that starts "My inference:" and carries no citation. Put words in quotation marks only when they appear word for word in a source. If no passage supports a point, say that no source in this notebook covers it rather than citing a nearby passage. Keep the answer in the chat.

Each notebook went back to its earlier setting after the last run (the public one to Default, the private one to its own custom style).

## Runs

- **Public:** the 35-source demo notebook, C1 and C2 from the [case-citations round](../2026-11-case-citations/), twice each, with that round's "Answer here in the chat." line.
- **Private:** the 292-source AARBuddy notebook, C1, C2 and C3, twice each. Captures, packets and scores stay outside the repo; this README gives counts only.
- **Capture:** the case-citations round's [`capture.js`](../2026-11-case-citations/capture.js); chat history deleted and Studio empty before each run. Public captures are in [`runs/`](runs/), packets in [`packets/`](packets/).
- **Comparison:** the same cases' default-style chat runs, already graded per marker by Sol and jointly per sentence by Sol and Opus.

## Scoring

The same three steps as the default-style re-grade, so the two columns compare:

1. **Per marker:** the case-citations [scoring brief](../2026-11-case-citations/scores/scoring-brief.md), by Sol (`gpt-6.1-sol`, reasoning effort high) and Opus 5.5 (effort high). "My inference:" sentences carry no marker and are not graded.
2. **Joint, per sentence:** every cited sentence with two or more markers and none that carries the claim alone, re-graded with its markers together ([`joint/brief.md`](joint/brief.md)), by both families; up to six single-marker sentences per answer mixed in blind as controls.
3. **Per sentence:** a cited sentence counts as carried if one marker carries it in Sol's first pass, or its markers together carry it in that family's joint grade.

## Results

| Gemini | Public, default | Public, strict | Private, default | Private, strict |
|---|---|---|---|---|
| Answers | 4 | 4 | 6 | 6 |
| Markers / cited sentences | 404 / 165 | 220 / 109 | 728 / 286 | 231 / 146 |
| Markers carrying their sentence (Sol) | 17% | 30% | 20% | 52% |
| Sentences carried by one marker (Sol) | 28% | 52% | 35% | 71% |
| **Sentences carried by their markers together, Sol** | **37%** | **67%** | **42%** | **77%** |
| **Same, Opus** | **35%** | **64%** | **41%** | **76%** |

Across both notebooks: 40% (Sol) and 39% (Opus) at default, 73% and 71% under the strict style.

- **Against the pre-registered bar.** It helps on both notebooks (a rise of 10 points or more in both families). It fixes on the private notebook (70% or more in both) and falls short of that on the public one.
- **How.** Gemini cites fewer sentences, and about as many of them are carried as before (112 against 121 on the private notebook, 73 against 61 on the public). The overreach moves into 8 to 16 "My inference:" sentences per answer, uncited and marked as Gemini's own.
- **Agreement.** On the stacked sentences re-graded jointly, Sol and Opus agree on carried-or-not for 40 of 45 (public) and 28 of 33 (private); on the blind controls, 21 of 24 and 28 of 33.
- **Quotations.** Located by the case-citations round's check (whole-corpus search on the public notebook; first six words by grep on the private one, which misses line-broken quotations): public 1 of 9 at default against 9 of 11 strict; private 0 of 15 against 9 of 17.
- **Coverage.** The design measured coverage against the case-citations answer keys. That measure was dropped after the run, because Claude wrote the keys and Claude also wrote one of the arms' answers; coverage is reported from the [pooled-coverage round](../2026-11-05-pooled-coverage/) instead, which pools the ideas across every answer with no list written in advance. For the record, against the keys the strict answers covered 33 key ideas against 35 at default on the public notebook (Sol), and 23 against 30 on the private one.

## Which Gemini

Every Gemini run in this round and the default-style rounds used Gemini Notebook on Google's Pro plan, between 31 October and 5 November 2026. Google says Notebook runs on Gemini 3.5 models, and the answers showed the reasoning panel that came with that June upgrade; it doesn't say which model answers a given chat. Its newest model, Gemini 4 Argon, opened to Pro and Ultra subscribers in the Gemini app on 13 October and hasn't been announced for Notebook. The Ultra plan, which has higher usage limits and more sources per notebook, wasn't tested.

**Argon over the same notebook, one unscored run.** On 6 November the Gemini app, with Argon at its High thinking level, answered C1 over the public notebook, with the strict style pasted at the top of the question ([`runs/argon-app-demo-C1.txt`](runs/argon-app-demo-C1.txt), source chips marked `[CHIP: …]`). It wrote 4,289 words with 14 "My inference:" sentences. Its citations are 17 chips, one per section, each naming several whole files; opening one lists file names, with no passage, page or line, so the answer can't be graded at the sentence-and-chunk grain the Notebook runs were. [`verbatim_runs.py`](verbatim_runs.py) finds 15 of its 75 unquoted sentences of eight words or more copied word for word from a source with no quotation marks, and 3 of its 22 quotations of five words or more in a source word for word. A third run of the same question, screenshotted in [`runs/argon-screens/`](runs/argon-screens/), showed the same form, and its Sources panel listed web pages as well as notebook files (reddit.com, scribd.com, docs.wixstatic.com), with a note that the response "may include quotes" from five more sites. The Gemini app doesn't keep chats while Gemini Apps Activity is off, so only the first saved run's text is here.

## Limits

Ten answers over five cases and one style give a direction, not a rate. The style text was written once and not tuned. The joint pass grades a little stricter than the per-marker pass: on the blind controls, first-pass `supports` dropped to partial for 8 of 28 (Sol) and 9 of 28 (Opus) at default, and for 6 of 52 and 8 of 52 under the strict style. Both columns lean the same way, the default one slightly more. grounded-forge's own answers are not in this round; graded per sentence by the same first pass, `answer-from-corpus` carried 86% (public) and 82% (private) of its cited sentences in the case-citations round.
