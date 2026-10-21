# Pass I source audit: owasp-asvs-5-0

- **Deep reference:** `references/owasp-asvs-5-0-deep.md` (418 lines, read in full: lines 1–418)
- **Tape:** `sources/converted/owasp-asvs-5-0.md` (2,516 lines, 38,513 words, read in full: lines 1–2516, Frontispiece through the last row of Appendix E)
- **Original:** `sources/original/owasp-asvs-5-0.pdf` (123 pages). No page renders used: the tape is the upstream Markdown, undamaged, with no figures beyond the licence badge (tape line 19), and no `[V]` quotation rests on a scanned page.
- **Auditor:** Claude Opus 5.5, fresh same-family leg, fix-in-place mode. A blind cross-family leg (codex) runs in parallel on a frozen copy; until it reports, treat this reference as audited-but-unverified.
- **Date:** 2026-10-15
- **Calibration:** fixtures 01, 07 and 12 read before the cold read.

## Outcome

| Measure | Count |
|---|---|
| Claims audited | about 400: 326 marker-tagged claims (69 `[V]`, 192 `[AP]`, 38 `[AR]`, 7 `[AE]`, 20 `[BT]`), 20 key-statistics rows, 12 connections, 13 positions framed against, and about 30 frontmatter and source-integrity facts |
| Source-anchored | all, after the corrections below |
| Stripped | 0 |
| Marker-corrected | 0 |
| Quotation-corrected | 0 |
| Claims corrected in place | 4 (plus 1 typo) |

The reference passes. TOC-vs-anchors: all 27 upstream files, all 17 requirement chapters and every one of their 80 sections are anchored in the body; no coverage gap.

## Verbatim check

`python3 scripts/check-verbatim.py` before and after: no findings. Its 18 unchecked figure claims (the key-statistics rows) were checked by hand against the tape: every value matches its cited requirement or section.

## Mechanical checks done by hand

- **Level tallies.** Every per-chapter and per-section L1/L2/L3 spread recounted from the tape's Level columns: all 17 chapter totals and the corpus totals (L1 70, L2 183, L3 92; 345) match. `grep` confirms 345 requirement rows, every one beginning "Verify that", and 17 References sections.
- **Upstream file map** (deep line 404): all 27 line numbers match the tape's `<!-- Upstream file: … -->` markers.
- **Counts:** glossary 87 terms (tape 1946–2032); Appendix E 249 entries (62 rows of 4, plus 1); 24 Diffie-Hellman groups; 11 chapters with a documentation section.
- **PDF metadata:** 123 pages, creator "LaTeX via pandoc with the Eisvogel template", created 2025-05-30, sha256 `f3e9a2f1…d30c6`: all match line 402.
- **As-printed spellings** (line 410): all twelve misspellings and both grammatical slips found at the places described.

## Changes to the deep reference

| Line | Before | After | Reason |
|---|---|---|---|
| 75 | "A patch release may only remove requirements … or make them less stringent" | "may remove requirements …" | The source ("Release strategy") says requirements "may be removed … or made less stringent"; "only" is not in it. |
| 236 | "… public [AP]. if the code flow is used" | "If the code flow is used" | Typo (sentence-initial lowercase). |
| 377 | NIST and FIPS publications and BSI TR-02102-2 "the basis of the approved-algorithm lists and parameters" | cited as references for the approved algorithms and parameters and in the V11 references; SP 800-52 Rev. 2 and BSI TR-02102-2 named, alongside Appendix C, as places to find approved cryptographic methods for WebRTC DTLS | Overreach. Appendix C cites these documents in its reference columns; V17.2 names SP 800-52 and the BSI TR only as other places to find approved methods ("either in the Cryptography Appendix of the ASVS or in documents such as …"). No passage calls them the basis of the lists, and FIPS 140-3 appears only in V11's References. |
| 378 | "RFC 4180, 2616, 6455, 6266 and 8705 in individual requirements" | "RFC 4180, 2616 and 6266 in individual requirements and RFC 6455 and 8705 in section introductions" | RFC 6455 is cited in the V4.4 introduction and RFC 8705 in the V10.4 introduction, not in a requirement. |
| 381 | "the Orange Tsai SSRF and Bishop Fox JSON interoperability papers" | "the Orange Tsai SSRF paper and the Bishop Fox post on JSON interoperability vulnerabilities" | The V1 References list the Bishop Fox item as a blog page ("An Exploration of JSON Interoperability Vulnerabilities", bishopfox.com/blog), not a paper. |

## Looked at and left standing

These were checked because they could be read as defects, and they trace:

- Line 196: "Most requirements are L1 because from L2 multi-factor authentication is required". V6.2 gives "most important at that level" as its reason, and "What is the ASVS?", "Level 1" gives the MFA reason in so many words. Supported.
- Line 200: "NIST treats PSTN and SMS as 'restricted' and to be deprecated". The source sentence carries the same ambiguity about who says "should be deprecated"; the paraphrase does not add an attribution the source lacks.
- Line 247: the "since" linking where the balance is struck to the cost of retrofitting. The two are adjacent sentences in the V11.1 introduction, and reading them as cause and effect is a fair `[AR]` reading.
- Line 259: "may compromise all of them" against the source's "may lead to a compromise of the security posture of the applications using it". Close enough as a paraphrase.
- "Positions the author explicitly frames against" (lines 386–398): each entry rests on an explicit contrast or prohibition in the source; none of them invents an opposition from a bounded positive claim.

No training-data leakage, post-source vocabulary, cross-corpus drift, task-application guidance, or source-external evaluative framing found.

## Derived tier

No distillation mentions `owasp-asvs` (searched `distillations/`). Light reference `references/owasp-asvs-5-0.md`, which this audit did not edit:

- **Light line 73**, "NIST and FIPS cryptographic publications, IETF RFCs and OpenID specifications: the basis of V9, V10, V11, V17 and Appendix C". This carries the same "basis of" framing corrected at deep line 377. Re-derive it from the audited deep.
- Light line 29 (release strategy) does not carry the "only" corrected at deep line 75; no change needed.
- The deep edits at lines 378 and 381 concern detail the light reference does not carry.

## Left open

- Deep line 416 reads "Pass I: see the stamp on line 2 and the audit log". Line 2 is currently blank. This audit set no stamp and edited no Pass I line, per the dispatch; the driver stamps once both legs are done.
- The cross-family leg's findings are still pending.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `126043d64aae5715876003750c5891cb64c3308efced3ce5db0cc305d98a136b`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `293797e04663375f17e03350a87a32d8cb4a2367a2fe422a59f8e4a4da699f2a`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_owasp-asvs-5-0_crossfamily_blind.md`, `_ingest_pass_I_owasp-asvs-5-0_crossfamily_sort.md`, `_ingest_pass_I_owasp-asvs-5-0_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 16 deep-reference defects (4 fixed by the fixer, 1 recognised but left unresolved, 10 missed by the fixer, 1 found by the sort itself), counted 1 over-flagged by the fixer and 1 by the blind auditor, 0 disputed, capture fixer=5 blind=11 both=1, and gave a pass verdict once its 12 remaining edits were applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 5, the blind audit 11, both 1. The Chapman estimate is 35 in all, about 20 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of 12 remaining edits, 9 were applied as written, 2 with changed wording (5.3.1 now says 'accessed directly with an HTTP request' as the source does, 11.3.4 reads 'encryption key and data-element pair, generated by a method appropriate to the algorithm', and the line-395 opposition keeps the reference's US spelling 'authorization'), and 1 declined: edit 12 (strip line 416, 'see the stamp on line 2') is not a defect, because the driver writes that exact sentence and inserts its stamp at line 2 (scripts/pass_i/run.py:356-357), so the pointer is true once the driver stamps.

**Gate:** pass. Deep reference sha256 `cec6c81d3bfaa28073db3fcc9f26d226c337ffc6732021b1c854a11d1150ae70`, stamp included.

## Derived-tier fidelity check (2026-10-15)

The fidelity check of `owasp-asvs-5-0` covered the light reference only, because the source has no distillation and no distillation-index row. Of 86 claims in the light reference, 4 were fixed in 5 narrow edits, each checked against the audited deep reference and the tape. Three claims had dropped hedges restored: a major release "may change almost everything, including requirement numbers"; DAST and SAST tools "may" find issues, and it "may be possible" to write application-specific tests on existing test infrastructure; testability is a "relative and, at times," misleading criterion. One widened claim was narrowed: "running an off-the-shelf tool is not verification" became the source's two claims, that testable using automation does not mean running an off-the-shelf tool and that running a tool without thorough testing is insufficient for certification. No claim lacked support in the deep reference, no anchor was wrong, and no deep-reference defect was found.
