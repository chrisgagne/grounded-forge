# Jones, Evidence-based Software Engineering, Decision-Making Distillation

**Source:** Derek M. Jones (2020). *Evidence-based Software Engineering: based on the publicly available data*. Version 1.0. ISBN 978-1-8382913-0-3. CC BY-SA 4.0. http://www.knosof.co.uk/ESEUR/. **Distribution note:** This distillation is a derivative of a CC BY-SA 4.0 source and carries the same SA copyleft obligation.

## Decision-Making Relevance

Jones treats software engineering as "an economically motivated cognitive activity occurring within one or more ecosystems" (Ch 1). Decision-making is therefore woven through the whole book rather than confined to a single chapter. The book treats decisions about software systems as investment decisions under cognitive constraint — the cognitive limits of stone-age brains processing modern problems (Ch 2), the economic structure of intangible goods (Ch 3), the path-dependency of ecosystems (Ch 4), and the bidding, estimation, and resource-allocation dynamics of projects (Ch 5). The book is unusually willing to expose the *evidence base* (or lack thereof) for the rules-of-thumb that practitioners use to make decisions about software systems.

This distillation consolidates the threads of decision-making analysis from the book into a working pattern: how to detect when a decision is being made under empirically unsupported folklore; how to frame investment decisions when the survival rate of the system is uncertain; how to read the cognitive-bias literature (anchoring, overconfidence, hyperbolic discounting, the "rational" overconfidence of entrepreneurs) without taking the experimental claims as load-bearing without scrutiny; how to use Goodhart's Law as a brake on measurement-driven decisions; and how to recognise when the question being asked of an estimate is *not whether the estimate is right* but *whether the decision-maker can act on it*.

## Key Concepts for Decision-Making

1.  **Sellers-market bias in software decisions.** Decisions about software development have been made in a seller's market for ~70 years — customers paid whatever it took because the potential benefits exceeded the costs. As a result, vendors have low pressure to invest in evidence-based decision practices, and customers have low experience of pushing back. Recognise this market structure before benchmarking your decision against industry norms. (Source: Ch 1, "Introduction")

2.  **Decisions under cognitive constraint, not under formal logic.** "The human mind is a story processor, not a logic processor" [V] (Source: Jones, *Evidence-based Software Engineering*, Ch 2.6, "Reasoning"). Decision-making models that assume logical optimisation are weak predictors of actual human decision behaviour. People use fast-and-frugal heuristics, exhibit anchoring (especially to the first number heard), and exhibit confirmation bias when collecting evidence. (Source: Ch 2.2.1, "Built-in behaviors"; Ch 2.6, "Reasoning"; Ch 2.8.3, "Decision-making")

3.  **The investment frame for any software decision.** Creating software is an irreversible investment — incomplete software has little resale value. Standard ROI/NPV calculations apply, but with two adjustments specific to software: (a) the discount rate must include a risk premium for software development uncertainty, and (b) the survival rate of the system over time must be factored in. With annual survival rates of 0.79 (Google SaaS) to 0.87 (mainframe), software half-lives are years, not decades. (Source: Ch 3.2, "Investment decisions"; Ch 3.2.2, "Taking risk into account"; Ch 3.2.3, "Incremental investments and returns")

4.  **Reject "technical debt" as a financial concept.** As Jones puts it, "Implementing functionality using the minimum of investment, with the intent of investing more later, has the form of an American call option" [V] (Source: Jones, *Evidence-based Software Engineering*, Ch 3.2.5, "Real options"). The "debt" metaphor is incorrect — there is no debt, and there may not be any need for more work in the future. Apply real-options analysis instead: a call option may or may not be exercised. (Source: Ch 3.2.5, "Real options")

5.  **Black-Scholes does not apply to software decisions.** The derivation of Black-Scholes assumes liquidity (so portfolios can be rebalanced) and historical performance data — neither holds for software development. Some researchers have applied this equation to software anyway; the text describes this as a mistake. (Source: Ch 3.2.5, "Real options")

6.  **The cone of uncertainty is a useless metaphor.** The cone shape that appears in plots of Actual/Estimated ratio against percentage-complete is a mathematical artefact of the axis choice. Don't use it for project decision-making. (Source: Ch 5.4.4, "Managing progress")

7.  **Estimates are not predictions; they are commitments under social pressure.** Software estimates are subject to anchoring (the customer's number shifts the bid), the cost of producing the estimate, the willingness of management to penalise bad news, the path-dependency of who got to the room first, and the unit of measurement (work-hours vs work-days produce different estimates for the same project). Round numbers dominate empirical estimate distributions — peaks at multiples of seven hours, almost no estimates of six, eight, or nine. (Source: Ch 5.3, "Resource estimation"; Ch 2.7.1, "Numeric preferences")

8.  **Decisions under risk vs decisions under uncertainty.** When all probabilities are known, the decision is under risk and standard expected-utility theory applies. When information is incomplete and probabilities are not known, the decision is under uncertainty and bounded rationality describes actual human behaviour better than optimisation models. Many real software decisions are under uncertainty, not risk. (Source: Ch 2.8.3, "Decision-making")

9.  **Overconfidence is evolutionarily stable.** Within a population, individual overconfidence has benefits — entrepreneurs commercialising new inventions are more confident than the general population, even though the average ROI on invention commercialisation is negative. Treat individual overconfidence as expected, not as a failure mode. (Source: Ch 2.8.5, "Overconfidence")

10.  **Hyperbolic discounting, not exponential.** People accept less satisfaction in the short-term than they could obtain by pursuing a longer-term course of action — but the discount rate is hyperbolic, with V/(1+kd), not exponential. This means decision-makers will switch preferences as the time of reward approaches; if you want to commit a decision to a long-term path, you need to make the commitment far enough in advance that the hyperbolic curve has flattened. (Source: Ch 2.8.6, "Time discounting")

11.  **The information-asymmetry trap for clients.** Vendors bidding to win an implementation contract have less information than they would have after the system existed; once one vendor has implemented a system, they have intimate familiarity with the system, and information asymmetry deters competing maintenance bidders. The client is at a disadvantage in any negotiation with the established vendor. (Source: Ch 3.4.6, "Information asymmetry")

12.  **Goodhart's Law as a decision-quality brake.** "Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes" [V] (Source: Jones, *Evidence-based Software Engineering*, Ch 13.1.1, "Measurement uncertainty"). If a measurement is used to control or evaluate the development team, the team has motivation to cause the measurement to move in a direction favorable to themselves. Don't use measurements that are easy to game. (Source: Ch 13.1.1, "Cultural influences")

13.  **Round-number bias and unit-of-measurement effects on estimates.** People prefer round numbers; the value of a measurement depends on the unit used to express it (kilo-, mega-, hours, days). Estimates given in different units for the same work are not the same number. (Source: Ch 2.7.1, "Numeric preferences"; Ch 5.3, "Resource estimation")

14.  **The Wason 2-4-6 task and positive vs negative testing.** People use a *positive test strategy* (confirmatory testing) by default. Klayman and Ha showed this is actually adaptive when the sought-after rule is a minority case or roughly the right size. Don't reflexively treat positive testing as cognitive bias — it's often optimal. (Source: Ch 2.2.1, "Built-in behaviors")

15.  **The Bass diffusion model for new-product adoption.** Customer adoption follows innovators + imitators; sales peak time and volume are derived analytically; this is a defensible quantitative model for one class of software-product-launch decisions. (Source: Ch 3.6.3, "Predicting sales volume")

## Questions to Ask During Decision-Making

### Phase 1: Framing (recognising what kind of decision is being made)

| Need | Question |
|---|---|
| Is this decision actually new, or am I recapitulating a folklore-based decision pattern? | Which of the rules-of-thumb supporting this decision are evidence-based, and which are folklore? Have I checked recent empirical work on the underlying processes? |
| Is the customer paying for the decision quality? | Who bears the cost of getting this decision wrong — me, the vendor, the customer, or someone not at the table? In a seller's market, vendors don't need to invest in evidence-based decisions; should I be treating this as a buyer's-market decision? |
| Is the decision under risk or uncertainty? | Do I have probability distributions for the outcomes, or am I in incomplete-information territory? If the latter, am I treating bounded-rationality heuristics as failures or as reasonable behaviour under constraint? |
| Have I anchored on the first number I heard? | What was the first dollar/time figure I encountered for this decision, and is my current estimate still shifted by it? Should I get an independent re-anchor? |
| Is round-number preference shaping my estimate? | Am I rounding to a multiple of the work-day, or to a multiple of a meaningful work unit? If I had to estimate in the *other* unit (hours vs days, MB vs GB), would my number be roughly proportional? |
| What does my measurement system reward? | If I use this measurement to control the team, will the team's behaviour shift in a way that makes the measurement collapse? |

### Phase 2: Bounding (defining the decision space)

| Need | Question |
|---|---|
| What is the survival rate of the system over the decision horizon? | If this system has an annual survival rate of 0.79–0.87, what is the probability it still exists in 5 years? In 10? Should the cost-benefit analysis include a non-trivial probability of project cancellation? |
| What is the cost of NOT making the decision today? | The opportunity cost frame: if I delay this decision, what other options open or close? |
| Is the decision an investment, an option, or a payment? | The investment frame requires sunk-cost commitment. The option frame allows future flexibility. The payment frame requires only immediate cash; "technical debt" is not a fourth category. |
| What is the cost asymmetry between the parties? | With COTS software, the customer bears the cost of fault experiences and the vendor chooses whether to fix; with bespoke software, the cost lies elsewhere. Who is paying for which outcome? |
| What information do I have that other parties don't? | Information asymmetry — am I in the role of the informed party (vendor maintaining an existing system, e.g.) or the uninformed party (client receiving competitive bids from new entrants)? |

### Phase 3: Exploring (generating alternatives)

| Need | Question |
|---|---|
| Have I considered alternatives that don't involve the software solution? | Sometimes the right decision is to not build software, or to use an existing system, or to wait for the ecosystem to stabilise. |
| Have I generated alternatives with different time horizons? | A 6-month commitment, a 2-year commitment, and a 5-year commitment are different decisions with different ROI calculations. |
| Have I considered the real-options structure? | Implementing minimum viable functionality with the intent to invest more later is a call option; what is the cost of acquiring the option and what is the strike price for exercising it? |
| Have I sought evidence from the cited literature, not just from my own experience? | If I am invoking a productivity-difference claim, an estimate-accuracy claim, or a maintenance-cost claim, has that claim been empirically supported or is it folklore? |
| Have I separated the question of "what should we do" from "what should we measure"? | A measurement that is good for decision-making may collapse if used for control. |

### Phase 4: Deciding (analysing and selecting)

| Need | Question |
|---|---|
| Apply the survival-adjusted ROI calculation. | Use the system survival rate to compute expected return, not just the unadjusted ROI. |
| Confirm the decision is not driven by overconfidence. | Have I treated this prediction as if it were a 95% confidence interval, or am I asserting a point estimate that the data does not support? |
| Use hyperbolic discounting for time-variable preferences. | If the choice involves immediate vs future payoff, what will my preference look like when the future payoff is much closer in time? |
| Apply the Bass model (if relevant) for sales forecasting. | If the decision depends on new-product adoption, fit the Bass model to comparable products to estimate likely volume and timing. |
| Distinguish "absence of evidence" from "evidence of absence". | If experimental data didn't show a difference, was the study powered to detect a difference of the size that matters? |
| Apply the front-page test for ethical decisions. | If this decision were on the front page of a major newspaper tomorrow, would the reader conclude that the cost-benefit analysis was made honestly? |

### Phase 5: Ratifying (committing to and communicating the decision)

| Need | Question |
|---|---|
| Make commitment rather than option-talk. | Once the decision is made, communicate the commitment in clear, time-bound terms — not as a tentative direction subject to renegotiation. |
| Communicate the survival-rate assumption. | If the project ROI depends on a 5-year half-life, say so explicitly so that future re-evaluation has a baseline to compare against. |
| Communicate the uncertainty bounds. | Give the equation and its coefficient uncertainties at the point they apply, rather than expecting readers to decode statistical summary output. |
| Stress-test the commitment against measurement gaming. | Ask: if this decision is later used to evaluate the team's performance, what gaming will appear? Goodhart's Law as a pre-commitment exercise. |
| Lock in the contract terms with information-asymmetry awareness. | If this is a vendor-client contract, what mechanisms (escrow, source-code-availability clauses, change-control procedures) reduce future information asymmetry? |

### Phase 6: Monitoring (post-decision review)

| Need | Question |
|---|---|
| Distinguish bad outcome from bad decision. | An outcome that was bad despite a reasonable expected value at the time of decision is not a bad decision. Don't post-hoc penalise decisions that were unfortunate. |
| Re-check the survival-rate assumption. | If the system has survived longer than expected, the maintenance-cost-vs-development trade-off may have changed. If it died early, the original ROI calculation needs to be revised. |
| Watch for measurement collapse (Goodhart's Law). | If a measurement that was useful for decision-making is now being used for control, expect the measurement to lose its statistical regularity. |
| Re-check anchoring on past decisions. | New decisions about the same system should be re-anchored, not shifted by prior estimates. |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| Project uses a productivity-difference claim (e.g., "10x developer") without citing a specific study | Folklore-based decision — the 28-to-1 claim is the canonical example; actual controlled-study ranges are much narrower (Source: Ch 1, "Folklore") | Ask for the primary study; verify whether the sample was students or professionals; check whether the ratio has been reproduced |
| A cost estimate anchors on the client's stated budget or the first number in the room | Anchoring failure — estimates are shifted by the customer's number even for trained professionals (Source: Ch 2.2.1, "Built-in behaviors") | Get an independent re-anchor before committing; run the estimate from scratch without the anchor present |
| The team is amortising "technical debt" by estimating future maintenance costs as multiples of development cost | Misapplication of a folklore ratio — the maintenance-cost ratios (5:1, 9:1) are from large-org contexts and are survival-unadjusted (Source: Ch 3.2, "Investment decisions") | Apply a survival-adjusted ROI calculation using the relevant annual survival rate for the system type |
| A measurement used for decision-making is now also used to evaluate individual team-member performance | Goodhart's Law conditions forming — the statistical regularity will collapse once control pressure is applied (Source: Ch 13.1.1, "Cultural influences") | Separate the decision-making measurement from the performance-evaluation measurement; use different metrics for each purpose |
| Estimates are converging on round numbers (multiples of 7 hours, 5 days) without explicit reason | Round-number preference in play — round numbers dominate empirical estimate distributions regardless of actual task distribution (Source: Ch 2.7.1, "Numeric preferences"; Ch 5.3, "Resource estimation") | Run a sanity check in the alternative unit (hours vs days); if the proportional conversion does not hold, the number is not a measurement, it is a preference |
| An Agile adoption decision is supported only by success stories from the vendor's case studies | Seller's-market bias — vendors have low pressure to publish failure cases; the evidence base for any specific practice claim needs independent verification (Source: Ch 1, "Introduction") | Ask for peer-reviewed comparative evidence, not vendor case studies, before treating the claim as load-bearing |

## When to Use This Reference

- A software investment decision needs a survival-adjusted ROI calculation rather than a naive NPV: the annual survival rates (0.79–0.87 depending on system type) and the real-options framing are the tools.
- A project estimate is being anchored on the client's budget, a previous estimate, or a round number: the anchoring literature and the round-number-preference evidence are the diagnostic tools.
- A folklore-based decision rule is being invoked (28-to-1 productivity claim, 5:1 maintenance cost ratio, cone of uncertainty, Brooks's Law): Jones is the primary reference for identifying which of these are evidence-based and which are not.
- A measurement is being used for both decision-making and team performance evaluation and Goodhart's Law failure is suspected.
- An estimate is being used as if it were a prediction rather than a social commitment under pressure: the cognitive-bias and social-pressure analysis is the diagnostic frame.
- A vendor-client contract needs information-asymmetry analysis: the lock-in dynamics after initial implementation, and the competitive maintenance-bid problem.
- An overconfidence pattern is present in technical decisions: treating individual overconfidence as expected and evolutionarily stable rather than as a personal failure.
- The question is whether a study's null result means "no effect" or "underpowered": the distinction between absence of evidence and evidence of absence is the frame.
- Reach for the OpenStax Organizational Behavior distillation (Ch 6) when the question is the general decision-making process and its cognitive barriers; Jones is the software-engineering specialisation of the same cognitive terrain.

## Anti-patterns this distillation helps avoid

- Treating "technical debt" as a financial concept and over-investing in repayment of imagined liabilities.
- Applying Black-Scholes or Brooks's-Law as if they were physical laws rather than (in the first case, inapplicable to software; in the second case, derivable conditions).
- Using productivity-difference claims (28-to-1, etc.) from folklore-supported sources to justify staffing decisions.
- Using maintenance-cost-vs-development claims (5:1 or 9:1) to justify upfront over-engineering when the survival-adjusted ratio is below 1.
- Using the cone-of-uncertainty as a project-management guide when the cone is a mathematical artefact of the plotting choice.
- Treating cost-of-fixing-faults grows-by-orders-of-magnitude as a universal rule when it derives from NASA/DOD-specific hardware-cost contexts.
- Confusing "absence of evidence" with "evidence of absence" — if the study wasn't powered to detect the effect, the null result is not informative.
- Treating estimates given in different units as fungible — work-hours and work-days produce different numbers for the same project.
- Allowing measurement systems to be used for both decision-making and team-evaluation, then being surprised when the measurement collapses.
- Treating individual subject performance in laboratory experiments as predictive of professional developer performance — students are typically 50–150 hours of programming, professionals 1,000–10,000.

## Worked Example

A product manager is evaluating a vendor proposal to replace a legacy CRM system. The vendor's pitch includes a productivity claim ("our developers deliver 3-5x faster than industry average") and a cost projection anchored at $1.2 million over three years.

Three Jones-grounded diagnostic moves apply. First, the productivity claim traces to a case-study portfolio, not a controlled study; applying Jones's folklore-detection frame (Source: Ch 1, "Folklore"), the product manager asks for the primary study. The vendor cites an internal analysis using the Grant-Sackman approach — self-selected developers, no control group. The claim is folklore.

Second, the $1.2M anchor has already shaped the product manager's internal estimate. Recognising the anchoring pattern (Source: Ch 2.2.1, "Built-in behaviors"), the product manager commissions an independent re-anchor from a third-party estimator who has not seen the vendor's number. The third-party estimate lands at $1.6M.

Third, the product manager applies the survival-adjusted ROI frame (Source: Ch 3.2, "Investment decisions"; Ch 3.2.2, "Taking risk into account"). CRM systems in their market segment show an annual survival rate near 0.84; over a five-year horizon, the probability the system is still running is 0.84⁵ ≈ 0.40. The ROI calculation includes a 60% chance of early termination, changing the investment case materially. The project proceeds with a reduced initial scope (real-options framing — implement minimum viable functionality, option to expand) and with the maintenance-cost claim flagged as folklore-supported rather than evidence-based.

All framework citations trace back through the deep reference.

## Integration with Other References

| Reference | How it pairs with Jones |
|---|---|
| **OpenStax, *Organizational Behavior*** (Ch 6) | Provides the general six-step decision process, cognitive barriers, and ethical decision frame that Jones operationalises for software investment decisions. OB for the framework; Jones for the evidence-calibration discipline. |
| **OpenStax, *Principles of Finance*** | Provides NPV, IRR, and capital-budgeting tools that Jones's survival-adjusted ROI calculation extends. Finance for the tools; Jones for the adjustment required in software contexts. |
| **Letaw, *Handbook of Software Engineering Methods*** | Letaw operationalises Agile practices (spike, planning poker, story points) that Jones reads critically. Use Letaw for how to run the practices; use Jones to know which outcome claims for those practices are evidence-based. |
| **OpenStax, *Psychology 2e*** | Provides deeper treatment of the cognitive-bias literature (anchoring, overconfidence, hyperbolic discounting) that Jones applies to software decisions. Use OB/Psych for the theory; Jones for the software-specific evidence. |
| **Barbrook-Johnson & Penn, *Systems Mapping*** | Both sources deal with decision-making under uncertainty in complex systems; both are critical of folklore-based decision rules. Jones focuses on the evidence base; Barbrook-Johnson on the structural mapping of the system that produces the outcome. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The deep reference contains the following `[BT]` citations — passages where Jones cites third parties not held as primary references in this corpus:

- *Grant-Sackman study (Sackman, Erikson & Grant 1968)* — not held. The source of the 28-to-1 productivity folklore claim; Jones cites the original paper and the corrected readings. The distillation's treatment of the 28-to-1 claim as folklore traces to Jones's reading of this source.
- *Jørgensen & Sjøberg (anchoring study)* — not held. Cited for the empirical finding that professionals' estimates are shifted by the customer's offered estimate. Key Concept 7 paraphrases Jones's rendering.
- *Klayman & Ha (Wason task analysis)* — not held. Cited for the positive-test-strategy finding in Key Concept 14.
- *Ericsson et al.* — not held. Cited for the 10,000-hours deliberate practice finding (Ch 2.5.2). Not surfaced in this distillation's Key Concepts but underlies the student-vs-professional performance gap cited in Anti-patterns.
- *Anderson, Newell, Baddeley* — not held. Cognitive psychology lineage cited for memory and cognition sections.
- *Gigerenzer* — not held. Cited for fast-and-frugal heuristics.
- *Tockey, Return on Software* — not held. Cited as recommended reading on software economics.
- *Brealey & Myers, Principles of Corporate Finance* — not held. Cited for corporate finance framing applied to software investment decisions.
- *Kahneman, Thinking Fast and Slow* — not held. Implicit through the cognitive-bias treatment; not directly cited by name in the body but underlying the bounded-rationality framing.

The book cites approximately 2,035 bibliography entries; the above are those most directly load-bearing for Key Concepts in this distillation.

**Named limits of the source.** Jones is explicit that the book's contents are dictated by the available public data, not by the importance of topics, and that coverage is "very patchy." The book does not cover: specific technology choices (Python vs Java, AWS vs Azure); detailed Agile vs Waterfall comparative analysis (the book is Agile-critical, not Agile-prescriptive); ethics and security; accessibility. Jones explicitly labels much of his own analysis as HARKing ("Hypothesizing After the Results are Known") and warns readers not to treat it as rigorous science.

**Evidence-marker continuity.** This distillation paraphrases throughout; verbatim passages live in the deep reference (`jones-evidence-based-sweng-deep.md`). Key `[V]` passages that this distillation paraphrases — including the seller's-market framing (Ch 1, "Introduction"), the story-processor framing (Ch 2.6, "Reasoning"), the Goodhart's Law citation (Ch 13.1.1, "Cultural influences"), and the cone-of-uncertainty critique (Ch 5.4.4, "Managing progress") — are cited by chapter and section name in the Key Concepts section above. Evidence markers from the source (`[AP]`, `[AR]`) are preserved in the deep reference and should be consulted when using a Jones claim as load-bearing evidence in a decision context.
