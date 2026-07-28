# OKF round, 2026-07-28: audited bundle vs naive bundle vs app

The first published round of the comparative eval, and the first to run entirely on public artifacts — every arm reproduces from this repo. It tests the claim in [`okf-interop.md`](../../../architecture/okf-interop.md): OKF standardises the *container*; the *producer* discipline is what separates two conformant bundles.

## Arms

| Arm | What it is | Reproduce |
|---|---|---|
| **D** | Compiled app (`apps/decision` for p01, `apps/stakeholder` for e01), consumed via its AGENTS.md operating contract | `npm run build`, open the app folder |
| **E** | The emitted all-axes OKF bundle, generic consumer prompt | `corpus.commons/demo/okf/matrix/` + [`capture-prompts/okf-consumer.md`](../../harness/capture-prompts/okf-consumer.md) |
| **F** | Naive flat-OKF baseline: the same converted sources heading-split into concept files, no ingestion protocol, no audit | `node docs/evals/harness/build-naive-okf.js` |

Both E's and F's bundles pass `okf validate` (spec v0.2). The audited bundle validates at 0 errors / 0 warnings; the naive one at 0 errors / 1,288 warnings with all 644 concepts unverified. **Conformance is a container property.** The question this round asks is whether a blind judge can tell them apart by their answers.

## Method, and deliberate deviations from the standing protocol

Cross-model round: **all captures and all judging by OpenAI's `gpt-5.6-sol`** (via Codex), not by a Claude model — so any capture-model self-preference is constant across arms, and the consumer resembles the GPT-based tooling an OKF adopter is likely to point at a bundle. Each capture was a fresh, read-only session in a clean-room copy of its arm, placed outside the repo so a naive session could not reach the audited corpus. Captures were automated rather than operator-manual (a deviation from [`methodology.md`](../../methodology.md), labelled here). The judge received the rubric ([`default`](../../harness/judge-prompts/default.md) for p01, [`essay`](../../harness/judge-prompts/essay.md) for e01) as its entire system instructions, with answers shuffled and de-identified; two permutations per prompt as a rank-stability check. Decoded judge output is in [`judge/`](judge/), verbatim captures in [`captures/`](captures/).

## Results

| Run | Rubric | Ranking | Totals D / E / F (of 50) |
|---|---|---|---|
| p01 perm 1 | default | **D > E > F** | 48 / 44 / 42 |
| p01 perm 2 | default | **E > D > F** | 46 / 47 / 45 |
| e01 perm 1 | essay | **D > E > F** | 48 / 47 / 45 |
| e01 perm 2 | essay | **E > D > F** | 47 / 47 / 45 |

Evidence-marker survival (mechanical count, no judge): p01 — D 27, E 47, F 0; e01 — D 0 (its trace declares prose attribution for the essay register), E 11, F 0. F's zero is structural: the naive bundle carries no markers to preserve.

## Findings (directional — two prompts, one capture per arm)

1. **The producer effect is real and consistent: F ranked last in all four blind runs.** The margin is modest — a strong model over naive chunks writes fluent, file-grounded prose — but the judge's blind rationales name the gaps the naive bundle created: on e01 the consumer never found the organisational-behaviour conflict chapter inside the heading-chunks and answered entirely from practice cards (no conflict modes, no power analysis, no negotiation theory); on p01, thin vendor-contract and lock-in coverage and a "near-binary, insufficiently calibrated" decision rule. F carries no in-band audit trail of its own — no evidence markers, no verbatim register; the addendum below reports what an external citation audit found.
2. **The runtime layer is invisible to this rubric.** D and E carry byte-identical distillations and split 2–2 across permutations — within 4 points in the widest run (p01 perm 1) and within 1 point in the other three, including one run where their totals tied at 47 and the judge's stated ranking is its qualitative call, recorded as returned. What the runtime added shows up only in conduct the rubric doesn't score: the retrieval trace, and the source-boundary paragraph distinguishing borrowed-through findings from corpus-held evidence — which one judge run praised in exactly those terms.
3. **The multi-axis bundle out-breadths a single-axis app.** E repeatedly earned credit for cross-axis pulls (software-engineering economics and business-law material on a decision prompt) that the single-axis app could not make. The fair next comparison is an all-axes D.
4. **A new judge-limit shape:** one run penalised the in-band evidence markers as "unexplained citation codes" that "impede readability." The audit discipline costs rubric points with a judge that was not told what the markers mean — input for the planned rubric rework (an audit-trace fidelity score would measure what this rubric punishes).
5. The dual-runtime port held: a non-Claude agent followed `answer-from-corpus` as a written procedure via AGENTS.md, unprompted, producing conformant traces.

## Addendum, same day: audit-trace fidelity

The ranking round measures preference; this addendum measures grounding. For each capture, a fresh read-only session in the arm's clean room extracted every citation-bearing claim, sampled 12 evenly spaced, resolved each cited source to its file, and graded strictly (instructed to grade down when in doubt). The grader is the same model family as the capture agent — a leniency risk, applied equally across arms. Decoded results: [`fidelity-audit.json`](fidelity-audit.json).

| Arm | Full support | Partial | Unsupported / contradicted / file-not-found |
|---|---|---|---|
| D | 18/24 | 6 | 0 |
| E | 18/24 | 6 | 0 |
| F | **21/24** | 3 | 0 |

Zero fabrication in any arm — and F graded marginally cleanest on strict attribution. The mechanism is legible: F cites raw source chunks and restates them at low altitude, so support is trivial to verify; D and E cite distillations while making more synthesised claims, and their PARTIALs are light over-specification (a qualifier or location the cited file does not state), not error. A deterministic splitter never rewrites the source, so it has nothing to fabricate.

This bounds the round's headline, and the bound matters: on clean, canonical, openly licensed sources consumed by a strong model, the naive path's measured deficit is coverage and synthesis (finding 1), not truthfulness. Two limits keep the bound honest. This corpus is the naive path's best case — non-canonical or messily converted corpora are where naive chunking degrades, per the harness's earlier findings. And fabrication risk enters when a producer *writes* new prose rather than splitting it: the un-audited LLM wiki-fication path (F+) is the arm where the ingestion audit itself would be the isolated variable, and it has not yet been run.

## Caveats

Two prompts, one capture per arm, one judge model, automated capture. F is a deterministic floor; the fairness upgrade (F+: one-shot LLM wiki-fication of the same sources, still un-audited) has not been run. Treat the ranking as directional and the blind rationales — which name *specific, checkable* coverage gaps — as the more informative artifact.
