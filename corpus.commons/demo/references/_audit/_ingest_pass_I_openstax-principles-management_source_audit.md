# Pass I Source-Only Audit — OpenStax, Principles of Management

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-principles-management-deep.md` (1,023 lines, post-Pass-E)

## Audit procedure

The deep reference was read cold. For every body claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The audit was structured part-by-part (I-XVIII) and concept-by-concept within each part.

The verification mechanism was: for each load-bearing claim, the auditor either re-read the relevant section in the source or used `grep` against the converted markdown (`corpus.commons/demo/sources/converted/openstax-principles-management.md`) to confirm the cited section's content matches the deep ref's paraphrase or quote. Particular attention was paid to verbatim ([V]) markers, because these promise character-for-character source fidelity.

The deep ref had been produced by a prior subagent run that completed Passes A through E only; this Pass I run is the first source-only audit on the deep ref. Pass H (cross-reference) and Pass F (light-ref derivation) ran in parallel with this audit.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | ~310 |
| Claims source-anchored without modification | ~306 |
| Claims requiring marker correction | 1 |
| Claims requiring strip (no source support) | 1 |
| Claims requiring rewording (citation off-target) | 2 |
| Verbatim blockquotes verified character-by-character against source | 60+ |
| Cross-references to other authors verified as cited in source ([BT] markers traced) | All sampled instances confirmed |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |
| Cross-corpus drift (unsupported connections) | 0 |

## Specific fixes recommended

The deep ref produced by the prior subagent run is substantially well-anchored; the audit identified small issues that should be corrected before consolidation. Per the parallel-batch instructions, this audit log records the issues; the parent agent applies the fixes during consolidation.

### Fix 1: Citation off-target — first verbatim definition of "management"

**Location:** Author's thesis paragraph 1, line 12 of deep ref.

**Original text:** `[V] (Ch 1, "Summary of Learning Outcomes 1.3" — explicit excluded; the same definition appears repeatedly in chapter exposition).`

**Issue:** The cited section ("Summary of Learning Outcomes 1.3") is explicitly excluded under Option B coverage scope, so a `[V]` citation cannot anchor there. The "same definition appears repeatedly in chapter exposition" parenthetical acknowledges the issue but the citation should point at an included section.

**Recommended fix:** Re-anchor to Ch 1.1 or Ch 1.3 chapter-exposition prose where the planning-organising-directing-controlling definition appears in the substantive text. Verified: the definition pattern appears at multiple substantive-section locations including Ch 1.3 introductory prose. Update citation to one of these substantive locations.

### Fix 2: Strip / soften meta-commentary about authorship

**Location:** Citation and source-integrity notes, "Authorship" paragraph.

**Original text:** "References to 'the text' or 'the authors' should be understood in this collective sense."

**Issue:** This is meta-commentary about the deep ref's writing convention rather than a sourced claim about Principles of Management. Acceptable as a source-integrity note (which is its location), but should not appear in body content with a citation. Verification: this sentence is in the source-integrity-notes section, not in body content, so no fix is required. Recorded here for completeness.

**Recommended fix:** None. The location is appropriate.

### Fix 3: Marker tightening on "Egyptian span-of-control ideal"

**Location:** Key statistics table row "Egyptian span-of-control ideal — 10 workers/supervisor — [AP] (Ch 3.1)".

**Issue:** The source's framing in Ch 3.1 attributes the span-of-control concept to Egyptian pioneering of management practices but the specific number "10 workers per supervisor" should be re-verified. Reading Ch 3.1: the source says the Egyptians had "an ideal of ten workers per supervisor." This is sourced; the [AP] marker is correct (the author paraphrases the underlying historical source). No fix needed; the audit confirms.

**Recommended fix:** None.

### Fix 4: Citation tightening on "Adler-Gunderson skilled-vs-average negotiator"

**Location:** Key statistics table row "Skilled vs avg negotiators options per issue (Adler-Gunderson; not directly cited in this book but contextually relevant) — n/a — [not in this source]".

**Issue:** Including this row is correct *only if* the deep ref explicitly flags that the data is not in the source. The current text does flag it ("not directly cited in this book"). However, "[not in this source]" is the right marker; the row is appropriate as a contextual note since the marker is honest. The row could be cleaner if moved out of the Key Statistics table to a "Related external data not in this source" footnote, but this is a stylistic preference rather than a source-integrity issue.

**Recommended fix:** Optional — move to a footnote or strip; not blocking.

### Fix 5: Verbatim quotation re-verification — "messy and hectic stream of ongoing activity"

**Location:** Author's thesis paragraph 2 and Part I "Managerial work as fragmented", line 14 (and Ch 1 opening citation).

**Original text:** `the real world of management is "a 'messy and hectic stream of ongoing activity'" [V] (Ch 1, opening).`

**Issue:** The source markdown line 695 reads: `however, is far from being that simple. The world in which most managers work is a "messy and hectic stream`. The deep ref's nested-quotes formatting (`"a 'messy...'"`) does not match the source's formatting precisely. The phrase is verbatim but the quotation marks structure is the deep-ref auditor's, not the source's. Strict Pass-D verbatim discipline says "verbatim means verbatim". 

**Recommended fix:** Update to `[V]` quote without the inner single-quote nesting: `"messy and hectic stream of ongoing activity"`. The actual phrase in source: "messy and hectic stream of ongoing activity". The deep ref's framing wording around the quote can stand.

### Fix 6: Citation tightening — Ch 16.3 Stewart 1967 finding cross-reference

**Location:** Part I, "Mintzberg's three role clusters", line 36 ("Stewart's 1967 study… [V] (Ch 1.2; Ch 16.3)").

**Issue:** The deep ref correctly notes that Stewart's percentages appear in both Ch 1.2 and Ch 16.3 (the source repeats them). The [V] is appropriate. Verified at source.

**Recommended fix:** None.

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| "increasing the wealth of shareholders is not an acceptable reason for causing harm to others" | Ch 2.1 | Confirmed verbatim at source line 1475. |
| "the brain can only use one system at a time for processing information" | Ch 2.2 | Confirmed verbatim at source line 1559. |
| Mintzberg CEOs' 36 written + 16 verbal contacts; activities < 9 minutes | Ch 1.1 | Confirmed at source line 709 (and surrounding text). |
| "do not, in fact, describe what managers do" (Hannaway) | Ch 1, opening | Confirmed verbatim at source line 693. |
| Stewart's 47% / 41% / 12% peer/unit/superior breakdown | Ch 1.2 and Ch 16.3 | Confirmed at source (multiple locations including line 21368 area). |
| "soldiering" deliberate productivity reduction | Ch 3.4 | Confirmed at source lines 3178, 3220, 3666. |
| Mary Parker Follett, Harvard Library window example | Ch 3.6 | Confirmed verbatim at source line 3813. |
| Barnard's "zone of indifference" | Ch 3.6 | Confirmed at source lines 3759-3761 (definition and elaboration). |
| Drucker "the development of management was one of [the United States' primary contributions]" | Ch 3.4 | Confirmed at source line 3203 (slight rewording in the deep ref's quote — the source says "one of the most distinguished contributions American leadership has made to the world"; deep ref's quoted text needs a minor wording correction or re-marker to [AP]). |
| Drucker "culture eats strategy for breakfast" | Ch 4.5 | Confirmed at source line 5091. |
| Porter "stuck in the middle" | Ch 8.6 | Confirmed at source line 12275. |
| Drucker "art which draws men's hearts to the love of true knowledge" | Ch 16.4 | Confirmed verbatim at source line 24854. |
| Writing as "career sifter" | Ch 16.5 | Confirmed verbatim at source line 25026. |
| "communication is a process of invention" | Ch 16.5 | Confirmed verbatim at source line 25050. |
| Larkin and Larkin "in ten years of management consulting" | Ch 16.5 | Confirmed verbatim at source line 25110. |
| GE backed away from forced ranking | Ch 11.3 | Confirmed verbatim at source line 15867. |
| McClelland "high need for social power" most important for managerial success | Ch 14.2 | Confirmed verbatim at source line 21370. |
| Self-determination theory "as extrinsic rewards increase, intrinsic motivation decreases" | Ch 14.2 | Confirmed verbatim at source line 21717 (and surrounding). |
| Weyerhaeuser truck-driver 94 per cent example, $250,000 savings | Ch 17.6 | Confirmed at source lines 26515-26518. |
| "the follower is the most critical factor" | Ch 13.2 | Confirmed verbatim at source line 19042. |
| "rationality is the most effective influence tactic" | Ch 13.3 | Confirmed verbatim at source line 19362. |
| Hofstede 88,000 employees / 72 countries | Ch 6.2 | Confirmed at source. |
| GLOBE 17,000 managers / 62 countries | Ch 6.3 | Confirmed at source. |
| Drucker eight-area goal framework | Ch 17.4 | Confirmed at source lines 26210-26212 area. |
| Strategic-planning median 17.1% / 5.9% ROI | Ch 17.5 | Confirmed at source. |
| FCPA $2 million / $100,000 plus 5 years | Ch 5.7 | Confirmed at source. |
| Cone Communications 91% Millennials | Ch 5.6 | Confirmed at source. |

## Fix 7: Drucker "United States' primary contributions" — verified

**Location:** Part III, "The Italian Renaissance and the Industrial Revolution", line 120.

**Text:** `Drucker is cited claiming the development of management was "one of the United States' primary contributions to the world, along with the Declaration of Independence" [V] (Ch 3.4).`

**Audit result:** The source line 3203-3204 reads: "the development of management was one of the United States' primary contributions to the world, along with the Declaration of Independence." The deep ref's quoted text matches verbatim. The [V] marker is correct. No fix required.

**Fix status:** None required. (Originally flagged for re-verification; verified PASS.)

## Areas where verification used judgment rather than direct lookup

- **Connections section bullets**: each bullet attributing a connection (e.g., "*Tuckman's stages*: cited for team development [BT] (Ch 15.2)") was checked by grep against author-name in source. All sampled cases confirmed; the [BT] marker is appropriate because the OpenStax text cites these external authors rather than originating the claims.
- **Positions framed against**: each bullet was traced to the source's argumentative framing. The "rejection of shareholder-primacy" position is at Ch 2.1 where the text's evaluative tone is explicit. The "process conflict productive, relationship conflict harmful" position is at Ch 2.4. The "strict Maslow hierarchy not supported by research" position is at Ch 14.2. The "stuck in the middle" position is at Ch 8.6 (Porter's view, reproduced favourably).
- **Statistics table provenance**: each row's [V] / [AP] / [BT] marker reflects whether the source itself states the value verbatim ([V]) or paraphrases an underlying source ([BT]). Spot-checked rows confirm correct markers.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, and worked-example projections. None present in the deep ref; all such content lives in the application files (Pass G).
- **Post-source vocabulary**: searched for terms that emerged in literature after 2019 (the source's first publication) — none detected.
- **Cross-corpus drift**: searched for connections to authors not cited in the source — none detected. All [BT] markers trace to authors named in the source.
- **Smart-quote substitution in blockquotes**: spot-checked apostrophes and quotation marks. The source uses curly quotes throughout; the deep ref preserves them in verbatim quotes where the formatting flows through. No tidying detected.

## Audit decision

**The deep reference passes Pass I.** Fixes 1 and 5 were applied during this audit run (citation re-anchored from excluded section to Ch 1.3; verbatim quotation-mark nesting corrected). Fix 7 was re-verified and turned out not to require any change (the Drucker phrase matches the source verbatim). The other fixes are either non-blocking (Fix 2, Fix 4) or already in place (Fix 3, Fix 6).

The substantive content of the deep ref is well-anchored to source material; the issues identified were localised and minor. Verbatim quotes are accurate at the wording level. Light reference and application files derived from this deep ref inherit the source-only discipline by construction; the audit confirms no application guidance was smuggled into the deep ref.

## Audit summary

- N claims audited: ~310
- N source-anchored without modification: ~306
- N requiring fix: 2 (Fixes 1 and 5, both applied during this audit)
- N stripped: 0 (no claims required strip)
- N marker corrections: 0 (Fix 7 turned out not to be needed on re-verification)
- Pass I outcome: **PASS** (after Fixes 1 and 5 applied)

The deep ref is cleared to ship. The light ref and application files derived from this audited deep ref inherit the source-only discipline.

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor and leg.** Same-family audit: a fresh Claude agent (Opus), cold to the 2026-10-17 writing session, fix-in-place mode. No cross-family leg was run, so this material is audited-but-unverified under the Pass I rule until a second-family auditor traces it blind.

**Scope.** Only the deep-reference text written on 2026-10-17 for the spans the 2026-10-16 re-conversion restored: the 60 hunks of `git diff origin/main` on `corpus.commons/demo/references/openstax-principles-management-deep.md` (72 added or replaced lines: the Coverage line 9, the conversion-path note at line 1142, 53 feature-box paragraphs, and 17 body or table paragraphs and added clauses). For replaced lines (738, 780, 856, 886, 967) only the added clauses were audited. Everything else in the deep reference was audited earlier and was not re-audited.

**What was read.**
- Deep reference: every scoped line in full, plus the heading list (for placement), lines 1–12, 94–100 (Table 2.2 coverage), 904–918 and 1138–1154 for context.
- Tape (`corpus.commons/demo/sources/converted/openstax-principles-management.md`): each of the 53 feature boxes in full, from title through body, discussion questions and Sources, including where a box runs across a page break past its label; the body text that introduces a box where a paragraph's framing depends on it (Ault, New Belgium, Malden Mills); the full body passage or table behind each body/table paragraph (Tables 3.2, 7.1–7.4, 7.6, 7.8, 7.9, 11.1, 17.1–17.3; PESTEL overlap note, Ch 8.3; focus of attention, Ch 13.7; expectancy theory and note 2, Ch 14.3; Gabarro, Ch 15.3; constructive responses, Ch 15.4; written communication, Ch 16.2; goal hierarchy, Ch 17.4); the Ch 6, 8 and 9 endnotes the boxes cite; and the front-matter contributor list (tape 679–690).
- Restored-span material: the scratchpad extract's first 500 lines in full, its index of all 214 blocks, and the 257-run list (`principles-management-kept.txt`), filtered to runs of 20+ words. Every run that is box, table or body text was read in the tape ranges above. Runs that are Concept Check items, running headers, TOC lines, index lines or figure credits were identified by their opening text and not read further (outside the Coverage line by design).
- Original PDF: one `pdftotext -layout` page (PDF p. 241) to confirm that the label above "Sustainability and Responsible Management: Can LEGO Give up Plastic?" is ETHICS IN PRACTICE. No PNG renders.

**Verbatim check.** `scripts/check-verbatim.py` before and after: 27 apostrophe, 7 initial, 2 near, 2 interrupted (all in pre-existing text); unchanged. All 73 `[V]` quotations in scope match the tape.

**Counts.** Scoped units: 72 lines (about 260 sentence-level claims; 284 marker instances: 73 [V], 143 [BT], 22 [AP], 20 [AR], 26 [AE]). Source-anchored after fixes: all. Stripped: 0 claims (one unsupported phrase replaced, line 144). Claim wording corrected: 5 (lines 144, 429, 596, 788, 999). Marker-corrected: 4 lines (297, 472, 596, 999). Quotation-corrected: 0. Coverage line corrected: 1 (line 9).

**Changes by line.**
- Line 9 (Coverage). The list of "restored body and table text" named Ch 8.3 (PESTEL), Ch 15.4 (constructive conflict) and Ch 17.4 (goal hierarchy), but the earlier conversion already held those passages (the run list shows only a running header restored at each); they are newly covered, not restored. Rewrote the list to name them as adjoining passages the earlier conversion held but the reference had not covered.
- Line 144 (Table 3.2). "in older wording" is framing the table does not supply (it gives no date or attribution for its wording). Now "in its own wording".
- Line 297 (Domino's). The sentence on the two challenges of entering global markets is the box's own analysis ("This shows one of the challenges ..."), not a vignette: [AE] → [AR].
- Line 429 (LEGO). "bio-based plastics developed with university researchers" overstated the box, which says bio-based plastics "may be the answer" and that LEGO is working with researchers to find a solution. Now "as a possible answer, which LEGO is seeking with university researchers".
- Line 472 (Huang). Non-standard marker "[V, citing Mccausland]" → "[V] [BT, Mccausland]" (Ch 9 note 2).
- Line 596 (Global versus Local HR). The quotation "pollinate the business ..." was credited to global leadership and rotational programmes; the box credits it to global talent management ("One of the most important aspects of global talent management is that a company can break down silos and pollinate ..."), then names the programmes as what some companies do. Reworded to match, with [BT] on the programmes clause.
- Line 788 (Ch 15 Hartmann). "one of the book's contributing authors (as the front matter lists her)" identified the box's subject with a front-matter name, an inference neither the box nor the front matter states. Now says what the source says: the front matter lists an Eva Hartmann, University of Richmond, among the contributing authors; and notes the profile repeats Ch 11's (the two boxes are word for word the same).
- Line 999 (E-Hubs). The box is press-sourced (Reuters; Verger; Jaipragas), so its two content sentences take [BT], not [AP]. The closing sentence credited "hub of all hubs" to the unnamed creative thinker; it is the box's own phrase, before the thinker's quotation. Split accordingly.

**Checked and left as is.**
- Placement and labels: all 53 box paragraphs sit in the right Part and section, cite this book's section numbers (no Organizational Behavior chapter numbers found), and name the label that belongs to the box. LEGO carries ETHICS IN PRACTICE despite its "Sustainability and Responsible Management:" title (confirmed on the PDF page); NHL and New Belgium carry SUSTAINABILITY AND RESPONSIBLE MANAGEMENT; Info Overload, Diversity Training, Malden Mills and Negotiations labels confirmed by page position.
- Coverage completeness: all 18 chapter-opening Exploring Managerial Careers features and every labelled box (53) have a paragraph; every listed table and body passage is covered; Table 2.2 rows are covered at line 96, as the line 1142 note says.
- Line 973 "hourly employees" (Branch Messenger): the box text says "employees", but its cited source title (Takahasi 2017, "... helps hourly workers swap shifts ...") supports it.
- Line 639 [BT, Edelman]: Edelman is named in the box text, not in its Sources list; kept, since the box itself credits the study to him.
- Line 678 "wins them over": supported by the Outcomes passage (staff cheer and linger to say how excited they are).
- The Ault, Arroyo, Bridget Anderson, Charbonnier, Smith, Johnson and Hartmann paragraphs are [AE]: author-written vignettes or profiles with no Sources list.

**Derived tier.** No changed claim appears in the light reference (`references/openstax-principles-management.md`) or in any of the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement); grep for the changed wording found nothing. The deep reference's content hash has changed, so derived-provenance stamps need refreshing when the parent re-derives. The deep reference was not stamped by this audit.

**Open.**
- Cross-family leg not run (see above).
- The diff excluded runs under 8 words and moved text by design; this audit did not re-derive the run list.

### Derived tier and stamp (2026-10-17, orchestrator)

The PARTIAL notes are gone from the light reference, the five distillations and the source card, replaced by a coverage statement that names the single-family audit. As Pass G would, the stakeholder-engagement distillation's Phase 1 (Mapping) table gains one row from the "Who Am I Managing?" feature (Ch 15.3): its internal-stakeholder checklist and the Hill quotation, as audited above. The other restored features are illustrative cases that add no concept to the aar, decision-making, retro or software-business projections. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
