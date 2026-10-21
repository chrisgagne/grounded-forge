# Pass I source audit: owasp-agentic-top10-2026

- **Deep reference:** `references/owasp-agentic-top10-2026-deep.md` (526 lines)
- **Source:** `sources/converted/owasp-agentic-top10-2026.md` (2,172 lines; `pdftotext -layout`, poppler 26.08.0), original `sources/original/owasp-agentic-top10-2026.pdf`
- **Date:** 2026-10-15
- **Auditor:** claude-opus-5-5, same-family leg, fix-in-place mode. A blind cross-family leg (codex) runs separately on a frozen copy; this log does not read or anticipate it.
- **Stamp:** not set here. The driver stamps once every leg is done.

## Coverage

- Deep reference read in full: lines 1–526 of 526.
- Tape read in full: lines 1–2172 of 2172 (cover through the p. 56 footer).
- Page renders (110 dpi, 3 of the 10 allowed): PDF p. 9 (printed p. 8, At A Glance diagram), PDF p. 14 (printed p. 13, garbled ASI02 scenario 4 title), PDF p. 56 (printed p. 55, Sponsors page with no text layer). All three succeeded.
- Calibration exemplars read first: fixtures 01, 07, 12.
- Not a scanned source (born-digital text layer), so no tesseract check was needed.

## Verbatim check

`python3 scripts/check-verbatim.py` before the read: no findings. Re-run after the edits: no findings.

## Mechanical checks

- `pdfinfo`: 57 pages, letter, title field "Microsoft Word - OWASP Top 10 for Agentic Applications 2026 12.6.docx", created Wed Dec 10 13:11:24 2025 NZDT. Matches the Source line and the integrity notes.
- sha256 `a2db94cd…6fcb5c` matches the integrity notes and the source card.
- Tape: 2,172 lines, 13,820 words, 57 form feeds; a double form feed at line 2132 (p. 55 has no text layer). Matches the notes.
- Page anchors in the integrity notes (p. 1 at line 11 through p. 56 at 2132): all 20 checked, all correct.
- Project Supporters count: 107 cells on p. 56. Matches.
- Items-per-entry tally (examples / scenarios / mitigations / references) for all ten entries: checked, all correct.
- Exploits & Incidents Table: 25 rows (7 Oct, 4 Sep, 5 Jul, 3 Jun, 2 May, 1 Apr, 2 Mar, 1 Feb). Matches; every row's date, mapping, links and page checked.
- Appendix A and Appendix C tables: every cell checked against the tape. All correct.
- Resource-page title and date, and the fetch URL: on the source card (`sources/original/owasp-agentic-top10-2026.source.md`), labelled as not in the document. Correct.
- Image-scope claim in the Coverage line: `_planning/image-ingestion-log.md` line 28 records the 2026-10-11 classification. Correct.

## Render checks

- p. 8 diagram: the badge positions in Part I (ASI01/03/09 between the Inputs and processing panels; ASI10 on the red-dashed agent; ASI07 on the dashed arrow between agents; ASI06 on Connected data/RAG; ASI02 on Tools; ASI04/05/08 under a bracket spanning all three panels) all match the render.
- p. 13: title reads "Internal Query → External Exfiltration". Matches.
- p. 55: sponsor statement matches the paraphrase; 5 gold logos (HiddenLayer, Mend.io, Snyk, Palo Alto Networks, Trend Micro) and 20 silver (4 rows of 5); "Sponsors list, as of publication date." Matches. Nothing from this page carries `[V]`, which is correct.

## Counts

| | Count |
|---|---|
| Claims audited | ~520 (prose sentences, list items, table rows and cells, markers, front-matter lines, integrity notes) |
| Source-anchored as written | all but 2 |
| Stripped | 0 |
| Marker-corrected | 2 |
| Quotation-corrected | 0 |
| Corrected for accuracy or completeness | 2 (the same two lines) |

## Changes

1. **Line 19 (thesis, last sentence). Misattributed subject; marker corrected `[AR]` → `[AP]`.** It read "Appendix D's tracker, run by the ASI Exploits and Incidents initiative, 'seeks to inform and establish' the Top 10". The source (p. 44, tape line 1683) makes the *initiative* the subject that "seeks to inform and establish". It does not say the initiative "runs" the tracker. Rewritten: "In Appendix D, the ASI Exploits and Incidents initiative 'seeks to inform and establish' [V] the Top 10 by referencing real-world incidents and exploits (p. 44) [AP]." The sentence reports a statement of purpose, not an argument, so `[AP]` fits.
2. **Line 462 (Appendix D, scenario/tracker overlap). Marker relabelled and completed.** The paragraph was marked plain `[AP]`, which presents it as the author's point. The source never draws this cross-reference: the comparison is the ingester's. Relabelled "[AP] ingester's comparison", matching how the Key statistics table labels the ingester's tallies, and reworded the opening to "Comparing the entries' scenarios with the tracker rows, …". It also left out ASI07 scenario 5, "Agent-in-the-Middle via MCP descriptor poisoning" (p. 28, tape line 1054), which shares the Agent-in-the-Middle name. Added it, and added p. 28 to the page list. The count of seven names stands.

## Considered and left as they are

- *Positions the author explicitly frames against* (lines 503–510). Checked against the invented-opposition pattern. Each item rests on an explicit contrast or prohibition in the source: "avoid unnecessary autonomy" (p. 7), "not contribute to an overload" (p. 6), "make perimeter-based security models ineffective" (p. 27), "rather than relying on ad-hoc conventions" / "rather than relying on syntax alone" (pp. 13–14), "(not model-generated rationales)" (p. 35), "rather than attempting full semantic alignment" (p. 29), "Ban eval" / "Never run as root" / "Prevent direct agent-to-production systems" (p. 22), "no open registration" (p. 20), "Keys must never be directly available to agents" (p. 38). Kept.
- Heading "Mappings and the human-speed gap" (line 287). This is a label the ingester coined. The paragraph under it quotes the source's own wording ("a potential discrepancy in the speed and scale of fault propagation … and the ability of humans to keep up with them"). The heading is not a claim, so it stays; it is flagged here in case Pass H picks "human-speed gap" up as a source term.
- `[BT]` on Appendix B's CycloneDX description (line 409) and on T8's "fundamental defense" (line 287). Both report what the document says about another OWASP project. Defensible either way, so kept.
- ASI01 description (line 49) drops "(when used)" after "panning". The paraphrase stays faithful, so kept.

## Derived tier

- **Light reference** `references/owasp-agentic-top10-2026.md`, line 13: "its incident tracker seeks to inform and establish the Top 10". This carries the same misattribution as deep line 19 (the source's subject is the ASI Exploits and Incidents initiative). Re-derive.
- Light reference line 61: "Several tracker rows share names with entry scenarios, …". This is the ingester's comparison stated in the source's voice; on re-derivation, label it as a comparison or drop it. It names five of the seven and is otherwise accurate.
- **Distillations:** none found for this slug under `distillations/`. A Pass G staging file exists at `_planning/staging/aarbuddy/warranting-index-staging-2026-10-11/_ingest_warranting-agent-built-software_owasp-agentic-top10-2026.md`; it carries neither changed claim.
- Neither derived artefact was edited. Re-derive and stamp after the driver stamps the deep reference.

## Open

- None from this leg. The cross-family leg's findings are still to be sorted against this log.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `dcd8c22e1656ddda3ad4397a5def375a239249f339f66675d570bb0772b80138`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `e37c9c5d0f08e8480f0203e59b6ff819f154c39feed56564cd008dfee473235c`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_owasp-agentic-top10-2026_crossfamily_blind.md`, `_ingest_pass_I_owasp-agentic-top10-2026_crossfamily_sort.md`, `_ingest_pass_I_owasp-agentic-top10-2026_crossfamily_prompts.md`.

**Sort result:** The sort found 5 confirmed defects (4 in the deep reference, 1 in the light reference), 3 missed by the fix-in-place audit, 3 over-flagged by the fixer and 0 by the blind auditor, 1 disputed (the line 19 marker, left at [AP]) and 0 new defects from fixer edits, with a gate of pass once its three remaining edits were applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 1, the blind audit 3, both 0. The Chapman estimate is 7 in all, about 3 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Two remaining edits were applied as written (line 49 restores 'when used' per tape line 309; line 29 moves Connected data/RAG onto the Inputs–Integration/Processing boundary with a two-way link to Memory, checked against a render of printed p. 8) and one was declined: line 526's 'Pass I: see the stamp on line 2 and the audit log.' is the driver's own substitution text (scripts/pass_i/run.py lines 355–358), and the driver inserts the stamp at line 2 in the same step, so the pointer resolves on stamping and the brief bars touching that line.

**Gate:** pass. Deep reference sha256 `268b7ef1fabe1ea21d9656239fb4ff7c7fa265855c2bfc50dc3ab166bd9f2b47`, stamp included.

## Derived-tier fidelity check (2026-10-15)

The derived tier of `owasp-agentic-top10-2026` (OWASP Top 10 for Agentic Applications 2026) is the light reference alone: the source has no distillation and no index row. All 72 claims in the light reference were checked against the audited deep reference, with the tape opened where wording needed it, and 5 were fixed in place. Two fixes restore scope the condensation had widened (the eval ban applies to production agents; ASI08's rule sends the initial defect to ASI04, ASI06 or ASI07 only when it is a direct compromise). One restores a dropped hedge (ASI10's actions "may" each appear legitimate). One corrects a misdescribed scenario (ASI06: attempts, not rejections, are split across sessions). One realigns the ASI07 description's verb list with the source (block, not replay). The verbatim check is clean, and the deep reference has no defects.
