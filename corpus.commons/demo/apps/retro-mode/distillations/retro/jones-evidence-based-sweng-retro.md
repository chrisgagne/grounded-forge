# Jones, Evidence-Based Software Engineering, Retro Distillation

**Source:** Jones, D. M. (2020). *Evidence-Based Software Engineering: based on the publicly available data*. Version 1.0. Knowledge Software, Ltd. ISBN: 978-1-8382913-0-3. Licence: CC BY-SA 4.0 (copyleft propagates to derivatives). Scope: open.

## Retro Relevance

Jones projects onto the retrospective as an *empirical corrective*: when a software team's retro moves are driven by folklore — productivity assumptions, measurement targets, complexity metrics, planning certainty — this source provides the empirical anchor that makes the corrective legible. The projection is moderate fire: Jones's material fires on three retro moments — Phase 2 (data gathering, where measurement-driven team beliefs surface), Phase 3 (insight and cause analysis, where Goodhart's Law and the cone of uncertainty need naming), and Phase 4 (experiment design, where estimates and productivity assumptions shape commitments). The core contribution is a posture: most software-engineering beliefs that drive retro decisions were never empirically tested; a team willing to hold its beliefs against evidence is more likely to design experiments that learn something.

## Key Concepts for Retro

1. **Goodhart's Law on team metrics.** "Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes" [V] (Ch 13.1.1, "Measurement uncertainty"). When a velocity target, defect rate, or coverage threshold has become a team-management tool rather than a learning signal, Goodhart's Law predicts the metric's collapse as a reliable indicator. The retro is the right moment to name which metrics have shifted from learning signals to control targets.

2. **Cone of uncertainty is a mathematical artefact, not a planning oracle.** The cone shape is "at best useless" — "a mathematical artefact created by the choice of axis" [V] (Ch 5.4.4, "Managing progress"). When a retro revisits estimates that were accepted as reliable at an early project stage, the cone of uncertainty is the often-cited but empirically groundless justification. The correct position: early estimates carry intrinsic variance that the cone diagram does not quantify.

3. **Anchoring to the customer's number.** Professionals' and students' estimates are strongly shifted by a customer's or manager's offered figure [AP] (Ch 2.2.1, "Built-in behaviors", citing Jørgensen and Sjøberg). Agile-task data shows peaks at multiples of seven hours with almost no estimates of six, eight, or nine [AP] (Ch 5.3, "Resource estimation"). When a retro's data-gathering surfaces that Sprint estimates felt off, anchoring — not poor skill — is often the explanatory frame.

4. **Grant-Sackman 28:1 corrected to roughly 6:1.** The 28:1 productivity spread between best and worst developers is folklore from a misread 1968 table; corrected, the maximum difference is 14:1, the minimum 6:1 [V] (Ch 1, "Folklore"), and a study separating subject performance found 1:5 [AP] (Ch 1, "Folklore"). When a retro surfaces team-productivity beliefs ("if everyone coded like X..."), the corrected figure is the reference point.

5. **Post-1980 evidence collapse as substrate against folklore-driven retro decisions.** Only 2% of software-engineering papers (1993–2002) reported experiments; of those, 72.6% used students only [V] (Ch 1, "History of software engineering research"). Most retro practices — standups, velocity tracking, pair programming, code review ratios — lack controlled-experiment support. This does not invalidate them, but it means teams are running experiments rather than following evidence; their retro should treat Sprint experiments with the same epistemic humility.

6. **Standard deviation of LOC estimates is approximately one-quarter of the mean.** Across multiple implementations of the same specification, "the standard deviation is approximately one quarter of the mean" in lines-of-code [AP] (Ch 5.3.1, "Estimation models"). Any LOC-driven estimate carries intrinsic variation that is structural, not a sign of team incompetence.

7. **Software half-lives and the survival-adjusted break-even.** Software half-lives are approximately 5 years (mainframe) and 2.9 years (Google SaaS) [AP] (Ch 3.2.3, "Incremental investments and returns"). Investments aimed at long-term maintainability need the survival-adjusted break-even: if the system is likely retired in 2-3 years, the retro experiment "invest three Sprints in refactoring" carries a different expected value than the raw maintainability argument suggests.

8. **Over 80% of bit-flips have no detectable program-behavior impact** [AP] (Ch 6.3.2, "Propagation of mistakes"). Many mistakes in code never produce a user-visible fault. When a retro's data includes defect-count data, the visible defects are a fraction of the latent mistake population; count-based metrics systematically undercount the problem space.

9. **Overconfidence is evolutionarily stable.** Simulations show that overconfidence has benefits in some situations, averaged over a population; it is not simply bias [AP] (Ch 2.8.5, "Overconfidence"). When a retro surfaces that the team was consistently overconfident in Sprint commitments, the corrective is structural (smaller batches, explicit estimation discipline) rather than motivational — the overconfidence is a cognitive default, not a character flaw.

10. **Research-dataset availability falls 17% per year** [BT] (Ch 1, "Research ecosystems", citing Vines et al.). For a retro: retrospective data from past Sprints that was never written down or is scattered across tools is not a team-laziness problem but follows the same decay curve. The retro that tries to reconstruct a pattern across six Sprints from memory is working against this base rate.

## Questions to Ask During Retro

### Phase 2: Data gathering

| Need | Question |
|---|---|
| Velocity or other metric has been stable but feels wrong | Is this metric being used to manage the team rather than to learn? Has Goodhart's Law already fired — is the team optimising the number rather than the underlying capability? |
| Estimates feel systematically off | Were estimates made privately before a stakeholder figure was offered? If not, anchoring — not estimation skill — is the first hypothesis. Were estimates made in hours or days? (Unit choice shifts the number.) |

### Phase 3: Insight / cause analysis

| Need | Question |
|---|---|
| Team invokes a "known fact" about software development | Is the belief empirically supported? Name one study. If the belief comes from the post-1980 period of software-engineering literature, its experimental foundation may be thin or absent. |
| Productivity gap between team members is a recurring theme | What range is the team assuming? The corrected Grant-Sackman spread is roughly 6:1, not 28:1. Does the team's expectation about peer productivity match the empirical range or exceed it? |
| Cone-of-uncertainty was cited to justify early-estimate acceptance | The cone is a mathematical artefact of axis choice, not a predictive model. Which planning decisions were made on the assumption that the cone validated the estimate? |
| A metric target drove team behaviour | Name the Goodhart's Law prediction: once this metric became a target, what did the team start doing differently? Was the change visible in the retro data before the problem surfaced? |
| A recurring problem involves code quality | Are the coding mistakes that are producing fault experiences concentrated on a small set of high-frequency input paths (the bi-exponential pattern)? Or is the team treating defects as uniformly distributed? |

### Phase 4: Experiment design

| Need | Question |
|---|---|
| Experiment proposes a new metric | What is the Goodhart's Law prediction for this metric once it becomes a target? Name the failure mode in advance, and name how the team will detect measurement collapse early. |
| Experiment proposes a multi-Sprint investment in a system | What is the system's likely survival horizon? The survival-adjusted break-even shapes whether the investment pays off before the system is replaced. |
| Experiment involves estimation reform | Does the reform prevent anchor propagation — private estimates before stakeholder reveal? Does it change the unit of estimate (hours vs days)? |
| Experiment commits to a productivity improvement target | What range of improvement is realistic given the corrected 6:1 spread? Is the target within the empirical range of individual-developer variation, or does it assume a larger lever? |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| A metric is tracking upward but the team's stated experience is worsening | Goodhart's Law may have fired — the metric is now a management target, not a learning signal | Ask: is the team optimising the number or the underlying capability? Name the failure mode in advance |
| Estimates feel systematically off sprint after sprint | Anchoring to a stakeholder or manager figure is the more likely explanation than poor skill | Were estimates made privately before a figure was offered? Change the sequence |
| Team invokes a "known fact" about software productivity | The claim may be folklore — most post-1980 software-engineering beliefs lack controlled-experiment support | Ask for one named study and its experimental conditions before accepting the claim |
| A productivity gap between team members is a recurring retro theme | The team's assumption may exceed the corrected empirical range (6:1) | Ask what range the team is assuming; name the corrected Grant-Sackman spread |
| The team proposes a multi-Sprint refactoring investment | The survival-adjusted break-even has not been named | Ask about the system's likely survival horizon before committing the investment |
| Retrospective data is being reconstructed from memory across multiple Sprints | Data decay base rate applies — the 17%-per-year decay makes memory-reconstruction structurally unreliable | Name this explicitly; use written artefacts from prior Sprints, not reconstruction |

## When to Use This Reference

Reach for this distillation when:
- The retro surfaces measurement-driven beliefs — velocity targets, defect-count goals, productivity comparisons — that may be operating as Goodhart's targets rather than learning signals.
- Estimation discipline is the retro topic: anchoring, unit choice, and overconfidence are the empirical frames this source provides.
- A long-horizon investment experiment is proposed — the survival-adjusted break-even is this source's specific contribution to experiment design.
- The team is accepting folklore claims as evidence — the post-1980 evidence-collapse finding is the most portable corrective.

Do not over-reach: Jones's empirical posture is a corrective lens, not a general retro methodology. Prefer the Approach Perfect Field Guide for protocol and Liberating Structures for facilitation moves. This source fires on three moments (metrics, estimation, long-horizon investment) and is background discipline elsewhere.

## Worked Example

A team's retro returns for the third time to "our velocity has plateaued." The lead asks whether velocity is being used to manage the team (a management target) or to learn about capacity (a learning signal). The team realises: for the past four Sprints, the product manager has been asking at Sprint Review whether velocity hit the planned number.

In Phase 3, the lead applies the Goodhart's Law question: once velocity became a target, what did the team start doing differently? Two patterns emerge: stories were being split smaller to increase count, and incomplete stories were being closed before the retro. The metric is measuring story-closing behaviour, not delivery capacity.

In Phase 4, the team proposes an experiment: stop reporting velocity externally; instead, report cycle time per story. Before committing, the lead asks the Goodhart's Law prediction for cycle time: what will the team optimise when cycle time becomes the number the product manager sees? The team names the failure mode in advance (stories held artificially to avoid short cycles, or stories started but not finished). They add a safeguard: cycle time is reported alongside WIP count, so neither can be gamed independently.

The Goodhart's Law application, Grant-Sackman correction, cone-of-uncertainty reframing, and survival-adjusted break-even all trace to Jones (Ch 13.1.1, "Measurement uncertainty"; Ch 1, "Folklore"; Ch 5.4.4, "Managing progress"; Ch 3.2.3, "Incremental investments and returns").

## Anti-patterns This Reference Helps Avoid

- Treating velocity as a productivity signal when it is being used as a management target — Goodhart's Law predicts the collapse, and the retro is where the collapse becomes visible.
- Citing the 28:1 productivity spread as justification for staffing or peer-performance expectations; the corrected range is roughly 6:1 or smaller.
- Using the cone of uncertainty to validate early-Sprint estimates as "within expected variance"; the cone is a mathematical artefact, not a calibrated prediction interval.
- Designing retro experiments that involve long-horizon investments in a short-lived system without the survival-adjusted break-even calculation.
- Treating consistent overcommitment as a motivation problem rather than a structural cognitive default; the corrective is batch-size reduction and estimation discipline, not a talk about effort.
- Accepting folklore-based claims ("pairing doubles velocity," "code review reduces defects by X%") as evidence without naming the study and its experimental conditions — most such claims have no controlled-experiment backing from the post-1980 literature.
- Reconstructing a pattern across multiple Sprints from memory without acknowledging the 17%-per-year data-decay base rate; past-Sprint data that was never written down is structurally unreliable.
- Proposing a new metric as the experiment's success criterion without naming the Goodhart's Law failure mode in advance.

## Integration with Other References

| Reference | Relationship |
|---|---|
| Open Practice Library | OPL's Design of Experiments provides the hypothesis structure that Jones's empirical posture demands; Jones supplies the epistemic discipline (name the failure mode in advance), OPL supplies the experiment scaffold |
| Letaw Handbook of Software Engineering Methods | Letaw's INVEST criteria for experiment quality and Jones's Goodhart's Law test for metric experiments are complementary Phase 4 gates; use both |
| Open Kanban | Open Kanban's batch-size reduction and one-constraint discipline are the structural response to the overcommitment pattern Jones documents as a cognitive default |
| OpenStax Psychology 2e | Psychology 2e's anchoring and overconfidence findings provide the cognitive-science grounding for the estimation-bias patterns Jones documents empirically |
| SSDL Systems Thinking Foundations | When a metric's Goodhart collapse is visible in the retro data, SSDL's feedback-thinking lens names the reinforcing loop; Jones names the failure, SSDL explains the structure |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The 17%-per-year dataset-availability decay traces to Vines et al. (cited in Jones as research-dataset availability data) [BT] (Ch 1, "Research ecosystems"). The anchoring findings on Jørgensen and Sjøberg are cited in Jones as primary studies [BT] (Ch 2.2.1, "Built-in behaviors"). Goodhart's Law is cited by Jones as an established economic principle, not as primary empirical work Jones conducted [AP] (Ch 13.1.1, "Measurement uncertainty"). None of these sources are held directly in this corpus.

**Named limits of the source.** Jones is an evidence-disciplined secondary source — nearly every claim traces to a named primary study, and the author makes his data-cleaning and interpretive choices visible. However, the source's scope is academic and empirical: it does not address facilitation practice, retro ceremony design, or team coaching. Applying Jones in a retro requires translating findings from the research domain to the team-conversation domain; this distillation makes those translations. Jones explicitly acknowledges that most software-engineering findings used students as subjects [V] (Ch 1, "History of software engineering research"); claims about professional teams carry additional epistemic uncertainty. The text does not address Scrum, agile, or iterative delivery directly.

**Evidence-marker continuity.** Goodhart's Law is `[V]` in the deep ref (Jones's own framing of the principle); the distillation uses it as a named diagnostic gate (warranted). The Grant-Sackman correction is `[V]` in the deep ref; the distillation carries the corrected range (6:1) precisely. The cone-of-uncertainty claim ("at best useless — a mathematical artefact") is `[V]` in the deep ref; the distillation paraphrases the position without softening it. The 17%-per-year decay is `[BT]` in the deep ref and is marked as such in this distillation's Key Concepts entry. The overconfidence-as-evolutionarily-stable claim is `[AP]` in the deep ref (Jones's interpretation of the simulation findings); the distillation paraphrases it at the same level of confidence.
