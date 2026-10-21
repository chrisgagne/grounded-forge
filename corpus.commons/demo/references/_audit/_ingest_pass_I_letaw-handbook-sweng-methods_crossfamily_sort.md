**1. What I read**

Read in full: `sort-brief.md`, the three fixtures, `pass-i-spec.md`, both audit reports—including the fixer’s historical 17-fix log—and all 413 lines of `post-audit-deep.md`. Also read `blind-brief.md`, `source-card.md`, the repository operating rules and architecture documents.

Read the specified restored-callout ranges in `tape.md`, with additional passages for the historical findings. Compared `frozen-deep.md` with `post-audit-deep.md`; the current fixer made four changes. Both supplied SHA-256 values match their respective files.

Ran the deterministic verbatim checker against the post-audit reference and supplied tape: **no actionable mismatches or lookup errors**; 67 apostrophe notices and 23 initial-capitalisation notices.

I did not read the entire tape, inspect the PDF visually, or independently re-audit the derived files. This report sorts the supplied findings and checks the current edits; it does not replace a full-source audit. No files were modified.

**2. Sorted ledger**

Line numbers below refer to `post-audit-deep.md` and the supplied `tape.md`.

**Current scoped re-audit**

The blind auditor reported **no defects**. Its considered-but-rejected flags are addressed after the findings ledger.

| ID | Finding | Deep line | Tape lines | Classification and reasoning |
|---|---|---:|---:|---|
| S1 | Fixer stripped the observation that the CHAOS callout does not discuss its definition of failure. | 35 | 492–506 | **Disputed.** The fixer reads it as an unsolicited methodological caveat. The blind auditor reads it as a bounded description of the displayed passage. The passage indeed supplies figures without defining failure; the sentence neither declares the research invalid nor attributes a limitation to Letaw. Both readings are defensible. Its removal introduces no defect. |
| S2 | Fixer changed “The Manifesto is quoted in full” to “The source quotes the Manifesto.” | 39 | 535–550 | **Over-flagged by the fixer.** The reference reproduces the complete passage displayed by this source: preamble, four values and concluding qualification. In that context, “quoted in full” need not certify an external edition of the Manifesto. The replacement is nevertheless accurate and can remain. |
| S3 | Fixer removed “satirical” from “a satirical Twitter feed.” | 129 | 1763–1765 | **Disputed.** The blind auditor treats “satirical” as a faithful paraphrase of the humorous-example context. The fixer requires stronger support for that particular genre label. “Comically bad” establishes humour, but does not unambiguously establish satire. The narrower post-audit wording is supported and can remain. |
| S4 | Fixer completed the Coverage inventory with the quality-attribute/user-story callouts, GenderMag pointers and further-resources callout. | 9; corresponding content at 121, 129, 293, 299 | 1586–1588; 1709–1711, 1763–1765; 2801, 2838–2840; 3139–3143 | **Confirmed and fixed.** These additions exist in the body and source. The correction completes the restoration inventory; it does not repair missing substantive body coverage. |

**Historical findings retained in the fixer log**

These remedies already appear in the frozen reference. “Fixed” below means that the logged defect’s remedy is present and source-supported; the current four-hunk diff does not independently establish when the historical edit occurred.

| Historical fix | Deep line | Tape lines | Classification and verification |
|---|---:|---:|---|
| H1 — ISO definition | 13 | 252–260; 4082–4090 | **Confirmed and fixed.** The current definition matches the source. Adding “the” inside the original quotation was unsupported. The restored tape now also contains the definition in the Introduction, so the historical log’s glossary-only explanation is outdated. |
| H2 — sustainable/extensible fragments | 13 | 267–269 | **Over-flagged by the fixer.** Both original fragments—“feasible for the program to grow, exist, and be maintained” and “feasible to add more features”—are exact contiguous source text. Quoting those fragments does not require including “it’s.” The expanded current quotations are also correct. |
| H3 — risk-reduction catalogue | 19 | 721–725 | **Confirmed and fixed.** The current quotation restores “keeping track,” “your” and the conjunctions. |
| H4 — fist-of-five qualification | 79 | 1028–1029 | **Confirmed and fixed.** “Can reduce risk” preserves the source’s qualification. |
| H5 — SDLC marker split | 27 | 434–450 | **Confirmed and fixed.** The definition is quoted and marked `[V]`; the stage descriptions are marked `[AP]`. |
| H6 — grey-area hybrid markers | 15 | 278–285 | **Disputed.** The log says it added `[AP] [V]`, but that combined marker is absent from the current first sentence. A paragraph-wide reading of `[V]` favours adding `[AP]`; a quotation-local reading accepts the current `[V]` markers because the quoted wording is exact and the connecting summary is traceable. The supplied negative-control fixture does not settle marker scope for this hybrid construction. No unsupported substantive claim results. |
| H7 — WinGui Gateway wording | 242 | 2657–2659 | **Confirmed and fixed.** “Responsible for preparing…” matches the source; the logged quoted wording “prepares…” did not. |
| H8 — parameter-reduction qualification | 330 | 3369–3371 | **Confirmed and fixed.** “As appropriate” is restored. |
| H9 — heuristic 3 gerunds | 286 | 2918–2919 | **Confirmed and fixed.** “Approach decision-making by diligently gathering and thoroughly reviewing…” matches. |
| H10 — RACI source typo | 77 | 991–993 | **Confirmed and fixed.** The quotation preserves the source’s “a negative events and outcomes.” |
| H11 — functional-requirement formats marker | 127 | 1651–1668 | **Confirmed and fixed.** The summarising lead-in carries `[AP]`; the quoted explanation remains source-faithful. |
| H12 — Waterfall quotation’s bracketed tense change | 400 | 480–485 | **Disputed.** Strict verbatim fidelity favours the current exact quotation. Conversely, the original `[d]` visibly disclosed an editorial alteration rather than silently passing it off as source wording. The current replacement removes that ambiguity and is correct. |
| H13 — project-management reasons marker | 63 | 738–746 | **Confirmed and fixed.** These are paraphrased reasons, correctly marked `[AP]`. |
| H14 — Tuckman descriptions marker | 71 | 835–849 | **Confirmed and fixed.** The descriptions are paraphrases; `[AP] [BT]` fits. |
| H15 — managerial skill definitions | 67 | 809–820 | **Confirmed and fixed.** The current definitions are explicitly quoted and match. |
| H16 — elicitation definition | 115 | 1511–1515; 4026–4028 | **Confirmed and fixed.** The exact phrase is now quoted; both cited locations support it. |
| H17 — software-requirement citation | 105 | 1417–1418; 4021–4024 | **Confirmed and fixed.** The quotation matches the chapter opening. The glossary expresses the definition differently; removing it from this exact quotation’s citation is appropriate. |

**Other audit assertions and over-flag guards**

These are clean checks, not additional defect findings:

| Passage or concern | Deep lines | Tape lines | Sort result |
|---|---:|---:|---|
| CHAOS figures and Standish attribution | 35, 360 | 492–506; 519–525; 4459–4461 | All six figures and project-size pairings match. The same section supports the Standish attribution. |
| Cultural gesture meanings | 79 | 997–1001 | “Is an insult” faithfully paraphrases the source’s wording. |
| Clinician example and “alternating” | 148 | 1675–1701 | The example moves between clinician and software actions. “Alternating” reasonably summarises that interaction without asserting strict turn-taking at every step. |
| Figure 3.3 wording | 129 | 1719–1753 | Identifier, priority, Sprint, assignee and quoted story match. |
| Three acceptance criteria | 138–144 | 1835–1869; 3770–3780 | All three match, including “logged in as a user” and **10 milliseconds**. |
| SRS/SDD distinction | 152 | 1957–1961 | The overlap qualification is retained. |
| Eight heuristic recommendations | 284–291 | 2878–2884; 2903–2907; 2928–2932; 2959–2963; 2982–2988; 3008–3014; 3038–3042; 3061–3065 | These are the source’s recommendations, correctly retained as attributed quotations. |
| Strong coding recommendations and “arbitrary” thresholds | 324, 341 | 3324; 3373; 3464–3470 | The source supplies both the emphatic recommendations and the qualification. |
| Omitted RACI example and Wayback reminders | 9, 77, 152 | 907–978; 1977; 2251; 2336 | Summarisation choices, not evidence of an unread chapter or a newly missing substantive section. |
| Conversion-history statements | 9, 409 | Source card; relevant restored passages | The supplied provenance records support the restoration account. The tape alone cannot prove historical reading or conversion-comparison activity. |

The derived-tier discussion in the fixer log raises a **workflow dependency**, rather than another verified defect in `post-audit-deep.md`: derived artefacts require the protocol’s re-derivation decision and matching provenance stamps. The blind auditor’s acceptance of notice removal does not independently establish that those requirements have been completed.

**Confirmed, fix wrong or incomplete:** none established beyond the disputed marker-scope question H6.

**Missed by the fix-in-place audit:** none. The blind report contains no positive defect findings.

**New defects introduced by the current fixer edits:** none. The four changes leave supported wording, preserve the quotations and statistics, and remove no necessary source qualification.

**3. Remaining edits**

**None.** No source-verified replacement or strip is required in `post-audit-deep.md` to resolve the supplied findings. The narrower current wording can remain for all disputed or over-flagged edits.

**4. Counts**

Counts use one unit per numbered finding; S4 is one coverage-inventory finding.

| Classification | Current scoped audit | Historical log | Total |
|---|---:|---:|---:|
| Confirmed and fixed | 1 | 14 | **15** |
| Confirmed, fix wrong or incomplete | 0 | 0 | **0** |
| Missed by fixer | 0 | 0 | **0** |
| Over-flagged by blind auditor | 0 | 0 | **0** |
| Over-flagged by fixer | 1 | 1 | **2** |
| Disputed | 2 | 2 | **4** |
| **Findings sorted** | **4** | **17** | **21** |

New defects introduced: **0**.

**5. Gate verdict**

**PASS for the scoped deep-reference source-only gate.** No remaining edit is required, and the current fixer changes introduce no verified defect.

This verdict preserves the earlier-audit boundary; it does not recertify every unchanged claim. Shipping still requires the protocol’s audit recording, stamping and derived-tier provenance checks.