# Pass I source audit: nist-ssdf-1-1 (consolidated, cross-family)

**Gate status: PASS.** No unresolved source-fidelity defects. Stamp `Pass I applied 2026-09-25` added to the working deep only after this log was written.

Date: 2026-09-25.

Reference under audit: `corpus.commons/demo/sources/ingest/_nist-ssdf-1-1/nist-ssdf-1-1-deep.md` (working deep, corrected in place).
Source: `corpus.commons/demo/sources/ingest/_nist-ssdf-1-1/nist-ssdf-1-1.md` (deterministic tape; NIST SP 800-218, SSDF v1.1, February 2022, 36 PDF pages).
Immutable original: `_planning/srm-sources-ingestion-2026-09-25/nist-ssdf-1-1/pre-audit-deep.md`.

## Identities (three separate parties)

| Role | Identity | Evidence |
|---|---|---|
| Producer (draft author) | `GPT-6 (Codex)`, OpenAI family; effort recorded as xhigh (9-pass) | Deep frontmatter, `pre-audit-deep.md` L1. Producer-reported; not observed by this auditor. |
| First auditor (cold, same family as producer) | CLI family `codex`; runtime self-identified as `GPT-6 (Codex)`; operator requested `gpt-6-astra`, effort xhigh; exact backend variant not exposed to that session | `first-audit.md` L5 |
| Cross-family auditor (this leg) | `claude-opus-5-5` (Claude Opus 5.5), Anthropic Claude family; CLI family `claude` (Claude Agent SDK / Claude Code harness); requested model `opus`; effort xhigh as configured by the operator | This session's model identity. Tools: Read / Write / Edit only (no shell). |

The producer and first auditor share a model family, so this leg is the protocol's required different-family verification.

## Procedure and ordering

1. Read the protocol and the three calibration fixtures.
2. Read the full source tape and the full **original** pre-audit deep. Did not open `first-audit.md`, the working deep, or any first-leg ledger.
3. Wrote the blind findings to `cross-family-blind-findings.md` (20 findings, B1–B20).
4. Only then read `first-audit.md` and the working deep, which carried the first leg's fixes F01–F06.
5. Sorted each first-leg finding (confirmed / missed / over-flagged / disputed), re-resolved each of my own blind findings against the source, and withdrew my own over-flags.
6. Applied the residual corrections to the working deep and re-read the full corrected deep against the source.
7. Wrote this log. Stamped last.

## Calibration

| Fixture | Expected | This auditor's call | Result |
|---|---|---|---|
| `tests/audit-fixtures/01-training-leakage.md` (L1–29, full) | Strip the Hackman career sentence | Strip | Match |
| `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (L1–29, full) | `[V]` → `[AP]` or quote the source | `[AP]` | Match |
| `tests/audit-fixtures/12-clean-negative-control.md` (L1–37, full) | No findings | No findings | Match |

Rules read: `.claude/skills/ingesting-resources/9-pass-protocol.md` L1–384 (full, including Pass I at L303–354 and the Pass E note on invented oppositions at L101). Root `CLAUDE.md` was already loaded in session context and was followed from there. `docs/architecture/source-integrity.md` was not opened separately, because its operative rule is restated in root `CLAUDE.md` and the protocol.

## Full-read ranges

| File | Ranges (inclusive) | Coverage |
|---|---|---|
| Source tape | 1–249; 250–549; 550–849; 850–1149; 1150–1449; 1450–1749; 1750–2049; 2050–2299 (EOF) | 2299/2299 lines as displayed (L2299 is the trailing blank line; the first leg's 2298 counts the same content without it). PDF pages 1–36, all seen. |
| Original deep (`pre-audit-deep.md`) | 1–228 (EOF) | Full |
| First-leg report (`first-audit.md`) | 1–121 (EOF), read after the blind findings were written | Full |
| Working deep, as received | 1–228 (EOF), read after the blind findings were written | Full |
| Working deep, final | 1–227 (EOF) | Full re-read after corrections |

The first leg's ledgers (`claim-ledger*`, `structure-coverage.md`, `checks.json`, patch and snapshot) were not read: they were not needed to resolve any finding, and reading them would not change the source trace. No source or deep range went unread. No partial-coverage declaration was needed or made.

## Source structure and coverage (TOC-vs-anchors)

Enumerated source structure: Cover (PDF 1); Title/authors (PDF 2); Authority (PDF 3); Reports on Computer Systems Technology, Abstract, Keywords, Trademark Information (p. ii); Acknowledgments (p. iii); Audience (pp. iii–iv); Note to Readers (p. iv); Patent Disclosure Notice (p. v); Executive Summary (p. vi); Table of Contents / List of Tables (p. vii); 1 Introduction (pp. 1–3, footnotes 1–4); 2 The SSDF (p. 4) and Table 1 (pp. 5–19, footnotes 5–9); References (pp. 20–23); Appendix A with Table 2 (p. 24); Appendix B Acronyms (pp. 25–26); Appendix C Change Log (p. 27).

Table 1 inventory (tape L508–1987), all anchored in the deep: 19 live practices (PO.1–5, PS.1–3, PW.1, PW.2, PW.4–9, RV.1–3) and one retired practice row (PW.3). 42 live tasks: PO.1.1–1.3, PO.2.1–2.3, PO.3.1–3.3, PO.4.1–4.2, PO.5.1–5.2, PS.1.1, PS.2.1, PS.3.1–3.2, PW.1.1–1.3, PW.2.1, PW.4.1, PW.4.2, PW.4.4, PW.5.1, PW.6.1–6.2, PW.7.1–7.2, PW.8.1–8.2, PW.9.1–9.2, RV.1.1–1.3, RV.2.1–2.2, RV.3.1–3.4. Five retired task rows: PW.3.1, PW.3.2, PW.4.3, PW.4.5, PW.5.2. This matches the first leg's 19/1 and 42/5.

Every source-TOC section (Executive Summary, §1, §2, References, Appendices A–C) has a body anchor, and so does Table 2. Footnotes 1, 2, 4, 5, 6, 7 and 8 are anchored; footnotes 3 and 9 are small details (see Omissions). Front-matter boilerplate (Reports on Computer Systems Technology, Keywords, Trademark) is anchored only in **Structure**. It is not a TOC chapter and carries no argument. **TOC-vs-anchors: PASS.**

Figure-derived claims: the publication has no numbered figures (List of Tables only, tape L304–306). The deep's visual claims all trace to source text: four columns (header row, tape L513), group borders and shading with unshaded retired rows (Appendix C, L2295–2296), and Table 2 as two columns (L2174–2176). None depends on the page images alone.

## Counts

Counting rule (cross-family leg): one unit per sentence, table cell or bullet assertion, counting header, thesis, stats rows, connections, positions and notes. The first leg used a finer rule (every enumerated example action, 514 units). The two totals measure the same text at different grain and are not comparable one-to-one.

| Measure | Count |
|---|---:|
| Claim units checked (blind, on the original) | 194 |
| Source-content units | 174 |
| Source-content units anchored to a source passage (final) | 174 |
| Metadata / process units | 20 (9 corroborated against the tape; 11 producer-process or external-provenance statements, which are outside source-claim scope and noted below) |
| `[V]` checked | 2 of 2 exact (tape L274–275; L440–442), contiguous in Poppler `-raw` pages with sequential reading order |
| Evidence markers, final | 100: V 2, AR 4, AP 51, AE 30, BT 13 |
| Blind findings raised | 20 |
| Withdrawn on reconciliation (my own over-flags) | 3 whole + 1 sub-part |
| Blind findings coinciding with first-leg fixes | 4 (B7→F05, B10 part→F02, B11→F03, B13→F04) |
| First-leg findings confirmed | 6 of 6 (F01 and F06 missed by my blind pass, confirmed on source) |
| First-leg findings over-flagged / disputed | 0 / 0 |
| First-leg clean retentions disputed | 1 (the "Mandatory notional examples" position bullet) |
| Residual defects the first leg missed, now corrected | 14 (1 moderate, 13 low), touching 17 claim units |
| Whole claims stripped | 0 |
| Unsupported qualifiers stripped | 1 ("where appropriate", PO.4.2) |
| Structural strips (content kept elsewhere) | 1 (stand-alone opposition bullet merged) |
| Marker corrections / relocations | 1 relocation (`[BT]` for footnote 7 moved from PO.5.2 to PO.5.1); AP −1 from the merge |
| Unresolved defects | 0 |

## First-leg findings, classified

| First-leg ID | Deep anchor | Classification | Note |
|---|---|---|---|
| F01 | L91 PO.4.1 | **Confirmed; missed by my blind pass** | Source records "approvals, rejections, and exception requests" (tape L870–871). Correct fix. |
| F02 | L91 PO.4.2 | **Confirmed** (= part of B10) | Review object is the decision-making processes (tape L893–894). The same sentence also kept an added hedge, now fixed as R8. |
| F03 | L95 PO.5.1 | **Confirmed** (= B11) | Ex 4 and Ex 5 had been conflated (tape L931–935). Correct fix. |
| F04 | L119 PW.1.3 | **Confirmed** (= B13) | "approved" is not in the source (tape L1230–1231). Correct fix. |
| F05 | L65 PO.1.3 | **Confirmed** (= B7 main) | "Require", not "request" (tape L613–614, L632–634). Correct fix. |
| F06 | L23 Audience | **Confirmed; missed by my blind pass** | The NICE categories are cited to [SP800181] (tape L197–199). Adding `[BT]` is accurate. |

Disputed clean retention: `first-audit.md` L97 kept both opposition bullets (deep L218–219) as "explicit source exclusions". The checklist bullet is legitimate, because the source draws its own "not … but" contrast (tape L440–442) and rejects the same-objectives assumption (L421–422). The second bullet takes a scope disclaimer ("No examples or combination of examples are required", L486–488) and presents it as a stand-alone position that nobody holds. That is the protocol's invented-opposition shape (Pass E note, protocol L101). Resolved as R14.

## Residual defects found by the cross-family leg and missed by the first leg (all applied)

Deep line numbers refer to the working deep as received (same as the original) and, after the arrow, the final deep.

| # | Blind ID | Sev | Deep anchor | Defect | Source anchor (tape) | Applied correction |
|---|---|---|---|---|---|---|
| R1 | B1 | L | Thesis ¶1, L13→L13 | "SDLC models often do not specify security in sufficient detail" softens "Few SDLC models explicitly address software security in detail". "address causes … recur less often" drops the source's term *root causes*. | L137–139, L321–327 | "few SDLC models explicitly address software security in detail"; "reduce the number of vulnerabilities…", "reduce the potential impact of exploiting undetected or unaddressed vulnerabilities", "address the root causes of vulnerabilities to prevent recurrences". |
| R2 | B2 | L | Thesis ¶2, L15→L15 | "different security assumptions, needs and resources": *resources* is not among the differences the source recognises. | L421–424 | "each producer may have unique security assumptions and each acquirer unique security needs and requirements". |
| R3 | B4 | L | Acknowledgments, L25→L25 | "followed by public comments" imposes an order the source does not state ("Additionally"). | L165–172 | "together with public comments from dozens of organisations and individuals". |
| R4 | B5 | L | §2 reading notes, L53→L53 | "must be defined" upgrades the source's "should define". "limit lateral movement" softens "prevent". | L497–503 | Source modality restored; the terms are noted as undefined in the publication; "especially to prevent attackers' lateral movement between environments". |
| R5 | B6 | L | PO.1, L59→L59 | "avoids duplicated effort" overstates "duplication of effort can be minimized". | L519–522 | "Collecting requirements once and sharing them minimises duplicated effort." |
| R6 | B8 | L | Footnote 5, L67→L67 | Provenance definition moved "associated data" into the optional clause and dropped "chronology". | L713 | Definition restated in the source's structure. |
| R7 | B9 | L | PO.3.1 row, L83→L83 | "evaluate signed immutable audit records": the example evaluates tools' signing capabilities. | L765–766 | "evaluate tools' signing capabilities for creating immutable, auditable records/logs". |
| R8 | B10 residual | L | PO.4.2, L91→L91 | "where appropriate" is an ingester hedge, not in the example. | L893–894 | "automate gathering and criteria-based decision-making, periodically review those decision-making processes". |
| R9 | B12 | **M** | PO.5.1/PO.5.2, L95, L97→L95, L97 | Footnote 7 (SP 800-207) is attached to **PO.5.1 Example 10** ("zero trust architecture⁷"), not PO.5.2. The deep attached the footnote sentence, `[BT]` and citation to PO.5.2. "hardens development endpoints using risk" also garbled "using a risk-based approach". | L968–970, L990–991 (PO.5.2 Ex 7 has no footnote), L1047–1048; L971–974 | Footnote sentence, `[BT]` and "footnote 7" citation moved to PO.5.1. PO.5.2 now reads "secures and hardens development endpoints using a risk-based approach … [AP] [AE] (Table 1, PO.5.2, p. 9)". |
| R10 | B16 | L | PW.9.2, L161→L161 | "dependencies" narrows "relationships with other settings". | L1732–1733 | "relationships with other settings". |
| R11 | B17 | L | Appendix A, L183→L183 | "consistent with risk" garbles Table 2's "consistent with a risk-based approach". | L2191 | "all practices and tasks consistent with a risk-based approach". |
| R12 | B18 | L | Appendix B, L187→L187 | Overstated as a glossary that "supplies the … abbreviations used in the reference mappings". The source defines "Selected acronyms"; the mapping labels are keyed in the References. | L2205–2253; L1997–2153 | "defines selected acronyms…"; "expands several organisation and standard names that appear within the reference-mapping labels, such as BSIMM, CNCF, IEC, ISO, NTIA, OWASP and PCI; the mapping labels themselves are keyed in the References list"; citation adds References pp. 20–23. |
| R13 | B19 | L | Key statistics row 2, L202→L202 | "Input position papers for June 2021 workshop" asserts they were for the workshop. The source says NIST held a workshop *and* received the papers, in response to EO 14028 §4. | L164–168 | "Position papers NIST received in response to EO 14028 §4, alongside a June 2021 workshop". |
| R14 | B20 | L | Positions, L218–219→L218 | Stand-alone "Mandatory notional examples" position (see the disputed retention above). | L486–488; L421–422, L438–442 | Examples disclaimer folded into the checklist bullet, in the source's own terms ("not the only feasible options"); separate bullet removed. No content lost; Part I L53 also carries it. |

## Blind findings withdrawn on reconciliation (my over-flags)

| Blind ID | Deep anchor | Why withdrawn |
|---|---|---|
| B3 | Authority, L21 | "does not supersede … authorities or mandatory standards" is a fair paraphrase of "should not be taken to contradict … nor … altering or superseding" (tape L76–79). A reader takes away the same limit. Clean paraphrase. |
| B7 (sub-part) | PO.1.3, L65 "supplier selection criteria" | The source's software-selection criteria are the third party's own capabilities: disclosure programme, incident response, adherence to practices (tape L609–612). "Supplier selection" is a faithful gloss. |
| B14 | PW.3 L127; Tables L195 "preserve identifier history" | The retired rows state "Moved to …" (tape L1289–1293), which does preserve identifier history. The change log confirms they are retired identifiers shown without shading (L2292–2296). Clean paraphrase. |
| B15 | PW.4.1 row, L135 "publish secure configurations", "maintain approved versions" | These are paraphrases of "make these available … so developers can readily use" and "list of organization-approved … component versions" (L1315–1317, L1324–1325). Scope is not materially changed. |

## Checked and retained (clean)

- Both `[V]` blockquotes are exact. The Executive Summary version (tape L274–275) was correctly chosen over the differently worded §1 sentence (L352–366).
- Every body page citation resolves to the correct printed page, task by task.
- The PW.4.5 discrepancy (Table 1 "Moved to PW.4.1 and PW.4.4", tape L1425, vs the change log "merged into PW.4.4", L2268) is reported as the source presents it, with no invented reconciliation.
- Every work in Connections appears in the source's footnotes or References. There is no cross-corpus drift, no biography, and no post-source vocabulary.
- "regression tests" (L157), "actionable advisories" (L173) and "confidential code" (L103) are clean paraphrases of the source's examples.
- L205 (no measured percentage reduction) is a verified absence across the full tape, not a methodological verdict.
- The shifting-left, reuse-economics and secure-by-default rationales are explicit in the source (tape L330–335, L1294–1305, L1703–1708), not domain priors.

## Metadata and process claims (outside source-claim scope)

- Corroborated against the tape: the Source line (tape L12–24, L52), the Structure line (tape page headings), the Citation style (printed p. 1 = PDF p. 10, L309–316), and the mixed-converter split and restored appendix labels (tape L1). Quotation exactness and the Authority licence statement (L80) are also corroborated.
- Not re-run by this leg (no shell): the PDF SHA-256, Poppler 26.08.0, page-image inspection and retained-image counts. The first leg re-ran these and reports a matching PDF digest, a byte-identical fresh Poppler conversion and a byte-identical image set (`first-audit.md` L37, L103). They are ingestion provenance, not source claims, and they do not gate this pass.
- The licence string's worldwide-permission clause comes from NIST's policy page, is labelled as such in the notes, and the first leg checked it on 2026-09-25. It is accepted as Pass A metadata.
- `first-audit.md` L118 records `corrected_deep` sha256 `30ff8ff1…`. That hash is now **stale**, because this leg changed the working deep. Re-hash before any provenance stamping.

## Omissions noted (small details; not coverage failures; nothing added)

- §1 "Future work" paragraph (tape L344–351) and footnote 3 (L404–406).
- Footnote 9 naming the NVD as an example vulnerability database (L1797–1798).
- Practice-level rationales for PW.1 ("secure by design", L1155–1159), PW.5, PW.6, the PW.7 automation benefit, and RV.2.
- Two source-internal inconsistencies left unrecorded. The List of Tables says Table 2 covers EO 14028 "Clauses" (L306), while the appendix titles it "Subsections" (L2173). Footnote 2 says SSDF practices "do not map" to CSF Functions/Categories/Subcategories (L400–403), while Table 1 lists NISTCSF subcategory IDs. The deep reports footnote 2 accurately, as the first leg noted.

Per the brief, no new author claims were introduced.

## Final gate

- Every section of the source tape and every section of the deep were read in full, with no gaps.
- TOC-vs-anchors: PASS.
- All 174 source-content units trace to source passages after correction. Both `[V]` are exact, and every marker matches its support.
- No training-data leakage, cross-corpus drift, post-source vocabulary or task-application guidance. The one invented opposition has been removed.
- Unresolved defects: **0**.

**Pass I: PASS (cross-family verified).** Derived tiers (light ref, distillations) do not exist yet. The root should regenerate Passes F and G from this final deep and then stamp them with `scripts/check_derived_provenance.py --stamp`.

## Files written by this leg

- `_planning/srm-sources-ingestion-2026-09-25/nist-ssdf-1-1/cross-family-blind-findings.md` (blind findings, written before the first leg was read)
- `_planning/srm-sources-ingestion-2026-09-25/nist-ssdf-1-1/_ingest_pass_I_nist-ssdf-1-1_source_audit.md` (this log)
- `corpus.commons/demo/sources/ingest/_nist-ssdf-1-1/nist-ssdf-1-1-deep.md` (14 residual corrections in 15 edits, then the stamp line appended after this log was written)

No shared index, derived artefact, commit or external contact.
