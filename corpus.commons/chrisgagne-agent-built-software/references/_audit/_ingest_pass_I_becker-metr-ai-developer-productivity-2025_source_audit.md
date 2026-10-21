# Pass I source audit: becker-metr-ai-developer-productivity-2025

- **Date:** 2026-10-15
- **Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode (same-family leg; a blind codex leg runs separately on a frozen copy)
- **Deep reference:** `references/becker-metr-ai-developer-productivity-2025-deep.md` (251 lines, read in full)
- **Source:** `sources/converted/becker-metr-ai-developer-productivity-2025.md` (2,951 lines, read in full, `{page-1}` to the p. 51 folio)
- **Calibration:** protocol Pass I and failure-mode reference read; fixtures 01, 07 and 12 read before the cold read.
- **Verbatim check:** `scripts/check-verbatim.py` before and after the edits: no findings, 0 figure claims not checked.
- **Page renders:** 1 of 10 (p. 2, Figure 1, 110 dpi).

## Counts

| Measure | Count |
|---|---|
| Claims audited (counted by sentence; table rows and list items once) | ~245 |
| Source-anchored as written | ~243 |
| Stripped | 0 |
| Marker-corrected (attribution) | 1 |
| Table cell corrected | 1 |
| Quotation-corrected | 0 |

## Changes

1. **Line 90 (C.1.2, familiarity).** The `[V]` quotation "Sometimes, portions of one’s own codebase can be as unknown as a new API." followed "Developers say …" with a semicolon, so it read as a developer quotation. In the source (p. 19, tape l. 1068) it is the authors' own sentence between developer quotations. Split the sentence: the developer paraphrase now carries `(App. C.1.2, p. 19) [AE]`, and the quotation is introduced with "The authors add:". Wording and marker of the quote unchanged.
2. **Line 202 (Key statistics).** Row label "AI use in AI-allowed recordings" also held the AI-disallowed cheating count. Relabelled "AI use in labelled recordings" and stated both denominators as the source does (16.4% of 44 AI-allowed; AI used in 3 of 54 AI-disallowed, about 6%; App. C.3.2, p. 26, tape ll. 1408–1413).

## Verified, no change

- **Figure 1 values** (lines 70, 184–186): render of p. 2 confirms the observed interval runs from just below the 0% line (≈ +1%) to ≈ +39%, the developer-forecast whiskers ≈ −14% to −32%, and the post-study-estimate whiskers ≈ −10% to −31%. The caption gives no interval level, as the deep says.
- **Table 3 reading** (line 35): column-by-column linearisation re-assembled; "Our study" is the only row with ✓ in all four columns, consistent with the App. B text (p. 17).
- **Provenance notes** (lines 235–247): sha256 `3e18d9e0…ab25c` matches; pdfinfo gives 51 pages, letter, creator "arXiv GenPDF (tex2pdf:)", author metadata "Elizabeth Barnes"; tape is 2,951 lines / 22,918 words with 51 `{page-N}` markers; the five listed typos, the glued footnote numbers and dropped hyphens, Table 4's printed difference of 9, the 51 vs n = 50 respondent counts and the 74 / 44 / 54 recording counts are all in the tape as described. The licence string matches the source card (`licence: "CC BY 4.0"`, from the arXiv abstract page).
- **Connections and positions** (lines 205–227): every cited work is cited in the paper at the location given; every "frames against" entry is an explicit statement in the source (§1, §1.1, §4, App. B Table 2, App. G.1, App. G.2.1). No invented oppositions.
- **Structure and coverage**: every section and appendix in the paper (§1–§5, App. A–G and their subsections) has anchors in the body. No TOC gap.
- No training-data leakage, post-source vocabulary, task-application guidance, evaluative labels or methodological verdicts found. Statements of the paper's own hedges ("speculative, suggestive", "unclear", "cannot fully rule out") are the authors'.

## Left open

- Footnote 5 (p. 5) says the block-randomization sensitivity result is in "Section C.3.4"; it is in App. E.3 (p. 33). The deep cites E.3 correctly and does not repeat the source's cross-reference; not a deep-ref defect, noted for the record.
- Line 251 says "Pass I: see the stamp on line 2"; per dispatch, the driver stamps after every leg. Not edited.

## Derived tier

- Light reference `references/becker-metr-ai-developer-productivity-2025.md` exists. Neither change alters a claim it carries (it does not quote the C.1.2 sentence and does not carry the C.3.2 row). No re-derivation needed for these edits; the driver re-stamps provenance after all legs.
- No distillations for this slug were found under `distillations/`.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `edcceb39ce74977a062d7f20133cd6be88303b39e8257d2e6729f8505dcced22`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `f4ac36635a29a562f3028e66a54aca6cf78befb705bfbbd2e88213ba712c562c`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_becker-metr-ai-developer-productivity-2025_crossfamily_blind.md`, `_ingest_pass_I_becker-metr-ai-developer-productivity-2025_crossfamily_sort.md`, `_ingest_pass_I_becker-metr-ai-developer-productivity-2025_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 4 deep-reference defects (2 correctly fixed by the fix-in-place audit, 2 blind findings left unfixed: 1 overlooked, 1 deferred), 0 over-flagged by the fixer, 0 over-flagged by the blind audit, 0 disputed, and gave a pass verdict once the two remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 3, the blind audit 2, both 1. The Chapman estimate is 5 in all, about 1 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of 2 remaining edits, 0 applied as written, 1 applied with changed wording (line 207: the training-data qualifier restored from tape 106-109, adding 'of most software development work' to match the source's unrepresentativeness claim) and 1 declined (line 251: the 'see the stamp on line 2' sentence is the driver's own text, and the driver inserts the Pass I stamp as line 2 at stamping, scripts/pass_i/run.py:356-357, so the cross-reference becomes true then).

**Gate:** pass. Deep reference sha256 `9f0b5b37ed34af49a9fe17fe2802f0f9f961fd45389210cd8f1feab5765c5e8d`, stamp included.

## Derived-tier fidelity check (2026-10-15)

The fidelity check of the derived tier for `becker-metr-ai-developer-productivity-2025` (Becker, Rush, Barnes and Rein, METR, arXiv:2507.09089v2, scope `open`) read the audited deep reference in full and checked the light reference in full against it, opening the tape for the Abstract, §2.1 and App. B Tables 2 and 3. The source has no distillation and no distillation-index row yet. Of 57 claims in the light reference, 3 were fixed: a widened scope (the Table 3 comparison criterion given as "frontier models" where the table says AI at or above GPT-4), a dropped hedge ("broadly" on the repositories' quality bars), and a narrowed scope (Table 2's "many or most developers" given as "most"). The two rows in other sources' distillations that name this slug make no claim about it beyond what the deep reference carries. No defect was found in the deep reference.
