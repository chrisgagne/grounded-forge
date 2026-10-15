# Pass I source audit: why-language-models-hallucinate-kalai

- **Date:** 2026-10-15
- **Auditor:** Claude Opus 5.5, fresh subagent, fix-in-place mode (same-family leg; the generator was gpt-5-codex). A blind codex leg runs in parallel on a frozen copy; the driver stamps once both legs are done. **Not stamped here.**
- **Deep reference:** `references/why-language-models-hallucinate-kalai-deep.md`, read in full (363/363 lines pre-edit).
- **Source tape:** `sources/converted/why-language-models-hallucinate-kalai.md`, read in full (1161/1161 lines: body, appendices A–F, bibliography, footnotes).
- **Original / page renders:** original PDF not available; no renders made. The figure images named in the tape (`why-language-models-hallucinate-images/…`) are not on disk either, so Figure 1 and Figure 2 could not be inspected.
- **Calibration:** read the Pass I section and failure-mode reference, plus fixtures 01, 07 and 12.

## Counts

| | n |
|---|---|
| Claim units audited (marked prose claims, header/structure lines, evidence-map rows, integrity notes) | ~112 |
| Source-anchored as written | ~92 |
| Stripped (source-external framing) | 7 |
| Corrected (claim narrowed to what the tape says) | 9 |
| Marker-corrected (`[V]` → `[AP]`/`[AR]`) | 6 |
| Quotations corrected (wording) | 0 |
| Quotations reformatted so the verbatim check can see them | 5 |
| Coverage added (TOC section with no body anchor) | 1 section (§2), 6 bullets |

`check-verbatim.py`: 10 `no-quote` before; **no findings** after. All quotation wording already matched the tape. The checker skips a blockquote's text unless it contains quotation marks, so the five bare blockquotes (confidence-target instruction, and the four in §9) were compared by hand against tape lines 414, 75, 198, 436 and 456. All five match.

## TOC-vs-anchors

Fail condition met at intake: **§2 "Related work" was listed in the Structure line but had no body anchor anywhere in the deep reference.** I read §2 (tape 83–95) and added "§10 Connections the authors make in the text" (6 bullets, `[AP]`/`[BT]`/`[V]`), then renumbered Evidence map → §11 and Citation notes → §12. In-text citations in the tape are blank (pandoc dropped the author names, e.g. "is by , which we show…"), so the cited works are described as the paper frames them and not named. Naming them would mean inferring identities from the bibliography. Every other TOC section and appendix A–F has body anchors.

## Changes (line numbers are pre-edit)

### Stripped: source-external framing

1. **L19:** "The title should not be read as asserting one universal mechanism." Reading-guidance with no passage behind it. Replaced with the source's own words, "may occur due to a combination of multiple factors" `[V]` (§3.4, tape 343).
2. **L115:** "This is a deliberately limited calibration claim" and "the result does not say that all confidence statements from a post-trained assistant are calibrated." The first is an evaluative label and the second a boundary the paper doesn't draw. Rewritten to what §3.1 and App. D say: uniform p̂ gives δ=0 without knowing the language; "it is easy to have weakly calibrated responses" (tape 169, 869).
3. **L119:** "emphatic qualifier" is an evaluative label. Now "The paper's heading reads".
4. **L147:** "showing that the dependence is not merely an artefact of the lower-bound technique." This is the ingester's tightness verdict; the paper only states the upper bound. The upper bound is now transcribed.
5. **L149:** "The result does not establish that the measured hallucination rate of every deployed model equals the singleton rate." No passage. Stripped; the anchored sentence after it stays.
6. **L208:** "It is a decision-theoretic property of binary scoring, not an empirical claim about a particular training run." No passage. Replaced with what the paper says: the proof is "trivial" (tape 373).
7. **L269:** "This is not a claim that retrieval is ineffective. It is a claim that retrieval does not remove every statistical or incentive-based failure mode." This is an invented-opposition form, and "every … failure mode" over-generalises. Replaced with the source's concession (studies show search/RAG reduce hallucinations) plus "not panaceas".

### Corrected: claim narrowed to the tape

1. **L38, dissertation (fabrication-direction error):** "Three models also invented different titles, *institutions*, and dates". ChatGPT's answer named CMU, and the paper's own bibliography lists Kalai's thesis as Carnegie Mellon (tape 1025). The table caption only claims "None generated the correct title or year" (tape 48). Narrowed to titles and years.
2. **L52:** "applies whether the model uses reasoning, search, retrieval, or another architecture". "Another architecture" extends the source. Now "applies broadly, including to reasoning and search-and-retrieval language models" (tape 32).
3. **L56:** "turn a base density estimator into a useful assistant" and "scoring … abstentions as wrong". Now in the source's terms: "from one trained like an autocomplete model to one that does not output confident falsehoods", with abstentions given "no credit" (tape 355, 75).
4. **L119:** "fixed, *verified* set of questions" and the paraphrase of the calibration point. Now: question-answer database plus calculator, otherwise IDK; models that do not err "must not be calibrated" (tape 200).
5. **L121, Figure 2:** "the post-reinforcement-learning model was not similarly calibrated". The caption states only that the pretrained model is well calibrated, and the right-hand panel can't be inspected (no image, no PDF). Narrowed to the caption plus the text's contrast with post-trained models that "may deviate" (tape 200, 208).
6. **L127:** "develops two factors formally and names three additional ones". Computational hardness gets a formal treatment in App. D (Observation 2). Corrected.
7. **L177:** "The authors do not claim distribution shift is the only explanation". An invented negative. Now in the source's terms: distribution shift "could be a factor"; poor models "may be a greater factor" (tape 347).
8. **L220, WildBench:** "a partly helpful answer". The source's term is a "fair" response with factual errors (5–6) against IDK (3–4) (tape 927–929).
9. **L267:** "Search also does not directly solve intrinsic errors". The source hedges: "may not help with miscalculations … or other intrinsic hallucinations" (tape 438).

### Marker corrections

- **L90, L105, L147, L161, L206:** `[V]` on re-typeset LaTeX formulas plus paraphrase. The formulas are faithful but not character-exact (e.g. `2\cdot` dropped), so each is now `[AP] (…; formula transcribed)`. I checked every formula's content against tape 154, 222, 268/274, 310 and 368, and all are correct.
- **L119:** one `[V]` covered the heading quote and three sentences of paraphrase. Split into `[V]` (heading) and `[AR]` (the argument).
- **L359 (integrity note):** the `[V]` definition no longer covers "a displayed result reproduced verbatim". It now records the "formula transcribed" convention and defines `[BT]`.

### Quotation formatting

- §9's four blockquotes, with `[V]` on separate lines, became inline quoted bullets so the checker verifies them. The confidence-target blockquote's `[V]` moved onto the blockquote line. Wording is unchanged.

## Checked and left as is (worth a second look by the codex leg)

- Appendix letters A–F: the tape's headings carry no letters. They are consistent with pandoc's ref numbers 8–12 (B=8 `ap:arbitrary` … F=12 `sec:prevalence`) and with the stated official PDF.
- "94-item bibliography": counted 94 entries in the tape.
- §4.2 behavioural calibration: the tape literally reads "outputting IDK among examples where its correctness probability is greater than the target" (tape 422), which inverts the sense. The deep ref follows the paper's next clause ("the most useful response in which it is at least t confident"). This is a source-side slip, not a deep-ref defect.
- §2 in the tape says the closest prior work "inspired Theorem 3" (tape 89, `thm:agnostic`), apparently a label slip in the source (the missing-mass work matches Theorem 2). The added bullet avoids the theorem number.
- §12 "Model boundary" and "Causal boundary" notes: scope statements about what the paper does not do. They don't grade the source, so I kept them; the codex leg may disagree.
- Thesis L17 "reward calibrated abstention": a slight term-of-art gloss on "rewarding appropriate expressions of uncertainty" (tape 456). Left.

## Derived tier

No distillations exist for this slug. The **light reference** (`references/why-language-models-hallucinate-kalai.md`, not edited) carries claims the deep no longer supports. The parent should re-derive it:

- L45: "This is not an estimate of every deployed model's hallucination rate." The deep sentence was stripped.
- L51: "The result is decision-theoretic; it does not estimate the causal contribution…". The deep sentence was stripped.
- L53: "may still give a partly erroneous helpful answer more credit than abstention". The deep now says a "fair" response with factual errors (5–6) vs IDK (3–4).
- L31: "A verified question-answer system … can avoid hallucinations by giving up breadth". The deep now says question-answer database plus calculator, otherwise IDK; "verified" and "giving up breadth" are unsupported.
- L78: "do not remove the incentive to guess when retrieval or reasoning fails". OK on incentive, but the intrinsic-error point is hedged in the source ("may not help").
- L37: "No classical algorithm can solve problems that violate complexity assumptions" vs the source's "can violate the laws of computational complexity theory". Minor rewording; check.
- L25: "not universal folklore". This is the light ref's own framing.
- §2 / Connections: the light ref has no related-work content. Optional addition.

## Open

- Figure 2's post-RL panel could not be checked (no original, no image assets). If the codex leg has the PDF, it can confirm whether a "not calibrated" reading is visible; the text supports only "may deviate".
- Cross-family leg pending (codex, blind).


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `b79670d62aa97c0be0f2083b1cefad25e5eb13f221e946ebe830633c52ce29fe`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `b2fda0e111db2a1f5d665738b8abf824b0923f12a5677a44a7cd1e3b79f16ac9`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_why-language-models-hallucinate-kalai_crossfamily_blind.md`, `_ingest_pass_I_why-language-models-hallucinate-kalai_crossfamily_sort.md`, `_ingest_pass_I_why-language-models-hallucinate-kalai_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 15 original defects (10 fixed by the fix-in-place audit, 5 missed by it), found 13 over-flags by the fix-in-place auditor and 0 by the blind auditor, 4 disputed findings and 1 new defect introduced by the fixer, with capture fixer=10 blind=14 both=9, and gave a pass verdict once the remaining edits were applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 10, the blind audit 14, both 9. The Chapman estimate is 15.5 in all, about 0.5 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of the five remaining edits, two were applied as written (the Lemma 2 factor of two and the §2 [AP]/[V] split), three with changed wording (the reduction-direction fix at line 17 says 'using a base language model as an IIV binary classifier', following tape 56/147; the finite-set assumption went into the no-prompt setting under §3.1/footnote 4, not §3.2; the conversion caveat names two damaged bibliography titles), and none were declined. I also fixed the same direction error at line 66 and settled disputed finding D4 by rewording missing mass as a joint probability (tape 567); disputed findings D1 to D3 stand because the source supports them.

**Gate:** accepted by operator. Deep reference sha256 `54cbfdf12daba2f71ebbc2252583afafe010ebda53353d45d4648bb2a8bc7f20`, stamp included.

## Derived-tier fidelity check (2026-10-15)

Fidelity check of the derived tier for `why-language-models-hallucinate-kalai` (Kalai, Nachum, Vempala and Zhang, "Why Language Models Hallucinate", CC BY 4.0). The derived tier for this source is the light reference only: it has no distillation and no distillation-index row. In the light reference, 71 claims were checked against the Pass I–stamped deep reference, with the tape opened where wording needed checking, and 7 were fixed in place. Two restored dropped hedges ("should have a small discrepancy"; "would realign"). Two narrowed widened scope ("well-formed calculations"; "multiple-choice generation error", with the Appendix C Theorem 4 anchor added). One corrected Theorem 2, which the light reference had stated as error "close to" the singleton rate: it is a lower bound for any algorithm, and the response-set term is restored. One removed an open-ended-output example and a "needs" the deep lacks. One fixed a label ("secure-encryption"). `check-verbatim.py` reports no findings. One deep-reference defect is recorded: an unsupported "severity" in §7's open-ended-output paraphrase.
