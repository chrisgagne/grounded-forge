# Method — locked decisions and mechanics

The decisions below were locked before the comparisons ran and held through the round.

## Judging design

- **Cross-family judging** for the headline comparison: each arm judged by the other model family, to defeat self-audit leniency (the failure mode this round ultimately demonstrated directly). Naive G notes (produced by `gpt-5.6-sol`) → judged by Claude; 9-pass deep references (produced by Claude Opus) → judged by Sol (`gpt-5.6-sol` via the Codex CLI).
- **Same-judge and matched-priming controls** were added when the cross-family numbers looked asymmetric: Sol re-judged G at claim grain (control for judge family), and the naive notes were re-audited with the identical primed hunt-list used on the deep references (control for audit prompt). The matched arm is the only one from which the no-detected-difference claim is drawn.
- **Subject-matter scope only.** Deep-reference audits exclude the metadata header (Source/Scope/Structure/Citation style/Coverage), licence/URL/publisher claims, conversion notes, "Citation and source-integrity notes" sections, and pure structural tallies. These layers are legitimately external to the source text; G's notes never had them, so auditing them against the source would be a category error. Cross-corpus "Connections" observations (claims about sibling references rather than the source under audit) are likewise out of scope: mcdp1-warfighting's cross-family row excludes 15 such flags, which the corpus audit-of-record lists separately.
- **Rubric:** FAITHFUL / MINOR-DRIFT / UNSUPPORTED / CONTRADICTED; strict, grade down on doubt; per-claim targeted search against the source (multiple phrasings) plus reading of matching regions; `[V]`-marked quotes must match essentially verbatim. "Hard" = UNSUPPORTED + CONTRADICTED.
- **Primed hunt-list** (used on both arms in the matched comparison): attributions the source doesn't make, enumeration miscounts, dropped qualifiers, dated-fact drift.
- **Grain:** each artefact audited at its native grain, with the claim-grain comparison as the fair one (the deep reference faces the *harder*, finer-grained test). Direction is trusted over decimals; judge variance at this grain is large.
- **Census over sampling** for the 11-source cross-family table; the producer-model and matched arms ran on 3–4 sources by construction.

## Producers

- **9-pass deep references:** the shipping protocol (Passes A–I), produced by Claude Opus. For the producer-model arm, `gpt-5.6-sol` re-produced eight references running Passes A–E only (full-source reads, coverage verified), deliberately without Pass I so the production passes could be compared without a cleanup pass; four entered the producer-model and matched arms. All eight are in [`arm-d-sol-refs/`](arm-d-sol-refs/).
- **Naive G notes:** Google's `web_ingestion_instruction.md` (the only pathway in the OKF reference implementation that touches prose) executed per source by `gpt-5.6-sol`, with mechanical substitutions and one disclosed semantic adaptation: the reuse gate treated as satisfiable by prospective cross-source reuse. Run with no adaptation the instruction minted zero references on both pilot sources — every productive pathway presupposes an existing warehouse concept spine (enrich needs existing concepts, the reuse gate needs existing concepts, the mandatory extractions want SQL metrics and join clauses, and "when in doubt, skip" closes the rest). One further note: *Introduction to Business* minted nothing because its title trips the instruction's meta-page skip-list.

## Receipts map

| File(s) | What they are |
|---|---|
| [`receipts/claude-on-g-claim/`](receipts/claude-on-g-claim/) | Claude's claim-grain audits of the G notes, per source; `{slug}-primed.json` are the matched-priming re-audits |
| [`receipts/sol-on-g-claim/`](receipts/sol-on-g-claim/) | Sol's claim-grain re-audits of G (same-judge control) |
| [`receipts/full-census-audit-sol.json`](receipts/full-census-audit-sol.json) | Sol's same-family full-census audit of all 221 G notes (the lenient baseline, note grain) |
| `receipts/*-deep-audit-claude.json` / `*-OPUS-deep-audit-claude.json` | Claude's matched-priming audits of the Sol-produced and Opus-produced deep references (producer-model arm) |
| Sol-on-deep-ref audits (11 sources) | Ten of the eleven are republished unchanged in the corpus audit-of-record at [`corpus.commons/demo/references/_audit/independent-2026-08-08/`](../../../../corpus.commons/demo/references/_audit/independent-2026-08-08/); the accounting-vol2 audit was re-run fresh for that record, so the round's original per-claim JSON for that source was not retained (its row totals are preserved in the table) |

Model identities: producer Claude Opus (4.x, per-reference provenance in the corpus git history); auditor/re-producer `gpt-5.6-sol`; cross-family judge Claude (general-purpose agent). Confidence intervals were not computed; the round reports observed counts and treats direction, not decimals, as the finding. Anyone re-running the audits should expect judge variance of the magnitude documented in the round README.
