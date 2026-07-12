# Jones, Evidence-Based Software Engineering, AAR Distillation

**Source:** Jones, D. M. (2020). *Evidence-Based Software Engineering: based on the publicly available data*. Version 1.0. Knowledge Software, Ltd. ISBN: 978-1-8382913-0-3. Licence: CC BY-SA 4.0 (copyleft propagates to derivatives). Scope: open.

## AAR Relevance

Jones projects onto the software-incident AAR as an *empirical anchor*: the book's central claim — that most software-engineering belief is folklore unsupported by public data [V] (Source: Jones, *Evidence-Based Software Engineering*, Ch 1, "History of software engineering research") — has direct consequences for contributory-factor analysis. When a team reconstructs why an incident happened, the contributory factors they name (a metric threshold crossed, a productivity assumption, a maintenance-cost belief) may themselves be folklore. Jones gives the facilitator hard numbers to hold against those beliefs: the bi-exponential fault-report pattern, the survival-adjusted maintenance-to-development ratio, Goodhart's Law on measurement collapse, and the corrected Grant-Sackman productivity range. The projection is moderate fire: Jones's content is most load-bearing at Phase 2 (contributory-factor analysis) and Phase 4 (retraining-resource allocation), and is the empirical corrective when a software incident's post-mortem turns on metrics, vendor coordination, or reliability assumptions.

## Key Concepts for AAR

1.  **Post-1980 evidence collapse.** Only 2% of software-engineering papers (1993–2002) reported experiments; of those, 72.6% used students only as subjects. (Source: Jones, *Evidence-Based Software Engineering*, Ch 1, "History of software engineering research") A systematic lack of evidence is itself a contributory factor when incident cause-analysis relies on claims that were never empirically tested.

2.  **Goodhart's Law as measurement contributory factor.** "Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes" [V] (Source: Ch 13.1.1, "Measurement uncertainty") When an incident's contributory factors include metrics used as control targets — velocity, defect count, coverage thresholds — this is the explanatory frame.

3.  **Cone of uncertainty is a mathematical artefact.** The cone shape produced by plotting Actual/Estimated against percentage-completed is "at best useless" — it is "a mathematical artefact created by the choice of axis" [V] (Source: Ch 5.4.4, "Managing progress") When an AAR revisits why estimates were accepted as certain, this finding disarms a frequently cited but empirically groundless excuse.

4.  **Bi-exponential fault-report duplicates pattern.** The number of times the same fault is experienced, ranked, fits a bi-exponential: a × e^(bx) + c × e^(dx) [V] (Source: Ch 6.3.1, "Input profile") This pattern implies two distinct underlying processes; during an AAR it means many fault experiences trace to a small set of high-frequency input paths meeting a small set of concentrated mistakes.

5.  **Over 80% of bit-flips have no detectable program-behavior impact.** [AP] (Source: Ch 6.3.2, "Propagation of mistakes") Many coding mistakes never produce a fault experience; the cost of finding and fixing every mistake is wasted effort. For software-incident AARs on reliability failures, the population of latent mistakes that did not fire is a legitimate scope constraint on remediation.

6.  **Survival-adjusted maintenance-to-development ratio.** Mean total maintenance-to-development cost ratio, adjusted for system survival, is below one — "closer to 0.8" [V] (Source: Ch 4.2, "Evolution") — not the oft-cited 5:1 or higher, which reflects survivorship bias. Software half-lives are approximately 5 years (mainframe) and 2.9 years (Google SaaS) [AP] (Source: Ch 3.2.3, "Incremental investments and returns").

7.  **Grant-Sackman 28:1 corrected to roughly 6:1.** The widely cited productivity spread was the result of confounding; corrected, "the maximum difference ratio is 14:1, the minimum 6:1" [V] (Source: Ch 1, "Folklore") When productivity assumptions appear in the incident timeline, the 28:1 figure has no empirical support.

8.  **Anchoring in estimates.** Professionals' and students' estimates are strongly shifted by the customer's offered figure. (Source: Ch 2.2.1, "Built-in behaviors", citing Jørgensen and Sjøberg, borrowed-through) Agile-task data shows round-number anchoring — peaks at multiples of seven hours. When deadline pressure appears in the AAR timeline, anchoring is a plausible contributory factor.

9.  **Agency theory and moral hazard in vendor-client relations.** Information asymmetry and moral hazard between client and vendor are analysed using agency theory. Standard form contracts "almost all had a net bias, relative to relevant default rules, in favor of the software company" [V] (Source: Ch 5.2.1, "Contracts") When an incident involved vendor coordination, agency theory names the structural incentive divergence.

10.  **Bidding behaviours not connected to technical cost.** Bidding decisions are "driven by factors that have little or no connection with the technical aspects of software implementation, or its costs" [V] (Source: Ch 5.2, "Pitching for projects") — including keeping staff busy, bidding low to win then recouping in maintenance. When an AAR reveals that contracted scope was known to be unrealistic at contract time, this is the named pattern.

11.  **Folklore metrics (Halstead, McCabe) scale with LOC and are manipulable.** McCabe's cyclomatic complexity is "easily manipulated by splitting functions… the software equivalent of accounting fraud" [V] (Source: Ch 6.4.2, "Source code") When decisions were justified by complexity metrics, the metrics' evidential status is in question.

12.  **Brooks's Law stated as a condition, not a maxim.** The condition under which adding a person delays a project is expressed as an inequality. (Source: Ch 5.5.1, "New staff") When staffing decisions appear in the incident timeline, the actual condition — not the maxim — is the relevant frame.

## Questions to Ask During AAR

### Phase 2: Contributory-factor analysis

| Need | Question |
|---|---|
| A metric was being tracked as a target | Is this a Goodhart's-Law situation — did control pressure cause the metric to collapse as a reliable signal? What did the team start doing differently once the metric was a target? |
| An incident-postmortem relies on a "known fact" about software | Is the belief empirically supported, or is it inherited folklore? Which of the ~2% of software-engineering papers that actually ran experiments supports this claim? |
| Fault distribution is being described as random or uniform | Does the fault-experience pattern fit the bi-exponential shape? Are there a small number of high-frequency input paths hitting a concentrated set of mistakes? |
| A reliability improvement investment is being sized | What is the software system's likely survival horizon? Investments aimed at reducing maintenance costs need the survival-adjusted break-even calculation. |
| Productivity of individuals appears in the timeline | Is the spread being assumed 28:1? The corrected range is roughly 6:1; what decisions would have been different if the narrower range had been used? |
| A vendor is implicated in the incident | What were the contractual incentives on the vendor's side? Where did the vendor's interest diverge from the client's, and did the contract reinforce or address that divergence? |

### Phase 4: Action design

| Need | Question |
|---|---|
| Retraining investment is being scoped | What is this system's survival horizon? The survival-adjusted ROI calculation shapes how much it is worth investing in improvements. |
| A metric is proposed as the action's success criterion | How will control pressure change what people do to meet this metric? What is the Goodhart's Law prediction for this measure? |
| An action targets "all defects" or "zero defects" | Over 80% of coding mistakes never produce a fault experience; what threshold of risk reduction, not completeness, is the action targeting? |
| Estimation process is being redesigned | How will the redesign prevent anchor propagation from stakeholder figures? Private estimates before stakeholder reveal is the named response. |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| The AAR confidently names a "known fact" about software productivity, defect rates, or maintenance cost | Folklore-as-contributory-factor risk: the claim may have no empirical backing | Ask for the primary research; if none, name it as an unverified assumption, not a fact |
| A metric was the control target before the incident and is proposed again as the corrective measure | Goodhart's Law on both sides of the event | Ask: what did the team start doing differently when the metric was a target, and how does the proposed corrective avoid replicating that dynamic? |
| Vendor coordination is named as a factor but the structural incentive analysis is skipped | Agency-theory gap: the structural incentive divergence is not named, so the action targets the symptom (a missed communication) not the cause (misaligned incentives) | Ask: where did the vendor's incentives diverge from the client's, and what in the contract reinforced that divergence? |
| The action scales remediation investment to defect count (more defects = more investment) | Linearity assumption — the bi-exponential pattern implies concentration, not uniformity | Ask: what is the input-path concentration profile? Are we investing in the high-frequency paths or spreading across all defects? |

## When to Use This Reference

Reach for this source when:
- A software incident's contributory-factor analysis is turning on metrics (velocity, coverage, complexity scores) that may have been control targets.
- A vendor is implicated and the incentive structure of the contract has not been named.
- Productivity assumptions (staffing ratios, individual output estimates) appear in the incident timeline.
- The action design proposes to fix "all defects" or scale remediation investment linearly with defect count.
- The post-mortem treats a widely-cited software-engineering belief as fact without naming its evidential status.

Do not reach for this source as the facilitation or protocol guide — TC 25-20, LFUO, and NHS carry those functions. This source is the empirical corrective for the belief layer: when the room needs numbers to challenge an inherited assumption.

## Worked Example

A software team's incident review reveals that delivery velocity was set as a Sprint commitment target, and teams began gaming story-point estimates to hit it. The facilitator applies the Goodhart's Law frame: "Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes." (Source: Jones, *Evidence-Based Software Engineering*, Ch 13.1.1, "Measurement uncertainty".) This is not a general principle the facilitator imports from training — it is the named empirical finding the deep ref carries as `[V]`. The group then reconstructs what changed in estimation behaviour once velocity became a target: estimates shifted to round numbers, stories were split to increase point counts, and high-complexity items were underestimated to avoid push-back. In Phase 4, the proposed corrective is a velocity dashboard — but the same Goodhart's Law dynamic applies to the corrective. The facilitator names this explicitly and asks: how will we detect measurement collapse early? The group instead proposes outcome-focused review (did the work ship? did customers use it?) rather than a velocity target.

## Anti-patterns This Reference Helps Avoid

- Treating a metric that contributed to an incident as a reliable target for the corrective action — Goodhart's Law applies on both sides of the event.
- Citing the 28:1 productivity spread as justification for staffing or timeline decisions; the figure is folklore.
- Using the cone of uncertainty as evidence that estimates were "within the expected range" — the cone is a mathematical artefact with no predictive content.
- Scoping technical-debt remediation against the 5:1 or higher maintenance-to-development ratio without survival-adjusting; most systems are retired before substantial maintenance costs accumulate.
- Treating reliability investment as linearly scalable with defect count; the bi-exponential pattern implies concentration, not uniformity.
- Accepting folklore about complexity metrics (Halstead, McCabe) as evidence that design was sound or unsound at the time of the incident.
- Analysing vendor-coordination failures without naming the agency-theory incentive divergence that structured the failure.
- Closing an AAR on a software incident without noting which causal beliefs in the room lacked empirical support.

## Integration with Other References

| Reference | Relationship |
|---|---|
| Letaw Handbook (letaw-handbook-sweng-methods) | Letaw provides practitioner methods (RACI, fist of five, code smells) for the same software-incident domain; Jones provides the empirical corrective for the beliefs those methods operate on; use both when the incident involves both process decisions and metric assumptions |
| LFUO 2024 (lfuo-learning-review-guide-2024) | LFUO provides the networked-causality and local-rationality framework; Jones provides the empirical content for naming which beliefs constituted the local rationality and which were folklore |
| OpenStax Organizational Behavior (openstax-organizational-behavior) | OB names the cognitive biases (confirmation bias, anchoring) that allow folklore to persist; Jones names the specific software-engineering folklore; use together when the incident involves both a metric belief and the cognitive mechanism that kept it alive |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The anchoring finding (Jørgensen and Sjøberg) is cited borrowed-through in the deep ref (Ch 2.2.1); neither Jørgensen nor Sjøberg is held directly in this corpus. The agency-theory framework is applied borrowed-through from economics literature; the demo corpus does not hold the underlying agency-theory texts. Brooks's Law is cited as a condition from Brooks's own work, which the corpus does not hold directly. The bi-exponential fault pattern is documented from Microsoft Office, GCC, and KDE data — these studies are cited in the source but not held in the corpus.

**Named limits of the source.** Jones is explicit that the book covers only "publicly available data" — it is a secondary analysis of published datasets, not a primary study. Many findings are tentative or constrained by dataset availability; Jones uses explicit uncertainty language ("closer to 0.8", "roughly") rather than treating his estimates as precise. The book explicitly does not cover real-time, embedded, or safety-critical software development as distinct domains with their own datasets. Its findings apply most directly to commercial software development contexts.

**Evidence-marker continuity.** The Goodhart's Law quotation is `[V]` in the deep ref; the distillation quotes it directly in Concept 2 with the `[V]` marker. The maintenance-to-development ratio is `[V]` in the deep ref for the 0.8 figure and `[AP]` for the half-life estimates; the distillation preserves this distinction in Concept 6. The anchoring finding is `[AP]` in the deep ref with `[BT]` to Jørgensen and Sjøberg; the distillation preserves the borrowed-through flag in Concept 8 and in this section.
