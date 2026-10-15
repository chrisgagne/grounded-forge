# Pass I source audit: egashira-testsuitebench-2026

**Leg:** same-family (Claude Opus 5.5), fresh subagent, fix-in-place. The blind cross-family leg (codex) runs separately on a frozen copy; this leg did not read it.
**Date:** 2026-10-15
**Deep reference:** `corpus.commons/chrisgagne-agent-built-software/references/egashira-testsuitebench-2026-deep.md` (341 lines; read in full, 341/341)
**Source:** `corpus.commons/chrisgagne-agent-built-software/sources/converted/egashira-testsuitebench-2026.md` (2,860 lines; read in full, front matter through Table 7). The original PDF was not available, so no page renders were made and no `pdftotext -layout` check could be repeated.
**Calibration:** 9-pass protocol Pass I and failure-mode reference read; fixtures 01, 07 and 12 read before the cold read.

## Counts

| Item | Count |
|---|---|
| Claims audited (sentence-level assertions, table rows and cells, list items, markers, cross-references, notes) | about 230 |
| Source-anchored | about 228 |
| Stripped | 0 |
| Marker-corrected | 1 |
| Claim-corrected (mischaracterised reference) | 1 |
| Quotation-corrected | 0 |

`check-verbatim.py` before the read: no findings. After the edits: no findings (the new `[V]` caption quotation passes).

## Changes

1. **Line 158, Table 2 caption (marker mismatch).** The sentence said the caption "reads:" and then gave the caption's words, unquoted, under `[AP]`. The text is the caption word for word (tape lines 433-434). Made it a quotation of the caption with `[V]`.
2. **Line 316, Connections, model citations (mischaracterised reference).** The entry called all five model citations "system and model cards". DeepSeek-AI et al. (2026) is an arXiv preprint, "Deepseek-v4: Towards highly efficient million-token context intelligence" (tape lines 865-867), not a card. Rewrote the entry to name the three system cards, the Gemini model card and the DeepSeek-V4 preprint, and added the §2.1 and App. C citation sites (OpenAI 2026a is also cited in §2.1 for the construction model).

## Traced and kept

Every other claim traced to a passage. The sections most at risk of source-external framing all hold:

- **Thesis and conclusion.** "Within reach", "out of reach", "test design rather than specification precision", "too small and miss the input combinations" are the paper's own words (§1 lines 41-95; §6 lines 822-830).
- **Evaluative words** ("concerning implication for practitioners", "clear logarithmic relationship", "by far the fewest", "only modest gains", "unsurprising", "the core of TestSuiteBench") are all the paper's.
- **Positions section.** All six entries rest on explicit framing in the text: "However" after the within-reach suggestion (§1), "giving the impression of well tested software" (§3.1), "does not explain the low mutation scores" (§3.2), "severely underspecified and thus unsuitable" (§2.1), "which generic rule-based mutations cannot guarantee" (§1), and "two crucial differences" (§4). The rule-based-mutation entry is the weakest (the source states it as a construction difficulty), but the source does name the alternative and say what it cannot do, so it stays.
- **Line 181**, "no citation is given for those patterns", is a true provenance note (tape lines 497-498), not a judgement.
- **All numeric tables** (Table 1, 2, 3, 6; Figure 4 split; Figure 6a legend ρ values; Figure 12 counts) match the tape's values in the tape's order. The Figure 12 counts sum to 12,130, which supports the parse in the notes.
- **Appendix claims** (B.1 limits, B.2 flow formulation, B.3 counts 20 + 14 = 34, App. C containers and harnesses, all six D.1/D.2 prompt summaries, the A.5 hostctl and Skeema examples, the A.6 cmatrix and ast-grep panels) all trace.
- **Notes section.** Coverage line (2,860 lines, 13,308 words, markitdown 0.1.5, 25 pages) matches `wc` and the acquisition manifest at `_planning/staging/chrisgagne-agent-built-software/acquisition/egashira-testsuitebench-2026.json`. The tape's SHA-256 (`6945eed7…bbf`) matches the manifest. The listed source inconsistencies (ρ vs r; Validity Rate vs Validity Score; §2.5 and §2.1 cross-references for §2.6 material; `build.sh` vs `./compile.sh`; test vs repository internet filtering; 82% not restated in the body; doubled specification lines in Figures 7 and 14) are all present in the tape.
- **Coverage (TOC-vs-anchors).** Every section, appendix, prompt, table and figure in the Structure block is anchored in the body. No gap.

## Left open

- **Licence string (CC BY 4.0).** Neither the tape nor the acquisition manifest carries it, and there is no `sources/original/*.source.md` sidecar for this slug. It comes from Pass A's reading of the arXiv listing and could not be checked here.
- **`pdftotext -layout` alignment claims** (lines 133, 169, 246, 333). The original PDF is not available in this leg, so these could not be re-run. The table values the deep reference gives agree with the tape's values in order, so nothing depends on them, but the claim itself is unverified here.
- **PDF SHA-256.** Only the tape hash was checked; the PDF is not present.

## Derived tier

No light reference and no distillation for this slug exists in the corpus, so nothing downstream carries the changed claims. If one is derived later, the two changes above are the ones that touch content: the Table 2 caption is now a `[V]` quotation, and the model-citation entry now describes the DeepSeek reference as a preprint.

## Stamp

Not stamped by this leg, per dispatch. The "Audit pending. No Pass I has run on this reference." line was left as it is for the driver.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `dcbb789ee1829356bc3867e65a2da99f804897138047c46b0fc7a44140811e9e`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `53942e2dc5d323b0fc4e76a3861bf06c988df35c81b4ebb47ea155d530c81cc3`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_egashira-testsuitebench-2026_crossfamily_blind.md`, `_ingest_pass_I_egashira-testsuitebench-2026_crossfamily_sort.md`, `_ingest_pass_I_egashira-testsuitebench-2026_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 7 defects across 6 findings (2 fixed by the fix-in-place audit, 5 missed by it and caught by the blind audit), found 0 over-flagged by the fixer, 4 provenance groups over-flagged by the blind auditor and 0 disputed, and gave the gate as pass once the five remaining edits are applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 2, the blind audit 5, both 0. The Chapman estimate is 17 in all, about 10 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Three remaining edits were applied as written (the mutation-position bullet and the two blockquote line-break restorations), two were applied with changed wording, and none were declined: the Validity Score edits at lines 140 and 337 drop the Abstract as the sort said, and also credit §1 "Our work" (tape 80) and §3.1 (tape 485, 493), which use "validity score" too.

**Gate:** pass. Deep reference sha256 `9ec9babd2d91db9d79740e101b1118f86273b261f2a374795e32224c5fcef83d`, stamp included.
