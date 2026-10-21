
# Kalai et al., Why Language Models Hallucinate, Warranting Agent-Built Software Distillation

**Source:** Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala and Edwin Zhang, "Why Language Models Hallucinate", arXiv:2509.04664v1, 4 September 2025, 36 pages. Licence: CC BY 4.0. Scope: open.

**Applicability gate (Pass G.0): clear yes.** (1) The source answers practitioner questions this axis asks directly: which claims about a build were shown and which only asserted (a model's fluent, specific answer is the kind of output that scoring rewards whether or not it is right), whether a run of passes is evidence (a pass-rate score that gives no credit for abstaining rewards guessing), and how the harness itself is checked (model graders can pass wrong answers; calibration error alone does not show how often a system is wrong). (2) Its concepts land in all eight phases, most heavily in Phases 5 to 7. (3) Its contrarian position, that hallucination persists because most evaluations reward guessing over abstaining, is the axis's first reflex ("the agent says it's done") explained from the model side: an agent trained and scored on pass or fail has every reason to report an answer rather than *not verified*.

**Phase mapping.** Primary: Phase 5, Gating deterministically (binary grading; model graders; a gate that scores *blocked* as *failed*); Phase 6, Reviewing independently (reviewer agents as graders; choosing the model behind an agent on a pass-rate score); Phase 7, Warranting the change (confident output is not a demonstration; what an LLM feature's warranty can promise). Secondary: Phase 1, Specifying the change (latent context; a confidence target and a permitted *not verified* outcome in the agent's instructions); Phase 4, Building in the sandbox (arbitrary facts the agent cannot infer; empty lookups; character-level reasoning). Supporting: Phase 2, Triaging risk (a change that adds an LLM call or retrieval; the error factors the change leans on); Phase 3, Locking the tests (tests for an LLM feature that expect abstention); Phase 8, Releasing and operating (production metrics for an LLM feature). Phase 2 and Phase 8 rows are narrow: the source sorts no change by auth, personal data, money or infrastructure, and it tracks nothing after deployment; its rows there apply only to changes that ship a language-model feature.

**Transfer caveat.** The paper is about language models answering prompts and about the benchmarks that score them. It does not study coding agents, harnesses or software delivery; its one coding link is that it classes SWE-bench's scoring as binary, with no credit for an uncertainty response (§4.1, Table 2; Appendix F.3) [AP]. Its formal results are lower bounds for base models under stated assumptions, and its post-training account documents an incentive, not a measured effect on any named deployed model (§12 of the deep reference, "Model boundary" and "Causal boundary"). Where this distillation carries a finding to an agent, a gate or a reviewer, it says the step is its own inference.

## Warranting Agent-Built Software Relevance

This source supplies the corpus's account of why a model's confident answer is no evidence of a correct one. The authors define hallucination as a plausible falsehood (Source: Kalai et al., Why Language Models Hallucinate, §1, "Introduction") [AP], show that a model trained in the standard way will produce some under stated assumptions (§3.1, "Hallucinations are inevitable only for base models") [AR], and argue that post-training keeps them because most influential evaluations score an answer one or zero and give an abstention nothing, so guessing always scores at least as well as saying *I don't know* (§1.2, "Why hallucinations survive post-training"; §4.1, "How evaluations reinforce hallucination") [AR]. A builder whose warranty rests on agents' reports inherits that incentive: an agent's *done* is an answer produced under scoring that never paid it to say *not verified*. That is this distillation's inference from the paper's account; the paper did not test agents.

The source is just as useful for how to score instead. It proposes stating a confidence target in the instructions, with a wrong answer costing more than an abstention, so that answering pays only above the target (§4.2, "Explicit confidence targets") [AP]; it warns that a small number of special hallucination checks cannot offset a larger set of pass-rate scores (§4.1) [AR]; that language-model judges can mark incorrect long answers as correct (Appendix F) [AP]; that calibration error alone does not show how often a system is wrong (Appendix F.3) [AR]; and that search and retrieval reduce hallucination without removing the incentive to guess (§5, "Search (and reasoning) are not panaceas") [AP]. For the harness, those are rules for the gates, the reviewer agents and any LLM feature the change ships.

## Key Concepts for Warranting Agent-Built Software

1.  **Hallucination is a plausible falsehood.** The paper uses *hallucination* for a plausible falsehood a language model generates, as distinct from nonsense; it is an important special case of generation error, not the whole category (Source: Kalai et al., Why Language Models Hallucinate, §1, "Introduction"; §3.1, "Hallucination errors") [AP]. Intrinsic hallucinations contradict the prompt (miscounting the letters in a word); extrinsic ones contradict the training data or external reality (§1) [AP]. For the harness, the danger is in *plausible*: the false output looks like a right one.

2.  **Generating is at least as hard as recognising.** Producing a valid response implicitly requires telling valid candidates from plausible errors; the authors formalise this by using any base model as a classifier for the Is-It-Valid problem and lower-bounding its generation error by about twice that classifier's error, plus correction terms (Source: Kalai et al., Why Language Models Hallucinate, §1.1, "Errors caused by pretraining"; §3.1, Corollary 1; §3.2, Theorem 1) [AP]. The bound says something useful only when the correction terms are small (§3.1; §3.2) [AR].

3.  **Inevitable only for base models; a verified set or IDK.** The paper's heading is exact: "Hallucinations are inevitable *only for base models*." [V] (§3.1). A model that never hallucinates could be built from a question-answer database and a calculator that answers a fixed set of questions and well-formed calculations and otherwise outputs IDK; the lower bound says that models which do not err must not be calibrated, and calibration, hence error, follows naturally from the standard training objective (§3.1, "Hallucinations are inevitable only for base models") [AR]. The formal bounds do not prove that every possible AI system must hallucinate (deep reference §12, "Model boundary").

4.  **Arbitrary facts.** An arbitrary fact has no succinct pattern from which the right answer can be inferred, such as a person's birthday; in the authors' stylised model, error is lower-bounded by roughly the singleton rate, the share of facts seen exactly once in training (Source: Kalai et al., Why Language Models Hallucinate, §3.3.1, Definitions 1–2, Theorem 2) [AP]. Asked for one author's birthday only if it knew, a model gave three different wrong dates in three attempts (§1; footnote 1) [AP].

5.  **Poor models: a limit of representation, not a missing fact.** Error also comes from a model family that cannot represent the target, or one fitted poorly (§3.3.2, "Poor models") [AP]. The authors read a model's miscounting of the letters in a word as a representational limit: the word is split into multi-letter tokens, and a reasoning model that worked character by character counted it reliably (§3.3.2) [AR].

6.  **Other error sources: hardness, shift, bad training data.** Errors "may occur due to a combination of multiple factors" [V] (§3.4, "Additional factors"). The paper names computational hardness (a task no efficient system can do better than chance on, in a stylised construction), distribution shift (a prompt unlike the training prompts), and garbage in, garbage out (factual errors in the training corpus the model may reproduce) (§3.4; Appendix D) [AP].

7.  **Binary grading rewards guessing.** Under scoring that gives one point for a correct answer and zero for a wrong answer or an abstention, any answer with a non-zero chance of being right has a higher expected score than abstaining; Observation 1 states that no abstention maximises expected score (Source: Kalai et al., Why Language Models Hallucinate, §1.2; §4.1, Observation 1; Appendix E) [AP]. The authors liken it to students guessing on a test scored right or wrong, where bluffs tend to be specific and overconfident (§1.2) [AR]. "Put simply, most evaluations are not aligned." [V] (§1.2).

8.  **Side checks cannot offset the primary score.** A model that abstains when unsure can lose to an otherwise similar model that always guesses across the many accuracy and pass-rate evaluations that score abstention zero, so a few hallucination-specific evaluations may be outweighed by the larger set of misaligned primary ones (Source: Kalai et al., Why Language Models Hallucinate, §1.2; §4.1) [AR]. Of ten evaluations used by influential leaderboards, the authors class nine, SWE-bench among them, as binary with no credit for IDK (§4.1, Table 2; Appendix F) [AP]. Their conclusion is that the majority of mainstream evaluations reward hallucinatory behaviour (§6, "Conclusions") [AR].

9.  **Model graders can pass wrong answers.** Language-model judges can mark incorrect long answers as correct, even in mathematical domains, potentially rewarding plausible bluffing (Source: Kalai et al., Why Language Models Hallucinate, Appendix F, "Current grading of uncertain responses") [AP]. One rubric-graded evaluation may score an IDK below a fair answer that contains factual errors (Appendix F.1) [AR].

10.  **Calibration error is not a measure of being wrong.** A system that is always wrong and reports zero confidence, and one that is always right and reports zero confidence, behave in opposite ways, yet calibration error alone does not express the difference (Source: Kalai et al., Why Language Models Hallucinate, Appendix F.3) [AR]. Calibration plots reproduced from previously published work show a pretrained model well calibrated and contrast post-trained models, which may move away from it (§3.1, Figure 2) [AP] [BT].

11.  **Explicit confidence targets and behavioural calibration.** State the threshold *t* in the instructions and charge a wrong answer *t*/(1−*t*) points, so answering beats IDK exactly when the chance of being right exceeds *t*; thresholds of 0.5, 0.75 and 0.9 imply penalties of 1, 2 and 9, and plain binary grading is *t* = 0 (Source: Kalai et al., Why Language Models Hallucinate, §4.2, "Explicit confidence targets") [AP]. The target goes in the instructions and into mainstream evaluations, not only special ones (§4.2) [AP]. *Behavioural calibration* means giving the most useful answer that clears the stated threshold, or abstaining; it needs no numeric probability and can be audited by comparing accuracy and error rates across thresholds, and the authors offer it as a useful objective, not a property shown in current systems (§4.2) [AP]. The ideal threshold would reflect downstream harm, which varies by application; the authors prefer a stated, perhaps conventional, threshold to an unstated penalty (§4.2) [AR].

12.  **Search and retrieval are not panaceas.** Search and retrieval can reduce hallucination, but Observation 1 still applies: when retrieval yields no confident answer and scoring still rewards guessing, the incentive survives; search may not help with miscalculation or other intrinsic hallucinations (Source: Kalai et al., Why Language Models Hallucinate, §5, "Search (and reasoning) are not panaceas") [AP].

13.  **Latent context, and more ways to signal doubt than IDK.** Some errors turn on context absent from the prompt: a question about phones may mean land lines while the model assumes cellphones, and the paper's error definition cannot represent that (§5, "Latent context") [AP]. Models can signal doubt by hedging, leaving out a doubtful detail, or asking a clarifying question (§5, "Beyond IDK") [AP]; right, wrong and IDK do not capture degrees of error, but even that incomplete three-way split permits abstention, unlike a right-or-wrong split (§5, "A false trichotomy") [AR].

## Questions to Ask During Warranting Agent-Built Software

### Phase 1: Specifying the change

| Need | Question | Source-tag |
|---|---|---|
| Surface the context the agent would assume | Which terms in the spec could carry a meaning the agent will fill in silently, the way "phones" can mean land lines or cellphones, and has the spec picked one? | §5, "Latent context" |
| Give the agent a way not to answer | Do the agent's instructions permit *not verified* or *blocked* as an outcome, or is *done* the only result that scores? | §4.1; §5, "A false trichotomy" |
| State the confidence target | Do the instructions say how sure the agent must be before it acts or reports, and what a wrong report costs against an abstention, scaled to what the change can harm? | §4.2 |
| Invite the clarifying question | Can the agent ask a clarifying question instead of guessing, and does the harness route that question to a person? | §5, "Beyond IDK" |

### Phase 2: Triaging risk

| Need | Question | Source-tag |
|---|---|---|
| Decide what an LLM feature promises | If the change adds an LLM call, a prompt or a retrieval step, what does the feature promise about false answers: answers only from a verified set, and IDK otherwise, or something weaker? | §3.1; §5 |
| Check the retrieval claim | Does the design assume retrieval will stop false answers, and what does the feature do when retrieval finds nothing? | §5, "Search (and reasoning) are not panaceas" |
| Name the error sources the change leans on | Does the change depend on facts with no pattern to infer them (client-specific values), on character-level logic, on prompts unlike anything common, or on idioms the training data may carry errors in? (Mapping the paper's factors to code is this distillation's inference.) | §3.3.1; §3.3.2; §3.4 |

### Phase 3: Locking the tests

| Need | Question | Source-tag |
|---|---|---|
| Test the abstention path | For an LLM feature, do the locked tests include prompts outside its coverage, or with no supporting document, that expect an abstention? | §3.1; §5 |
| Score so guessing doesn't pay | Is a wrong answer scored below an abstention in the feature's tests, at a stated threshold? | §4.2 |
| Check the grader | If a model grades any test, has anyone checked whether it passes fluent wrong answers? | Appendix F |

### Phase 4: Building in the sandbox

| Need | Question | Source-tag |
|---|---|---|
| Trace arbitrary values | Does the diff carry a client-specific value (a rate, an ID, a date, a limit) that no spec line or recorded lookup supplied? | §3.3.1 |
| Check the lookup behind a claim | Where the agent cites documentation or an API, does the tool log show a lookup that returned the answer, or none, or an empty result followed by a confident claim? | §5, "Search (and reasoning) are not panaceas" |
| Run what was reasoned | Did the agent report a count, length or offset it reasoned out rather than computed by running code? | §3.3.2 |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| Separate blocked from failed | Does the gate record *blocked* or *not verified* separately from *failed*, or does it score them the same, so the agent does better by guessing? | §4.1, Observation 1 |
| Check model-graded gates | Does any gate's pass rest on a model's verdict, and have its passes been checked against a deterministic check or a person? (Sampling is a harness rule.) | Appendix F |
| Refuse stated confidence as a pass | Does any gate accept the agent's stated confidence as evidence in place of a run? | Appendix F.3; §1.2 |

### Phase 6: Reviewing independently

| Need | Question | Source-tag |
|---|---|---|
| Know what the reviewer agent is scored on | Is the reviewer agent able to say *unsure*, and is a false finding scored below an abstention? | §4.1; §4.2 |
| Check the reviewer's passes | Has anyone sampled the reviewer agent's passes to see whether it passes fluent wrong work? | Appendix F |
| Read a model-choice claim | Was the model behind a builder or reviewer agent chosen on a pass-rate score, and what are its error and abstention rates under scoring that puts a wrong answer below an abstention? | §1.2; §4.1; §4.2 |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Separate confident from shown | Which claims in the pack are confident assertions, by the agent or a model reviewer, with no run behind them? | §1; §1.2 |
| Read a confidence statement | Does the pack's assurance rest on a stated confidence or a calibration figure rather than a check? | Appendix F.3 |
| State the LLM feature's promise | Does the warranty say what the feature promises about false answers, and is that promise backed by the abstention tests? | §3.1; §4.2; §5 |

### Phase 8: Releasing and operating

| Need | Question | Source-tag |
|---|---|---|
| Score the LLM feature honestly in production | Does the feature's production metric count *I don't know* or a hand-off as a failed answer, or report one accuracy number with no error rate beside it? | §4.1; §4.2 |
| Keep the side metric from being outweighed | If a hallucination or error metric exists, does the primary metric still reward answering over abstaining? | §4.1 |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| The agent's instructions say *make the tests pass* or *finish the task*, with no permitted *not verified* outcome | Binary scoring: abstaining never scores, so guessing is always at least as good (§4.1, Observation 1) [AP] | Add *not verified* and *blocked* as outcomes, and state what a wrong report costs against one |
| A spec term has more than one common reading (*delete*, *user*, *account*) and the spec does not pick one | Latent context: the error turns on context the prompt left out (§5) [AP] | Settle the meaning before the build |
| The diff hard-codes a client-specific value no spec line or recorded lookup supplied | An arbitrary fact: there is no pattern to infer it from (§3.3.1) [AP] | Trace it to a source or send it back |
| The tool log shows an empty lookup, then a confident claim | Retrieval did not yield an answer and the incentive to guess survives it (§5) [AP] | Mark the claim unverified until a lookup backs it |
| The agent reports a count, length or offset it reasoned out | A representational limit, not a missing fact (§3.3.2) [AR] | Run it |
| A gate or reviewer agent is a model, and nobody has checked its passes | Model judges can mark incorrect long answers as correct (Appendix F) [AP] | Sample its passes against a deterministic check or a person (a harness rule) |
| The pack says "high confidence" or cites a calibration figure | Calibration error alone does not show how often a system is wrong (Appendix F.3) [AR] | Replace the confidence with the check that would show it |
| A design note says retrieval or grounding will stop the feature from hallucinating | Search is not a panacea (§5) [AP] | Require a tested path for when retrieval finds nothing |

## When to Use This Reference

- When an agent's report, a model reviewer's verdict or a stated confidence is about to stand in for a check: this source explains why fluent, specific, confident output is what scoring rewards whether or not it is right.
- When designing a gate's outcomes or a reviewer agent's scoring: this is the corpus's source on scoring that rewards abstention over a wrong answer, and on why a side check does not fix a primary score that rewards guessing.
- When the change ships an LLM feature: what it can promise about false answers, why retrieval alone does not settle that, and how to test and measure the abstention path.
- When choosing the model behind an agent from a leaderboard: the source classes most influential evaluations, SWE-bench among them, as giving no credit for abstaining.
- Reach for `jimenez-swe-bench` instead for how a change's tests are built and validated, and for how model patches fail against them; for the risks of an LLM feature as a threat list, `owasp-llm-top10-2026`. This source explains *why* a model answers when it should abstain; it says nothing about code, tests or delivery as such.

## Worked Example

A small builder is adding a support-answer feature for a client's customer portal: an LLM call that answers account questions from the client's help pages through retrieval. The builder's coding agent writes the feature and its tests in one session, a model-graded check scores the answers as acceptable, and the agent's summary reads "done; answers are grounded in the help pages, so hallucination is handled".

The independent reviewer starts from what the feature promises. The paper's construction of a model that does not hallucinate is a fixed set of answers plus IDK for everything else (§3.1) [AR], and its heading puts the point plainly:

> “Hallucinations are inevitable *only for base models*.” [V] (§3.1, heading)

So the reviewer asks the builder to write the promise down: answers only from the help pages, and IDK or a hand-off when they don't cover the question. The agent's claim that grounding handles hallucination fails on the source's own boundary:

> “Search (and reasoning) are not panaceas.” [V] (§5, heading)

Retrieval can reduce hallucination, but when it finds nothing and scoring still rewards an answer, the incentive to guess survives (§5) [AP]. The reviewer checks the tests and finds no prompt outside the help pages' coverage; every test expects an answer. That is binary grading in the test suite: an abstention would have failed every one of them (§4.1, Observation 1) [AP]. The reviewer requires out-of-coverage and no-document prompts that expect an IDK, scored so a wrong answer costs more than the IDK. For the threshold, the paper's form is the model:

> Answer only if you are $`>t`$ confident, since mistakes are penalized $`t/(1-t)`$ points, while correct answers receive 1 point, and an answer of “I don’t know” receives 0 points. [V] (§4.2, "Explicit confidence targets")

The builder picks *t* = 0.75 for account questions, a penalty of 2 for each wrong answer (§4.2) [AP]; the paper ties the ideal threshold to downstream harm and prefers a stated one to an unstated one (§4.2) [AR]. Choosing 0.75 for this client is the builder's call, not the paper's.

Last, the model-graded check. Model judges can mark incorrect long answers as correct (Appendix F) [AP], so the reviewer samples twenty of its passes against the help pages by hand and records how many it would have failed (sampling and recording are harness rules). The warranty pack then states the feature's promise, the abstention tests and their scores, and the grader's sampled disagreement rate, in place of "hallucination is handled".

## Anti-patterns This Reference Helps Avoid

| Anti-pattern | Signal | Diagnosis | Follow-up |
|---|---|---|---|
| *Done* as the only scoring outcome | Gates and instructions recognise pass and fail only | Under binary scoring, abstaining never maximises the score (§4.1, Observation 1) [AP] | Add *not verified* and *blocked*, and record them apart from *failed* |
| Fluency taken as evidence | The pack quotes the agent's specific, confident summary as the reason to sign | Bluffs under right-or-wrong scoring tend to be specific and overconfident (§1.2) [AR] | Ask for the run behind each claim |
| Grounding taken as a guarantee | "It's retrieval-backed, so it won't make things up" | Search is not a panacea; the guessing incentive survives an empty retrieval (§5) [AP] | Test and promise the empty-retrieval path |
| One extra check to offset a pass-rate score | A hallucination test added beside a suite that still rewards answering | A few special evaluations can be outweighed by the larger set of misaligned primary ones (§4.1) [AR] | Change the primary score so a wrong answer costs more than an abstention |
| A model grader nobody grades | A model-judged gate or reviewer whose passes are never sampled | Model judges can pass incorrect long answers (Appendix F) [AP] | Sample its passes (a harness rule) |
| Confidence as assurance | "The model is well calibrated", "high confidence" | Calibration error alone does not express how often a system is wrong (Appendix F.3) [AR] | Replace it with the check |
| Choosing a model on a pass-rate leaderboard | The builder or reviewer model swapped for a higher pass rate | A model that always guesses can outscore one that abstains on binary evaluations (§1.2; §4.1) [AR] | Ask for error and abstention rates under scoring that puts a wrong answer below an abstention |

## Integration with Other References

| Reference | Relationship |
|---|---|
| `jimenez-swe-bench` | Kalai et al. class SWE-bench's scoring as binary with no credit for an uncertainty response (§4.1, Table 2; Appendix F.3) [AP] and propose adding explicit confidence targets to benchmarks such as SWE-bench (§4.2) [AP]. SWE-bench's metric is the share of instances resolved, pass or fail (Jimenez et al., §2.2) [AP]; its six-outcome analysis of applied patches separates a No-Op from a Regression (App. C.5) [AP] but gives no route to abstain. Together: SWE-bench supplies the shape of a checkable change, this source the case for scoring a wrong patch below an abstention. See the named disagreement |
| `owasp-llm-top10-2026` | Its misinformation entry names overreliance on fluent, confident output as a key factor and says it is often built into agentic system design (LLM07, p. 43) [AR], lists verification signals, not confidence alone, among its mitigations (p. 44) [AP], and gives a scenario of an agent reporting a backup done that never ran (p. 45) [AE]. This source explains the model-side reason confident output is no evidence; OWASP supplies the system-side controls. OWASP also lists hallucination among the causes of misinformation (p. 43) [AP] |
| `openssf-finding-fixing-vulnerabilities-ai` | The guide recommends separating identifying findings from validating them ("Separate identifying findings from validation") [AP] and says a task verifier trusted to accept or reject an agent's work becomes part of the workflow's trusted computing base ("Preparing CI/CD") [AR]. This source adds why a model-based verifier needs checking of its own: model judges can pass incorrect answers (Appendix F) [AP]. Linking the two is this distillation's inference |
| `uk-duck-book-qa-of-code` | The Duck Book's golden rules (review any LLM-written code yourself; you alone are responsible for it) ("Vibe coding: Using LLMs to write code in the workplace") [AR] put a person behind every agent claim; this source explains why the claim itself carries no proof. The two disagree on whether hallucination is inevitable; see the named disagreement |

**Named disagreement: `uk-duck-book-qa-of-code` vs this source, on whether hallucination is inevitable.** The Duck Book says LLMs regularly generate plausible but inaccurate statements and that their production is mathematically inevitable, citing an arXiv paper its deep reference does not identify [BT]; it calls this a feature of the models rather than a failure, and says they have no internal model of what is true and false ("Vibe coding: Using LLMs to write code in the workplace") [AP]. Its deep reference carries those phrases as verbatim. Kalai et al. agree that a base model trained in the standard way will err under their assumptions, but their heading limits the claim to base models, they describe a system that would not hallucinate (a fixed answer set plus IDK), and they place hallucination's persistence after pretraining in evaluation incentives that can be changed (§3.1; §4) [AR]. For the harness both lead to the same act, check the claim, but they differ on whether better scoring could make an agent's *done* more trustworthy.

**Named disagreement: `jimenez-swe-bench` vs this source, on how a coding benchmark should score.** See the first row of the table: SWE-bench scores resolved or not; Kalai et al. class that as binary and propose explicit confidence targets for it.

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The authors cite prior work for the causes of hallucination listed in their related-work section, for the earlier theory of missing-mass estimates and hallucination that they show is a special case of their result, for the trade-off between avoiding invalid output and breadth, for the finding that post-training methods reduce some hallucinations, for the calibration plots in Figure 2, and for the report that hallucination benchmarks have struggled to gain traction (§2; §3.1, Figure 2) [BT]. None of those works is held in this corpus and this distillation does not draw on them. The converted tape drops author names from in-text citations, so the deep reference describes those works rather than naming them.

**Named limits of the source.** The formal lower bounds concern base models under specified distributional and calibration assumptions, including an error-free training distribution the authors call favourable and unrealistic (§3.1; §3.2) [AP]. The post-training section shows that binary scoring rewards guessing and documents how common it is in selected evaluations; it does not estimate how much of any named model's hallucination rate those evaluations caused (deep reference §12, "Causal boundary"). Behavioural calibration is proposed, not shown in current systems (§4.2) [AP]. The paper focuses on single factual questions; for open-ended output it treats any response with one or more falsehoods as an error and says a graded measure would be more natural (§5, "Open-ended generations") [AP]. Its error definition cannot represent latent context (§5) [AP]. The paper does not study coding agents, and every step here from model answers to agent reports, gates and reviewers is this distillation's inference. The deep reference records that the converted tape lacks one of the PDF's nine footnotes (Table 1's access details).

**Evidence-marker continuity.** Definitions, theorems, the benchmark review and the proposal carry `[AP]`; the authors' readings (the test-taking analogy, the base-model scope of inevitability, side checks outweighed by primary scores, calibration error not expressing hallucination, the harm-based threshold) carry `[AR]`; the calibration plots and the related-work causes carry `[BT]`. Five passages are copied from the deep reference's audited `[V]` blocks: "Put simply, most evaluations are not aligned." (§1.2); the multiple-factors phrase (§3.4); and three blockquotes in the worked example (§3.1 heading; §5 heading; the §4.2 instruction). The Duck Book's words in the named disagreement are paraphrased, since its deep reference holds them as `[V]` against a different source. None was re-extracted from the tape. The §6 conclusion sentence the deep reference carries as `[V]` is paraphrased here (Key Concept 8).

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The builder says "the agent will figure out the details" (Phase 1) | Latent context: errors can turn on context the prompt leaves out (§5) [AP]; under scoring that gives abstaining nothing, guessing scores better (§4.1, Observation 1) [AP] | What the agent figures out unseen, it guesses. Name the terms it could read two ways, and give it a permitted *not verified* outcome. |
| The change adds an LLM call, a prompt, a tool an agent can call, or memory (Phase 2) | A non-hallucinating system answers from a fixed set and says IDK otherwise (§3.1) [AR]; search is not a panacea (§5) [AP] | Decide what the feature promises about false answers, and what it does when retrieval finds nothing. |
| The agent runs for an hour unattended and reports success (Phase 4) | Bluffs under right-or-wrong scoring are specific and overconfident (§1.2) [AR]; scoring rewards an answer over an abstention (§4.1) [AP]. Applying this to an agent's report is this distillation's inference | A report of success is an answer from something never paid to say *not verified*. Check the run, not the report. |
| The reviewer and builder agree too quickly (Phase 6) | Model judges can mark incorrect long answers as correct (Appendix F) [AP] | A model reviewer passing a model's work is not a check yet. Sample its passes against something that isn't a model. |
| The pack says "all tests pass" with no run record (Phase 7) | Plausible falsehood (§1) [AP]; calibration error alone does not show how often a system is wrong (Appendix F.3) [AR] | A fluent claim and a stated confidence are not evidence. Ask for the run. |

## Trigger extensions surfaced by this source

| Phase | Trigger (what the practitioner notices) | Response (grounded in this source) |
|---|---|---|
| 1 | The task instructions say *make the tests pass* or *finish the task* and give the agent no permitted *not verified* or *blocked* outcome | Add one, and state the confidence target and what a wrong answer costs; when abstaining scores zero, guessing has the higher expected score (§4.1, Observation 1; §4.2) [AP] |
| 1 | A spec term has more than one common reading (*delete*, *user*, *account*) and the spec does not pick one | Settle the meaning before the build; errors can turn on context the prompt leaves out (§5, "Latent context") [AP] |
| 2 | An LLM feature's design note says retrieval or grounding will stop it hallucinating | Require a tested path for when retrieval finds nothing; search does not remove the incentive to guess (§5) [AP] |
| 3 | An LLM feature's tests include no prompt outside its coverage, or every test expects an answer | Add out-of-coverage and no-document prompts that expect abstention, scored so a wrong answer costs more than an abstention (§3.1; §4.2) [AP] |
| 4 | The diff hard-codes a client-specific value (a rate, an ID, a date, a limit) that no spec line or recorded lookup supplies | Trace it to a source or send it back; an arbitrary fact has no pattern to infer it from (§3.3.1) [AP] |
| 4 | The agent cites documentation or an API, and the tool log shows no lookup, or a lookup that returned nothing | Mark the claim unverified until a lookup backs it; retrieval that finds nothing does not remove the incentive to guess (§5) [AP] |
| 4 | The agent reports a count, length or offset it reasoned out instead of running | Run it; the authors read letter-counting failures as a representational limit, not a missing fact (§3.3.2) [AR] |
| 5 | A gate records *blocked* or *not verified* the same as *failed* | Record them apart; under binary scoring no abstention maximises the score (§4.1, Observation 1) [AP] |
| 5 | A gate or test is graded by a model, and its passes have never been sampled against a deterministic check or a person | Sample them and record the disagreement rate (a harness rule); model judges can mark incorrect long answers as correct (Appendix F) [AP] |
| 6 | The model behind a builder or reviewer agent is swapped on the strength of a pass-rate leaderboard | Ask for error and abstention rates under scoring that puts a wrong answer below an abstention; on binary evaluations a model that always guesses can outscore one that abstains (§1.2; §4.1) [AR] |
| 6 | A reviewer agent can only say pass or fail and never reports being unsure | Let it abstain, and score a false finding below an abstention at a stated threshold (§4.2) [AP]. Carrying the scoring rule to a reviewer agent is this distillation's inference |
| 7 | The pack's assurance is a stated confidence or a calibration figure ("high confidence", "the model is well calibrated") in place of a check | Replace it with the check; calibration error alone does not express how often a system is wrong (Appendix F.3) [AR] |
| 8 | An LLM feature's production metric counts *I don't know* or a hand-off as a failed answer | Score a wrong answer below an abstention; a side metric may not offset a primary one that rewards answering (§4.1; §4.2) [AR] |
