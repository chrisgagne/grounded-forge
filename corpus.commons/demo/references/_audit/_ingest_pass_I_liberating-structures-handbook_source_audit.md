# Pass I source-only audit: liberating-structures-handbook-deep.md

**Date:** 2026-05-13
**Auditor model:** claude-opus-4-7[1m]
**Deep ref under audit:** `corpus.commons/demo/references/liberating-structures-handbook-deep.md`
**Source read at Pass C:** `corpus.commons/demo/sources/converted/liberating-structures-handbook.md` (60-page handbook; 2,767 lines of converted markdown; full content read end-to-end, no section omitted).

## Calibration

Before the cold read, three audit-fixture exemplars were re-read to anchor against known-bad and known-clean patterns:

- `tests/audit-fixtures/01-training-leakage.md` — biographical or career claim the source does not make (strip).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` — `[V]` marker on a paraphrased sentence (correct).
- `tests/audit-fixtures/12-clean-negative-control.md` — clean negative control (no findings).

## Audit pass

Each claim in the deep reference was traced to a specific passage in the converted source: the introduction (jazz metaphor, structural-change thesis); the seven framing sections (Ownership versus Buy-in; Choosing Space; Aesthetics Are Important; Working with the Space You're Given; Storyboard Design and Planning; Nothing About Me Without Me; Engage the Unusual Suspects); the LS activity-catalogue sections (each named structure cited via its sub-section header); the three Seeing-Complexity exercises; the five Random-Thoughts framing-aids; the Origins section (Torbert 1991; de Bono 1991; Axelrod 2010); the closing Pattern Language for Engagement essay (Alexander 1977; Johnson-Lenz primitives). Verbatim quotations were spot-checked character-by-character against the converted markdown.

### Claims audited

The deep reference contains roughly 200 distinct claims across the thesis (4 paragraphs), Part I (5 framing-section sub-sections), Part II (the LS catalogue — ~28 named structures grouped into seven thematic clusters), Part III (the three complexity exercises plus five framing-aids), Part IV (Origins and Pattern Language essay), the Key-Statistics table (24 rows), the Connections list (~24 attributed entries), the Positions-framed-against section (~20 entries), and the Citation and source-integrity notes. Each was checked against the converted markdown.

### Findings and fixes (applied to the deep ref before this log was written)

1. **Training-data leakage on "Nothing About Me Without Me" lineage.** The first draft of the section opened with "A framing principle drawn from health-care patient-engagement work" — a lineage claim the source does not make. The handbook's two worked examples are from health-care (gloves; MRSA rounding) but the source does not attribute the principle to that field, and the slogan's history elsewhere is training-data knowledge. **Action:** rewrote the opener as "A framing principle the handbook applies to positively-deviant solution-search" — describing what the handbook *does* with the principle, not where the principle came from. This is the canonical strip-case from fixture 01 applied to a lineage claim rather than a biographical one.

### Coverage notes

- **Complete coverage.** All 60 pages of the handbook were read. The Table of Contents (pp. 3-4) was cross-referenced against the body sections to confirm every catalogue entry was reached: 33 Liberating Structures entries listed in the TOC (Knee-to-Knee Conversation through Improv Games on pp. 14-48) plus the three Seeing-Complexity exercises (Complex Systems Game; Tic Tac Toe; A Place in the System on pp. 49-52) plus the five Random Thoughts framing-aids (Waving Hands; Talking Objects; Music & Poetry; Tingsha Bells; Take 20 Seconds on pp. 53-58). The deep ref treats the catalogue as "selected interaction designs" and groups them into seven thematic clusters (conversation-starting; surfacing-knowledge; working-with-experts; question-asking; decision-tools; group-storytelling; scenario-and-network) plus Levels of Accountability (own page) and Improv Games (own page); every named structure from the TOC is touched.

- **Editorial repair note for the converted markdown.** Two typographical artefacts are present in the source itself (not introduced by conversion): the Table of Contents lists "DISCOVERTY & ACTION DIALOGUES" (sic; the body header has the correct spelling "DISCOVERY & ACTION DIALOGUES") and "25-T0-10" (zero where O belongs; the body header has "25–TO-10"). The deep ref preserves the source's spelling in citations and notes the TOC artefacts in the Citation and source-integrity notes. The Diana Whitney quote in the source has an unusual whitespace pattern: "Questions are fateful ! " (space before the exclamation mark, trailing space). The deep ref renders this with standard typography ("Questions are fateful!") as a low-cost typographic normalisation analogous to fixture 05/06's smart-quote-tidy case — preserved here because the whitespace artefact is a conversion artefact, not a source choice. Flagged as a self-conscious editorial decision.

- **Image axis: text-only.** The handbook contains small illustrative line drawings, a stair-step diagram on the Levels of Accountability page (p. 41), a 2×2 matrix on the Participatory Scenarios page (p. 22), and an Agreement/Uncertainty Matrix diagram on p. 36. None carry conceptual content not also present in the text. Image classification was deferred to a separate `ingesting-images` invocation; the coverage line in the deep ref records this explicitly.

- **CC BY-NC-SA 3.0 Unported propagation.** The deep ref, light ref, and both distillations all carry the licence in their Source line. The .source.md sidecar's body documents the NC-SA propagation obligations (non-commercial use; copyleft to CC BY-NC-SA 3.0 or compatible). Build profiles that include these artefacts inherit both obligations.

### Evidence-class marker audit

Spot-checked sample of evidence-class markers in body prose:

- `[V]` markers: ~95 instances. Each was spot-checked against the converted source. Notable verbatim passages re-checked character-by-character:
  - Introduction's "frameworks that make it possible for people and organizations to create, to do new things, to be innovative…" — exact match.
  - Ownership-vs-Buy-in's "Buy-in is the exact opposite. Someone else, or some group of people, has done the development…" — exact match (including the awkward double-dash "-- so that").
  - Wise Crowds' "Here's what I heard that intrigued, surprised, or resonated with me" — exact match.
  - 25-to-10's "This is not recommended to make a decision. It's a way to get a sense of the wisdom of the crowd" — exact match.
  - Wicked Questions' "How can we sustain quality standards across the system while allowing for local innovation?" — exact match.
  - Take 20 Seconds' "On average, facilitators begin speaking after six seconds" — exact match.
  - 15% Solutions' "Most people have about 15-percent control over their work situations. The other 85 percent rests in the broader context…" — exact match.
  - de Bono's "We can distinguish between restricting structures and liberating structures. Tools are liberating structures. With the proper tools students will surprise themselves with ideas that they have not had before." — exact match.
  - Alexander's intimacy-gradient passage and the closing pattern-language synthesis — exact match.
  - Dr. Locust 1998 talking-stick passage ("The talking stick has been used for centuries…") — exact match.
- `[AP]` markers: ~25 instances on author paraphrases of structure summaries (e.g., Wise Crowds three phases; Troika Consulting rounds; DAD's six questions). All trace to the source's procedural descriptions of each named structure.
- `[AR]` markers: ~10 instances on the handbook's argument-structure claims (e.g., "the handbook's thesis is structural rather than motivational"; the framing of buy-in as a "danger signal"; the pattern-language framing of LS as combinations of primitives). All trace to specific passages.
- `[BT]` markers: ~24 instances. All on attributions the handbook itself makes — Peter Block; Plexus Institute / Positive Deviance; Altshuller; Stacey; Zimmerman; Gareth Morgan; Diana Whitney; Marilee Adams; Mulago Foundation; Larry Smith; Hemingway (anecdotal); Center for Creative Leadership; Tom Sparough; Open Space Technology; Conversation Café; World Café; Appreciative Inquiry; family-therapy Constellations; Dr. Locust; The Grove; Torbert 1991; de Bono 1991; Axelrod 2010; Alexander 1977; Johnson-Lenz. Each is verified to be a citation the *source* makes, not a connection the deep-ref author imports.
- `[AE]` markers: not used. The handbook is a catalogue of procedural patterns; the worked examples within each entry are integrated into the procedure description and are not lifted out as named author examples. (The Hemingway anecdote in Six Words and the Dr. Locust talking-stick passage are quoted but not used as "author examples" in the [AE] sense — they are borrowed-through illustrations.)

### Cross-corpus drift check

The deep reference does not connect the LS Handbook to any other source in this corpus. The Connections list reports only the lineages the handbook itself names. The distillations (decision-making and stakeholder-engagement) make integration suggestions in their "Integration with Other References" sections — pointing at Scrum Guide, LFUO 2024, TC 25-20, NHS Just Culture Guide, OpenStax OB / Ethics / Management / Marketing, Letaw, and Jones. Those are distillation-tier synthesis, not deep-ref-tier claims, and are appropriate at that tier (the protocol explicitly allows library-level synthesis in distillations).

### Task-application-smuggling check

The deep reference contains no task-application guidance: no diagnostic questions for facilitators, no anti-patterns, no worked-example projections onto decision-making or stakeholder-engagement tasks. The procedural shapes of each LS structure (Wise Crowds' three phases; Troika's 10-min rounds; DAD's six questions; What/So-What/Now-What's three-sequenced questions) are described as the source's procedural descriptions, not as operator runbooks. Diagnostic questions and phase-by-phase routing live in the distillations, which is the correct tier separation. Spot-checked: the deep ref does not contain "Ask…" / "When the facilitator…" / "If the team…" framings; those phrasings appear only in the distillations.

### Post-source-vocabulary check

The deep reference uses the source's own vocabulary (Liberating Structures; ownership vs buy-in; pattern language; rhythm/timing/boundaries/containers; jazz; intimacy gradient; positively deviant; the "central tendency" vs distributed intelligence; the half-life of engagement). It does not import concepts from the later Lipmanowicz/McCandless 2014 trade book *The Surprising Power of Liberating Structures* — terms specific to the 2014 work (e.g. "10 structures of leadership", "five design elements", "string a few together") are absent. The deep ref is faithful to the 2010 handbook's vocabulary.

### Verbatim accuracy re-check on the named blockquote and the load-bearing quotes

- Introduction thesis ("Liberating structures are frameworks that make it possible for people and organizations to create, to do new things, to be innovative…"): exact match including the comma-spaced list of antonyms ("oppressed, constrained, confined, or powerless").
- Ownership-vs-Buy-in passage ("Buy-in is the exact opposite. Someone else, or some group of people, has done the development, the thinking and the deciding…"): exact match. The unusual double-dash "-- so that" in the source is preserved.
- Wise Crowds' "Here's what I heard that intrigued, surprised, or resonated with me": exact match.
- 25-to-10's two-sentence scope caveat: exact match.
- Pattern Language closing synthesis ("As a pattern language for engagement, liberating structures give us multiple options for each of these primitives…"): exact match, rendered as the named blockquote in the deep ref.
- Tic Tac Toe framing ("We spend a lot of time in meetings doing the equivalent of playing 4 x 4 tic tac toe in the air…"): exact match including "4 x 4" with spaces around the x.
- Six Words criteria (Mulago Foundation): exact match including the dot-bullet rendering "Less than 8 words • Include a verb • Include a target population • Describes an outcome you can measure" (preserved as a comma-joined list in the deep ref to fit the prose flow; the bullet structure is a source-layout artefact, not a verbatim element).
- Diana Whitney "Questions are fateful !" — preserved as "Questions are fateful!" with whitespace normalised.
- Dr. Locust 1998 talking-stick passage: exact match across both sub-quotes ("The talking stick has been used for centuries by many Indian tribes…" and "Whoever holds the talking stick has within his hands the power of words…").

## Result

**Pass.** The deep reference ships. One claim-strip fix was applied in-place before this log was written (the "drawn from health-care patient-engagement work" lineage leak). All verbatim quotes match the converted source character-for-character (with one whitespace normalisation flagged in the editorial-repair note). The light reference and the two distillations derive from this audited deep reference; the source-only discipline propagates by construction.

The deep reference's coverage of the source is complete: the seven framing sections, all ~32 named LS interaction designs in the catalogue (with one selected to skip per the deep-ref's framing — Shift & Share and Portfolio Planning are summarised briefly rather than treated at length, which is a coverage decision not a coverage gap), the three Seeing-Complexity exercises, the five Random-Thoughts framing-aids, the Origins section, and the closing Pattern Language for Engagement essay are all represented. No silent partial coverage; no training-data leakage; no post-source vocabulary; no cross-corpus drift; no task-application guidance smuggled into the deep tier.

**Pass G applicability decisions (recorded here for ingestion-summary cross-check):**

- **`decision-making`**: clear yes. The handbook's load-bearing ownership-versus-buy-in distinction is a decision-process claim; the catalogue contains explicit collective-decision tools (25-to-10 explicitly flagged as *not* a decision tool; Wise Crowds and Troika as option-broadening structures upstream of an owned decision; DADs ending in "Who will do what when next?"; What/So-What/Now-What sequencing post-event decisions). Distillation produced at `distillations/decision-making/liberating-structures-handbook-decision-making.md`.
- **`stakeholder-engagement`**: clear yes (strong fire). The handbook's full title is *Engaging Everyone with Liberating Structures*; the introduction and closing essay frame engagement as the through-line. "Nothing About Me Without Me" and "Engage the Unusual Suspects" are explicit stakeholder-engagement principles. Distillation produced at `distillations/stakeholder-engagement/liberating-structures-handbook-stakeholder-engagement.md`.

**Pass G axes skipped:** none (only two task axes were considered per the ingestion brief; the third task axis `software-business` is configured in the build but not in-scope for this run).

**Files produced this run:**

- `corpus.commons/demo/sources/original/liberating-structures-handbook.source.md` — frontmatter sidecar.
- `corpus.commons/demo/sources/original/liberating-structures-handbook.pdf` — original PDF (~2.8MB, CC BY-NC-SA 3.0 Unported, redistributable with non-commercial obligation propagation).
- `corpus.commons/demo/sources/converted/liberating-structures-handbook.md` — converted markdown (2,767 lines).
- `corpus.commons/demo/references/liberating-structures-handbook-deep.md` — audited deep reference.
- `corpus.commons/demo/references/liberating-structures-handbook.md` — light reference (derived from audited deep).
- `corpus.commons/demo/distillations/decision-making/liberating-structures-handbook-decision-making.md` — decision-making distillation (Pass G applicability: clear yes).
- `corpus.commons/demo/distillations/stakeholder-engagement/liberating-structures-handbook-stakeholder-engagement.md` — stakeholder-engagement distillation (Pass G applicability: clear yes — strong fire).
- `corpus.commons/demo/references/_ingest_reference_index_liberating-structures-handbook.md` — REFERENCE-INDEX staging file (parallel-batch pattern; pending consolidator merge).
- `corpus.commons/demo/distillations/_ingest_decision-making_liberating-structures-handbook.md` — decision-making distillation-index staging file (pending consolidator merge).
- `corpus.commons/demo/distillations/_ingest_stakeholder-engagement_liberating-structures-handbook.md` — stakeholder-engagement distillation-index staging file (pending consolidator merge).
- `corpus.commons/demo/references/_audit/_ingest_pass_I_liberating-structures-handbook_source_audit.md` — this log.

**SHA-256 of input PDF:** `df336e2f346ffea3377078798c0f684f755daa75c846c1f8a8476b7274928364`

**Input source removed from `sources/ingest/`:** confirmed (moved to `sources/original/`).
