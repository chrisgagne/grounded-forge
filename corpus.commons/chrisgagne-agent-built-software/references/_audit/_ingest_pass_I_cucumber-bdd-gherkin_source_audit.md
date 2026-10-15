# Pass I source audit: cucumber-bdd-gherkin

- **Deep reference:** `references/cucumber-bdd-gherkin-deep.md` (364 lines before audit, 364 after)
- **Tape:** `sources/converted/cucumber-bdd-gherkin.md` (1,210 lines; sha256 `4f43ba2c…7fee`, matches the source card and the acquisition manifest)
- **Original:** not available; audited against the tape only. No page renders used (the tape is Markdown with no pages; the one figure is carried as alt text and caption, which the deep ref cites as such).
- **Auditor:** claude-opus-5-5, fresh subagent, fix-in-place leg. Date 2026-10-15. A blind cross-family leg (codex) runs in parallel on a frozen copy.
- **Coverage read:** deep reference 364/364 lines; tape 1,210/1,210 lines. Source card and acquisition manifest (`_planning/staging/chrisgagne-agent-built-software/acquisition/cucumber-bdd-gherkin.json`) read to check the header and conversion-path claims.

## Gates

- **Verbatim check** (`scripts/check-verbatim.py`): no findings before the audit; no findings after.
- **TOC vs anchors:** all 12 pages in the tape are anchored in the body (Part I: 8 BDD pages; Part II: 4 Gherkin pages, including the two near-empty MDX pages). The `coverage: partial — operator-approved 2026-10-14` line matches the source card and the manifest; the subset is operator-approved and every page of it is covered. Pass.
- **Conversion-path claims** (line 358): front matter dropped from ten pages, MDX imports from two, nothing from `docs/bdd/index.md` — confirmed against the manifest's per-file `dropped` lists. Tape sha256 confirmed by `shasum`.

## Counts

| | |
|---|---|
| Claims audited | ≈310 (280 marked claims: 83 [V], 144 [AP], 8 [AR], 26 [AE], 19 [BT]; plus ≈30 unmarked: header and structure lines, card-colour bullets, stats table rows, 8 "frames against" positions, 8 source-integrity notes) |
| Source-anchored | all, after the two fixes below |
| Stripped | 0 |
| Corrected (over-extension) | 1 |
| Citation corrected | 1 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 |

## Changes

1. **Line 232 (Part II, "Rule")** — over-extension. Was: the "Highlander" rules "There can be only One" and "There can be Two (in some cases)", "each with examples about ninjas". The tape (reference.md lines 586–607) gives the first rule two ninja examples; the second rule has one example, "Two -- Dead and Reborn as Phoenix", whose steps are elided with `...` and mention no ninjas. Now says so.
2. **Line 38 (thesis, fourth recurring point)** — citation. "Implementation details kept in step definitions" is stated in the Gherkin reference's `When` admonition ("Implementation details should be hidden in the step definitions", reference.md line 687), not under `Then`. Added `"When"` to the citation.

## Considered and kept

- **"quoted approvingly"** (lines 330, 335: Brooks as the Discovery epigraph; Keogh as the answer to the first myth). The pages use both quotations as their own framing and argue in line with them (index.md lines 54–58; myths.md lines 406–412). Kept as a description of how the page uses the quotation; flag to the cross-family leg if it reads it as an evaluative label.
- **"described neutrally"** (line 333, OOPSI and Feature Mapping). The two descriptions (discovery-workshop.md lines 251–257) are factual, with no evaluation. Kept.
- **Line 346, "formulation before automation"**. myths.md line 412 says examples can't be automated before the most important ones are found or the stakeholder has given feedback on their wording; with Keogh's ordering (line 408) this supports the claim. Kept.
- **Line 289, "a Norwegian scenario, 'Gjett et ord'"**. "Gjett et ord" is the `Funksjonalitet` (feature) name, but the page itself introduces the block as "a Gherkin scenario written in Norwegian" (reference.md line 991). Kept.
- **Line 5 licence and attribution** (MIT, "Copyright 2014 Aslak Hellesøy and contributors", "associated documentation files"). Not in the tape; sourced from the source card and manifest licence evidence, which is the right home for provenance metadata. Kept.
- **History bullets marked [BT]** (lines 193–194, 324). Consistent with the scheme stated at line 362 ([BT] where the page credits a named person or work, [AP] for its own narration). Kept.

## Derived tier

No light reference and no distillations exist for this slug (`references/` holds only the deep; no `distillations/*/cucumber-bdd-gherkin-*.md`). Nothing to re-derive. If they are derived later, they take the audited deep; the two changed claims are the "Highlander" example description (line 232) and the thesis citation (line 38), neither of which a light ref would be likely to carry.

## Open

- Not stamped, per dispatch: the driver stamps after the cross-family leg. The "Pass I: audit pending." line (364) is left as is.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `867cbaea5e8f8f6a2c026cef887c911c08ffc0fa4a50791ff5699bd04d394816`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `47efac84c95a3074de3be1f413b2937f25a342b11c9ac9b27c48465e1f9e9dd0`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_cucumber-bdd-gherkin_crossfamily_blind.md`, `_ingest_pass_I_cucumber-bdd-gherkin_crossfamily_sort.md`, `_ingest_pass_I_cucumber-bdd-gherkin_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 5 deep-reference defects (2 fixed by the fix-in-place audit, 3 missed by it and caught by the blind audit), found 0 over-flagged by either auditor and 1 disputed (blind, the <Term> placeholder count), with 1 confirmed defect outside the deep (source-card publish_year) and a gate verdict of pass once the three remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 2, the blind audit 3, both 0. The Chapman estimate is 11 in all, about 6 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of 3 remaining edits, 2 were applied as written (line 23 'five sentences', tape 1203–1208; line 108 restores 'the details of', tape 155) and 1 with changed wording (line 289 says 'with two examples' in place of 'containing the scenarios', matching the tape's Eksempel keyword at 997 and 1001), none declined; the disputed placeholder line 359 was settled against tape 1025/1032/1034/1081/1195 by rewording to 'five <Term> placeholders ... naming four terms (file-extension, twice; ...)'.

**Gate:** accepted by operator. Deep reference sha256 `625c51e72121c5e1ea4065c6b189298dcdc47658f6a096ac62535d0b9a297df1`, stamp included.
