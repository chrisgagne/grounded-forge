## 1. What I read

Read in full: `sort-brief.md`, the three calibration fixtures, `pass-i-spec.md`, both audit reports, all 184 lines of `post-audit-deep.md`, all 109 lines of `tape.md`, and `source-card.md`. Also read the repository operating contract and required architecture documents.

Inspected the complete original poster, including its routing, footer, logos and strapline:

(`_planning/pass-i/demo/nhs-just-culture-guide/source.pdf`)

Verification:

- Both supplied deep-reference hashes are correct. **`frozen-deep.md` and `post-audit-deep.md` are byte-for-byte identical**, with SHA256 `e30802c2306b9e025a7f53fbf0559e4fc269993f439d41c7e3f1fc274080b114`.
- The PDF hash matches the source card. Its metadata confirms one A3 page and March 2018 creation/modification dates.
- Independent whole-page Poppler extraction has exactly the same word-token multiset as the regional tape.
- The verbatim checker reports only the permitted initial-letter difference at deep line 15. All seven recommendation blockquotes match.

Consequently, “confirmed and fixed” below means that the defect described in the fixer’s log has a correct resolution **present in the supplied post-audit file**. The packet does not demonstrate that this audit made those changes: the frozen snapshot already contains them.

No files were edited. This response is the report.

## 2. Sorted ledger

`B` identifies the blind auditor’s numbered findings; `F` identifies the fixer’s numbered changes. All deep-reference line numbers refer to the supplied post-audit file. Tape references are line numbers; the original occupies PDF page 1.

### Confirmed and fixed

| Finding | Post-audit line | Tape lines | Assessment |
|---|---:|---:|---|
| F1 — “calibrated to this prior” | 15 | 8–10, 74–77, 88–91 | Unsupported design intent has been replaced with an observable relationship: D/E repeat the qualified position against singling out. |
| F2 — enumerating “all parties” as users | 19 | 18–28 | The replacement preserves the source’s unspecified “all parties” and separately identifies the communication audience. |
| F3 — poster “opens with” four caveats | 25 | 5–41 | “The preamble closes with four caveats” correctly locates the block after the three purpose/use paragraphs. |
| F4 — investigation-input mechanism | 28 | 34–36 | The source permits use at any point and revisiting with more information. It does not state that every test input is a fact surfaced by investigation. Removing that additional mechanism is justified. “Re-entrant” alone would not establish a defect. |
| F6 — culpability/default framing and sequencing | 42 | 15–17, 42–105 | The replacement distinguishes the early deliberate-harm exit from G and accurately quotes the preamble. Individual intervention is broader than culpability. |
| F7 — system’s “side of the contract” | 70 | 68–78 | The contract metaphor supplies an explanatory framework absent from the poster. It is absent from the post-audit text. |
| F9 — training disadvantage and ordinary supervision | 80 | 83–86 | The corrected 4b/4c paraphrases retain peer-group training and supervision that normally should be provided. A separate 4a defect remains; see S1. |
| F10 — substitution explained through different outcomes | 80 | 80–86 | The poster asks about comparable peers’ behaviour, not whether substitution would produce a different outcome. The invented explanation is absent. |
| F11 — “exoneration” | 88 | 79–93 | “No to” the Q4 questions correctly replaces an exoneration claim. E expressly permits wider actions that include the individual. The separate Q3 narrowing remains under B3. |
| F12 — mandatory occupational-health response and uniform investigation wording | 92 | 54–64, 74–105 | B and C are distinguished; occupational-health referral remains qualified as likely. The replacement accurately distinguishes A–C’s investigation wording from D–G’s wider-actions wording. |
| F13 — deliberate phrasing and exclusively system-level correction | 124 | 74–77 | The replacement accurately preserves individual-directed action as a possibility within the wider actions indicated by investigation. |
| F15 — Q4 negatives and graduated management sequence | 148 | 80–86, 103–105 | The corrected passage preserves “no indications” for 4a, treats 4c as a direct question, and reports G’s possibilities without inventing an escalation sequence. Other defects in this paragraph remain under B3/B4. |
| F16 — `[V]` on calculated counts | 156–159 | 29–105 | Five tests, eleven sub-questions, seven exits and four caveats are correct counts, rather than verbatim statements. `[AP]` with explicit counting provenance is appropriate. |
| F17 — B/C both described as occupational-health pathways | 161 | 54–64 | Correctly distinguishes substance-abuse-at-work guidance from health guidance likely to include occupational-health referral. |

### Confirmed, fix wrong or incomplete

| Findings | Post-audit line | Tape lines | Assessment |
|---|---:|---:|---|
| F14 / B5 — ranking F’s wording | 140 | 74–77, 88–99 | Removing the causal explanation was justified, but “a softer formulation” remains. The poster gives different wording without ranking its strength. Report the wording and mitigation guidance directly. |
| F19 / B6 — contributors considered “before the individual” | 172 | 15–17, 26–28, 42–49 | Replacing “individual blame” did not remove the unsupported structural claim. Q1 immediately considers individual intention and can route to management action. The source’s actual temporal qualification concerns principles considered before **formal management action**. |

### Missed by the fix-in-place audit

| Finding | Post-audit line | Tape lines | Assessment |
|---|---:|---:|---|
| B1 — licence assignment and legal propagation | 5, 184; associated scope declaration at 6 | Entire tape, especially 108–109; PDF p. 1 | Neither the poster nor its metadata establishes OGL applicability, CC BY equivalence or derivative conditions. The source card repeats these assertions without providing their evidential basis. Bibliographic placement does not substantiate them. |
| B2 — publisher history and canonical equivalence | 5 | 109; PDF p. 1 | The printed domain is supported. The 2022 merger, page retirement and equivalence to a separately authenticated canonical copy are not established by this packet. |
| B3 — dropping “accepted practice” from Q3 | 70, 88, 132, 148 | 67–79 | Confirmed. Questions 3a/3b explicitly include protocols/**accepted practice**. The summaries narrow the condition to protocols; line 70 strengthens that narrowing with “the only path”. |
| B4 — health factors declared absent | 148 | 52, 59–60, 67 | Confirmed. No to the questions establishes no **indications** of the listed conditions, rather than their actual absence. |
| B7 — individual support versus wider investigation | No direct deep counterpart; source card 21 | 5–10, 45–105 | Confirmed sidecar defect. Individual support/intervention and wider investigation are not mutually exclusive. Every exit retains investigation or wider actions. The deep reference correctly preserves that relationship. |

B1’s proposed `scope: unverified` remedy should **not** be adopted automatically: `unverified` is outside the repository’s scope taxonomy. Scope is an operator distribution classification, distinct from verified licensing. The unsupported rights assertions must be removed; the open-distribution decision still needs substantiation.

### Over-flagged

| Finding | Post-audit line | Source location | Assessment |
|---|---:|---|---|
| F20 — “1.5MB” | 176, where the size is absent | Supplied PDF: 1,516,336 bytes | **Fixer over-flag.** Approximately 1.5 MB is correct bibliographic information about the supplied original. It need not appear in the poster’s prose. The fixer reportedly lacked the PDF, which explains its inability to verify the figure, but does not make the figure a source defect. No restoration is necessary. |

### Disputed

| Finding | Post-audit line | Tape lines | Both readings |
|---|---:|---:|---|
| F5 — internal decision aid / external communication tool | 38 | 5–7, 18–28 | **For flagging:** the source does not divide uses into internal/external categories; communication also includes staff. **Against:** these can be ordinary descriptions of the managers’ conversation and communication with patients/families, without claiming exclusive audiences. The present quotation avoids the ambiguity and needs no edit. |
| F8 — “potential individual accountability” | 70 | 15–17, 67–79 | **For flagging:** accountability can suggest a culpability framework broader than the source’s support/intervention language. **Against:** onward movement towards possible formal management action reasonably supports that qualified paraphrase; a synonym’s absence is insufficient by itself. The present “proceeds to Q4” wording is accurate. |
| F18 — NPSA tree as structural predecessor | 166 | 109 | **For flagging:** “based on the work of” does not specify which features were inherited. **Against:** describing the named Incident Decision Tree as a structural antecedent is a reasonable reading of attribution on a decision-tree poster. The current literal attribution is supported and needs no edit. |

### Additional defect found during the sort

| Finding | Post-audit line | Tape lines | Assessment |
|---|---:|---:|---|
| S1 — Q4 paraphrase loses epistemic and comparability qualifications | 80 | 80–84 | “Whether a peer … would have done the same thing” drops **indications**, comparable experience and qualifications, and changes the source’s conditional behavioural question into a retrospective formulation. The training paraphrase also drops “relevant”. Replace it with a faithful summary. This is a remaining defect, not an introduced edit. |

### Fixer’s downstream carry-forward observations

These are follow-up claims about other artefacts, rather than additional findings in the supplied deep reference. Their source fidelity can be assessed from the quoted wording; their continued presence at the reported downstream lines cannot be verified from this packet.

| Reported downstream wording | Source assessment | Deep counterpart / tape |
|---|---|---|
| “Re-entrant” | Supported shorthand for revisiting; not independently defective. | Deep 28; tape 34–36 |
| Enumerated users and “for managers, staff, patients, families” | Audience/user distinction needs the correction described under F2. | Deep 19/38; tape 18–28 |
| “Patient-safety outcomes are not exhausted by the individual response” | Broad interpretive wording; the narrower claim that every exit retains investigation/wider actions is supported. | Deep 92; tape 45–105 |
| Q4: peers would have done the same, training missed, supervision absent | Incomplete qualifications; use the actual questions. | Deep 76–80; tape 80–86 |
| Generic health pathways | Must preserve B/C differences and C’s qualified occupational-health referral. | Deep 92/161; tape 54–64 |
| Graduated response before regulatory bodies | Unsupported sequence. | Deep 148; tape 103–105 |
| System contract / individual accountability | Contract confirmed unsupported; accountability disputed as above. | Deep 70; tape 67–79 |
| Substitution producing a different outcome | Unsupported outcome explanation. | Deep 80; tape 80–86 |
| “Structural predecessor” | Disputed as F18. | Deep 166; tape 109 |
| “Default to system, not to individual” | Overgeneralises: Q1 permits an immediate individual response. | Deep 15/42; tape 42–49 |
| System question never extinguished by individual findings | Supported when confined to the poster’s retained investigation/wider-action requirements. | Deep 92/100; tape 45–105 |
| Q2 “Yes to any → exit” | Correct as a coarse statement that Yes exits, but incomplete as routing guidance: 2a goes to B; 2b/2c go to C. | Deep 60; tape 52–67 |

### Did a fixer edit introduce a new defect?

**No demonstrable introduced defect.** The supplied snapshots are identical. The historical changes described in the log have been checked against the source; their present resolutions introduce no additional defect identified here. S1 and the incomplete fixes already exist in both snapshots.

## 3. Remaining edits

These are exact changes needed in `post-audit-deep.md`. Line numbers refer to its current version. No sidecar or downstream changes are included in this list.

1. **Line 5 — replace the licence sentence.**

   Current:
   > Licence: **Open Government Licence v3.0** (UK public-sector open licence; CC BY 4.0-equivalent for redistribution and derivative purposes).

   Replacement:
   > Licence: not stated in the supplied poster; applicability of the source card's Open Government Licence claim has not been verified from the supplied materials.

2. **Line 5 — replace the canonical-URL sentence.**

   Current:
   > Canonical URL: https://cpcw.org.uk/wp-content/uploads/sites/19/2018/03/180316-NHSi_just_culture_guide_A3.pdf (mirror; publisher page at improvement.nhs.uk has been retired following the 2022 merger of NHS Improvement into NHS England).

   Replacement:
   > PDF URL recorded on the source card: https://cpcw.org.uk/wp-content/uploads/sites/19/2018/03/180316-NHSi_just_culture_guide_A3.pdf. The poster prints improvement.nhs.uk in its footer.

3. **Line 70 — retain the first sentence; replace the remainder.**

   Current:
   > If there is no agreed protocol (3a), or the protocol is unworkable or not in routine use (3b), or the individual did not knowingly depart from it (3c), then action singling out the individual is unlikely to be appropriate — the wider investigation should indicate the actions needed, and those actions may include, but not be limited to, the individual [AR]. The test isolates the case of *knowing departure from a workable, routinely-used, agreed protocol* — the conjunction of all three sub-conditions — as the only path that proceeds to Q4.

   Replacement:
   > Q3 proceeds to Q4 only on Yes to all three questions: applicable agreed protocols/accepted practice are in place, they were workable and in routine use, and the individual knowingly departed from “these protocols”. No to any routes to Recommendation D, which says action singling out the individual is unlikely to be appropriate and that the wider actions indicated by the investigation may include, but not be limited to, the individual [AP].

4. **Line 80 — replace the second sentence.**

   Current:
   > The substitution test asks whether a peer in the same circumstances would have done the same thing (4a), whether the individual was missed out of training given to their peer group (4b), or whether more senior team members failed to provide supervision that normally should be provided (4c).

   Replacement:
   > The substitution test asks whether there are indications that other individuals from the same peer group, with comparable experience and qualifications, would behave in the same way in similar circumstances (4a), whether the individual was missed out when relevant training was provided to their peer group (4b), or whether more senior team members failed to provide supervision that normally should be provided (4c) [AP].

5. **Line 88 — replace the Q3 parenthetical.**

   Current:
   > (Q3 — knowing departure from an agreed, workable protocol in routine use)

   Replacement:
   > (Q3 — Yes to all three questions about applicable agreed protocols/accepted practice, workability and routine use, and knowing departure)

6. **Line 132 — replace the second sentence.**

   Current:
   > The repetition is structural to the poster — the same qualified response applies whether the routing arises from a foresight finding (no workable protocol, no knowing departure) or from a substitution finding (peer behaviour, training gap, supervision absence) [AR].

   Replacement:
   > The same qualified response applies at two different exits: No to any of Q3's questions routes to D, and Yes to any of Q4's questions routes to E [AP].

7. **Line 140 — replace the first sentence.**

   Current:
   > The shift from "is unlikely to be appropriate" (D and E) to "may not be appropriate" (F) is a softer formulation, reached only after the prior filters, and F's guidance turns on the degree of mitigation.

   Replacement:
   > Recommendations D and E say “is unlikely to be appropriate”; Recommendation F says “may not be appropriate” and directs the reader to organisational guidance likely to include senior HR advice on the degree of mitigation (Q3–Q5 recommendations) [AP].

8. **Line 148 — replace the first sentence.**

   Current:
   > The G end-state is the residual after all prior filters have routed elsewhere: deliberate harm absent (Q1 No), health factors absent (Q2 No to all), foresight present (Q3 Yes to all — workable protocol, in routine use, knowingly departed from), substitution findings absent (Q4 No to all — no indications that peers would have behaved the same way, the individual was not missed out of training, and more senior team members did not fail to provide supervision that normally should be provided), and no significant mitigating circumstances (Q5 No).

   Replacement:
   > Recommendation G is reached on No to Q1; No to all Q2 questions about indications of substance abuse, physical ill health and mental ill health; Yes to all Q3 questions about applicable agreed protocols/accepted practice, workability and routine use, and knowing departure from “these protocols”; No to all Q4 questions about indications of comparable peer behaviour, omission from relevant training provided to the peer group, and failure by more senior team members to provide supervision that normally should be provided; and No to significant mitigating circumstances at Q5 [AP].

9. **Line 172 — replace the paragraph.**

   Current:
   > The source does not explicitly frame against named positions or authors. Its argumentative work is structural: the decision tree is built to surface system, training, supervision, and mitigating contributors *before* the individual. The implicit frame is against what the source calls "the tendency to treat wider patient safety issues as individual issues" (Preamble, paragraph 3). The source treats this tendency as a pattern to be corrected by structural means (the tree), not as a position attached to a named author or school [AR].

   Replacement:
   > The source does not identify a named opposing author or school. It states that using the guide helps protect patients “by removing the tendency to treat wider patient safety issues as individual issues” (Preamble, paragraph 3) [V]. It also says the guide highlights principles to consider before formal management action is directed at an individual staff member (Preamble, paragraph 2) [AP].

10. **Line 184 — strip the entire OGL propagation bullet.**

    Current:
    > - **OGL v3.0 propagation.** The Open Government Licence v3.0 is a UK public-sector open licence with terms compatible with CC BY 4.0: redistribution and derivatives are permitted with attribution; commercial use is permitted; no copyleft obligation propagates. Derivative artefacts in this corpus (light reference, distillations, build-profile extracts) inherit only the attribution requirement.

    Replacement: **strip**.

## 4. Counts

Counts use grouped findings, rather than individual clauses or edit locations. B5/F14 and B6/F19 each count once in the combined total.

| Disposition | Unique findings |
|---|---:|
| Confirmed and fixed in the supplied text | 14 |
| Confirmed, fix incomplete | 2 |
| Missed by fixer | 5 |
| Additional confirmed defect found during sort | 1 |
| Over-flagged | 1 |
| Disputed | 3 |
| **Total** | **26** |

**Confirmed defects: 22**, comprising 14 resolved and 8 remaining grouped defects. One remaining defect is sidecar-only.

| Auditor | Confirmed numbered findings | Over-flagged | Disputed |
|---|---:|---:|---:|
| Blind | 7 | 0 | 0 |
| Fixer | 16 | 1 | 3 |

The fixer missed five blind findings entirely: **B1–B4 and B7**. Its partial treatment of B5/B6 is counted separately as incomplete fixes. Downstream carry-forward observations are not added to these counts because their current artefact occurrences were not supplied for verification.

## 5. Gate verdict after the remaining edits

**FAIL for the complete Pass I release gate.**

Applying edits 1–10 would make the deep reference’s source-content claims pass this source-only review. The remaining release blockers are:

- The claimed open licence remains unverified; retaining `Scope: open` does not establish redistribution rights.
- The source card still contains unsupported provenance/licensing assertions and B7’s false individual-versus-investigation choice.
- The fixer explicitly records that the light reference and distillations have not been re-derived and re-stamped. Their fidelity to the corrected deep reference therefore remains unverified.

No substantive source section, routing branch or recommendation quotation requires re-ingestion.