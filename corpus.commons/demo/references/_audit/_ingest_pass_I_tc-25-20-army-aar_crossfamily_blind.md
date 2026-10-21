## Scoped re-audit 2026-10-16: restored Figures 1-1 to 1-4

**Result: three defects—one source-integrity description in the deep reference and two derived-tier defects. The restored figure quotations themselves match the tape.**

### 1. Material read

Read in full: `blind-brief.md`, all three calibration fixtures, `pass-i-spec.md`, `frozen-deep.md`, and `source-card.md`. The frozen reference’s SHA-256 matches its manifest.

Read the complete prescribed tape ranges: **100–345, 760–800, and 885–897**. Searched the tape for ALL-CAPS headings to check the Chapter 2 and Chapter 3 ordering claim. No other tape passages were substantively audited.

Read every specified derived-tier passage in the light reference, AAR and retro distillations, and their two Markdown indexes.

Checked PDF metadata and deterministically extracted its cover, title/contents, Preface, authentication, opening Chapter 1, and final pages for provenance. The PDF has **35 pages**, and its SHA-256 matches the source card.

The historical assertions about the earlier converter, the previous auditor’s reading, the 802-line comparison, and earlier page-render checks could not be independently established from the supplied snapshots. They remain provenance assertions, not newly verified facts. The unchanged APD-status and doctrinal-history discussion was outside this restored-material audit.

No files were edited. The filesystem is read-only; this report is supplied here, and the existing audit log remains untouched.

### 2. Findings

1. **Deep reference line 290: inaccurate verbatim-coverage claim.**

   **Problem class:** source-integrity description.

   The paragraph says Figure 4-1 “is captured verbatim in Part IV above.” Part IV, line 149, summarises the outline using arrows and semicolons and omits source wording. For example, tape line 772 includes “(what was supposed to happen)”, and line 774 includes “(TTPs)”; both are omitted from that summary.

   **Evidence:** tape **767–798**, compared with deep-reference line **149**.

   **Exact fix:** replace:

   > is captured verbatim in Part IV above.

   with:

   > is summarised in Part IV above.

   This finding concerns the explicitly scoped integrity paragraph; it does not reopen line 149’s unchanged evidence marker.

2. **Derived AAR distillation line 56, “Is the plan complete?”: incomplete checklist presented as complete.**

   **Deep-reference anchor:** line **72**, which correctly preserves the complete Planning list.

   **Problem class:** dropped source content in an exhaustive task checklist.

   The question asks whether **each** Figure 1-4 planning action has been completed, but its document-review item includes only the training and evaluation plan. Figure 1-4 also specifies reviewing ARTEP mission training plans and soldier training publications.

   **Evidence:** tape **295–302**, particularly **296–297**.

   **Exact replacement question:**

   > Has each Figure 1-4 planning action been done: qualified OCs selected and trained; the training and evaluation plan, ARTEP mission training plans and soldier training publications reviewed; AAR timing identified; attendance determined; potential sites selected; training aids chosen; and the AAR plan reviewed (Source: *TC 25-20*, Ch 1, Figure 1-4)?

3. **Derived AAR distillation line 44, concept 17: unsupported formal-AAR qualification.**

   **Deep-reference anchor:** line **46**, which describes Figure 4-1 without restricting it to formal AARs.

   **Problem class:** unsupported source attribution.

   “Figure 4-1 expands it for the formal AAR” introduces a restriction absent from the cited material. The source calls Figure 4-1 a recommended sequence “for conducting an AAR.” Chapter 1 says all AARs follow the same general format and informal AARs use the standard format.

   **Evidence:** tape **151–156**, **232–235**, and **765–798**.

   **Exact replacement sentence:**

   > The format is the skeleton a facilitator can run in order; Figure 4-1 gives a recommended sequence for conducting an AAR as a grouped outline with additional discussion subtopics.

### 3. Counts and required checks

**Claims checked:** all **50 distinct restored figure-list entries**, including their repetitions in the scoped derived passages:

| Figure | Entries checked |
|---|---:|
| 1-1 | 8 |
| 1-2 | 10 |
| 1-3 | 10: five formal, five informal |
| 1-4 | 22: seven Planning, eight Preparation, four Conduct, three Follow up |

The surrounding scoped prose, counts, markers, cross-references, provenance statements and task mappings were also checked. Repeated claims are not recounted as additional distinct figure entries.

**Defects: 3 total.**

| Class | Count |
|---|---:|
| Inaccurate source-integrity description | 1 |
| Dropped content in an exhaustive derived checklist | 1 |
| Unsupported derived source attribution | 1 |
| Restored quotation or evidence-marker defects | 0 |
| Changed quantities | 0 |
| Missing restored figure coverage | 0 |

**Key-statistics/planning-targets table:** the two scoped rows are correct: Figure 1-1 contains **eight** key points, and Figure 1-2 contains **ten** format items. Their quoted endpoints match. The remaining table rows were outside this re-audit.

**Author-stated limitations:** the scoped additions introduce no list of author-stated limitations. The reference’s unchanged limitations and absence claims were not revalidated against the unread remainder of the source.

### 4. Over-flag guard

- **“integrate into tutors training plans”: clean.** It matches tape lines 325–326; the brief explicitly confirms the printed wording.
- **Figure lists joined with spaces: clean.** The brief permits this treatment of drawn bullets. The restored wording and item order match.
- **Figure 1-3’s first formal cell lacks a final full stop: clean.** The tape likewise gives “controllers (OCs)” without one.
- **“Three items carry a gloss in parentheses”: retained.** The sentence identifies three question-bearing glosses; it need not mean that only three items contain any parenthetical material.
- **Planning and Preparation follow the chapter-heading order: clean.** Their corresponding actions occur in the stated sequence. The claim does not promise identical heading wording or exhaustive reproduction of every heading.
- **Figure 1-2 and Figure 4-1 share a grouped sequence: clean.** Figure 4-1 groups the objectives-and-intent items and adds discussion subtopics while preserving the sequence.
- **“C2”: clean.** Tape line 895 prints “Command and Control (C2)”.
- **Sprint Goal/plan and assessment-recipient questions: permitted derived guidance.** They occur in task distillations; the retro mapping is explicitly identified as the distillation’s own mapping.
- **The quotation checker’s line-178 warning: not a scoped defect.** It concerns the unchanged BOS quotation’s conversion spacing around “Figure 4-2”; the scoped `C2` correction matches the source.
- **Historical coverage assertions: not automatically defects.** An unavailable earlier conversion prevents independent confirmation, but does not establish that the assertions are false.