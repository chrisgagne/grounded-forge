# Pass I source audit: aristotle-rhetoric (same-family leg)

- **Deep reference:** `corpus.commons/demo/references/aristotle-rhetoric-deep.md` (610 lines, read in full, 610/610)
- **Tape:** `corpus.commons/demo/sources/converted/aristotle-rhetoric.md` (6502 lines, read in full, 1–6502: Bk I Parts 1–15, Bk II Parts 1–26, Bk III Parts 1–19, archive header and copyright statement)
- **Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode, 2026-11-17
- **Calibration:** fixtures 01, 07, 12 read before the cold read
- **Cross-family leg:** codex, blind, running in parallel on a frozen copy. This log is the same-family leg only. Until that leg's sort is done, treat this reference as audited but unverified.
- **Stamp:** not set. The driver stamps once every leg is done.

## Counts

| Item | Count |
|---|---|
| Claims audited | ≈606: 440 `[V]` quotations, 166 marked prose units (paragraphs and list items), plus the anchor list, 15 statistics rows, 8 connection rows, 11 positions and 4 integrity paragraphs |
| Source-anchored as written | all but those below |
| Stripped | 0 |
| Corrected (hedge, condition, comparative or framing restored) | 29 |
| Marker-corrected | 1 |
| Quotation-corrected | 0 (three new `[V]` quotations added to carry restored hedges) |
| Integrity-note corrections | 1 (plus the table-row fix counted above) |

**Quotations.** `check-verbatim.py` reported no findings, before and after the edits. Its JSON output gives no quote count, so I also ran an exact whitespace-normalised match of every italic quotation and blockquote against the tape. All matched before the edits, and all match after them, including the three added quotations. No quotation presents itself as Aristotle's Greek. The integrity note "What [V] means here" correctly says that `[V]` marks Roberts's English.

**Coverage and anchors.** All 60 parts appear as body anchors. No `coverage: partial`. TOC-vs-anchors check passes.

**Post-source vocabulary.** The deep reference has no ethos, pathos, logos, kairos, "rhetorical triangle", topoi or stasis. "Bekker" appears only to say that the tape has no Bekker numbers. "Deliberative" appears only inside quotations and paraphrases of the tape's own usage (Bk I Parts 6, 9). Clean. The light reference and both distillations are clean on the same terms.

## Changes (deep reference, by line before editing)

Most defects are dropped hedges and lost conditions. None is a fabrication.

| Line | Section | Change | Reason |
|---|---|---|---|
| 85 | Thesis | "come within the ken of all men" → "come, more or less, within the general ken of all men" | Hedge dropped (Bk I Part 1) |
| 110 | Bk I P1, use 2 | "even exact knowledge will not produce conviction" → "not even the exactest knowledge will make it easy to produce conviction" | Hedge dropped: tape says "make it easy" |
| 144 | Bk I P3 | political orators "concede" → "often concede" | Hedge dropped ("often make any concession") |
| 170 | Bk I P7 | Greater number of goods: added "if the smaller number is included in the count". Accompaniment: added "that does not always accompany it" | Conditions lost |
| 172 | Bk I P7 | "look greater when divided" → "look better when divided into their parts", with the climax as a further effect | Wording drift ("look better") |
| 186 | Bk I P9 | Added "according to the usual view" to the definition of virtue, and the conditional "if virtue is a faculty of beneficence" to "the highest kinds" | Hedge and condition dropped |
| 188 | Bk I P9 | Rewritten. The deep reference had the author *naming* a misleading practice. In the tape he *prescribes* treating allied qualities as identical in praise or blame ("We are also to assume…"), then adds that the method "enables an advocate to draw a misleading inference from the motive", glossed by the noble-cause argument | Framing inverted an instruction into a criticism |
| 210 | Bk I P11 | Learning and wondering: added pleasant "as a rule" | Hedge dropped |
| 216 | Bk I P12 | "Kinds of wrong expected to be forgiven are…" (four kinds) → only wrongs done universally or commonly are expected to be forgiven; the rest are kinds of wrong (kept dark, shameful to speak of, trifling and litigious to prosecute) | Condition misattributed to all four |
| 224 | Bk I P13 | Equity: added that its existence is partly unintended, where legislators noticed no defect. "Guilty by the letter" → the tape's own "*according to the unwritten words of the law*" [V], marked "(so the tape prints it)" | Condition lost. The paraphrase smoothed over the tape's wording. "Unwritten" reads oddly in context but is what Roberts's text prints, and it is not corrected here |
| 240 | Bk I P15 | "not following the letter" → "not simply following the letter of the written law" | Hedge dropped |
| 242 | Bk I P15 | "plus soothsayers and proverbs for future events" → ancient witnesses concern past events; soothsayers for future events; proverbs also a form of evidence | Proverbs were wrongly tied to future events |
| 246 | Bk I P15 | "Great weight is attached" → "is often attached" | Hedge dropped |
| 272 | Bk II P3 | "Those who deny an obvious offence are punished more" → tied back to the tape's servants example | Generalised beyond its context |
| 280 | Bk II P4 | "Enmity arises from… may arise from character alone" → "may be produced by…; may arise from what we take to be a person's character alone" | Hedges dropped |
| 322 | Bk II P12 | Young "are courageous" → "more courageous than older men" | Comparative made absolute |
| 324 | Bk II P13 | Elderly "are formed of the contrary" → "may be said to be formed, for the most part, of the contrary" | Hedges dropped |
| 330 | Bk II P15 | Good birth makes men "ambitious" → "more ambitious" | Comparative made absolute |
| 334 | Bk II P17 | Power "shares some of wealth's traits but is better" → "and is better in others". Good fortune makes men "more supercilious and more reckless" | Comparatives and the partial claim restored |
| 358 | Bk II P20 | Fables "easy to invent" → "comparatively easy to invent" | Hedge dropped |
| 427 | Bk II P25 | A negative instance refutes an example argument only "*in so far as it is proved not inevitable*" [V]; "dissimilar" is used where the positive examples are more numerous | Condition dropped |
| 481 | Bk III P9 | A member too short "often" makes the listener stumble | Hedge dropped |
| 487 | Bk III P10 | "People are taken neither by…" → "not much taken either by…" | Hedge dropped |
| 493 | Bk III P11 | "Similes, proverbs and hyperboles are forms of metaphor" → successful similes are "*in a sense metaphors*" [V]; proverbs and successful hyperboles are metaphors too | Hedges dropped ("in a sense", "successful") |
| 521 | Bk III P16 | Defendant should not waste time on admitted fact "unless it bears on his own contention" | Condition dropped |
| 545 | Bk III P18 | `[BT]` moved to the Gorgias sentence; the irony sentence, which is the author's own, is marked `[AR]` | **Marker correction**: one `[BT]` covered a borrowed claim and the author's own |
| 568 | Statistics | "numbered 1–27, with gaps and one unnumbered line" → "numbered 1–27 with no 9; logical division (after 8) and meanings from names unnumbered" | Miscount: one gap and two unnumbered lines |
| 608 | Integrity notes | "none of [the verse quotations] is quoted here" → two short ones are quoted ("Potter to potter…", Bk II P4; "Potter against potter", Bk II P10) | False statement about the reference itself |

Also corrected: the grammar of the new Bk II P25 sentence, in a follow-up edit.

## Checked and left as written

- Line 89: "the enthymeme is a compressed syllogism". The tape says it "must consist of few propositions, fewer often than… the normal syllogism" (Bk I P2), so "compressed" is a fair paraphrase.
- Line 101: "for three reasons". The tape says "several reasons" and lists three.
- Line 220: `[BT]` on Sophocles, Empedocles and Alcidamas is correct; Alcidamas does break off in the tape.
- Line 580: "Theodorus… whose 'novelties' he cites approvingly". Bk III P11 cites them as an example of lively sayings. "Approvingly" is a mild reading; left as written.
- Line 602: the process note about the brief's 6,565-line figure is provenance, not a source claim.
- Line 604: "scattered, garbled transliterations" describes the tape's state ("tekmerhiou", "porheueseai"), not the source's quality.

## Conversion noise noted

The tape's slips and bracketed passages listed in the integrity notes all check out: "hetter", "mysell", "as ahas", "As in the therefore", "alway", "snot"; the brackets in Bk I P6, P9, P11 and P15; and the three ellipses. Other garbles exist but are not quoted, among them "a man aging war" (Bk II P2), "the constitution a in which" (Bk I P8) and "therefor snot" (Bk III P16).

## Derived tier: edits that change claims they may carry

The derived tier was not edited or stamped. The parent should re-derive:

1. **Light reference, line 18:** "The author flags the practice of calling allied qualities identical (rashness as courage) as a way to draw a misleading inference." This carries the Bk I P9 misframing (deep line 188). The author prescribes the practice in praise and blame; only the extension to motive is the "misleading inference".
2. **Stakeholder-engagement distillation, line 177** ("Denying the obvious"): "people are more incensed with those who deny an obvious offence". The tape's example is masters punishing servants (Bk II P3). Narrow it or keep the context.
3. The other edits (hedges and conditions) are not echoed in the light reference or the distillations as far as a grep for the affected claims shows. Re-derivation should still use the audited wording for Bk I P12 (forgiven wrongs), Bk I P13 (equity), Bk II P13 (elderly), Bk II P25 (refuting examples) and Bk III P11 (similes and hyperboles).

## Integration rows checked against neighbour deep references

**Decision-making distillation**

- *Organizational Behavior (Ch 6.4, 6.6)*: barriers (bounded rationality, escalation of commitment, biases, conflict avoidance) and groupthink "keep the peace" are supported (OB deep lines 227–234, 254). **Supported.**
- *MCDP 1*: "treats decisions as time-competitive" is supported (Ch 4 "Decisionmaking", deep line 152). "Warns against waiting for certainty" has no passage. The nearest are "any decision is generally better than no decision" and the advice to work through uncertainty with flexible plans, and the same passage says not to rush decisions where time is not limiting. **Narrow** to "holds that any decision is generally better than no decision". On the *Rhetoric* side, "refusing an option because it is not inevitable is a spurious refutation (Bk II, Part 25)" recasts a defence's objection to an accuser's probability as option-refusal. That is the distillation's transfer, not the source's claim, and it should be worded as a transfer.
- *NHS Just Culture Guide*: the gated sequence of tests and one action at a time are supported (NHS deep lines 31, 43). Separating outcome from culpability fits the preamble's "differ according to the circumstances". **Supported.**
- *Business Ethics*: stakeholder theory, and identifying and prioritising stakeholder claims, are supported (BE deep line 18). **Supported.**

**Stakeholder-engagement distillation**

- *Business Ethics*: "who counts as a stakeholder and how to weigh their claims" is supported (BE deep line 18).
- *Organizational Behavior*: process versus relationship conflict (deep line 238), negotiation stages and cross-cultural negotiation styles (lines 594–602) are supported. "Empirical frame" is fair: the OB deep reference reports studies (e.g. Table 14.4).
- *MCDP 1*: "understanding an opposing party on its own terms" is supported ("see the enemy as he sees himself", Ch 4 "Orienting on the enemy", deep line 138).
- *Liberating Structures; FLO Facilitation Guide*: "practices for running participatory meetings" fits Liberating Structures. FLO is a guide to facilitating online learning courses; its deep reference never mentions meetings. **Narrow** to "Liberating Structures carries practices for participatory meetings; FLO, for facilitating online learning".

## Open

- The cross-family (codex) leg's sort is pending. Treat this reference as audited but unverified until it lands.
- No page renders were used: the source is a plain-text transcription.

## Gate settlement (orchestrator, 2026-11-17)

The gate stopped on one open question: the source card said the conversion only added heading marks (sort finding B40). Checked against the original: `BOOK I` became `# Book I`, `Part 1 ` became `## Part 1`, and the 63 blank lines around the headings were removed (6,565 → 6,502 lines). With headings and blank lines set aside, the original and the converted text are identical line for line. The source card's `converted_via` and conversion paragraph now say so. The apply leg's partial tape read needs no action: it read only the passages its edits touched, and the sort leg's full read (lines 1–6502) is the coverage of record. Resumed with `--accept-gate`.


## Second leg

**Auditor:** gpt-6.1-sol via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `eed751d108157e4ed7e54f3b514f0768f89937442b2bbbee9b237982d7e53e17`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `6a7dd67e3b97c3255863adf763dfe045de29543b05801815d2b89efe5f1fda87`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_aristotle-rhetoric_crossfamily_blind.md`, `_ingest_pass_I_aristotle-rhetoric_crossfamily_sort.md`, `_ingest_pass_I_aristotle-rhetoric_crossfamily_prompts.md`.

**Sort result:** The sort found 58 confirmed deep-reference defects (27 fixed correctly, 2 fixed wrongly or incompletely, 29 missed by the fix-in-place audit), 4 over-flagged by the fixer and 0 by the blind auditor, 1 disputed (F15, needing no edit), capture fixer=29 blind=42 both=13, and a gate verdict of fail because the derived files were unavailable to it.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 29, the blind audit 42, both 13. The Chapman estimate is 91.1 in all, about 33.1 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-11-17):** Of the 30 remaining edits, 23 were applied as written, 7 with changed wording (4 'defines each but virtue'; 13 keeps the tape's 'every one else'; 19 keeps the [V] quotation and the 'reverse of indefinite' reason; 20, 22, 24 and 27 tightened to the tape's wording), and none was declined.

**Gate:** accepted by operator. Deep reference sha256 `e17add6a41b1a3884c31d9f5814efcb151f67d4358a780f6badefa18989bb662`, stamp included.

## Derived-tier fidelity check (2026-11-17)

The fidelity check of the `aristotle-rhetoric` derived tier read the Pass I–stamped deep reference in full, plus the light reference, the decision-making and stakeholder-engagement distillations, and the slug's 20 rows in the two distillation indexes. It checked about 405 claims against the deep reference, opening the Roberts tape at the anchors in question, and fixed 36: 8 in the light reference, 17 in the decision-making distillation, 9 in the stakeholder-engagement distillation and 2 index rows. Most fixes restore dropped hedges ("properly speaking", "practically always", "tends to", "some, if not all", "often", "as a rule"), narrow widened scope (Book I as wholly about deliberation; enthymeme materials as "practical reasoning"; the ceremonial end assigned to observers), fix one misplaced anchor, and trim two `[V]` quotations to the deep reference's spans. Four tape-true claims the deep reference lacks were also taken out. Of the eight integration rows naming other corpus sources, two were narrowed against those sources' deep references (MCDP 1's time-competitive decisionmaking applies to execution; the NHS guide judges by circumstances, not outcome against culpability). `check-verbatim.py` reports no findings on any edited file, no later-theory labels or Bekker numbers appear, and no deep-reference defect was found.
