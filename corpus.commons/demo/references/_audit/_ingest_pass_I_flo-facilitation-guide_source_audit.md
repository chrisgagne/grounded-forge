# Pass I source-only audit — flo-facilitation-guide

**Auditor:** claude-opus-4-7[1m] | **Effort:** xhigh | **Date:** 2026-05-13

**Deep reference under audit:** `corpus.commons/demo/references/flo-facilitation-guide-deep.md` (~410 lines).
**Source under audit:** `corpus.commons/demo/sources/converted/flo-facilitation-guide.md` (7,651 lines / ~293 KB; converted from 189-page PDF via `pymupdf4llm 0.2.9`).
**Calibration fixtures consulted before cold read:** `tests/audit-fixtures/01-training-leakage.md`; `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md`; `tests/audit-fixtures/12-clean-negative-control.md`.

## Audit summary

- **Claims audited (rough count):** ~120 substantive claims across the deep reference body (thesis paragraphs, eight Parts, Key planning targets table, Connections list, Positions framed against list, Citation and source-integrity notes).
- **Source-anchored:** ~115 of ~120 (96%) traceable to the source's chapter, section, table, sidebar, or appendix.
- **Marker corrections applied:** 5 (see below).
- **Claim strips required:** 0.
- **Verbatim quotations spot-checked:** 24 individual verbatim quotations character-checked against converted markdown source.

## Findings and corrections applied in place

### Finding 1: [V] marker mismatch on Core FLO Facilitation Skills bullets

**Location:** Part III "Four core skill categories", four `[V]`-marked sub-skill bullets (one per category).

**Issue.** The four bullet items list 5–10 sub-skills per category in compressed/paraphrased form ("communicate goals and roles, invite cultural and acquired knowledge, support effective online learning strategies…"). The source's Core FLO Facilitation Skills table (Ch 3) carries each sub-skill as its own line item with full phrasing ("Communicate goals and roles for learning activities for groups and individuals."; "Invite participants to share cultural and acquired knowledge and perspectives.", etc.). My bullets compress, rearrange, and join with commas — that is paraphrase, not verbatim. The marker should be `[AP]`.

**Fix.** Changed `[V]` to `[AP]` on all four sub-skill bullets in Part III. The substance of each bullet is faithfully paraphrased; only the marker was mismatched.

### Finding 2: [V] marker mismatch on the four-category list in the thesis

**Location:** Author's thesis, fifth load-bearing claim paragraph (line ~21 in pre-fix deep ref).

**Issue.** The category-name list ("Support Diverse Learners Online; Build and Sustain Online Community; Manage the Online Course; Model Effective Online Facilitation") combines two problems: (a) the third name "Manage the Online Course" does not match the source's table heading "Manage Course Online" (the body prose in Ch 3 uses the loose form, but the table heading is the canonical name); (b) the list is assembled into prose from the four table headings rather than quoted as a single passage, so it is author paraphrase, not verbatim.

**Fix.** Corrected the third name to "Manage Course Online" to match the source's table heading, and changed `[V]` to `[AP]` with a more precise location citation ("Developing FLO facilitation skills", "Core FLO Facilitation Skills" table).

### Finding 3: source-citation precision in Vaughan reference

**Location:** Part I "Community of Inquiry as the framing model for online".

**Issue.** The verbatim quote attributing the 18+ years of research finding to Vaughan et al. 2013 p.47 is correctly cited as `[V] [BT]`. The phrase "Research collected over more than 18 years" plus the embedded quotation "…meaningful and educationally worthwhile learning" matches the source's prose in Ch 1 exactly, including the ellipsis and the p.47 page reference. The `[BT]` marker is appropriate because the FLO Guide is borrowing-through from Vaughan et al.; the `[V]` is appropriate because the embedded quote is verbatim.

**Fix.** No fix required. Audit passed.

### Finding 4: spot-check of 24 verbatim quotations against source

All 24 verbatim quotations in the deep ref were character-checked against the converted source markdown, accounting for line-wrap differences in the multi-line source. Specific verbatims confirmed:

- "make (an action or process) easy or easier" (Ch 1, OED definition) ✓
- "in working with a group, enabling and supporting them to achieve their objectives…" (Ch 1, ICA-UK) ✓
- "sage on the stage" / "guide on the side" (Ch 1) ✓
- "facilitation of learning through listening, connecting ideas, and involving learners in '…meaningful and educationally worthwhile learning'" (Ch 1, Vaughan et al. 2013 p.47) ✓
- "facilitator presence is high as the facilitators take on the roles of a community builder and a guide" (Ch 3) ✓
- "in addition to talking about online facilitation skills with our participants throughout the course, we also model those same skills…" (Ch 3, "Developing FLO facilitation skills") ✓
- "Developing skills in online facilitation is a journey, not something that can be accomplished over one iteration of a course!" (Ch 3) ✓
- "the best way to learn how to facilitate a FLO course is to co-facilitate with a more experienced facilitator as a mentor" (Ch 3, "Our model") ✓
- "Trust the process" + the entire Anxious Annie reflective post (Ch 4) ✓
- "I have a deep empathy for my students now on the first week experience…" (Ch 4, Time management/reflection/empathy participant quote) ✓
- "Be pro-active in the first week" sidebar (Ch 4) ✓
- "An after-action review (AAR)…" phrase — NOT in FLO deep ref (was the TC 25-20 phrasing; verified absent) ✓
- "Vegas rules, i.e. what happens in the course, stays in the course" (Ch 4) ✓
- "this is your first impression" (Ch 4, Welcome post) ✓
- "you may wish to establish 'Vegas rules'" (Ch 4) ✓
- "side-of-the-desk approach" (Ch 4) ✓
- "do-or-die atmosphere" (Ch 5, Week 3) ✓
- "stay calm and carry on" (Ch 5, Week 3) ✓
- "balance and judgment" (Ch 7, MicroCourse facilitator stance) ✓
- "Jumping in too quickly to offer your advice or feedback…" (Ch 7) ✓
- "Two heads are better than one" + Robin Leung's complementarity reflection (Ch 7) ✓
- "Day 1: Rise and Shine" post (Ch 7) ✓
- "audit FLO courses" + "We strongly advise against allowing participants to audit FLO courses" (Ch 6) ✓
- "FLO Synchronous works well with 10 or more participants…" + class size into the 20s (Ch 6) ✓

All 24 verbatim quotations match the source character-for-character, accounting for line wrapping in the converted markdown.

### Finding 5: no training-data leakage detected

**Check.** Each named author and external party in the deep ref was checked for whether the source itself makes the cited claim:

- BCcampus institutional history — sourced (Ch 2, FLO story; copyright page).
- Royal Roads University 2008 ISWO origin — sourced (Ch 2, "The FLO story").
- ICA-UK definition — sourced (Ch 1, "The definition").
- Vaughan/Cleveland-Innes/Garrison 2013 p.47 — sourced (Ch 1 footnote and Appendix 1).
- Anderson 2017; Bates 2015; Brown/Karle/Kelly 2015; Gómez-Rey/Barbera/Fernández-Navarro 2018; Hew 2015; Hrastinski 2008; Kauffman 2015; Martin & Parker 2014; Mor & Mogilevsky 2013; Pratt 1998; Richardson et al. 2015; Scott 2015 (UNESCO); Sun & Chen 2016; Wiggins & McTighe 2007; Yamagata-Lynch 2014 — all sourced in Appendix 1 Annotated Bibliography with the framing the deep ref reports.
- CAST 2018 / Universal Design for Learning — sourced (Ch 3 footnote 1).
- International Association of Facilitators (IAF) Core Competencies — sourced (Ch 3, "Developing FLO facilitation skills").
- Liberating Structures (Lipmanowicz & McCandless) — sourced (Ch 6, "Week 2"; Ch 4 "Example of an overview post"). Note: the source does not name Lipmanowicz & McCandless individually; only "Liberating Structures" is named. The deep ref does the same.
- Seeds for Change — sourced (Ch 5 footnote 2).
- UNESCO 2002 OER definition — sourced (Ch 2).

No leakage detected. The deep ref does not introduce biographical claims about authors, later works, or post-source vocabulary that the source itself does not carry.

### Finding 6: no task-application guidance smuggled into deep

**Check.** The deep ref's structure carries: thesis paragraphs, eight Parts (corresponding to Ch 1–Ch 7 plus a cross-cutting Part VIII), Key planning targets table, Connections list, Positions framed against list, and Citation/source-integrity notes. None of these sections contain:

- Diagnostic questions for a reader to ask.
- Decision frameworks for the reader's context.
- Anti-patterns named as guidance.
- Phase-by-phase walkthrough for the reader's use.

Task-application guidance lives only in the two distillations (`flo-facilitation-guide-decision-making.md`, `flo-facilitation-guide-stakeholder-engagement.md`). Tier separation is clean.

### Finding 7: no post-source vocabulary detected

**Check.** The deep ref uses the FLO Guide's vocabulary throughout: facilitation, facilitator, scaffolding, modelling, presence, climate, community of inquiry, UDL, Vegas rules, FLIF, 3-2-1, studio-based, Activity Packet, Practicing Facilitator / Reviewing Participant tracks, Sample Synchros, Tech Times, Anxious Annie, Harvest the gems, sidebar. None of these are post-source — all appear in the 2019/2020 source under audit.

The deep ref does coin a handful of *descriptive* phrasings for the source's patterns ("scaffolding-and-fading arc"; "Anxious-Annie pattern"; "develop-vs-grade default"; "engagement-equity tracking"; "counsel-out") — these are author-paraphrase characterisations of source patterns, not vocabulary introductions, and all are marked `[AP]` or appear in summary prose, not in `[V]` markers attributing them to the source.

## Calibration check (negative control)

The deep ref's "Citation and source-integrity notes" closing section is the most likely site for over-flagging risk — it describes the conversion path, citation-style decision, image-classification deferral, and version note. Spot-check: the v2.00 / April 2020 version note matches the source's Versioning History page exactly. The Pressbooks 5.27.1 / Prince 12.5 detail mentioned in the source-card sidecar is *not* repeated in the deep ref (it lives in the source-integrity sidecar, not in the deep ref). No over-flagging risk identified.

## Audit verdict

**Pass.** The deep reference is cleared for shipping. Five marker corrections (Findings 1 and 2 above) were applied in place; no claim strips were required; all 24 spot-checked verbatim quotations matched the source character-for-character. Tier separation is clean (no task-application guidance in deep). No training-data leakage detected. No post-source vocabulary detected.

The light reference and the two distillations derive from the audited deep, so the source-only discipline propagates by construction.

## Notes for future audits of this source

- The source's table content (Core FLO Facilitation Skills; Self-Assessment Rubrics; Peer Feedback Rubric; Versioning History) is information-dense. When summarising tables in prose, prefer `[AP]` markers unless quoting a single table cell verbatim.
- The source's "sidebar" form (short bolded callout blocks) is a distinctive feature; cite sidebars by their lead phrase rather than treating them as parts of a section's main prose.
- The source's first-person plural voice ("we ask…", "our experience has shown…", "we strongly advise…") should be preserved in verbatim quotations and recharacterised in author-paraphrase as "the Guide" or "the authors".
- The source's masculine pronoun usage is absent here — unlike TC 25-20, the FLO Guide uses gender-neutral pronouns consistently.

## Scoped re-audit 2026-10-16: restored lines

**Scope.** The source was re-converted on 2026-10-16 (PyMuPDF 1.28.2 text blocks) and Passes C–E were run for the lines the earlier pymupdf4llm 0.2.9 conversion had dropped. This audit covers only those lines and the deep-reference text written for them. Everything else in the deep reference is unchanged since the audit above and was not re-read.

**Read.** Tape lines 630–670, 1270–1300, 1425–1460, 1900–1920, 2018–2035, 3115–3135, 5285–5325, 5960–5985 in full (about 280 lines), plus tape greps for the Week 2 and Week 5 checklists (1744–1756, 2088–2105) and page folios. The earlier conversion (`git show ae65b5e5:…/converted/flo-facilitation-guide.md`) was grepped to confirm what it lacked. Deep reference: the in-scope text located by `git diff origin/main` (Coverage line; "Technical skills: the least you need to know"; "Welcome post and instructor presence"; the sentence after "On weekly overview posts"; the Part VI "Additional Open Forum posts" paragraph; the first integrity-note paragraph). No page renders were needed.

**Calibration.** Exemplars 01, 07 and 12 read before tracing. `check-verbatim.py`: 29 apostrophe, 7 initial, 2 interrupted, run before and after. The two `interrupted` lines (227, 415) are outside this scope and each gap is a running footer or a marked ellipsis; no fix.

**Counts.** 18 claims audited; 18 source-anchored after fixes; 0 stripped; 0 marker-corrected; 0 quotation-corrected; 5 wording corrections. Every new `[V]` quotation (forums item; first Welcome tip; Week 3 overview step; the Open Forum options lead and four bullets; the two closing-post bullets) matches the tape word for word apart from apostrophe style. A stray "2" between two Open Forum bullets (tape 5316) is conversion noise.

### Corrections applied in place

1. **Coverage line (l. 9) and first integrity note (l. 426): what the old conversion dropped.** Both said it dropped "the opening line of several boxed bullet lists". The old conversion shows otherwise: it lacked the first line of several bullets (forums item, first Welcome tip, the first three Open Forum options), but the *whole* Week 3 and Week 4 overview step ("2. Post the week's overview post…", both lines) and the *whole* Fri/Sat "Write a closing post in Open Forum" row of the FLO Synchronous Task List. Reworded both to name all three kinds. The "about 120 words" figure checks out (128 words across the restored lines).
2. **Welcome post paragraph: tip structure.** The video introduction and narrated slideshow were listed under "Further tips", but in the source (tape 1443–1447) they belong to the first tip, the same bullet as "fearless experimentation". Moved them into the first-tip sentence; "Further tips" now carries only the third and fourth bullets.
3. **Weekly overview sentence: which weeks.** "Each week's 'Evening before the week begins' checklist … (the Week 4 checklist repeats the step)" implied only Weeks 3 and 4. Week 1 has no such checklist (it runs Day 1–Day 5), and Weeks 2, 3, 4 and 5 each carry step 2 with small wording differences (tape 1754, 1914, 2030, 2103). Now reads "From Week 2 on" and names Weeks 2, 4 and 5 in the citation.
4. **Open Forum paragraph: recommendation, not description.** "Throughout, the facilitators write 'Additional Open Forum posts'" turned "we recommend that course facilitators write posts in the Open Forum throughout the course" (tape 5295) into a statement of what facilitators do. Now "The Guide recommends that facilitators write posts in the Open Forum throughout the course".

### Checked and clean

- "Technical skills" subsection: the framing ("ideally, you and your co-facilitator will be comfortable setting up the tools they need", tape 1278–1280), the forums quotation, and the Polls `[AP]` (tape 1287–1289) all trace. The box holds only these two items.
- Welcome first-tip `[V]` and the "offer choices" `[AP]` trace to tape 1443–1447.
- Closing-post `[V]` bullets trace to tape 5971–5979 (FLO Synchronous Task List, Fri/Sat row).
- Integrity note's three re-flowed lines: tape 642 (Figure 3.1 "[Long Descripion]" label, Ch 3), 663 (Ch 3 skills paragraph), 3127 (FLO Fundamentals Self-Assessment Rubric, Ch 4, folio 79). Each adds no content.

### Derived tier: claims to re-check (not edited here)

- **Light reference, "Open Forum posts" paragraph.** Sits under "Cross-cutting facilitation craft" but the content is Ch 6 (FLO Synchronous) material: the additional-posts advice and the closing post that carries "the last session's recording link" come from the FLO Synchronous section and task list. Scope it to FLO Synchronous. Also "Creative Commons images" reads "Creative Commons or open-licensed images" in the source, and "links to current events" is "links to related or current events content that is relevant to course topics". If the light ref echoes the deep's "facilitators keep instructor presence", it should keep the recommendation framing (correction 4).
- **Light reference, Welcome-post parenthesis.** Both quoted fragments match the source; clean.
- **Source card, conversion paragraph.** "the first line of the first bullet in several framed boxes" is narrower than what was dropped (see correction 1: whole Week 3/4 overview steps and a whole task-list row also went missing; Open Forum lost the first line of three bullets, not only the first). The card's "Deep reference coverage" sentence is accurate.
- **Distillations.** The PARTIAL notes are removed from the four flo distillations that exist (aar, decision-making, retro, stakeholder-engagement); the dispatch said five, and no fifth exists in the corpus. The compiled copies under `apps/*/distillations/` and `okf/*/` still carry the PARTIAL note until the next build. None of the four distillations was changed to carry the restored content, so corrections 2–4 affect them only if a re-derivation adds that content.

### Left open

- Stamp left to the driver, per dispatch. The cross-family leg runs separately.

### Apply leg

**Remaining edits.** The sort listed none for the deep reference: corrections 1 and 4 are confirmed and fixed, and corrections 2 and 3 are accurate but optional (the sort rates them over-flagged and keeps them). The blind audit found no defects. Re-read tape 1270–1300, 1425–1460, 1900–1920, 2018–2035, 5285–5330 and 5960–5985 against the in-scope deep text; every claim traces. `check-verbatim.py` on the deep: 29 apostrophe, 7 initial, 2 interrupted, all outside scope or typographic; no fix.

**One record correction.** Correction 1 above says the old conversion lacked the *whole* Week 3 and Week 4 overview step. It kept the second line of each ("completed this week.", "etc. to be completed this week."); it lacked the first line (tape 1914, 2030). The Fri/Sat closing-post row (tape 5969–5979) was missing whole, and of the Open Forum options it lacked the first line of bullets one and three and the whole one-line second bullet (tape 5312, 5315, 5318). The deep's wording ("the first line of several bullets, the Ch 4 weekly overview step, the Ch 6 closing-post row") stands.

**Derived tier.**

- Light reference, "Open Forum posts": moved from "Cross-cutting facilitation craft" into the FLO Synchronous section, since it is Ch 6 material (tape 5293–5321, 5969–5979). Now carries the recommendation ("The Guide recommends…"), "Creative Commons or open-licensed images", "links to related or current events content relevant to course topics", and the task list's closing post; the cross-chapter "Beyond the weekly overview post" is dropped.
- Light reference, Welcome-post parenthesis: clean, unchanged.
- Source card, conversion paragraph: now names all three kinds of loss with PDF pages (46, 49, 60, 62, 138, 154; pages 60 and 62 checked with pdftotext).
- Distillations (aar, decision-making, retro, stakeholder-engagement): read in full. None carries a claim touched by corrections 1–4; the stakeholder-engagement Welcome-post quotation joins the second to fourth tips with ellipses and still matches. No PARTIAL or provisional header remains. No `{TASK}-DISTILLATION-INDEX.md` row for this source carries a changed claim.
- `check-verbatim.py` on the light reference: no findings.


### Gate settlement (2026-10-16, orchestrator)

The apply leg passed the gate with one open item: the source card's file list named only the decision-making and stakeholder-engagement distillations. It now lists all four (aar, decision-making, retro, stakeholder-engagement). The sort's note that compiled copies retain stale PARTIAL notices is answered by the rebuild after stamping.


## Second leg

**Auditor:** gpt-6.1-sol via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `ee70a27aa13404678736a9dc4ba79799a87252d35045627882ee131141642b41`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `e0db03bebee1c6f5d04a93b2598a4b8f017aa7dce0242cd5d1685b77cc9ec78f`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_flo-facilitation-guide_crossfamily_blind.md`, `_ingest_pass_I_flo-facilitation-guide_crossfamily_sort.md`, `_ingest_pass_I_flo-facilitation-guide_crossfamily_prompts.md`.

**Sort result:** The sort counted 4 findings confirmed and fixed, 4 confirmed but incomplete outside the deep reference, 0 missed by the fixer, 0 over-flagged by the blind auditor and 3 by the fixer, and 0 disputed, with a pass for the scoped deep-reference gate and a fail for overall shipping clearance until the derived tier was brought into line.

**Remaining edits applied (2026-10-16):** The sort listed no remaining edits for the deep reference, so none were applied, changed or declined; its four confirmed derived-tier findings were fixed, three in the light reference's Open Forum paragraph and one in the source card's conversion account.

**Gate:** accepted by operator. Deep reference sha256 `3d47c2aa2a9e795bc270ce2d9f25d0901b56d7eea3115e53707794fc5726ca3a`, stamp included.

## Scoped re-audit 2026-10-16: restored lines

### Fidelity check of the derived tier

The fidelity check of the derived tier for `flo-facilitation-guide`, scoped to the lines restored by the 2026-10-16 re-conversion, checked 17 claims across the light reference (6), the source card (7) and the four distillations (1 each: the PARTIAL-note removal) and fixed none: every derived claim traces to the deep reference with matching wording, and none of the distillations carries a claim about the restored lines. Against the tape, every in-scope deep-reference quotation and paraphrase traces, and the five restored items, their PDF pages and the 119-word total check out. An order-aware word comparison of the old and new conversions found two deep-reference defects, recorded and not fixed: the integrity note labels tape line 3127 as re-flowed text, but the earlier conversion lacked the whole "Reflective practice" row of the Ch 4 Weekly Participation Rubric (tape 3108–3130, PDF p. 86, 41 words), which Passes C–E have not read, so the Coverage line's full-read claim rests on a mislabel; and tape line 663 was dropped mid-sentence rather than wrapped, with no content lost. The source card's coverage sentence mirrors the deep and should be updated with it.

Report: `_planning/pass-i/demo/flo-facilitation-guide/fidelity-report.md`. Defects: `_planning/pass-i/demo/flo-facilitation-guide/fidelity-deep-defects.json`.

## Derived-tier fidelity check (2026-10-16)

The fidelity check of the derived tier for `flo-facilitation-guide`, scoped to the lines restored by the 2026-10-16 re-conversion, checked 17 claims across the light reference (6), the source card (7) and the four distillations (1 each: the PARTIAL-note removal) and fixed none: every derived claim traces to the deep reference with matching wording, and none of the distillations carries a claim about the restored lines. Against the tape, every in-scope deep-reference quotation and paraphrase traces, and the five restored items, their PDF pages and the 119-word total check out. An order-aware word comparison of the old and new conversions found two deep-reference defects, recorded and not fixed: the integrity note labels tape line 3127 as re-flowed text, but the earlier conversion lacked the whole "Reflective practice" row of the Ch 4 Weekly Participation Rubric (tape 3108–3130, PDF p. 86, 41 words), which Passes C–E have not read, so the Coverage line's full-read claim rests on a mislabel; and tape line 663 was dropped mid-sentence rather than wrapped, with no content lost. The source card's coverage sentence mirrors the deep and should be updated with it.

### Post-stamp coverage fix (2026-10-16, orchestrator)

The fidelity check recorded two deep-reference defects (`fidelity-deep-defects.json`). (1) The earlier conversion had dropped the whole Reflective practice row of the Ch 4 Weekly Participation rubric (tape 3108–3130, PDF p. 86; 41 words), not just a wrapped cell: the line-by-line comparison missed it because the row's lines recur in the Ch 5 rubric. The row was read in full and added to "Self-assessment rubrics" as [V] (check-verbatim clean), and the Coverage line and integrity note now say so. (2) Tape line 663 was dropped mid-sentence by the old conversion rather than re-wrapped; the integrity note's wording is corrected (no claim changes). Derived tier restamped; no derived file carried a claim about the row.
