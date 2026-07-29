# OKF round: four producers, one corpus, traced to source

*Run 28–29 July 2026, entirely on public artifacts — every arm reproduces from this repo.*

**TL;DR.** Four producers of the same 27-source corpus were tested behind identical consumers and judges: the audited grounded-forge app (**D**), its content exported to an OKF bundle (**E**), a deterministic heading-split bundle (**F**), and an un-audited LLM-minted bundle built under Google's own document-ingestion instruction (**G**). Every bundle validates as conformant OKF — the validator never distinguished any of them. Blind preference rankings put the audited arms first, but only by points. The separating instrument was tracing claims to sources: D and E audited clean; F cannot fabricate (it only copies) but misses whole chapters; **G fabricated or contradicted source content in 9.4% of audited notes** — a wrong WACC formula, invented notation, definitions the model's training data overrode against the source's own words — and one invented claim propagated into a cited answer, where the citation audit graded it *supported*. Conformance is a container property; preference is fluency; grounding only shows up when you trace. That tracing is what an ingestion audit is.

## The question

[`okf-interop.md`](../../../architecture/okf-interop.md) claims OKF standardises the *container* while the *producer* discipline — how concept files get made and whether anything checked them against a source — remains the open problem. This round measures that claim: hold the corpus, the consumer, and the judge constant; vary only the producer.

## Arms

| Arm | Producer | Reproduce |
|---|---|---|
| **D** | Compiled app (audited 9-pass pipeline + runtime), consumed via its AGENTS.md contract | `npm run build`, open the app folder |
| **E** | The same audited content emitted as the all-axes OKF bundle, generic consumer prompt | `corpus.commons/demo/okf/matrix/` + [`capture-prompts/okf-consumer.md`](../../harness/capture-prompts/okf-consumer.md) |
| **F** | Deterministic naive bundle: the converted sources heading-split into concept files, no ingestion, no audit | `node docs/evals/harness/build-naive-okf.js` |
| **G** | Un-audited LLM-minted bundle: Google's [`web_ingestion_instruction.md`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/src/reference_agent/prompts/web_ingestion_instruction.md) — the reference implementation's only document pathway — executed verbatim per source by `gpt-5.6-sol` | [`g-exhibits/EXAMPLE-INSTRUCTIONS.md`](g-exhibits/EXAMPLE-INSTRUCTIONS.md) shows the exact per-source instruction |

Two disclosures on G. Run with **no** adaptation, the instruction minted zero references on both pilot sources — every productive pathway presupposes a warehouse concept spine documents don't have (enrich needs existing concepts, the reuse gate needs existing concepts, the mandatory extractions want SQL metrics and join clauses, and "when in doubt, skip" closes the rest). One labelled semantic adaptation — treating the reuse gate as satisfiable by prospective cross-source reuse — made the arm answerable; everything else ran as written, and *Introduction to Business* still minted nothing because its title trips the instruction's meta-page skip-list. Second, a generosity that favours G: the executor could read entire books, where the reference implementation's page-fetch pathway could not.

## Method

Cross-model throughout: **all captures, minting, judging, and audit-tracing by `gpt-5.6-sol`** (via Codex), not a Claude model — capture-model self-preference is constant across arms, and the consumer resembles the GPT-based tooling an OKF adopter is likely to use. Each capture ran in a fresh read-only session in a clean-room copy of its arm, placed outside the repo. Captures were automated rather than operator-manual — a labelled deviation from [`methodology.md`](../../methodology.md). Judges received the rubric ([`default`](../../harness/judge-prompts/default.md) for the diagnostic prompt, [`essay`](../../harness/judge-prompts/essay.md) for the essay) as their entire instruction set, answers shuffled and de-identified, two label permutations per prompt. Fidelity audits were open-book and strict (instructed to grade down on doubt); the grader shares a model family with the producers, a leniency risk applied equally to every arm. Verbatim captures: [`captures/`](captures/). Decoded judge and audit records: [`judge/`](judge/), [`fidelity-audit.json`](fidelity-audit.json).

## Result 1 — conformance distinguishes nothing

All bundles pass `okf validate` (spec v0.2). The audited bundle: 0 errors, 0 warnings. The naive bundle: 0 errors, 1,288 warnings, all 644 concepts unverified. The LLM-minted bundle: **0 errors, 0 warnings** across its 221 `type: Reference` notes. A conformant bundle full of un-audited claims validates exactly as cleanly as an audited one — conformance is a container property.

## Result 2 — traced fidelity separates the producers

Claims traced to their cited files, and minted notes traced to their sources, under the same strict protocol:

| Arm | Layer traced | Unsupported / contradicted |
|---|---|---|
| D | 24 answer-claims vs cited distillations | **0** (18 full support, 6 light over-specification) |
| E | 24 answer-claims vs cited distillations | **0** (18 full, 6 partial) |
| F | 24 answer-claims vs cited chunks | **0** (21 full, 3 partial) — a splitter never rewrites, so it has nothing to fabricate |
| G | **64 minted notes vs their sources** | **6 (9.4%)** — 3 unsupported, 3 contradicted, plus 15 minor drift |

G's errors are checkable exhibits, copied verbatim into [`g-exhibits/`](g-exhibits/): a [WACC formula](g-exhibits/openstax-accounting-vol2/investment_center_performance_measures.md) that applies after-tax treatment to every capital source where the textbook applies it to debt only; [invented `PMT` notation and an annuity formula](g-exhibits/openstax-accounting-vol2/time_value_of_money_conventions.md) the source never gives; a [wealth definition](g-exhibits/openstax-economics-3e/income_distribution_measures.md) that drops the required debt subtraction; and [pre-2020 M1/M2 definitions presented as current](g-exhibits/openstax-economics-3e/money_supply_and_multiplier.md) although the source explicitly states the May 2020 redefinition — the model's training prior overriding the document it was summarising. Errors concentrate in quantitative sources; procedural handbooks barely drift.

**The laundering chain, confirmed end-to-end:** the [balanced-scorecard note](g-exhibits/openstax-accounting-vol2/balanced_scorecard_perspectives.md) invents a requirement absent from its source; the G capture repeats it, citing the note; the answer-level citation audit grades that use *supported*, because the note is the cited authority. Fabricated content in an intermediate layer becomes invisible one hop downstream — a consumer auditing answers against the bundle finds everything in order. Only source-level tracing catches it, which is what a corpus-level audit-of-record exists to be.

## Result 3 — blind preference rankings, and what they cannot see

Eight blind runs (three-way before G existed, four-way after; all decoded in [`judge/`](judge/)):

| Prompt | Runs | Stable outcome |
|---|---|---|
| p01 (diagnostic) | 2 × three-way, 2 × four-way | Audited arms first every time; **G last in both four-way permutations**; F last in both three-way runs; margins 1–6 points of 50 |
| e01 (essay) | 2 × three-way, 2 × four-way | Rank-unstable within 4 points — noise at this n |

Three rubric-blindness results, consistent across runs: the judges scored **G's calibration 9–10** while its bundle carries contradicted formulas; D and E — byte-identical content — were indistinguishable on scores, so the runtime layer's value never reached the rubric (it shows only in trace conduct and evidence-marker survival: D 27 / E 47 / F 0 / G 0 markers on p01); and the audit machinery itself was *penalised* — E's in-band markers read as "unexplained citation codes," D's retrieval trace as "extraneous." A preference rubric measures fluency; it cannot measure grounding.

## Findings

1. **The producer effect is real, and it lives where writing begins.** Copy-only production (F) is grounding-safe but misses whole chapters and connections — the blind rationales name them. LLM production without an audit (G) is fluent, conformant, and wrong at roughly one note in ten. The audited pipeline is clean at every traced layer.
2. **Fabrication launders.** An invented claim in an intermediate artefact acquires a valid citation downstream and passes bundle-level auditing. Grounding must be checked at the source layer, once, at production time — exactly the pre-emptive position an ingestion audit occupies.
3. **Neither the validator nor a preference judge can substitute for tracing.** Conformance passed everything; the rubric ranked a fabricating arm's calibration 9–10.
4. **The container carries audited value faithfully.** E matched D throughout — the distillations survive export into the standard format, so the interchange story holds; the multi-axis bundle even out-breadths a single-axis app (the fair next comparison is an all-axes D).
5. **The reference implementation cannot see a document corpus.** Verbatim, its instruction minted nothing, twice; its own skip-list rejects a textbook by its title. The document-producer side of the OKF ecosystem is unbuilt.

## Caveats

Two prompts; one capture per arm; one judge/grader model, same family as every producer; automated capture; six of 27 sources sampled for G's bundle audit; G's one labelled gate adaptation and one labelled generosity. This corpus — clean, canonical, openly licensed — is the *best* case for naive producers; non-canonical or messily converted corpora are where prior rounds show naive routing degrades further. Treat the rankings as directional and the traced fidelity results — which name specific, checkable errors and gaps — as the more informative artifact.
