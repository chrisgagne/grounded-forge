## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md` and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`, lines 1–626.
- `tape.md`, lines 1–2,060, including every quiz, bibliography entry and licence provision.
- The repository’s `CLAUDE.md` and its nine required architecture documents.

Also inspected the complete diff between `frozen-deep.md` and `post-audit-deep.md`, the evidence-marker taxonomy and statistics template in `9-pass-protocol.md`, and the supplied post-audit hash.

Verified hashes:

```text
frozen-deep.md:
12ae9c71876f9d4e8f1fd0c8433ea4eafe45a635399560c98d73963422f236ab

post-audit-deep.md:
7fce3c2d99e0f03dacdf3570968b05cf1a40a9b7bd24bc586b1a7783174417de
```

The tape contains 2,060 lines and 36,749 whitespace-delimited words. Running `check-verbatim.py` against the post-audit reference with `--source tape.md --no-corpus-search` returned **no findings; 33 numerical claims unchecked**. That result does not settle the manually identified statistics-table defects.

No original `source.*`, acquisition manifest, producer receipt or image binaries were supplied in this folder. I did not use external sources to resolve what the pinned tape says.

No files were edited. This response is the report; the filesystem is read-only.

## 2. Sorted ledger

Identifiers **F1–F5** refer to the fixer’s numbered changes; **B1–B16** refer to the blind findings. All deep-reference line numbers below refer to `post-audit-deep.md`.

### Confirmed and fixed

| Finding | Raised by | Deep line | Tape lines | Determination |
|---|---|---:|---|---|
| F1: chapter-order summary marked `[AR]` | Fixer | 51 | 143–174; 1886–1897 | The sentence enumerates the guide’s organisation and method rather than reporting a claim–warrant–conclusion structure. `[AP]` correctly classifies this paraphrase. |
| F3: publisher described as another OpenSSF project | Fixer | 208 | 692 | The original “both are OpenSSF projects, as is the guide’s publisher” misstates the relationship. The replacement correctly identifies the tools as OpenSSF projects and OpenSSF as the producer of the guide. |
| F4: AI-written reports said to lack deployment context | Fixer | 400 | 1557 | The original substitutes an assertion about report contents for the source’s explanation about missing inputs to the AI. The replacement correctly restores that explanation. |
| F5: quoted “don’t report” lacks `[V]` | Fixer | 579 | 1195 | The words occur in the guide. Adding `[V]` correctly marks the quotation. The surrounding `[BT]` remains appropriate for the sentence’s account of Yan’s claim. |

### Confirmed, fix wrong or incomplete

| Finding | Raised by | Deep line | Tape lines | Determination |
|---|---|---:|---|---|
| F2: two-kind separation taxonomy attributed to the author | Fixer | 51 | 1163–1168; 1331–1333; 1730–1736; 929–933; 980–989; 1555; 1519–1527 | The individual practices trace, but the guide does not organise them into these two kinds. Acknowledging “this reference’s grouping” improves transparency but does not make that grouping an author paraphrase eligible for `[AP]`. Replace the organising frame with direct summaries of the source’s practices. |

This is an incomplete repair of an existing defect, rather than a separate defect introduced by the edit.

### Missed by the fix-in-place audit

| Finding | Raised by | Deep line | Tape lines | Determination |
|---|---|---:|---|---|
| B1: five claims instead of four | Blind | 75 | 94–102 | Confirmed. Both the source list and the reference’s enumeration contain four claims. |
| B2: functionality qualifier omitted | Blind | 367 | 1457 | Confirmed. The source qualifies maintaining functionality with “where practical”. |
| B4: model-lag comparison broadened | Blind | 536 | 290 | Confirmed. The comparison concerns the **most advanced** models in both groups. |
| B5: CI-time recommendation loses its setting | Blind | 551 | 1088 | Confirmed. The source specifies most projects and acknowledges difficulties for operational technology and physical-device software. Body line 269 does not supply those qualifications inside this independently readable row. |
| B6: severity thresholds lose adaptation instruction | Blind | 559 | 1375–1379 | Confirmed. The quoted thresholds are system-dependent suggestions; the row omits “Adjust the thresholds to your system.” |
| B7: package-hallucination averages and cohort date omitted | Blind | 564 | 1504 | Confirmed. The figures are averages for models available in 2024. Both qualifiers matter alongside the newer-model replication. |
| B8: zero-observation finding loses boundary and caveat | Blind | 566 | 1506 | Confirmed. The finding concerns imports for everyday tasks with mainstream libraries. The source expressly denies that the sample establishes a zero rate and reports nonexistent imports under different prompts. |
| B10a: OSS-CRS numerical wording changed under `[V]` | Blind | 546 | 756 | Confirmed. “25 … 16” preserves the quantities but does not reproduce “twenty-five … sixteen” character-exact. Restore the source’s wording. |
| B10b: reviewer-count wording changed under `[V]` | Blind | 557 | 1337 | Confirmed. “10 reviewers” is a paraphrase of “ten dedicated [AI] reviewers”. Use `[AP]` for this compressed row. The tape also contains the row’s other figures. |
| B11: availability citation assigned capability/process role | Blind | 579 | 267; 68–76; 490–499; 579–586 | Confirmed. The collective description incorrectly encompasses the export-control citation. It supports interruption of availability, not discovery capability or process advice. |
| B12: Capoot connection lacks its section locator | Blind | 595 | 260–267 | Confirmed. Capoot occurs under “External versus local models”, absent from the supplied locator list. |

### Over-flagged

**None.** Findings involving genuine uncertainty are classified below as disputed rather than declared false positives.

### Disputed

| Finding | Raised by | Deep line | Tape lines | Both readings and disposition |
|---|---|---:|---|---|
| B3: deletion failure mode silently resolves ambiguous wording | Blind | 367 | 1461 | **Blind reading:** “fail … to silence the crash by deleting” does not assert that deleting functionality is the attempted bad repair described by the reference. **Alternative:** the paragraph discusses symptom-only repairs and functional breaks; deletion is plausibly another failure mode, awkwardly expressed. The tape does not decisively resolve this. Remove the deletion-specific paraphrase and record the ambiguity without choosing either reading. |
| B9 / fixer’s “Left open”: MDASH count assigned the wrong key | Both | 543; corroborating body treatment at 202 | 638–643 | **Blind reading:** Bishop supports the first sentence; Kim’s closing citation supports the subsequent count, quotation and stages. **Fixer reading:** the count sits between those citations within one continuous bullet, so its precise attribution is ambiguous. The tape supports the count but cannot establish exclusive attribution. Use both keys rather than replacing Bishop with Kim alone. |
| B13: acquisition identity lacks supplied records | Blind | 5, 7 | 1; 3–9; 35 | **Blind reading:** the packet cannot independently substantiate the URL, repository commit/date or acquisition-record assertions. **Alternative:** acquisition metadata may legitimately come from records outside the source and need not appear in the tape. No evidence establishes that these details are false. Label the acquisition identity as recorded but independently unverified, and use the tape’s own `gen-html` comment for the structural assertion. |
| B14: local image availability unverified | Blind | 20, 623 | 118; 130; 1404; 1786, and the other image links | **Blind reading:** the asserted local directory and binaries were not supplied. **Alternative:** the directory may exist in the originating corpus outside this packet. The figure descriptions themselves trace to alt text and prose. Remove the unsupported availability assertion without changing those descriptions. |
| B15: conversion fidelity and manifest completeness unverified | Blind | 619 | 1; 5; 2049–2060 | **Blind reading:** byte fidelity, conversion operations, original word count and manifest completeness cannot be checked here. **Alternative:** these are legitimate acquisition-record claims if the manifest exists. The tape verifies its own path marker, counts and licence ending, but cannot adjudicate the remaining assertions. Replace the unqualified provenance claims with verified packet facts and an explicit limitation. |
| B16: producer’s full-read claim lacks receipt | Blind | 620 | No supporting passage in tape 1–2060 | **Blind reading:** the producer’s actions cannot be verified without the receipt. **Alternative:** a producer receipt is procedural evidence outside the source, and its absence from this packet does not demonstrate incomplete reading. Attribute the claim to the frozen reference and label it unverified. |

### Did the fixer introduce a new defect?

**No separate new defect confirmed.** The edits at lines 208 and 400 restore the tape’s meaning; the marker changes at lines 51 and 579 are appropriate. F2 remains defective for the reason already identified by the fixer.

The unchanged “Audit pending” statement at line 626 follows the dispatch instruction that stamping occurs after all legs finish; it is not a newly introduced source defect.

## 3. Remaining edits

Apply the following literal replacements in `post-audit-deep.md`. Line numbers identify the present file. Edits 4, 10 and 15–20 resolve disputed passages conservatively; they do not assert that unavailable records or underlying publications are wrong.

1. **Line 51 — replace the separation-grouping passage.**

   Current text, from:

   > Two kinds of separation recur across these chapters; the pairing is this reference's grouping of points the guide makes section by section [AP].

   through:

   > The other keeps the rules that must hold outside the AI: a sandbox rather than text instructions, a human gate the AI cannot bypass, invariants enforced by hooks, approval enforced in the tool or workflow, and deterministic checks rather than reruns of AI (Finding.md, § "Preparing the sandbox" › "Need for sandboxes"; § "Establish a human gate and kill switch"; § "Reporting to externally maintained projects"; § "Turn findings into durable checks").

   Replacement:

   > The guide recommends separating identifying findings from validating them, using an independent verifier, and separating analysis from action when reviewing untrusted proposed changes [AP] (Finding.md, § "Separate identifying findings from validation"; § "Validate findings" › "Tips for validation"; § "Evaluate merge/pull requests"). It also recommends sandboxing rather than relying on text instructions alone, enforcing human gates and invariants outside the AI, enforcing required approval in the tool or workflow, and turning findings into deterministic checks rather than depending on repeated AI analysis [AP] (Finding.md, § "Preparing the sandbox" › "Need for sandboxes"; § "Establish a human gate and kill switch"; § "Reporting to externally maintained projects"; § "Turn findings into durable checks").

2. **Line 75 — correct the count.**

   Current:

   > The guide’s five claims:

   Replacement, preserving the file’s apostrophe style:

   > The guide's four claims:

3. **Line 367 — restore the functionality qualification.**

   Current:

   > maintain existing functionality and insert no new vulnerabilities

   Replacement:

   > maintain existing functionality where practical and insert no new vulnerabilities

4. **Line 367 — avoid resolving the ambiguous deletion sentence.**

   Current:

   > Identifying and fixing the true cause without breaking functionality is vital [AP]; PatchBench found the most common failure was the AI guarding the *symptom* with incomplete local checks, and also reported failures to localise the vulnerability, silencing a crash by deleting the offending operation or even the whole functionality, and broader conditions that reject benign as well as invalid input [BT] [Shen2026-09].

   Replacement:

   > Identifying and fixing the true cause without breaking functionality is vital [AP]. The guide reports that PatchBench found the most common failure was guarding the *symptom* with incomplete local checks; it also reports failures to localise the vulnerability and broader conditions that reject benign as well as invalid input [BT] [Shen2026-09]. The source's intervening sentence about deleting an operation or functionality is ambiguous, so this reference does not resolve its meaning.

5. **Line 536 — narrow the model comparison.**

   Current metric:

   > Lag of open-weight behind closed-weight models

   Replacement:

   > Lag of the most advanced open-weight models behind the most advanced closed-weight models

6. **Line 551 — retain the CI recommendation’s setting.**

   Current metric:

   > Target CI time

   Replacement:

   > Suggested CI time for most projects; operational technology and physical-device software may find this difficult

7. **Line 559 — restore the adaptation instruction.**

   Current final portion of the value cell:

   > "Three or more, or local-only, is low"

   Replacement:

   > "Three or more, or local-only, is low"; "Adjust the thresholds to your system."

8. **Line 564 — replace the package-hallucination row.**

   Current:

   ```markdown
   | Package hallucination (USENIX Security 25) | 576,000 samples, 16 LLMs; at least 5.2% commercial, 21.7% open-source | [V] [BT] [Spracklen2025] (Finding.md, § "Have humans review the fix") |
   ```

   Replacement:

   ```markdown
   | Package hallucination (USENIX Security 25), models available in 2024 | 576,000 code samples, 16 LLMs; "the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models" | [V] [BT] [Spracklen2025] (Finding.md, § "Have humans review the fix") |
   ```

9. **Line 566 — replace the bounded zero-observation row.**

   Current:

   ```markdown
   | Package hallucination, everyday tasks (arXiv, no venue listed) | none in 1,134 short Python snippets from six models | [V] [BT] [Hillah2026] (Finding.md, § "Have humans review the fix") |
   ```

   Replacement:

   ```markdown
   | Package hallucination, everyday tasks using mainstream libraries (arXiv, no venue listed) | No hallucinated package names observed in imports from 1,134 short Python snippets generated by six models; the samples were too small to establish a zero rate. Every model imported nonexistent packages when prompted for niche or nonexistent libraries. | [AP] [BT] [Hillah2026] (Finding.md, § "Have humans review the fix") |
   ```

10. **Line 543 — retain both possible MDASH attribution keys.**

    Current:

    > [V] [BT] [Bishop2026]

    Replacement, in this row only:

    > [V] [BT] [Bishop2026] [Kim2026]

11. **Line 546 — restore numerical wording.**

    Current value:

    > 25 vulnerabilities across 16 projects

    Replacement:

    > "twenty-five vulnerabilities across sixteen projects"

12. **Line 557 — classify the compressed row as paraphrase.**

    Current value opening:

    > 10 reviewers endorsed a non-existent oracle

    Replacement:

    > ten dedicated AI reviewers endorsed a non-existent oracle

    In this row, also replace `[V] [BT]` with `[AP] [BT]`. Retain the other figures, key and locator.

13. **Line 579 — distinguish citation roles.**

    Current:

    > cited approvingly as evidence of AI capability (finding, chaining, reverse engineering, N-day exploits) and, in [Yan2026]'s case, as the most frequent source of process advice across threat models, sandboxing, discovery, deduplication, validation, triage and fixing.

    Replacement:

    > used for accounts of AI capability (finding, chaining, reverse engineering, N-day exploits), process advice, and model/service access. The capability reports are cited approvingly; [Yan2026] is the most frequent source of process advice across threat models, sandboxing, discovery, deduplication, validation, triage and fixing. [Anthropic2026-06-12-Export-Control] is cited separately for interruption of external model availability (Finding.md, § "External versus local models").

14. **Line 595 — add Capoot’s locator.**

    Current citation parenthesis:

    > (Finding.md, § "Need for sandboxes"; § "Evaluate merge/pull requests")

    Replacement:

    > (Finding.md, § "Need for sandboxes"; § "Evaluate merge/pull requests"; § "External versus local models")

15. **Line 5 — qualify acquisition identity.**

    Current:

    > URL: https://best.openssf.org/Finding-and-Fixing-Vulnerabilities-Using-AI/ ; source file docs/Finding-and-Fixing-Vulnerabilities-Using-AI/Finding.md in https://github.com/ossf/wg-best-practices-os-developers at commit 82590814cc174d8707cc805462cb53488d2d7f92 (2026-10-05). The guide is actively edited; this reference describes that commit.

    Replacement:

    > Acquisition metadata recorded in the frozen reference: URL https://best.openssf.org/Finding-and-Fixing-Vulnerabilities-Using-AI/ ; repository https://github.com/ossf/wg-best-practices-os-developers ; commit 82590814cc174d8707cc805462cb53488d2d7f92 (2026-10-05). The supporting acquisition record was not supplied for this audit, so that acquisition identity remains independently unverified. This reference describes the supplied tape, whose file marker identifies docs/Finding-and-Fixing-Vulnerabilities-Using-AI/Finding.md.

16. **Line 7 — ground the structural parenthesis in the tape.**

    Current:

    > (per the acquisition record, the site's HTML pages are generated from it)

    Replacement:

    > (the tape comments that each chapter is intentionally its own H1 and refers to `gen-html`)

17. **Line 20 — remove the unverified local-image availability assertion.**

    Current:

    > The image files are at `sources/converted/openssf-finding-fixing-vulnerabilities-ai-images/`.

    Replacement:

    > The tape contains relative image links and alt text; image binaries were not supplied for this audit.

18. **Line 623 — remove the second availability assertion.**

    Current:

    > The image files sit in `sources/converted/openssf-finding-fixing-vulnerabilities-ai-images/` for the orchestrator's inspection; this reference describes them only through alt text and surrounding prose.

    Replacement:

    > Image binaries were not supplied for this audit; this reference describes the figures only through the tape's alt text and surrounding prose.

19. **Line 619 — replace the conversion-provenance note.**

    Current: the entire bullet beginning:

    > - **Source and conversion.** Per the acquisition manifest, …

    Replacement:

    > - **Source and conversion.** The supplied tape identifies one file, `docs/Finding-and-Fixing-Vulnerabilities-Using-AI/Finding.md`, and contains 2,060 lines and 36,749 whitespace-delimited words. Its final section is the licence. The tape comments that each chapter is intentionally its own H1 and refers to `gen-html`. The acquisition manifest and original repository file were not supplied for this audit, so the pinned-commit identity, conversion operations, byte fidelity, original word count and manifest completeness declaration remain independently unverified. All ten divisions enumerated in this reference are represented in the supplied tape.

20. **Line 620 — qualify the producer-read claim.**

    Current:

    > - **Read coverage.** The producing session read every line of the tape (1–2,060) in bounded ranges before writing, including all 46 quiz blocks, the bibliography and the licence. Ranges are recorded in the producer receipt.

    Replacement:

    > - **Producer read coverage.** The frozen reference states that its producing session read every tape line (1–2,060), including all 46 quiz blocks, the bibliography and the licence, and recorded the ranges in a producer receipt. That receipt was not supplied for this audit; the producer's read coverage remains independently unverified.

## 4. Counts

Counts use distinct defects in distinct claims. B10 contributes two defects. Multiple missing qualifiers within one statistics claim count together.

| Classification | Count |
|---|---:|
| Confirmed defects, total | 16 |
| Confirmed and correctly fixed | 4 |
| Confirmed, fixer repair incomplete | 1 |
| Missed by fixer and still defective | 11 |
| Over-flagged by fixer | 0 |
| Over-flagged by blind auditor | 0 |
| Disputed, distinct finding groups | 6 |
| New defects introduced by fixer | 0 |

The six disputed groups are B3, the shared MDASH attribution finding, and B13–B16. Disputed findings are excluded from capture counts. The conservative replacements above do not convert those disputes into confirmed defects.

Capture: fixer=5 blind=11 both=0

## 5. Gate verdict once the remaining edits are applied

**Pass for fidelity to the supplied tape, after all 20 edits are applied and checked.**

The replacements repair all confirmed outstanding defects, avoid choosing unsupported readings of the ambiguous passages, and explicitly qualify unavailable provenance evidence. All ten source divisions have anchor coverage; no missing-chapter failure was found.

This verdict does **not** certify the pinned repository identity, original-to-tape conversion fidelity, local image availability or producer receipt. Those remain explicitly unverified. The current file still requires the listed edits; the subsequent driver must complete its normal recheck and stamping steps before shipping.