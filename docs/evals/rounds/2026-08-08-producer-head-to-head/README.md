# Producer head-to-head: the 9-pass protocol vs the naive OKF reference producer

**TL;DR.** On the fully matched arm, the 9-pass deep references carried 909 atomic claims to the naive producer's 526 — ~1.7× the coverage — at observed hard-error rates of 0.33% vs 0.38%: more coverage with no detected difference in error rate. Both producers ran over the same demo-corpus sources, and both outputs were audited claim-by-claim against those sources, cross-model, with matched judges and matched audit priming. A separate, less-matched arm reached ~3× coverage but does not support an error-rate comparison, and the two results are not merged. A public "more faithful / lower hallucination rate" claim is **not supported and is not made**. The round also delivered the protocol's most consequential fix: an in-context Pass I self-audit certified the producing model's own fabrications as "verified at source," and the same model running the same procedure in a fresh context failed the same file. Fresh-context verification is now mandatory in the protocol, and the corpus-wide independent re-audit followed.

**Date scope.** All audits in this round graded the deep references as they stood on 2026-07-29 to 2026-08-01, *before* the corpus-wide repair. The corpus has since been independently re-audited and repaired; that record, including the same auditor's per-source receipts, is at [`corpus.commons/demo/references/_audit/`](../../../../corpus.commons/demo/references/_audit/). The numbers below describe the pre-repair state.

## Question

Does the 9-pass ingestion protocol produce materially different output from the naive reference-implementation producer — Google's `web_ingestion_instruction.md` executed over the same converted sources — and in what direction: coverage, fidelity, or both?

## Producers compared

- **9-pass deep references** (this repo's protocol; production by Claude Opus, with a replication produced by `gpt-5.6-sol` running Passes A–E to isolate the producer-model effect — eight references re-produced, four entering the producer-model and matched arms). Artefacts: `corpus.commons/demo/references/{slug}-deep.md` (pre-repair state, per git history); all eight Sol-produced replications are at [`arm-d-sol-refs/`](arm-d-sol-refs/).
- **Naive OKF notes** ("G"): Google's document-ingestion instruction executed per source by `gpt-5.6-sol`, with mechanical substitutions and **one disclosed semantic adaptation** (the reuse gate treated as satisfiable by prospective cross-source reuse — run with no adaptation, the instruction minted zero references twice, because every productive pathway presupposes a warehouse concept spine that prose documents lack). Output: 221 conformant `type: Reference` notes across the minting sources, at [`g-bundle/`](g-bundle/). The instruction is preserved verbatim at [`web_ingestion_instruction.md.txt`](web_ingestion_instruction.md.txt) (extension changed only so this repo's link checker skips Google's illustrative example paths; upstream: [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog), Apache-2.0).

## Comparisons and results

Method details, rubric, and locked decisions: [`method.md`](method.md). "Hard" = UNSUPPORTED + CONTRADICTED at claim grain, strict, grade-down-on-doubt. Receipts for every table: [`receipts/`](receipts/). Comparison 4 is the fully matched arm and the only one from which the no-detected-difference claim is drawn; comparisons 1–3 are the controls that show why the unmatched numbers mislead in both directions.

### 1. Cross-family claim grain, 11 sources (each arm judged by the other model family)

| source | G naive (Claude-judged) | 9-pass deep ref (Sol-judged) |
|---|---|---|
| mcdp1-warfighting | 0 / 126 | 11 / 406 · 2.7% |
| liberating-structures | 2 / 283 · 0.7% | 2 / 246 · 0.8% |
| letaw-handbook | 0 / 94 | 2 / 286 · 0.7% |
| business-law | 0 / 191 | 3 / 738 · 0.4% |
| principles-management | 0 / 95 | 9 / 502 · 1.8% |
| organizational-behavior | 0 / 90 | 8 / 447 · 1.8% |
| principles-marketing | 0 / 124 | 4 / 354 · 1.1% |
| economics-3e | 0 / 139 | 19 / 593 · 3.2% |
| accounting-vol1 | 0 / 128 | 12 / 512 · 2.3% |
| accounting-vol2 | 1 / 232 · 0.4% | 5 / 237 · 2.1% |
| principles-finance | 1 / 167 · 0.6% | 6 / 600 · 1.0% |
| **TOTAL** | **4 / 1,669 · 0.24%** | **81 / 4,921 · 1.65%** |

The 9-pass tier extracts ~3× the claims per source. Read alone, this table also suggests a fidelity penalty — the next two comparisons show that reading does not survive scrutiny.

### 2. Same-judge control (Sol judges both producers, 5 sources)

Sol-on-G 5 / 1,041 (0.48%) vs Sol-on-9-pass 54 / 2,751 (1.96%): the gap survives removing the judge-family confound, so it is a real difference between these *instances* — but comparison 3 shows it tracks the producer model, not the protocol.

### 3. Producer-model effect (same judge, same audit priming)

Sol re-produced four deep references running Passes A–E. Claude-judged, matched priming:

| producer | hard / claims |
|---|---|
| Opus full 9-pass (3-source subtotal) | 13 / 494 · 2.6% |
| Sol A–E, no Pass I (3-source subtotal) | 3 / 523 · 0.57% |

Comparable coverage, ~4.5× fewer hard errors — with Sol *lacking* the Pass I cleanup Opus had. The hard-error rate is dominated by the producer model (enumeration miscounts and attribution leakage are Opus-specific tics; both models leak attributions at some rate), not by naive-vs-protocol.

### 4. The fully matched arm (same producer family, same judge, same primed audit)

Re-auditing the naive notes with the identical primed hunt-list used on the deep references:

| arm | hard / claims |
|---|---|
| Naive G, primed audit (4 sources) | 2 / 526 · 0.38% |
| Sol A–E deep refs, primed audit (4 sources) | 3 / 909 · 0.33% |

**No detected difference in hard-error rate, at ~1.7× the coverage.** The production passes add coverage at no measured cost in error rate. The earlier apparent penalty was two stacked evaluation asymmetries (leakier producer + harsher judge on one side; unprimed audit on the other). All five hard errors trace to the same producer model: the naive notes' two were dated M1/M2 definitions presented as current; the deep references' three were two unsupported attributions (Kuznets and Krugman) and an SEC-responsibilities miscount. Five hard errors across four sources is too few for an equivalence test; the claim is no detected difference, not equality of error rates.

### 5. Fresh-context vs in-context Pass I (the finding that mattered most)

On the same economics deep reference:

- **In-context Pass I** (the shipped self-audit): `✅ Akerlof lemons problem — verified at source Ch 16.1` (the name occurs zero times in ~58K lines of converted source); `Training-data leakage: none found`; verdict PASS.
- **Fresh-context Pass I, same model, same procedure**: flags Akerlof, Phelps, Lucas, Sargent, Perez, and Follett as leakage; verdict FAIL.
- Sol's fresh audit of its own A–E refs likewise caught its own leaks (Kuznets, Krugman).

**The causal variable is fresh-context vs same-context, not the model.** Fresh-context audits caught self-produced leakage in both model families; the paired in-context control (run on the Claude arm) certified the same leakage as verified. This retired the 99.4% self-audit figure and made fresh-context Pass I (different model preferred) mandatory in the protocol; the corpus-wide independent re-audit and repair followed on 2026-08-08.

## Bottom line

- On the fully matched arm, the 9-pass tier produced **~1.7× the claims with no detected difference in hard-error rate** — tiered, marked, source-traceable claims whose errors an audit can find and fix. A separate, less-matched arm produced ~3× the claims but does not support an error-rate comparison; the two results are not merged.
- A "more faithful / lower hallucination rate" claim is **not supported** by this round and is not made.
- The hard-error rate of a shipped reference is dominated by the **producer model**, not by the protocol; the protocol's audit pass only works when it runs in a **fresh context**.
- Trust the direction, not the decimal: judge variance at strict claim grain is large (up to ~4× between judge families on identical artefacts).

## Caveats

One generation per source per arm; four-source denominators on the matched arm; grader families overlap producer families except where stated; the naive producer ran with one disclosed gate adaptation and could read whole books where Google's page-fetch pathway could not (a generosity to the naive arm). The audited deep references are the pre-repair state; the shipped corpus has since been repaired against the independent re-audit.

## Licences

The `g-bundle/` notes and `arm-d-sol-refs/` references are derived from the demo corpus's sources and inherit their per-source licences (OpenStax volumes CC BY 4.0; the Liberating Structures handbook CC BY-NC-SA 3.0, so its derived notes inherit NC; MCDP 1 public domain; per-source terms in [`LICENSE-CONTENT`](../../../../LICENSE-CONTENT)). Google's ingestion instruction is Apache-2.0, © Google LLC, reproduced verbatim for reproducibility.
