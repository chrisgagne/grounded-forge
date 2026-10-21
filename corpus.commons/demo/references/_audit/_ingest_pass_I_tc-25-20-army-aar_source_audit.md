# Pass I Source-Only Audit — TC 25-20 (US Army, A Leader's Guide to After-Action Reviews)

**Date:** 2026-05-13
**Auditor:** claude-opus-4-7[1m] (effort: xhigh, cold read)
**Source under audit:** `corpus.commons/demo/references/tc-25-20-army-aar-deep.md`
**Source-of-truth:** `corpus.commons/demo/sources/converted/tc-25-20-army-aar.md` (35 pages, pymupdf4llm 0.2.9 conversion, full coverage)

## Calibration

Read three fixtures before the cold read:

- `tests/audit-fixtures/01-training-leakage.md` — strip-case anchor (biographical claim the source does not make).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` — correction-case anchor ([V] on a paraphrase).
- `tests/audit-fixtures/12-clean-negative-control.md` — over-flagging anchor (clean snippet that must not be flagged).

## Audit method

Cold-read traversal of the deep reference end-to-end. For each non-trivial claim (prose, blockquote, table cell, evidence-class marker, cross-reference, thesis paragraph), trace to the converted markdown by chapter + section name and verify the source passage supports the claim.

## Findings

**Claims audited:** ~75 distinct source-grounded claims (verbatim quotations counted once each; paraphrased claims counted once each).
**Source-anchored:** 75 / 75.
**Stripped:** 0.
**Marker-corrected:** 0.
**Blockquotes verified character-by-character:** 5 / 5.

### Per-section results

| Section | Claims | Anchored | Notes |
|---|---|---|---|
| Front matter (source/structure/citation) | 5 | 5 | Authentication, distribution, proponent, licence, structure all source-anchored. |
| Author's thesis | 8 | 8 | Four thesis paragraphs; all [V]-marked text matches source verbatim. The [AP] marker on the techniques list (line 17, "(enter the discussion only when necessary; reinforce that disagreement is permissible; use open-ended and leading questions; focus on learning)") is correct — the deep ref compresses the source's bullet list into a parenthetical paraphrase. |
| Part I (Ch 1) | 12 | 12 | Definition, three things AAR provides, keystone framing, feedback definition, not-cure-alls, AAR-vs-critique blockquote (verified char-by-char), formal vs informal, pinecones worked example (verified char-by-char), four-step process. |
| Part II (Ch 2) | 14 | 14 | AAR plan elements (5), Fig 2-1 fields (7), informal/formal evaluation distinctions, two-echelons-above rule (`division evaluates battalion; brigade evaluates companies; battalion evaluates platoons; and company evaluates sections, squads, teams, or crews` — verbatim from source line 322), OC selection criteria, experience-over-rank worked example, OC apprenticeship rule, stopping-point durations (30-45 / 1 hr / 2 hr), attendance scaling, site selection, soldier comfort, training-aid Fig 2-2 (formal vs informal aid lists verified item-by-item), training-aid selection checklist, caution-block on AAR-plan changes (verified char-by-char). |
| Part III (Ch 3) | 11 | 11 | Doctrine/TO/orders/METL review, six critical events (verified item-by-item), three-phases observation framing, recording-system list, no-gadget-fetishism rule, DTG discipline, Fig 3-1 worksheet fields (8 fields verified item-by-item), OC positioning rule, communications-net monitoring, OPFOR input, organise observations, horseshoe site arrangement (cross-cited to App A), rehearsal rule. |
| Part IV (Ch 4) | 18 | 18 | Attention-getter, three opening rules (blockquote verified char-by-char), Fig 4-1 sequence (verified step-by-step), participation atmosphere, leader techniques, training-objectives review, commander's-mission framing, OPFOR commander framing, open-ended-questions rule, Bradley/hill vs engage/tanks-to-front blockquote (verified char-by-char), problem-solving framing, three discussion techniques (chronological, BOS — seven BOS verified item-by-item, key events), fratricide mandatory deep-discussion with four diagnostic questions (verified item-by-item), flexibility rule, leader-must-bullet-list, optional discussion topics (soldier/leader skills with separate-AAR rule, train-to-weakness directive, statistics double-edged-sword, others), force protection mention-every-AAR rule, closing comments + leave-area convention. |
| Part V (Ch 5) | 7 | 7 | Real-benefits-come-from-follow-up principle, T-P-U assessment, retraining-delay rule, dynamic-link framing, immediate-retraining + critical-gate-tasks rule, critical-gate-tasks definition, revised-SOPs rule, AAR-in-combat framing. |
| Part VI (Appendix A) | 8 | 8 | CTC framing, site selection (overlook areas of significant action; environmental factors), site improvement (sun, rain, snow, wind countermeasures; cost-benefit), Fig A-1 seven training-aid categories (verified item-by-item, including the *bigger than 1:50,000 if possible* map-overlay scale qualifier at line 1274 of source), simplicity-not-elaboration rule, terrain-model-fits-the-question rule (squad ambush vs marksmanship example), leader position (centrally located, elevated for large groups), horseshoe seating with rank suppression (verified char-by-char on the rank-consciousness sentence), training-aids placement rule (centrally located, terrain boards angled, TVs out of direct light, block printing). |
| Key planning targets table | 13 rows | 13 anchored | Each row sourced; lead-time, durations, seating, evaluator echelon distance, map scale, fratricide and force-protection mandates, seven BOS, three techniques, four steps, T-P-U. |
| Connections | 5 | 5 | FM 25-100, FM 25-101, AMTPs/TEOs, CATS, CTCs — each cited only because the TC cites them, with the appropriate `[BT]` markers. The FM 25-101 connection carries a verbatim quote from the Preface line 73 ("It supplements and expands the guidance in Field Manual (FM) 25-101"). |
| Positions framed against | 7 | 7 | AAR-vs-critique, AAR-vs-grading + statistics misuse, yes/no questions, training-to-strength, rank consciousness, AAR-as-cure-all, gadgetry-for-its-own-sake — each anchored to verbatim source language. |
| Citation and source-integrity notes | 5 | 5 | Conversion provenance, figure-extraction caveat (diagrams not text-extracted; body prose carries the claim), masculine-pronoun preservation rule (with Preface justification), citation-style decision, no-bibliography note. |

### Blockquotes verified char-by-char

1. Ch 1 AAR-vs-critique blockquote (deep ref line 35–36) → source line 134–139. **Match.**
2. Ch 2 caution-on-AAR-plan-changes blockquote (deep ref line 84–85) → source line 565–568. **Match.**
3. Ch 4 three-opening-rules blockquote (deep ref line 121–122) → source line 786–795. **Match.**
4. Ch 4 Bradley-vs-engage worked-contrast blockquote (deep ref line 136–141) → source line 905–911. **Match.** The single-quotation-marks-inside-double-quotation-marks formatting is preserved. The em-dash `rather than-` (source line 909) is preserved as `rather than-` rather than being smart-corrected.
5. Glossary spot-check (terms used in body prose, e.g. OPFOR, BOS, METL, AMTP, CATS, T-P-U, OC, TEO) all match the source glossary (lines 1336–1519).

### Cross-references not made

The deep reference does *not* make cross-corpus connections to:

- John Boyd's OODA loop (a frequent association with AAR methodology in the practitioner literature, but the TC does not cite Boyd).
- Donald Schön's *The Reflective Practitioner* (no citation in the source).
- Garvin or Senge on learning organisations (no citation in the source).
- Civilian AAR derivatives (CDC, NHS, school review-and-improvement cycle, Sprint Retrospective) — the TC predates and does not anticipate these.

The connections the deep reference *does* make are limited to the four explicitly cited works/concepts: FM 25-100, FM 25-101, AMTPs/TEOs, CATS, and the practical experience of CTCs. This matches the source's actual citation discipline (no bibliography beyond the two-entry References page).

### Post-source vocabulary check

The deep reference does not use vocabulary that postdates 1993:

- No "after-action review" usage outside the TC's own usage (i.e., not "AAR" in the Six Sigma sense, the Sprint Retrospective sense, or the Reason just-culture sense).
- No "psychological safety" (Edmondson, 1999).
- No "reflective practice" (Schön, 1983 — predates but not cited).
- No "learning organisation" (Senge, 1990 — predates but not cited).

The vocabulary is the TC's own: AAR, OC, OPFOR, BOS, METL, T-P-U, critical gate tasks, fratricide, troop-leading procedures, intelligence preparation of the battlefield, situational training exercise.

### Task-application-guidance check

The deep reference does not smuggle in distillation-grade content:

- No diagnostic questions for the operator (those live in the two distillations).
- No anti-pattern lists for practitioners (those live in the two distillations).
- No "how to apply this in a civilian context" guidance (the distillations carry that work).
- No "when to use" routing (that lives in the distillation indexes).

The Part-by-Part structure is descriptive of the TC's content; it does not editorialise about how to apply that content.

### Image-classification status

Image scope: **text-only** for this ingestion. Figures 1-1, 1-2, 1-3, 1-4, 3-3 are referenced by name in the converted markdown but their diagram content was not text-extracted (these are bitmap/vector diagrams in the original PDF, not text-rendered tables). The deep reference notes this in *Citation and source-integrity notes* (line 263). Figures 2-1, 2-2, 4-2, A-1 survived as markdown tables/lists and are captured. Figure 4-1 was carried as a text outline in the source and is captured verbatim in Part IV.

Image classification can be completed later via the `ingesting-images` skill against `corpus.commons/demo/sources/original/tc-25-20-army-aar.pdf`.

## Verdict

**PASS.** The deep reference is source-grounded and ships.

- All 75 substantive claims trace to passages in the converted markdown.
- All 5 blockquotes verified character-by-character against the source.
- All evidence-class markers ([V], [AP], [BT]) match their content.
- No training-data leakage, no post-source vocabulary, no cross-corpus drift, no task-application guidance smuggled into the deep tier, no silent partial coverage.

Light reference and distillations derive from this audited deep, so the discipline propagates by construction.

## Pass I confidence and known limitations

The TC is a short doctrine document (35 pages, 52 KB of markdown). The audit's claim count is correspondingly modest (~75 versus a typical 200–800 for a full-length book). The audit is high-confidence because (a) the source is short enough for full traversal, (b) the conversion preserved structure cleanly, (c) the TC's prose is unusually quotable so most claims could be carried as [V] with verbatim text. The remaining audit risk is at the boundary between [V] and [AP] — where the deep ref paraphrases the source's directives. This audit treated paraphrase claims as [AP] when the deep ref's wording materially differs from the source and as [V] only when the deep ref reproduces the source's language exactly within quotation marks. A stricter pass might re-mark a few [AP] cases that include very short direct phrases lifted from the source (e.g. "low-key", "professional discussion") as mixed [V/AP], but this would not change the substance of any claim.

## Scoped re-audit 2026-10-16: restored Figures 1-1 to 1-4

**Auditor:** fresh-context Claude subagent (Opus 5.5), same family as the generator; the cross-family (codex) leg ran blind in parallel on a frozen copy and its findings sit outside this section.
**Scope:** the material restored by the 2026-10-16 re-conversion and the deep-reference text written for it. Everything else in the deep reference is unchanged since the 2026-05-13 audit and was not re-audited.

**Tape read in full:** lines 100–345 (Ch 1 "Definition and Purpose" through Figure 1-4, into Ch 2 "The After-Action Review Plan"), 760–800 (Figure 4-1) and 885–897 (Figure 4-2). The Ch 2 and Ch 3 ALL-CAPS headings were listed by grep. No other part of the tape was read.
**Deep reference read:** all 296 lines; the in-scope lines (9, 17, 19, 44–58, 70–78, 178, the two new Key planning targets rows, the first integrity-note paragraph) traced claim by claim.
**Other checks:** `pdfinfo` (35 pages, matches the Coverage line); `pdftotext -layout` of PDF pp. 6–7; one page render (PDF p. 6, printed p. 3: Figures 1-2 and 1-3); a line-by-line comparison of the earlier pymupdf4llm conversion (git `ae65b5e5`) against the new tape. Six lines miss only because the old conversion fused table cells with `<br>` and merged the title-page header cells. The text is all present, so the Coverage line's "every line of the earlier conversion is present" holds.

**Verbatim check (before):** 1 `near`, line 178 (Figure 4-2 BOS technique quote). The tape's difference is the running header and folio ("TC 25-20 19") inside the paragraph, plus "Figure 4- 2" split across a line. That is conversion noise, not a defect; no fix. After the fixes the check reports the same single `near` and nothing else.

### Counts

- Claims audited: 44
- Source-anchored as written: 41
- Stripped: 0
- Marker-corrected: 0
- Quotation-corrected: 0
- Prose corrected: 3

### Changes

1. **Line 17 (thesis ¶3), source-external framing.** "The same emphasis opens the circular: among the 'key points in all AARs', Figure 1-1 lists that AARs…" → "Chapter 1 lists two related practices among the 'key points in all AARs': Figure 1-1 says that AARs…". The Preface, not Figure 1-1, opens the circular (and ¶3 already quotes it), and the TC doesn't present Figure 1-1 as being about spirit or climate. The two quoted items do match Ch 4's techniques (participation, open-ended questions), so the link is kept, worded as a correspondence.
2. **Line 46 (Figure 1-2), inaccurate count.** "Three items carry a gloss in parentheses: …" → "The parentheticals include …". Figure 1-2 has more parentheticals than three: "(when appropriate)", "(discussed throughout)" and "(summary)" as well as the three quoted (tape 185–194; PDF p. 6 render). The three quotations themselves are verbatim and stay [V].
3. **Line 290 (integrity notes ¶1), inaccurate provenance claim.** Figure 4-1 "is captured verbatim in Part IV above" → "is given in Part IV above as an outline of its headings". Part IV line 149 joins the headings with arrows, lower-cases sub-items, and drops Figure 4-1's "(what was supposed to happen)" after "Commander's mission/intent" (tape 773). So it isn't a verbatim capture.

### Anchored without change (summary)

- Line 9 Coverage: 35 pages; pymupdf4llm dropped the four figures and the re-conversion restored them (source card, "Conversion"). Old-conversion lines are present (checked above).
- Line 19: Figure 1-4 lists actions under each step (tape 290–329).
- Lines 44–58: the NOTE (tape 166–167) supports "lists the key points", "shows the AAR format" and "lists characteristics". Figure 1-1 has eight items and Figure 1-2 has ten, both quoted word for word (bullets are drawn, so items are joined with spaces). All ten Figure 1-3 cells are verbatim; "Have external observers and controllers (OCs)" correctly has no period. The PDF p. 6 render confirms that the figure sets the two lists side by side in framed boxes, so the row pairing follows their order. Ch 3 "Rehearse" has the leader review the AAR format (Figure 1-2). Figure 4-1 gives the same sequence grouped (tape 765–797).
- Lines 70–75: the NOTE quote (tape 290–291), the caption "The AAR Process", the four headings and all four action lists are verbatim. "tutors" is as printed (PDF p. 8, per dispatch).
- Lines 77–78: checked against the headings. Figure 1-4's Planning items run in the order of Ch 2's sections after the opening "The After-Action Review Plan" (Selecting and Training OCs → Reviewing the T&E Plan → Scheduling Stopping Points → Determining Attendance → Selecting Potential AAR Sites → Choosing Training Aids → Reviewing the AAR Plan). Its Preparation items run in the order of Ch 3's eight sections (Review Doctrine… → Identify Key Events → Observe… → Collect Observations → Organize Observations → Select and Reconnoiter → Prepare the AAR Site → Rehearse). The claim holds.
- Line 178: "Command and Control (C2)" matches Figure 4-2 (tape 895).
- Key planning targets: "Key points in all AARs" (8) and "Items in the AAR format" (10). Counts and end-item quotations match.
- Integrity notes ¶1: "framed boxes, not diagrams" matches the p. 6 render. Drawn bullets, "C2" and Figure 3-3 as a picture all agree with the source card.

### Derived-tier claims the edits touch (for the parent to re-derive; not edited here)

- **"Three glossed items" framing (change 2).** AAR distillation concept 17 ("glosses three of its items"). Retro distillation concept 13 ("glosses three of its items"). `AAR-DISTILLATION-INDEX.md` row "Check the plan and the run against the TC's checklists" ("Figure 1-2's format glosses three items as…"). `RETRO-DISTILLATION-INDEX.md` row "Walk the AAR's three questions in order" (same wording). Each quoted gloss is verbatim. The issue is only the implied "exactly three". Suggested wording: "Among Figure 1-2's parentheticals are…". Or keep "three" and say which three are meant: the ones that pair with "what was supposed to happen / what happened / why".
- **Thesis Figure 1-1 framing (change 1).** The light reference's thesis carries no Figure 1-1 sentence, so it's unaffected. No in-scope distillation row carries "opens the circular".
- **Figure 4-1 (change 3).** AAR distillation concept 17 ends "Figure 4-1 expands it for the formal AAR". The TC introduces Figure 4-1 as "a recommended sequence for conducting an AAR" (tape 765), with no limit to formal AARs. That's an over-extension in the distillation, independent of the deep reference.
- Checked and consistent with the deep reference: light reference ¶¶21 and 23, thesis Figure 1-4 clause and the two table rows; AAR distillation concepts 2, 3 and 16, Phase 0 "Is the plan complete?", Phase 5 "Has the result reached the assessment?" and the "When to Use" first bullet (Figure 4-1 has seven top-level headings); retro Phase 1 "Have we said what was supposed to happen?". All [V] quotations in these match the tape.

### Left open (outside this scope)

- **Part IV line 149 (Figure 4-1) carries [V] but is not verbatim.** It is an arrow-joined outline that omits "(what was supposed to happen)" after "Commander's mission/intent" (tape 773) and changes capitalisation. Either reclassify it to [AP] or quote the outline as printed. The line was not re-audited here.
- The source card lists Figure 3-2 (example comment card) as image-only. The deep reference's integrity notes name only Figure 3-3. Unchanged since 2026-05-13; not re-audited.

Not stamped. The driver stamps after the cross-family leg.

### Apply leg (after the cross-family sort)

- **Left-open items settled.** Part IV's Figure 4-1 outline now carries [AP] (tape 767–796). The first integrity-note paragraph now names Figure 3-2 alongside Figure 3-3; a render of PDF p. 16 shows three handwritten cards held as an image under the caption at tape 667, and the sentence was tightened to say so.
- **Disputed (thesis ¶3, change 1).** Kept as revised: "Chapter 1 lists two related practices among the 'key points in all AARs'" states a correspondence the tape supports (Preface 89–93; Figure 1-1, 174–175; Ch 4, 800).
- **"Three glossed items" (change 2).** The deep's revised wording stays. The derived "glosses three" passages are left as written: they name three specific glosses, all present (tape 187, 190–191), and claim no total.
- **AAR distillation.** Phase 0 "Is the plan complete?" now lists every Figure 1-4 planning action, including the ARTEP mission training plans and soldier training publications (tape 295–302). Concept 17 no longer limits Figure 4-1 to the formal AAR; it quotes the TC's "a recommended sequence for conducting an AAR" (tape 765).
- **Verbatim check.** Deep reference: the single line-178 `near` (running header and folio inside the paragraph, tape 877–887), not a defect. AAR distillation: four `initial` case differences, none in the edited text.


## Second leg

**Auditor:** gpt-6.1-sol via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `e8095ccf5217df3d441a7a09ee2d8b48d1ea28e109906865f03935f5e2f35080`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `6429e0b66aea6979b7a8daf394000902ddfd92752ec82a3eb1b391c054df319b`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_tc-25-20-army-aar_crossfamily_blind.md`, `_ingest_pass_I_tc-25-20-army-aar_crossfamily_sort.md`, `_ingest_pass_I_tc-25-20-army-aar_crossfamily_prompts.md`.

**Sort result:** The sort found 5 confirmed defects (3 confirmed and fixed, 0 with a wrong or incomplete fix, 2 missed by the fix-in-place audit), 0 over-flagged by the blind auditor, 1 over-flagged by the fixer and 1 disputed, with a gate verdict of FAIL pending two AAR-distillation corrections.

**Remaining edits applied (2026-10-16):** Of the 2 remaining edits (both in the AAR distillation; none in the deep reference), 1 was applied as written (Phase 0 'Is the plan complete?') and 1 with changed wording (concept 17 now quotes Figure 4-1's 'a recommended sequence for conducting an AAR' [V] and names the subtopics under key issues and optional issues), none declined; the disputed thesis wording was kept, and the deep's Figure 3-2 note was tightened to 'three handwritten cards' after a PDF p. 16 render.

**Gate:** pass. Deep reference sha256 `f9f9bb80576820e76d0f46dd2ce83e7df0c5b1285060bb3a1a38f3d5ea1a164d`, stamp included.

## Derived-tier fidelity check (2026-10-16)

The fidelity check of the derived tier for the restored Figures 1-1 to 1-4 read the in-scope deep-reference text against tape lines 100–345, 760–800 and 885–897, plus the Ch 2 and Ch 3 headings, and found no deep-reference defects. It checked 94 claims: 39 in the deep reference, 12 in the light reference, 28 in the AAR distillation, 10 in the retro distillation, 1 in the stakeholder-engagement distillation, none in the decision-making distillation, and 5 across the two new index rows. It fixed 2, both in place. In the AAR distillation's concept 17, a `[V]` quotation of the Figure 4-1 NOTE that the deep reference doesn't carry became a paraphrase anchored to (Ch 4, Figure 4-1). In the stakeholder-engagement distillation's evidence-marker note, a marker count the restoration made stale was updated (132 → 152 [V] on 92 lines; 2 → 3 [AP], adding the Figure 4-1 outline). The light reference, the retro distillation and both new index rows trace to the deep reference with correct anchors and markers, and the index rows have four columns, matching their headers. `check-verbatim.py` reports only initial-capital differences that predate this audit.
