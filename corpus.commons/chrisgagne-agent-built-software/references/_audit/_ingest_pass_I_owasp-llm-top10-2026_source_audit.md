# Pass I source audit: owasp-llm-top10-2026

- **Deep reference:** `references/owasp-llm-top10-2026-deep.md` (452 lines incl. trailing blank; 451 content lines)
- **Source:** `sources/converted/owasp-llm-top10-2026.md` (5,118 lines, `pdftotext -layout`, poppler 26.08.0), born-digital text layer
- **Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode, 2026-10-15
- **Leg:** same-family leg. A blind cross-family leg (codex) runs in parallel on a frozen copy; this reference stays audited-but-unverified until that leg is sorted. The driver stamps.

## Coverage

- Deep reference read in full: lines 1–452.
- Source read in full: lines 1–5118 (cover through the Page 122 footer), every page.
- Calibration exemplars read first: fixtures 01, 07, 12.
- Page renders used: 0. Born-digital text layer; no scanned pages, so the tesseract check under Pass E does not apply. Figures and Appendix B images stay out of scope (text-only, as the reference declares).

## Verbatim check

`python3 scripts/check-verbatim.py` before and after the edits: no findings (70 `[V]` quotations, all match the tape).

## Counts

| Measure | Count |
|---|---|
| Claims audited | ~460: 295 evidence markers (70 [V], 71 [AP], 53 [AR], 24 [AE], 77 [BT]), 446 page citations, the 10 coverage-matrix rows and 90 framework-element mappings, 20 key-statistics rows, 11 connections, 16 framed-against positions, frontmatter and source-integrity notes |
| Source-anchored | all but the two below |
| Stripped | 0 |
| Marker-corrected | 1 |
| Paraphrase corrected | 1 |
| Quotation-corrected | 0 |

## Changes

1. **Line 409 (Connections), marker mismatch.** The regulatory-regimes bullet carried `[BT]`. The document names the EU AI Act, GDPR, HIPAA, CCPA/CPRA and ISO/IEC 42001 as applicable regimes (p. 19; Articles at pp. 18, 21, 51, 53); it does not cite them as sources for any claim, which is what `[BT]` asserts. Removed the marker and reworded the lead-in to "named as applicable, not cited as sources for claims".
2. **Line 209 (LLM05 description), garbled paraphrase.** "stored vectors steering retrieved content toward steered answers" turned the source's poisoning-of-vectors into vectors doing the steering, and was circular. Rewritten to the source's sense (p. 33, tape l. 1150–1151): poisoning targets stored vectors to influence retrieved content, resulting in steered answers or subtle misinformation.

## Checked and left as they are

- Every page citation traced to its page in the tape, including all page ranges in the Appendix A element mappings (pp. 59–104) and the reference-list spans (pp. 108–119).
- Coverage matrix: all 90 cells match pp. 58–59.
- Element mappings by risk: every primary/supporting split for all nine frameworks matches the appendix tables.
- "References named" lists: each matches the entry body's in-text citations and the entry's reference list; the "adds" items are exactly the list entries not cited in-text. LLM04's claim that every list item is cited in the entry holds.
- Structure line: 107 supporters (26 rows of 4 plus 3) and the entry leads match p. 122 and p. 120.
- Conversion facts: sha256 `ef87993a…6108e`, PDF author/creator/dates, 122 pages, 5,118 lines, 30,959 words (≈254 a page), 122 form feeds, page-start line anchors: all verified.
- "Positions the author explicitly frames against": each of the 16 rests on explicit source wording ("Stop trying…", "rather than a second LLM call", "is not a root control", "not a safe-harbor classification", "Not Just Confidence", etc.); none is an invented opposition.
- Appendix-only incidents (line 444): verified that the LLM01, LLM03 and LLM05 entry bodies do not describe them.
- "cited approvingly" (Willison, line 403): the entry adopts the trifecta as its own pre-deployment check (p. 13); the template asks for the citing stance, so left.

## Left open

- **Line 449, "Pass I: see the stamp on line 2 and the audit log."** Line 2 is blank; no stamp exists yet. Left untouched on instruction (the driver stamps once every leg is done). If the driver's stamp does not land on line 2, this line needs updating.
- Cross-family leg pending; sort its findings against this log before stamping.

## Derived tier

- Light reference `references/owasp-llm-top10-2026.md` exists; not edited. Neither change alters a claim it carries: its connections line 105 already lists the regimes "as applicable regimes" with no marker, and it does not carry the LLM05 vectorization-stage wording. Re-derivation is still due under the protocol (stamp with the audited deep's hash) once the driver stamps.
- No distillations exist for this slug.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `ca1435ffa6adabca34b1124fdcd178cd202749c68a298e40c50defb2caaf285f`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `10fddc5dae62761caf8e77cf8a0ebe1b50e2c7a543d92db9e9d69c4d56d16566`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_owasp-llm-top10-2026_crossfamily_blind.md`, `_ingest_pass_I_owasp-llm-top10-2026_crossfamily_sort.md`, `_ingest_pass_I_owasp-llm-top10-2026_crossfamily_prompts.md`.

**Sort result:** The sort counted 1 confirmed original defect (0 confirmed and fixed, 1 with the fix incomplete), 0 missed by the fix-in-place audit, 0 over-flagged by the fixer and 0 by the blind audit, 2 disputed, and 1 defect introduced by the fixer counted separately, with the gate verdict pass once its two remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 1, the blind audit 1, both 1. The Chapman estimate is 1 in all, about 0 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of the 2 remaining edits, 1 was applied as written (line 409 loses the fixer's categorical 'not cited as sources for claims', since tape ll. 573-574, 705, 713 and 1918 tie erasure and notification obligations to GDPR Articles 17 and 33, CCPA §1798.105 and EU AI Act Article 73, while p. 19, l. 582, names them as applicable regimes), 0 with changed wording, and 1 declined: stripping line 449, because 'Pass I: see the stamp on line 2 and the audit log.' is the driver's own pointer text (run.py finalize) and becomes accurate when finalize inserts the stamp at line 2; both disputed findings were settled against the source, keeping the line 209 vectorization wording (it follows tape ll. 1150-1151) and leaving the regulatory bullet unmarked, since [BT] means the author cites someone else for a claim and the document asserts these obligations itself.

**Gate:** pass. Deep reference sha256 `fd056f852e7cf1c8941846686393fd64ddc478f5f1e46235a9b9d5b7d898c5d0`, stamp included.

## Derived-tier fidelity check (2026-10-15)

Fidelity check of the derived tier of `owasp-llm-top10-2026` (OWASP Top 10 for LLM Applications 2026) against its stamped deep reference, with the tape opened at eleven passages. The light reference had 96 claims checked and 11 fixed in place: one misattribution (a What's New phrase credited to the project leads), four scope widenings or narrowings (graduated enforcement, "a defining characteristic", "production network segment", the user's own LLM), two dropped hedges or limits (prompt input "can" control output; the second limit of human confirmation), and four restatements of a mechanism or definition (the build-pipeline scenario, Misinformation's system-level-failure causation and "influence", Hidden Context Exposure's "unauthorized" and security-relevance condition, and what carries no instructions in LLM09). No distillation or distillation-index row exists for this source. Cross-reference rows about it in five other distillations claim nothing the deep reference lacks. No deep-reference defect was found, and `check-verbatim.py` reports no findings on the edited file.
