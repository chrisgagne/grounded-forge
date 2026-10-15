# Pass I source audit: owasp-agentic-threats-mitigations

- **Deep reference:** `references/owasp-agentic-threats-mitigations-deep.md` (520 lines, read in full: lines 1–520)
- **Source:** `sources/converted/owasp-agentic-threats-mitigations.md` (1,985 lines, read in full: lines 1–1985, cover through the p. 52 footer)
- **Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode, 2026-10-15
- **Cross-family leg:** codex, blind, on a frozen copy, run in parallel by the driver. This log is the same-family leg only; the driver stamps once both legs are in.
- **Calibration:** read fixtures 01, 07 and 12 before the cold read.

## Counts

| Item | Count |
|---|---|
| Claims audited | about 420 (344 marker-bearing claims: 109 [V], 105 [AP], 61 [AR], 41 [BT], 28 [AE]; plus about 75 unmarked claims in the header, threat-list table, diagram bullets, key-statistics table, connections and source-integrity notes) |
| Source-anchored | about 417 |
| Stripped | 0 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 (`check-verbatim.py`: no findings before or after) |
| Claims corrected (wording) | 3 |

## Mechanical checks

- `python3 scripts/check-verbatim.py` on the deep ref: "no findings; 0 figure claim(s) not checked", before and after the edits. All 109 `[V]` quotations match the tape.
- `pdfinfo`: 53 pages, title field "Microsoft Word - FINAL DRAFT__Agentic AI - Threats and Mitigations 1.1.docx", created 2025-12-07 10:18:12 NZDT, as the integrity notes state.
- sha256 `65e3bd59…10345ff` matches the integrity notes and the source card.
- Tape: 1,985 lines, 14,767 words, 53 form feeds, as stated. Page-anchor line numbers in the integrity notes (p. 1 at 40, p. 10 at 293, p. 16 at 527, p. 20 at 709, p. 32 at 1227, p. 33 at 1228, p. 42 at 1609, p. 49 at 1872, p. 52 at 1985) all confirmed.
- TOC-vs-anchors: every section in the printed Table of Content (Introduction through Project Supporters) is covered by a heading in the deep ref. No `coverage: partial`. Passes.
- Page citations: every threat's table, Navigator and scenario page, every playbook page and every example-threat-model page traced to its footer and confirmed.
- Threat-list table (deep lines 146–164): every Navigator step, playbook assignment and example-threat-model column checked against pp. 21–49. All correct, including T14's "none".
- Counted statistics: 66 Navigator scenarios (5+5+3+4+4+6+3+4+3+3+2+6+3+2+5+4+4), 10 patterns, 39 contributors in the text layer (2 co-leads, 12 core, 25 others), 7 reviewers, 108 supporters (27 rows by 4 columns). All confirmed.

## Renders (6 of the 10 allowed, at 110 dpi)

PDF pages 7, 9, 11, 15, 17 and 51 (printed pp. 6, 8, 10, 14, 16, 50). None failed.

- **p. 6:** both figure descriptions confirmed, apart from one detail, corrected below (Memory's dashed link).
- **p. 8:** single-agent diagram description confirmed.
- **p. 10:** multi-agent diagram description confirmed: the components of all four agents, the Shared memory, the Internal Services box, and the links from Agents 1–3 to Services.
- **p. 14:** the malformed RAG sentence ("…modern agentic AI systems, awareness and response accuracy…") is in the rendered original, as the integrity notes say.
- **p. 16:** every threat-ID placement in the summary-diagram bullets confirmed; 15 labels (T1–T15); T16 and T17 absent.
- **p. 50:** 38 contributors visible; "Hariprasad Holla, CrowdStrike" is in the text layer only. Confirmed.

## Changes to the deep reference

1. **Line 17 (thesis), wording corrected.** "autonomy, persistence and multi-agency amplify existing LLM risks" → "autonomy, memory and the complexity and scale of multi-agency amplify existing LLM risks". The cited pages (pp. 13–15) name memory as an attack vector (p. 13) and say multi-agency exacerbates risks "with their complexity and scale" (p. 15). "Persistence" is the ingester's word, not the source's framing of what amplifies the risks.
2. **Line 41 (p. 6 figure), corrected from the render.** The dashed link from Memory reaches both Planning and Reflection, not Planning alone.
3. **Line 393 (Playbook 6 Step 2), wording corrected.** "cut their network and system access" → "restrict their network and system access". The source says "Immediately restrict network and system access for flagged agents" (p. 41); "cut" overstated it.

## Considered and retained

- **"Positions the author explicitly frames against", third bullet** ("The LLM Top 10 entries alone, for agentic threats"). I checked it as a possible invented opposition. I kept it because, threat by threat, the Navigator draws the contrast against a named alternative: "partially covered by LLM06:2025 Excessive Agency. However…" (pp. 25, 26) and "Unlike the existing LLM01:2025 … and LLM05:2025" (p. 27). Each example in the bullet traces to its page. If the cross-family leg disputes it, the fallback is to strip the bullet: the same content is in each threat's Navigator paragraph.
- **"quoted approvingly" / "cited approvingly"** (Russell and Norvig; Threat Modeling Manifesto). The document adopts both without qualification, so these are stance labels of the kind the template asks for, not evaluative framing. Retained.
- **First-publication date 2025-02-17** (integrity notes). It is attributed to fetch metadata and recorded in the source card, and the note says it is not in the tape. This is provenance, not a source claim. Retained.

## Left open

- Line 520 reads "Pass I: see the stamp on line 2 and the audit log.", but line 2 is currently blank. Per the dispatch, the driver stamps; this audit left the line and the frontmatter untouched.

## Derived tier

- **Light ref** `references/owasp-agentic-threats-mitigations.md`, line 13, carries the pre-audit phrase "autonomy, persistence and multi-agency amplify existing LLM risks" (change 1). Re-derive.
- Changes 2 and 3 are below light-ref granularity; neither phrase appears in the light ref.
- **Distillations:** none found for this slug under `distillations/`.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `29802915745ce06f8300311a66c564aac6a29dc0d528542fad34ac3c9dfc2e4c`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `63e0605ccafb2b66a2477d7acf9e26b624366ff10fc957756ee2b10d0fb60c23`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_owasp-agentic-threats-mitigations_crossfamily_blind.md`, `_ingest_pass_I_owasp-agentic-threats-mitigations_crossfamily_sort.md`, `_ingest_pass_I_owasp-agentic-threats-mitigations_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 6 defects (2 confirmed and fixed, 1 confirmed with the fix incomplete, 3 missed by the fix-in-place audit), found 0 over-flagged by the fixer and 0 by the blind auditor, left 1 disputed (the thesis's "persistence" wording, resolved by keeping the fixer's replacement), and gave a pass verdict once its four remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 3, the blind audit 4, both 1. The Chapman estimate is 9 in all, about 3 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Three remaining edits were applied as written (marker corrections at deep lines 476 [BT]→[AP], 478 [BT]→[AE] and 490 [BT]→[AP], each checked against tape 178–180, 279–281 and 1714–1717), none with changed wording, and one was declined: stripping line 520's "Pass I: see the stamp on line 2 and the audit log.", because that is the driver's own post-stamp text (run.py:355–357 inserts the stamp at line 2 at finalize), so the pointer resolves when the driver stamps.

**Gate:** pass. Deep reference sha256 `15c9f7f12e52fadca74b293c8fbdb45e2eb40f0824fed39f82ed3952fdfba98a`, stamp included.

## Derived-tier fidelity check (2026-10-15)

For `owasp-agentic-threats-mitigations`, the derived tier is the light reference alone; there are no distillations and no distillation-index rows. All 73 sentence-level claims in the light reference were traced to the audited deep reference, with the tape opened where wording needed checking. Seven were fixed in place. Three restored a dropped hedge: "typically" on the three core capabilities, and "can" on rogue agents staying embedded and on agents escalating false positives. Four narrowed a widened scope: the second reason for following no methodology belongs to methodologies "like MAESTRO", not to methodologies in general, and only some Navigator entries are set against an LLM Top 10 entry, not every threat. Anchors, counts, threat names and recorded internal mismatches held. `check-verbatim.py` reports no findings. One deep-reference defect was recorded and not fixed: deep line 182 says every Navigator entry gives an LLM Top 10 relation, but seven do not.

## Gate settlement (2026-10-15)

- The fidelity check found the summary sentence before the per-threat entries over-generalised the Navigator's structure: seven Navigator entries (T7, T8, T9, T10, T14, T15, T16) relate the threat to no LLM Top 10 entry (tape lines 720-1230). The sentence now says ten of the seventeen do. The per-threat entries were already accurate.
