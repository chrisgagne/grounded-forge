# Pass I source audit: uk-duck-book-qa-of-code

- **Deep reference:** `corpus.commons/chrisgagne-agent-built-software/references/uk-duck-book-qa-of-code-deep.md` (508 lines)
- **Source (tape):** `corpus.commons/chrisgagne-agent-built-software/sources/converted/uk-duck-book-qa-of-code.md` (6,656 lines; sha256 `7126cd89…b0708`)
- **Original:** not available; audited against the tape only. No page renders used (web book, no PDF).
- **Auditor:** fresh same-family subagent (claude-opus-5-5), fix-in-place mode. Cross-family leg (codex) runs blind and in parallel on a frozen copy; this log was written without seeing it.
- **Date:** 2026-10-15

## Coverage

- Deep reference read in full: lines 1–508 of 508.
- Tape read in full: lines 1–6,656 of 6,656, all 19 `<!-- file: -->` sections.
- TOC-vs-anchors check: pass. All 19 files in the structure block (intro plus 18 chapters) are cited in the body. No `coverage:` field, and none needed.
- Tape provenance claims in the citation notes checked: sha256, 6,656 lines, 49,425 words and 19 file markers all match the tape.

## Counts

| Item | Count |
|---|---|
| Claims audited | 477 marker-tagged claims (245 [V], 161 [AP], 4 [AR], 28 [AE], 39 [BT]) plus the untagged items: the structure and figure blocks, 17 key-statistics rows, 11 connections, 11 positions, 8 integrity notes |
| Source-anchored without change | all but the 7 below |
| Stripped | 0 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 (`check-verbatim.py`: no findings before or after; 14 figure claims not checked by the script, traced by hand against the figure directives) |
| Claims corrected (wording) | 7 |

## Changes (line numbers as of the edited file)

1. **L279, Configuration.** The deep said YAML, TOML, JSON and XML "are 'compact and human-readable'". The source says this of "formats like YAML and TOML" only (configuration.md, "Use dedicated configuration files"). Over-extension: narrowed to YAML and TOML.
2. **L286, Data management / Spreadsheets.** "the European Spreadsheet Risks Interest Group's horror stories" took "horror stories" from the link URL, not the text. Rewritten in the source's words: its document on "spreadsheet related errors and their consequences".
3. **L317, Peer review case study.** "detailed bespoke comments" were "most informative": the source says "Perhaps the most informative part". Hedge restored.
4. **L363, Commit small changes often.** "treat an unfinished task at day's end as a sign it was not broken down enough": the source says "you should consider if the task has been sufficiently broken down". Hardened advice, softened back to the source's "consider".
5. **L401, Centaurs example.** "leaving the user a reverse-centaur": the source says "you may find yourself turning into a reverse-centaur". Hedge restored ("may turn into").
6. **L477, Connections.** "YAGNI, DRY": the abbreviations are not in the tape, which spells out "You ain't gonna need it" and "Don't repeat yourself". Vocabulary the source does not use; replaced with the source's phrases.
7. **L497, Positions framed against.** vague prompting "turns the user into a reverse-centaur": the same hedge as change 5. Changed to "can turn".

## Checked and left as is (calibration notes)

- The [V] markers in the key-statistics table sit on stated figures, not quotations. The template allows this, so they stay.
- L102 carries an embedded verbatim quotation ("doesn't bear on decisions at that level") under an [AP] marker. The quote is exact and the sentence is mostly paraphrase, so this is not a defect.
- L473 glosses the Aqua book as "guidance on producing quality analysis for government". The wording comes from the link slug, which is in the tape. Left as is.
- L106 and L488 say "time-consuming, frustrating and error-prone"; the source says "can be frustrating". A small loss of hedge inside a list; left as is.
- Every epigraph attribution (van Rossum, Knuth, Zen of Python, Conway, Macphereson, the Aqua book) and every [BT] in the generative AI chapter (arXiv, SSRN, METR, Anthropic, nature.com, Databricks, Time, FT, Guardian/Doctorow, Wolfram, Google MLCC) traces to a named link or credit in the tape.
- No task-application guidance, no outside cross-references and no evaluative framing were found beyond the items above. The "Positions" section is grounded: each entry carries a source passage that does the framing.

## Open items for the parent

- **No acquisition manifest or sidecar in the repo.** `sources/original/uk-duck-book-qa-of-code.source.md` does not exist (the converted file has a copy in `sources/ingest/`, same hash). The Source line's commit hash `fa39f208…` (2026-06-09) and the citation notes' "per the acquisition manifest", "matches the manifest" and "`gradient_descent.png` … absent from the manifest's image list" cannot be checked against anything in the repo. The tape itself checks out. I left these acquisition-metadata claims in place; they need the manifest or a sidecar to back them.
- The L508 "Pass I has not run" integrity line and the stamp are unchanged, as instructed. The driver stamps once both legs are in.

## Derived tier

- No light reference exists for this slug. No distillation file `*uk-duck-book*` exists.
- `tasks/warranting-agent-built-software.md` cites `uk-duck-book-qa-of-code` at L59, L66, L69, L85 and L98: proportional assurance, tests before logic, run all tests on every change, repeatable and reproducible tests, and managers needn't read the code to trust it. **None of the seven changes touches those claims**, so they still hold against the audited deep. The changed claims (YAML/TOML, the EuSpRIG wording, the rOpenSci hedge, the CI cadence hedge, the reverse-centaur hedges, the YAGNI/DRY spelling) could reach any light reference or distillation derived later, so re-derive from this audited deep.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `f5c68e6aefdf1d90ea08f354d8d284534c9e881119c7dc045680b290cbaff9d3`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `0008d32fc61c12c7c44aaee76a86d6259825452357c33cf8aaaccac5e8a2cc61`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_uk-duck-book-qa-of-code_crossfamily_blind.md`, `_ingest_pass_I_uk-duck-book-qa-of-code_crossfamily_sort.md`, `_ingest_pass_I_uk-duck-book-qa-of-code_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 18 defects (5 fixed by the fixer, 5 raised but left unfixed, 8 missed by the fixer), found 1 over-flagged by the fixer and 0 by the blind auditor, left 3 disputed, and gave a pass verdict once its 13 remaining edits were applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 10, the blind audit 12, both 4. The Chapman estimate is 27.6 in all, about 9.6 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Five remaining edits were applied as written (6 accessibility, 7 and 11 frustration hedge, 8 data-breach condition, 9 DBMS 'usually'), one with changed wording (10, which keeps the Anthropic finding as a verbatim [V] [BT] quote and splits the rest into [AR], [BT] and [AP]), and seven were declined (1-5, 12, 13) because the acquisition manifest the sort leg never saw, _planning/staging/chrisgagne-agent-built-software/acquisition/uk-duck-book-qa-of-code.json, records the commit fa39f208 and date 2026-06-09, the book/_toc.yml order, byte-for-byte concatenation with front matter and MDX imports dropped, the three remote images as 'remote, not copied', an image list without gradient_descent.png, and the tape sha256 7126cd89...b0708.

**Gate:** accepted by operator. Deep reference sha256 `969ae3f988094a8a159fa61993c78768c73e9b11e3b277da7e2d8c41dc26fef5`, stamp included.
