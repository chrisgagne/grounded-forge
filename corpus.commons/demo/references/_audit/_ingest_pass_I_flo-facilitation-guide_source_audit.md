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
