# SSDF v1.1 — Pass F/G derivation receipt

Producer: GPT-6 (Codex), high effort, 2026-09-25.

## Input and ordering

The final canonical `references/nist-ssdf-1-1-deep.md` was read in full after the root orchestrator reported both independent Pass I audit legs passed. This receipt records derivation and trace checks, not a further cold source audit. Pass I's consolidated receipt is `_ingest_pass_I_nist-ssdf-1-1_source_audit.md` in this directory.

Audited deep SHA-256: `2d50b8ceca4fc0465640ff4a957e731090f22c2c3b0aa500a97ea1f08bba6f81`.

The only additional substantive reading for the projection was the already-audited `open-kanban-deep.md`, Part II, “1. Visualize the workflow”, for the integration row. Source tape, original PDF and deep reference were not changed during Passes F/G.

## Pass F — task-neutral light reference

Output: `corpus.commons/demo/references/nist-ssdf-1-1.md`.

The light has 31 compact claim units: two thesis paragraphs, 23 numbered practice/interpretation units, two statistics rows, three connections and one contrarian-position paragraph. A unit is a paragraph or row containing related claims, not an atomised proposition count. Every component claim was compared with its cited audited-deep passage. Bibliographic/licence/structure metadata was also compared with the deep header and source-integrity notes. No task-application guidance appears in this tier.

| Light units | Audited-deep support |
|---|---|
| Thesis paragraphs 1–2 | Author's thesis; Part I, tailoring and Table 1 interpretation |
| Numbered 1–4 | Part I: Audience; integrate security; tailoring/shared responsibility; how to read Table 1 |
| Numbered 5–9 | Part II: PO.1, PO.2, PO.3, PO.4 and PO.5 respectively |
| Numbered 10–12 | Part III: PS.1, PS.2 and PS.3 respectively |
| Numbered 13–20 | Part IV: PW.1, PW.2, PW.4, PW.5, PW.6, PW.7, PW.8 and PW.9 respectively |
| Numbered 21–23 | Part V: RV.1, RV.2 and RV.3 respectively |
| Statistics rows 1–2 | Key statistics: four groups and more than 150 position papers |
| Connections 1–2 | Connections the author makes: NIST CSF and edition-specific OWASP mappings |
| Connection 3 | Part VI: Appendices A–C |
| Contrarian position | Positions the author explicitly frames against |

Notional examples remain distinguished from practices. Supplier requirements, protected evidence, the qualified-person/automated design-review options and contextual implementation expertise retain the final audited wording. The light does not treat SSDF as empirical proof of a particular security outcome.

## Pass G — software-business projection

Output: `corpus.commons/demo/distillations/software-business/nist-ssdf-1-1-software-business.md`.

All nine standard projection sections are present, followed by the runtime-trigger section. Source-backed content is separated explicitly from authored diagnostic questions, patterns and the illustrative scenario. The projection contains ten concept units with unique concept anchors; twelve questions across all six task phases; four diagnostic patterns; four use gates; four sourced worked-example application units; four anti-pattern rows; one qualified sibling integration; and eight runtime-trigger rows. Its two relevance paragraphs, source-integrity notes and scenario framing were checked as well.

| Projection material | Audited-deep support / trace result |
|---|---|
| Relevance and risk-based concept | Thesis; Part I Audience, tailoring, shared responsibility and Table 1 interpretation |
| Concepts 2–5 | PO.1 requirements; PO.2 roles/proficiency; PO.3 supporting toolchains; PO.4 criteria and safeguarded information |
| Concepts 6–7 | PO.5 and PS.1 environment/code protection; PS.2–PS.3 integrity, archives and provenance |
| Concepts 8–10 | PW.1–PW.2 design/review; PW.4–PW.9 production assurance; RV.1–RV.3 response and recurrence |
| Phase 1 questions | PO.1.3; PW.4; Part I shared responsibility |
| Phase 2 questions | Part I tailoring/shifting left; PW.1 |
| Phase 3 questions | Audience; PO.2.1–PO.2.3 |
| Phase 4 questions | PO.3.2–PO.4; PO.5; PW.7.2 |
| Phase 5 questions | PW.1–PW.2, PW.4–PW.9; RV.1–RV.3 |
| Phase 6 questions | Thesis common vocabulary; PO.1–PO.4; RV.1.3 stakeholder plans; RV.2.2 actionable advisories/trusted delivery |
| Diagnostic patterns 1–4 | PO.3.3–PO.4; PO.2/PW.2; PS.3/RV.1; RV.3 respectively |
| Use gates 1–4 | Four-group structure; shared responsibility/PO.1.3/PW.4; PO.3–PO.4; RV.2–RV.3 respectively |
| Worked-example applications 1–4 | Audience/shared responsibility/PO.1–PO.2; PO.3.3–PO.4; PW.1–PW.2/PW.4–PW.9/PS.2–PS.3; RV.1–RV.3 respectively |
| Anti-pattern rows 1–4 | Part I non-prescription; PO.3–PO.4; PW.5.1/PW.7; PS.3.2/RV.1–RV.3 respectively |
| Sibling integration | Open Kanban deep, Part II, “1. Visualize the workflow”, for visible work/status; SSDF PO.3.3–PO.4 for security evidence/criteria. Combination explicitly attributed to the projection author. |
| Source-integrity notes | Part I limits and Audience; edition-specific Connections; actual audit/derivation records |
| Trigger rows 1–8 | PO.1.3/PW.4/PS.3.2; PO.2/Audience; shared responsibility/PO.1.3; PO.2.3/PO.3.3/PO.4; RV.3; RV.1.3/RV.2/RV.3; tailoring/PO.3.3/PO.4; common vocabulary/PO.1–PO.4 respectively |

Both verbatim blocks are exact string matches to the final deep's audited Pass D quotations: Executive Summary p. vi (outcomes focus) and §1 p. 3 (risk-based planning rather than a checklist). The open scope and NIST attribution are retained. All eight runtime trigger strings exactly match existing software-business task seeds. No new trigger extension was introduced, and no operator-named lens was supplied or fabricated.

## Applicability and skips

| Task | Decision | Reason |
|---|---|---|
| software-business | Produced | Direct secure-delivery governance, capability, supplier, investment and response material for the six phases |
| decision-making | Skipped: clear no | Domain-specific security choices add no general decision method beyond the software-business projection |
| stakeholder-engagement | Skipped: clear no | Requirement/disclosure communication is covered in software-business Phase 6; no general engagement or conflict method |
| aar | Skipped: clear no | Technical root-cause feedback does not supply the cross-functional review/facilitation method |
| retro | Skipped: clear no | Secure-development improvement does not teach the ceremony, facilitation or experiment-review method |
| Lens variants | Skipped | No operator-named lens |

The per-source routing staging is `sources/ingest/_nist-ssdf-1-1/routing-rows.json`: six sections matching existing operator-index phase headings, containing six need rows plus eight exact-seed-trigger rows, all with four columns. Existing task seeds, operator indexes and runtime JSON indexes were not edited by this subagent. Root retains the shared merge/build step.

## Verification outcome

- Both derived artefacts stamped with the audited deep's SHA-256 using `scripts/check_derived_provenance.py --corpus demo --stamp --slug nist-ssdf-1-1`.
- Slug-scoped provenance check: **2 current, 0 unstamped, 0 stale**.
- Mechanical structure/quote/trigger checks: **23 numbered light units, 10 unique concept anchors, 12 questions, 10 projection H2 sections, 2 exact audited quotations, 8 exact seed triggers**.
- Full claim trace completed against the final audited deep; the supplier, evidence, expertise, example-status and edition limits survive into the derived tier.
- No source/deep edits, input removals, shared-index changes, build output edits, commits or pushes were performed in this F/G step.
