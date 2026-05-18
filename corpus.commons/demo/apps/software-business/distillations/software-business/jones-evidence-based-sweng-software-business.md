# Jones, Evidence-based Software Engineering, Software-Business Distillation

**Source:** Derek M. Jones (2020). *Evidence-based Software Engineering: based on the publicly available data*. Version 1.0. ISBN 978-1-8382913-0-3. CC BY-SA 4.0. http://www.knosof.co.uk/ESEUR/. **Distribution note:** This distillation is a derivative of a CC BY-SA 4.0 source and carries the same SA copyleft obligation.

**Source slug:** `jones-evidence-based-sweng`
**Task:** `software-business`
**Lens sections:** `business-executive-stakeholder` (partial reshape, Phase 6)

## Software-Business Relevance

Jones is the corpus's empirical anchor for software-specific economic and operational claims. Where the decision-making distillation reads Jones for the *generic decision-quality* lessons (anchoring, hyperbolic discounting, the investment frame) and the stakeholder-engagement distillation reads him for the *vendor-client information dynamics*, the software-business projection sits at the intersection where the technical and the commercial constrain each other simultaneously. Jones frames software engineering as "an economically motivated cognitive activity occurring within one or more ecosystems" (Ch 1, "Introduction") — and the software-business task is what happens when a founder, CTO, engineering manager, or technical product leader has to price, hire, structure, or report against that frame.

The distinctive contribution of Jones to this axis: empirical corrections to the rules-of-thumb that drive most software-business decisions. The post-1980 evidence collapse in software-engineering research (Ch 1) means most of what the practitioner has heard is folklore unsupported by data. Grant-Sackman's "28:1 developer productivity range" corrects to roughly 6:1 once batch-vs-time-sharing is separated out (Ch 1, "Folklore"; Ch 2.8.7). The "maintenance dominates over development" claim collapses to a survival-adjusted ratio of ~0.8 once project-cancellation is factored in (Ch 4.5.2). The "cone of uncertainty" is a mathematical artefact of axis choice, not a project-management law (Ch 5.4.4). KLOC, Halstead volume, and McCabe complexity all scale with each other and are "easily manipulated by splitting functions" — "the software equivalent of what is known as accounting fraud" (Ch 6.4.2; Ch 7.1.4). Jones supplies the evidential ground for the software-business practitioner to push back when consultant decks, board-paper framings, or industry-norm benchmarks invoke the folklore.

What this projection deliberately surfaces over the decision-making and stakeholder-engagement projections: cognitive capitalism as the economic frame for hiring, retention, and AI-integration decisions (Ch 3); agency theory and moral hazard for vendor and contractor decisions (Ch 3.4.6–3.4.7); the bi-exponential fault pattern as a reliability-investment guide (Ch 6.3.1); the asymmetric cost structure of COTS faults for pricing reliability work (Ch 6.2); and the *software-as-intangible-product* framing that anchors price, CLV, and Bass-diffusion calculations (Ch 3.6.3, Ch 3.6.4).

## Key Concepts for Software-Business

1. **The post-1980 evidence collapse as the operating context.** Since approximately 1980, very little published software-engineering research has been evidence-based; a systematic review of 5,453 papers (1993–2002) found 2% reporting experiments, 1.9% controlled experiments, of which 72.6% used students only. This is the operating context for every software-business decision: the literature the practitioner reaches for is mostly folklore. Treat industry-norm claims with explicit scepticism unless the underlying data is available. (Source: Ch 1, "History of software engineering research"; Ch 13.1, "Introduction")

2. **Grant-Sackman 28:1 corrected to ~6:1.** The famous productivity-range claim conflated batch-vs-time-sharing system differences with subject performance. Separated, max difference is 14:1 and min is 6:1; Dickey's 1981 reanalysis adjusting for individual subject differences found 1:5. Productivity-difference claims justify staffing decisions, compensation differentials, and investments in tooling — most of which are built on the 28:1 folklore. (Source: Ch 1, "Folklore"; Ch 2.8.7, "Developer performance")

3. **Software as intangible-product economics.** Software systems "are intangible goods that are products of cognitive capitalism; human cognition is the means of production" (Ch 3.1). Capitalist structures evolved for tangible goods and are being slowly adapted; the cost of replicating software is effectively zero, which inverts the economics of inventory, marginal cost, and capacity. For software-business decisions, this reframes everything from pricing (no marginal cost) to hiring (the cognitariate's labour is the means of production) to acquisition valuation (intangibles dominate the balance sheet). (Source: Ch 3.1, "Introduction"; Ch 3.4, "Group dynamics")

4. **Cognitive capitalism: the social factory.** Organisations whose income is derived from cognitive output are "social factories" — free meals, laundry, on-site amenities are not perks but mechanisms for "bringing employees together and creating life-norms that limit alternative employers, i.e., reducing knowledge loss and spillover" (Ch 3.3). Engineering management decisions about culture, perks, and workplace design are extraction mechanisms in this frame, not benefits. The software-business practitioner reading hiring decisions, retention investments, or remote-work policy should see them through this lens. (Source: Ch 3.3, "Capturing cognitive output")

5. **Software-development cost as 19% of revenue.** Across SIC 7371/7372 software companies, software development runs around 19% of revenue, with sales and marketing 22–40% and general & admin 11–22%, leaving the remainder as profit and taxes (Ch 3.1, "Introduction"; Figure 3.4). This is a useful benchmark for board memos and investor decks where the question is whether engineering spend is high, low, or normal for the business model. (Source: Ch 3.1, "Introduction")

6. **Irreversible investment + survival-adjusted ROI.** Creating software is an irreversible investment — incomplete software has little resale value, even completed software may not. The standard ROI/NPV calculation must be adjusted for survival: with annual application survival rates of 0.79 (Google SaaS, Ogden) to 0.87 (mainframe, Tamai), software half-lives are approximately 2.9–5 years. The cost-effectiveness of any maintenance-cost-reducing development-time investment must include the risk that the project is cancelled or the software has no future. (Source: Ch 3.2, "Investment decisions"; Ch 3.2.3, "Incremental investments and returns"; Ch 4.2.2, "Lifespan")

7. **Survival-adjusted maintenance-to-development ratio is ~0.8, not 5:1.** The often-cited claim that maintenance dominates over development is based on snapshot-based analyses that suffer from survivorship bias. Adjusted for system survival, the actual ratio is closer to 0.8 — less than one (Ch 4.2; Ch 4.5.2, "Pounding the treadmill", Dunn IBM dataset). The correlation between development and maintenance man-hours is 0.5 (95% CI 0.38–0.63). This radically changes the case for upfront over-engineering, internal-quality investment, and technical-debt-paydown roadmap allocations. (Source: Ch 4.2, "Evolution"; Ch 4.5.2, "Pounding the treadmill")

8. **"Technical debt" is not a financial concept.** The metaphor is "incorrect, there is no debt, and there may not be any need for more work in the future" (Ch 3.2.5). Real-options analysis is the correct frame: implementing functionality with minimum investment, with the intent of investing more later, has the form of an American call option. The option may or may not be exercised; the strike price is the rework cost; the option is worth more under uncertainty. Board memos and roadmap documents that price "technical debt" as a liability are pricing a phantom; the practitioner should reframe to option-value. (Source: Ch 3.2.5, "Real options")

9. **Estimates are commitments under social pressure, not predictions.** Resource estimates are subject to anchoring (the customer's offered estimate strongly shifts professionals' estimates, per Jørgensen and Sjøberg), round-number preference (Jones-and-Cullum agile data shows peaks at multiples of seven hours and almost no estimates of 6, 8, or 9), and unit-of-measurement effects (work-hours vs work-days produce different numbers for the same work). Estimation models give wildly varying estimates for the same project (Mohanty 1981: 12 models, widely varying outputs). The software-business practitioner reading a roadmap, hiring plan, or capacity model should treat the underlying estimates as commitments under social pressure with large intrinsic variation. (Source: Ch 5.3, "Resource estimation"; Ch 5.3.1, "Estimation models"; Ch 2.7.1, "Numeric preferences")

10. **The cone of uncertainty is a mathematical artefact.** The cone shape that appears in plots of Actual/Estimated against percentage-completed is "at best useless" — it is created by the choice of axis, not by a genuine project-management phenomenon (Ch 5.4.4). Roadmap-document conventions that show widening or narrowing cones to communicate estimation precision are smuggling in a claim the data does not support. (Source: Ch 5.4.4, "Managing progress")

11. **The bi-exponential fault pattern.** Repeated experiments on the same fault populations show that the number of times the same fault is experienced (sorted in rank order) is well fitted by a bi-exponential equation a × e^(bx) + c × e^(dx) — the two exponentials being driven by the two independent processes that interact to produce a fault experience: input-value distribution and source-code mistakes (Ch 6.3.1). Observed in Microsoft Office fuzzing, GCC fault reports, and KDE reports over 18 years. For reliability investment decisions, this means a small set of inputs drives most fault experiences — the right investment is in shaping the input profile and instrumenting the high-frequency patterns, not in pursuing comprehensive defect-free code. (Source: Ch 6.3.1, "Input profile")

12. **Asymmetric reliability cost in COTS software.** "The customer bears the cost of the fault experience itself, while the vendor can choose whether to fix the mistake and ship an update" (Ch 6.2). This cost asymmetry shapes pricing, SLAs, support contracts, and the question of how much reliability investment is commercially justified. One study found only 2.6% of NVD-listed vulnerabilities have been used in viruses and network threat attacks — so most security-investment decisions are about likely-never-exploited surface area. (Source: Ch 6.2, "Maximizing ROI")

13. **KLOC, Halstead, and McCabe are folklore metrics.** Halstead volume and McCabe cyclomatic complexity both scale with LOC for the 62,365 C functions in Linux 2.6.9 with at least 10 lines: Halstead_volume ∝ KLOC^1.1, McCabe_complexity ∝ KLOC^0.8 (Ch 7.1.4). The McCabe metric is "easily manipulated by splitting functions with high values into two or more functions, each having lower metric values… The software equivalent of what is known as accounting fraud" (Ch 6.4.2). When a board paper or vendor pitch cites complexity-metric improvements as evidence of engineering progress, treat as accounting-fraud-equivalent unless paired with empirical fault-rate or maintenance-cost data. (Source: Ch 7.1.4, "Folklore metrics"; Ch 6.4.2, "Source code")

14. **Agency theory and moral hazard in vendor-client relationships.** Information asymmetry between client and vendor structures the build-vs-buy decision, the contractor-mix decision, the AI-vendor-selection decision, and the acquisition-integration decision (Ch 3.4.6–3.4.7). Once a vendor has implemented a system, they have intimate familiarity that deters competing maintenance bidders. Moral hazard occurs when the more-informed party has control over unobserved attributes — developers making implementation decisions on personal enjoyment or career incentives rather than client interest. Agency theory is the analytic frame; mitigation mechanisms include source-code escrow, public APIs, transparent change-control, and documentation deliverables. (Source: Ch 3.4.6, "Information asymmetry"; Ch 3.4.7, "Moral hazard")

15. **Team-communication overhead and Brooks's Law quantified.** Assuming each team member spends t₀ fraction of time communicating, peak effective team size before adding people starts reducing output is Dpeak = (1 + t₀)/(2t₀); for t₀ = 0.1 (10% communication overhead per member), peak size is about 5 (Ch 5.5, "Development teams"). Brooks's Law has a quantitative derivation: the condition under which adding a new person doesn't delay the project is Te < (Dr − Dt)(En − (1 − c)Ea1) (Ch 5.5.1). Capacity-planning, team-restructuring, and hiring-against-deadline decisions should be priced against these quantitative limits, not against the qualitative "adding people to a late project makes it later" maxim. (Source: Ch 5.5, "Development teams"; Ch 5.5.1, "New staff")

16. **Bass diffusion model for new-product adoption.** Customer adoption follows innovators + imitators; peak sales occur at time t = (1/(p+q)) × ln(q/p) and peak volume at m(1/2 − p/2q) ln(q/p) when imitators dominate (Ch 3.6.3). This is a defensible quantitative frame for product-launch, market-entry, and capacity-planning decisions tied to expected adoption. (Source: Ch 3.6.3, "Predicting sales volume")

17. **Customer lifetime value under regular maintenance payments.** CLV calculations using regular maintenance payments give a structured way to value retention investments, support-contract design, and customer-success spend (Ch 3.6.4). Combined with the irreversible-investment frame, this gives the software-business practitioner a quantitative basis for the "managing customers as investments" decision. (Source: Ch 3.6.4, "Managing customers as investments")

18. **Goodhart's Law as a brake on measurement-driven decisions.** "Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes" (Ch 13.1.1). When velocity, story points, deployment frequency, MTTR, or any other engineering measurement is used to control or evaluate the team, the measurement loses its statistical regularity. Board reports and OKR designs that lean on metrics-as-controls should be designed with Goodhart's Law as a structural constraint. (Source: Ch 13.1.1, "Measurement uncertainty")

19. **The waterfall myth.** Royce 1970, which "gave birth to this [waterfall] demon meme," contained a diagram and accompanying text *warning against* the approach; subsequent pages showed the recommended iterative alternative. The "how not to do it" diagram was nonetheless taken up and "included in the first version of an influential standard, DoD-Std-2167, as the recommended project management technique" (Ch 5.4.1). Methodology choice is path-dependent on misreading of historical sources — useful context for any "we've always done it this way" defence of a development process. (Source: Ch 5.4.1, "Development methodologies")

20. **Cost-of-fixing-faults grows-by-orders-of-magnitude is NASA/DOD-specific.** The widely cited 1:10:100 figures for cost-of-fix at requirements vs design vs post-release come from NASA and DOD data where hardware costs were extreme; "in commercial development cost ratios are much smaller" (Ch 6.6). Investment cases for shifting quality work earlier in the lifecycle should not lean on these figures uncritically — the commercial-software context is different from the avionics context that generated them. (Source: Ch 6.6, "Checking for intended behavior")

## Questions to Ask During Software-Business Work

### Phase 1: Strategic positioning (pricing, market entry, build-vs-buy, AI integration)

| Need | Question | Source-tag |
|---|---|---|
| Price a feature against engineering effort and competitor parity | What is the marginal cost (near zero) vs the value-capture mechanism? Have I priced against intangible-product economics or against tangible-goods intuitions? Is the price dead zone (manager sign-off ceiling, sales-rep minimum) being respected? | Ch 3.1; Ch 3.6.2 |
| Make a build-vs-buy decision under information asymmetry | What is the information-asymmetry structure? Once we buy, the vendor has the intimate-familiarity moat — what mitigation mechanisms (source escrow, public APIs, documentation deliverables) are written into the contract? What does agency theory predict about the vendor's incentives over the next 3–5 years? | Ch 3.4.6, Ch 3.4.7 |
| Evaluate market entry where engineering is a barrier | Do economies-of-scale arguments apply (they often don't, given near-zero replication cost), or do network effects and switching costs dominate? Where is the Arthur lock-in threshold for the competing technologies in this niche? | Ch 4.2.3, Ch 4.3 |
| Make an AI-integration decision (productisation, build/buy, vendor selection) | Am I treating this as a cognitive-capitalism extraction question (whose labour is being captured, by whom, with what spillover) or as a productivity-tool question? What does the agency-theory analysis say about the AI vendor's incentives? | Ch 3.3, Ch 3.4.7 |
| Forecast new-product adoption for a planned launch | Have I fitted a Bass diffusion model to comparable products to estimate peak volume and timing? What are the p and q parameter estimates I'm using, and what's their basis? | Ch 3.6.3 |
| Value customer retention investments | Have I computed CLV under regular-maintenance-payment assumptions? Is the retention investment priced against expected lifetime value with appropriate discount? | Ch 3.6.4 |

### Phase 2: Product and engineering economics (technical-debt servicing, capacity planning, ROI, reliability-as-business)

| Need | Question | Source-tag |
|---|---|---|
| Justify or reject a technical-debt remediation programme against revenue work | Have I named the rework as a call option rather than as a debt? What is the strike price (rework cost), and what is the option's value under current uncertainty? If the survival rate suggests the system won't outlive the option's expiry, is the option worth exercising at all? | Ch 3.2.5, Ch 3.2.3 |
| Price a reliability investment against a commercial milestone | What does the bi-exponential fault-experience pattern imply about which inputs are driving most failures? Is the investment targeting the high-frequency tail or the long tail? What is the asymmetric cost (customer bears fault, vendor decides on fix), and does pricing recover that for the vendor? | Ch 6.3.1, Ch 6.2 |
| Plan capacity (hiring, contractor mix, team size) under uncertainty | What is the team-communication overhead at the proposed size (Dpeak = (1+t₀)/(2t₀))? Does the hiring plan account for Brooks's Law's quantitative form? Are estimates anchored on round numbers and on the requester's first number? | Ch 5.5, Ch 5.5.1, Ch 5.3 |
| Diagnose a roadmap-capacity mismatch | Which estimation model produced these numbers, and what is the model's known variance? Have I checked for anchoring (the customer's number), round-number preference (peaks at 7h), and unit-of-measurement effects (hours vs days)? Are different stakeholders working from different estimates of the same work? | Ch 5.3, Ch 5.3.1 |
| Resolve a "speed vs quality" tension | What is the survival-adjusted maintenance-to-development ratio for this kind of system (likely ~0.8, not 5:1)? If the system won't survive long enough for maintenance to dominate, the speed-vs-quality trade-off is differently weighted than the folklore suggests. | Ch 4.5.2 |
| Decide whether to invest in code-quality tooling or process change | What is the empirical evidence base for the proposed intervention? Is this a post-1980 evidence-collapse claim, or is there published controlled-experiment data with appropriate power? | Ch 1, Ch 13.1 |
| Budget for engineering as a fraction of revenue | How does our software-development-spend as a fraction of revenue compare to the SIC 7371/7372 benchmark (~19% development, 22–40% S&M, 11–22% G&A)? What does the variance tell us about our cost structure? | Ch 3.1 |

### Phase 3: Team and capability building (hiring, structure, levelling, succession)

| Need | Question | Source-tag |
|---|---|---|
| Set compensation differentials | Am I citing the 28:1 productivity-range folklore to justify differentials, or the corrected 6:1 (or smaller) figure? What does the company's measurement evidence actually support? | Ch 1, Ch 2.8.7 |
| Design hiring or role-structure decisions for engineering | Have I priced the team-communication overhead at the proposed structure? Is the team size at or near Dpeak? Are role boundaries reducing or increasing the t₀ communication fraction? | Ch 5.5 |
| Design retention investments (perks, on-site amenities, culture) | Am I designing the social-factory mechanisms (life-norm creation, knowledge-loss reduction, spillover prevention) explicitly, or am I copying perks from competitors without naming what they extract? | Ch 3.3 |
| Decide on contractor vs employee mix | What does agency theory predict about each option's incentive structure? What's the moral-hazard exposure with contractor work, and how is it being mitigated (deliverable-based payments, transparent IP arrangements, knowledge-transfer requirements)? | Ch 3.4.6, Ch 3.4.7 |
| Plan for knowledge transfer and succession | The intangible-product framing implies knowledge loss is the main cost of departure; what mechanisms are in place to externalise tacit knowledge before key staff leave? What's the survival-rate analogue for individual contributors (tenure-adjusted retention curve)? | Ch 3.3, Ch 3.4 |
| Evaluate developer-measurement systems | Will the measurement be used for decision-making (formative) or for control/evaluation (summative)? If the latter, expect Goodhart's-Law collapse — what mitigation is in place? Has the company tried (and how to read failures of) "measuring developer productivity"? | Ch 13.1.1, Ch 2.8.7 |

### Phase 4: Operations and process (delivery cadence, governance, decision rights)

| Need | Question | Source-tag |
|---|---|---|
| Defend a methodology choice (waterfall, iterative, agile-flavour) | Is the chosen methodology being supported by post-1980 evidence-base research, or by folklore? Specifically: has the Royce-1970-misreading-as-waterfall history been confronted? Is the iterative argument relying on Lehman-style empirical work or on consultant decks? | Ch 5.4.1 |
| Set or reset measurement systems | Which measurements are formative (decision-support) and which are summative (control)? Have I designed against Goodhart's-Law collapse on the summative ones? | Ch 13.1.1 |
| Communicate estimate uncertainty in roadmap documents | Am I using cone-of-uncertainty graphics? If so, am I aware they're a mathematical artefact, not a genuine project-management phenomenon? What's the alternative communication mechanism — direct equation + coefficient uncertainty, scenario ranges, prediction-interval reporting? | Ch 5.4.4, Ch 8.3.4 |
| Diagnose a chronically-late delivery system | Is the team at or above Dpeak for its communication overhead? Are estimates being anchored on the customer's number? Have round-number preferences and unit-of-measurement effects been controlled for in the estimating process? | Ch 5.5, Ch 5.3 |
| Defend a static-analysis or code-review investment | What is the false-positive rate of the analysis tool, and at what point does the consecutive-false-positive cascade cause developers to disengage from the tool? Is the manual code-review staffing past Nielsen-Landauer's diminishing-returns curve? | Ch 6.6.1, Ch 9.1 |

### Phase 5: Risk, reliability, compliance (incidents, security, legal, ethics)

| Need | Question | Source-tag |
|---|---|---|
| Price reliability or security work as a business decision | Where is the cost falling — on the customer (COTS asymmetric cost) or on the vendor? What fraction of CVE-style vulnerabilities are actively exploited (one study: 2.6% of NVD-listed)? Is the investment targeting the long tail or the high-frequency bi-exponential peak? | Ch 6.2, Ch 6.3.1 |
| Set a quality investment threshold | Many coding mistakes never produce a fault experience — Danglot et al. showed perturbations often had no observed effect; soft-error studies found >80% of bit-flips have no detectable impact. What fraction of detected defects produce customer-visible failures, and what fraction of fixes are worth the cost? | Ch 6.3.2 |
| Decide on a compliance investment with engineering cost | What is the survival-adjusted cost-benefit of the compliance work? Is the compliance period likely to outlast the system itself (annual application survival 0.79–0.87)? | Ch 3.2.3, Ch 4.2.2 |
| Translate technical-debt remediation into a board-paper investment case | Am I framing this as debt repayment (incorrect financial metaphor) or as call-option exercise (correct frame)? What's the strike price and the expiry? | Ch 3.2.5 |
| Communicate a software-related incident to commercial stakeholders | What was the input pattern (bi-exponential analysis: was this a high-frequency input or a rare edge case)? What was the cost asymmetry (who bore the cost)? What's the case for or against changing the cost asymmetry going forward? | Ch 6.3.1, Ch 6.2 |

### Phase 6: Stakeholder communication (board, exec, investor, customer)

| Need | Question | Source-tag |
|---|---|---|
| Produce a board memo on engineering investment or technical risk | Which folklore claims is the board likely to bring in (28:1 productivity, 5:1 maintenance, technical-debt-as-debt, cost-of-fixing-faults orders-of-magnitude)? Have I prepared the empirical corrections (~6:1, ~0.8 survival-adjusted, real-options framing, NASA/DOD-specific)? Is the engineering-spend-as-fraction-of-revenue benchmark (~19%) cited where it helps frame the ask? | Ch 1; Ch 2.8.7; Ch 4.5.2; Ch 3.2.5; Ch 6.6; Ch 3.1 |
| Defend a measurement choice to an executive who wants metrics | What measurements are being used for decision-making vs control? Have I named Goodhart's Law as the structural constraint on summative use? What's the proposed alternative for the control question (qualitative review, peer assessment, outcome measures rather than activity measures)? | Ch 13.1.1 |
| Communicate engineering progress to investors | Am I framing engineering output as a tangible-goods deliverable (LOC, story points, features shipped) or as an intangible-product investment (capability built, options created, knowledge captured)? Investors read either, but the framing implies different ROI expectations. | Ch 3.1 |
| Communicate reliability or security work to customers | What's the asymmetric-cost framing — what does the customer actually bear today, and what does the investment shift? Is the reliability claim framed against empirical fault patterns or against industry "best practice"? | Ch 6.2, Ch 6.3.1 |
| Negotiate a cross-function decision (engineering vs sales vs product) | Where is the moral-hazard exposure in each party's incentive structure? What information asymmetry exists between the parties? How does that asymmetry affect the negotiation? | Ch 3.4.6, Ch 3.4.7 |

### Through the `business-executive-stakeholder` lens

This lens reweights Phase 6 (and to a lesser extent Phase 4 governance-and-measurement) when the audience is a Paradigm-A-operating executive — one whose operating vocabulary is plan, commitment, KPI, named owner, variance against plan. Jones's empirical findings are most usable here when translated into that operating vocabulary, with the Paradigm-B reframes offered parsimoniously and as choices the stakeholder can take or leave.

The Jones-specific reweighting:

- **Folklore corrections land as register signal, not as content.** When a board paper cites 28:1, 5:1 maintenance-to-development, or 1:10:100 cost-of-fix, the executive's read is "this writer is repeating the industry consensus." The Jones-grounded correction (6:1, 0.8, NASA/DOD-specific) lands not as a content update but as a register-shift: it tells the executive that the writer has done the empirical work and is not deferring to consensus. Lead with the corrected number stated in Paradigm-A form (committed, with a named source: *"Updated industry-comparable benchmark: 0.8, not 5:1 — survival-adjusted across the Dunn dataset"*).
- **Technical-debt-as-call-option is a Paradigm-B reframe; deploy parsimoniously.** The financial reframe (no debt, call option) is the kind of structural acknowledgment that wins respect when offered once and undermines the artefact when deployed throughout. Make it once, name it explicitly as a reframe (*"The right financial analogue is a call option, not debt; here's the strike price and the expiry"*), and return to Paradigm-A operational vocabulary for the rest of the memo.
- **The empirical posture supplies KPI legitimacy.** When the executive asks for a KPI to track engineering quality, Jones supplies the empirical argument against the easy KPIs (LOC velocity, story points, defect counts that collapse under Goodhart). The artefact should name the easy KPIs, name the collapse mechanism, and offer one Paradigm-A-compatible alternative (committed quarterly survey, named outcome metric tied to a customer journey, etc.).
- **Anchor on the corrected number, not on the folklore.** When the executive is anchored on industry-standard productivity claims, Jones-grounded corrections work best when they land *first* and *as commitment* — not as caveats to a prior estimate. Open with the corrected number, then explain the basis. The order matters: anchoring effects shift the executive's subsequent reasoning.

What recedes when the lens reads:

- The methodological argument (the post-1980 evidence collapse) is rich content for a CTO or for a technical peer, but reads as throat-clearing to the executive. Reduce to a single sentence of register-signal (*"This is based on published longitudinal data, not industry survey consensus"*) and move on.
- The Bass-diffusion equations, the Brooks's-Law quantitative form, the bi-exponential fault equation. These are the load-bearing artefacts for engineering-internal communication; they read as decorative complexity to the Paradigm-A executive. State the conclusion in plain English with the equation attached as appendix or footnote.
- Jones's contrarian critiques of academic publishing (peer-review pathologies, predatory journals, dataset-availability collapse). Out of scope for the executive memo; relevant context for the writer to know but not for the artefact to carry.

The lens's reshape of Phase 6 questions (selected): *"How am I going to land the empirical correction without making the writer's evidence-base posture the topic of the memo?"; "What's the one Paradigm-B move (technical-debt-as-call-option, measurement-as-Goodhart-trap, etc.) the artefact carries — and is it named as a reframe rather than asserted as the writer's worldview?"; "Where is the named owner, the KPI delta, the timeboxed action, and the decision being requested?"*

## What to Look For

**Pattern: A board paper or investment memo invokes industry-norm productivity, maintenance-cost, or cost-of-fix claims.**
- **Signal.** The memo cites 28:1 developer productivity, 5:1 (or 9:1) maintenance-to-development ratio, 1:10:100 cost-of-fixing-faults, "technical debt" as a financial concept, or "the cone of uncertainty narrows as we approach delivery."
- **Diagnosis.** The memo is repeating folklore unsupported by empirical work. The audience is likely to accept these as established facts unless the writer corrects.
- **Follow-up.** Bring the Jones-grounded corrections (Grant-Sackman → ~6:1; survival-adjusted maintenance ratio → ~0.8; NASA/DOD context for 1:10:100; technical-debt-as-option not debt; cone-of-uncertainty as mathematical artefact). Cite the deep reference for the underlying data.

**Pattern: A "developer productivity" measurement is being introduced to evaluate or rank engineers.**
- **Signal.** A new metric (velocity, story-points-per-engineer, defect-rate-per-developer, deployment-frequency-per-team) is being proposed for use in evaluation, ranking, or compensation decisions.
- **Diagnosis.** The measurement will collapse under Goodhart's Law once it's used for control rather than for decision-support. Within a year or two the metric will lose its statistical regularity and the team's behaviour will have shifted to optimise the measurement, not the underlying outcome.
- **Follow-up.** Name the formative-vs-summative distinction. Propose alternative summative mechanisms (peer review, outcome metrics, qualitative assessment) and reserve the metric for formative decision-support only.

**Pattern: A "rebuild from scratch" or "comprehensive refactor" investment case is being framed as technical-debt repayment.**
- **Signal.** The investment case uses debt vocabulary (paydown, principal, interest, repayment, accrued).
- **Diagnosis.** The financial metaphor is misleading the analysis. There is no debt; there may not be future rework. The investment may be the right call, but the framing is hiding the actual decision (exercise a call option whose strike price is the rework cost, whose expiry is the system's survival horizon).
- **Follow-up.** Reframe as real-option exercise. Name the strike price (rework cost). Name the expiry (system survival horizon — likely 3–5 years given the 0.79–0.87 annual survival rates). Assess whether the option is worth exercising at the current uncertainty level, or whether the option's value is increased by waiting.

**Pattern: A reliability or security investment is being justified by "industry best practice" without empirical fault-pattern analysis.**
- **Signal.** The investment case cites generic security-investment ROI, OWASP-prevalence rankings, or industry-vertical benchmark spending — without engaging with the actual fault-experience pattern of the system in question.
- **Diagnosis.** The investment is likely targeted at low-frequency surface area (2.6% of NVD-listed vulnerabilities are actively exploited; >80% of bit-flips have no detectable impact). The high-frequency bi-exponential peak — the few input patterns and source-code mistakes that drive most fault experiences — is being underweighted.
- **Follow-up.** Bring the bi-exponential fault-experience analysis. Ask what input patterns drive fault experiences in our system specifically. Reweight the investment toward the high-frequency peak (input-profile shaping, instrumented detection of the common patterns) and away from the long tail.

**Pattern: A capacity-planning or hiring decision is being made against a sprint-velocity target.**
- **Signal.** "We need N more engineers to hit the velocity for this roadmap" or "we'll restructure the team to add capacity."
- **Diagnosis.** The team may already be at or above Dpeak for its current communication overhead; adding people will increase the communication fraction and may reduce effective output (Brooks's Law in its quantitative form). Estimates anchored on the customer's number, round-numbered to the work day, may significantly under-state the actual variance.
- **Follow-up.** Compute Dpeak for the current and proposed team sizes. Stress-test the velocity estimates against round-number-preference and unit-of-measurement effects. Consider non-additive alternatives (reducing communication overhead, scoping reduction, decomposing into smaller independent teams).

**Pattern: An AI-integration decision is being framed as "AI is what the consultant deck says it is."**
- **Signal.** The decision is anchored on framings from vendor pitches or external advisory work, with the engineering-team's analysis being secondary or absent.
- **Diagnosis.** The cognitive-capitalism extraction frame is invisible; the agency-theory exposure to the AI vendor is unpriced; the moral-hazard structure of the vendor relationship is unaddressed.
- **Follow-up.** Apply the cognitive-capitalism frame: whose labour is being captured, by whom, with what spillover? Apply the agency-theory frame: what are the vendor's incentives, and what mitigation mechanisms (escrow, public APIs, data-portability commitments) are in place?

## When to Use This Reference

Reach for Jones when the question turns on a software-specific empirical claim that the practitioner needs to ground or to contradict. Specifically:

- The audience is anchored on a folklore claim (28:1 productivity, 5:1 maintenance ratio, 1:10:100 cost-of-fix, cone-of-uncertainty, technical-debt-as-debt) and the practitioner needs the empirical correction with citation.
- A software-economic claim needs evidence-based grounding (intangible-product pricing, social-factory extraction analysis, agency-theory exposure, Bass diffusion forecasting, CLV calculations under maintenance payments).
- A reliability or security investment case needs empirical fault-pattern analysis (bi-exponential pattern, asymmetric COTS cost, low NVD exploitation rate, low fault-experience rate from coding mistakes).
- A measurement decision needs the Goodhart's-Law structural constraint named, with the formative-vs-summative distinction.
- A methodology defence needs the historical evidence base (Royce-1970-misreading, post-1980 evidence collapse, evidence-base of agile claims).

Reach instead for the decision-making distillation when the question is about generic decision-quality (anchoring, hyperbolic discounting, the investment frame in general). Reach for the stakeholder-engagement distillation when the question is about vendor-client information dynamics or stakeholder-network identification. Reach for OpenStax Accounting Vol 2 (Goldratt, cost-classification) when the question is primarily about commercial cost analysis without the software-specific empirical content. Reach for Letaw when the question is about software-engineering process discipline (RACI, microservices boundaries, methodology execution) rather than empirical economics.

## Worked Example

A founder-CEO of a 30-engineer B2B SaaS company is preparing a board paper to justify a 4-engineer-quarter investment in "platform reliability work" against a competing investment in "new feature velocity for upcoming customer commitments." The board has expressed scepticism about reliability investment; one director recently sent a McKinsey deck citing "9:1 maintenance-to-development cost as the case for upfront investment in quality."

The founder reaches for Jones (software-business projection) before writing the memo.

**What the projection surfaces:**

1. The 9:1 maintenance-to-development claim collapses to ~0.8 once adjusted for system survival (Ch 4.5.2). For a SaaS product with annual survival around 0.79 (Google SaaS, Ogden), the system half-life is ~2.9 years — most of the "maintenance cost" never materialises because the product is retired or rewritten before maintenance dominates. The board's anchoring on 9:1 is unsupported.

2. The reliability investment, if it goes ahead, should be priced against the bi-exponential fault-experience pattern (Ch 6.3.1): a small set of inputs drives most fault experiences; the right investment is in input-profile shaping and high-frequency instrumentation, not in comprehensive defect-free code. The memo should specify which high-frequency patterns the investment targets, not invoke comprehensive-quality language.

3. The competing feature-velocity case is also vulnerable to folklore corrections: if the team is already at or near Dpeak for its communication overhead, adding feature velocity by adding people will reduce effective output (Ch 5.5). The right capacity intervention may be reducing communication overhead, not adding engineers.

4. The board's "reliability vs feature velocity" framing is itself a tangible-goods intuition (you can only build one of them at a time, like you can only run one production line at a time). For an intangible product, the cost asymmetry is different (the customer bears the fault cost in COTS, the vendor decides; for SaaS the vendor bears more of it).

**The memo's shape (informed by the `business-executive-stakeholder` lens reshape):**

Opens with 1 sentence acknowledging the board's concern about reliability investment. Then opens the operational frame: the McKinsey 9:1 figure is the industry-consensus number, and the empirically-grounded survival-adjusted figure is 0.8 — the actual decision is therefore not about repayment of accrued maintenance debt (which doesn't exist in the empirical data) but about exercising a call option on platform-quality work whose strike price is 4 engineer-quarters and whose expiry is the system's survival horizon.

The memo then names the Paradigm-B reframe explicitly: *"The right financial analogue is a call option, not debt; here is the strike price, here is the expiry, here is the option value under current uncertainty."* It commits to the reframe in one bounded section, then returns to Paradigm-A operational vocabulary for the rest.

The closing names the decision: approve 4 engineer-quarters for input-profile shaping and high-frequency-pattern instrumentation, with named owner (the principal engineer), timeboxed first step (30-day input-pattern audit producing a ranked-fault-experience report), and 2 measurable success criteria (60% reduction in P1 incident frequency from the top-5 input patterns over the next 90 days; customer-perceived availability moves from current 99.5% to committed 99.9%).

The memo's appendix carries the empirical citations (Ch 4.5.2 survival-adjusted ratio, Ch 6.3.1 bi-exponential pattern, Ch 5.5 team-communication-overhead derivation) for the board members who want to verify, but the body of the memo states the conclusions in Paradigm-A form without leading with the methodology.

## Anti-patterns This Reference Helps Avoid

**Anti-pattern: Repeating folklore in board papers, investor decks, or roadmap documents.**
- **Signal.** Citations of 28:1 productivity, 5:1 or 9:1 maintenance-to-development, 1:10:100 cost-of-fix, "technical debt as debt," cone-of-uncertainty graphics, McCabe-complexity as a quality indicator.
- **Diagnosis.** The writer has accepted industry-consensus claims without checking the empirical base. The audience, taking the claims as established, will make decisions on a folklore foundation.
- **Follow-up.** Bring the Jones-grounded corrections. Replace the folklore claim with the empirically-grounded number, stated as commitment with citation.

**Anti-pattern: Pricing reliability or security work against industry-norm budgets rather than against the specific fault-experience pattern.**
- **Signal.** The investment case cites a percentage-of-revenue or percentage-of-engineering-time benchmark for reliability/security spend, without engaging with the system's actual fault-experience profile.
- **Diagnosis.** The investment will be uniformly distributed across surface area, most of which is low-frequency and unlikely-to-be-exploited. The high-frequency bi-exponential peak is underweighted.
- **Follow-up.** Demand fault-experience profiling before fixing the budget. Concentrate investment on the high-frequency patterns; treat the long tail as low-priority.

**Anti-pattern: Adding engineers to a late project to recover schedule.**
- **Signal.** Capacity-planning language framed as additive ("we need N more engineers to hit velocity").
- **Diagnosis.** Above Dpeak, adding people reduces effective output. The communication-overhead increase outweighs the additional capacity. Brooks's Law in quantitative form.
- **Follow-up.** Compute Dpeak. Consider non-additive alternatives: reduce scope, decompose into smaller independent teams, reduce inter-team coordination cost, delay the deadline.

**Anti-pattern: Using engineering metrics for both decision-support and team-evaluation.**
- **Signal.** A single metric (velocity, defects-per-engineer, deployment frequency) is used in standups, planning, *and* in performance reviews.
- **Diagnosis.** Goodhart's-Law collapse is structurally inevitable. Within 1-2 measurement cycles the metric will lose its decision-support utility because the team has shifted behaviour to optimise the measurement.
- **Follow-up.** Bifurcate the metrics: keep formative metrics for decision-support, develop separate summative mechanisms (peer review, outcome metrics, qualitative assessment) for evaluation.

**Anti-pattern: Framing AI integration as a productivity tool when it's a substrate decision.**
- **Signal.** The AI-integration case is built around faster current work, not around what becomes possible that wasn't before.
- **Diagnosis.** The cognitive-capitalism analysis is invisible; the agency-theory exposure to the vendor is unpriced. The decision is likely to land as derivative-of-consultant-frame rather than as native strategic choice.
- **Follow-up.** Apply the cognitive-capitalism frame (whose labour is being captured, by whom). Apply the agency-theory analysis (vendor incentives, moral hazard, mitigation mechanisms). Reframe the case in terms of capability built and options created, not in terms of productivity multiplied.

**Anti-pattern: "Rebuild from scratch" justified as technical-debt repayment.**
- **Signal.** The investment case uses debt vocabulary (paydown, interest, principal).
- **Diagnosis.** The financial metaphor is misleading the analysis. The actual decision is whether to exercise a call option whose strike price is the rebuild cost, whose expiry is the system's survival horizon — likely 3–5 years.
- **Follow-up.** Reframe as real-option exercise. Compute the option value under current uncertainty. Often the right move is to wait or to scope down, not to exercise.

**Anti-pattern: Defending waterfall (or any methodology) by appeal to "industry standard."**
- **Signal.** Methodology defence cites DoD-Std-2167, ISO 12207, or "industry best practice" as foundational.
- **Diagnosis.** Methodology choice is path-dependent on misreading historical sources (Royce 1970 *warned against* waterfall in the same paper that contained its diagram). Industry-standard documents have inherited the misreading.
- **Follow-up.** Don't defend by appeal to standards. Defend by appeal to the empirical fit between the methodology and the situation. Be specific about which situation (high-uncertainty, low-uncertainty, regulatory, exploratory).

## Integration with Other References

| Reference | Relationship | Where the projections differ |
|---|---|---|
| [`jones-evidence-based-sweng-decision-making`](../decision-making/jones-evidence-based-sweng-decision-making.md) | Same source, generic-decision-quality projection. The decision-making projection reads Jones for anchoring, hyperbolic discounting, investment-vs-option framing, Goodhart's Law as decision-quality brake. | This projection reads Jones for software-economic content (intangible-product economics, cognitive capitalism, survival-adjusted maintenance ratio, bi-exponential fault pattern, agency theory in vendor-client) that the decision-making projection touches only lightly or not at all. |
| [`jones-evidence-based-sweng-stakeholder-engagement`](../stakeholder-engagement/jones-evidence-based-sweng-stakeholder-engagement.md) | Same source, vendor-client-information-dynamics projection. The stakeholder-engagement projection reads Jones for network-identification (Lim/RALIC, PageRank), salience prioritisation (Mitchell-Agle-Wood), fixed-budget requirements allocation, agency theory and moral hazard from the *engagement-process* side. | This projection reads agency theory and moral hazard from the *commercial-decision* side: build-vs-buy, contractor mix, AI-vendor selection, acquisition target evaluation. The stakeholder-engagement projection asks *how do I engage these parties?*; this projection asks *what does the agency-theory analysis say about the commercial structure of the relationship?* |
| `openstax-accounting-vol2-software-business` (pending) | Complementary cost-classification + theory-of-constraints frame. OpenStax Accounting Vol 2 supplies the cost-classification primitives (fixed, variable, sunk, relevant), CVP analysis, breakeven, and Goldratt theory of constraints; Jones supplies the survival-adjusted ROI, the intangible-product framing, and the empirical corrections to industry-norm productivity and maintenance claims. | Combine the two for any pricing, build-vs-buy, or technical-debt-remediation memo: cost classification from OpenStax, survival adjustment from Jones, theory-of-constraints from OpenStax, communication-overhead Dpeak from Jones. |
| `letaw-handbook-sweng-methods-software-business` (pending) | Complementary process-discipline frame. Letaw supplies the process discipline (RACI, decision rights, triple-constraint, methodology execution, Conway's Law as applied to team structure); Jones supplies the empirical critique that lets the practitioner distinguish evidence-based process choices from folklore-based ones. | Combine for any methodology defence: Letaw for what the process actually says and how to execute it; Jones for whether the empirical evidence supports the process claim. |
| `openstax-principles-management-software-business` (pending) | Complementary on team-structure and motivation. OpenStax Principles of Management supplies Mintzberg's structures, Maslow/Herzberg/SDT motivation frameworks, environment-scan and five-forces analysis; Jones supplies the cognitive-capitalism reframe of motivation (the social factory) and the quantitative team-communication-overhead derivation. | Combine for hiring, structure, and retention decisions: Mintzberg for the structural taxonomy, Jones for the team-size quantification, OpenStax motivation theory for the levers, Jones cognitive-capitalism for the extraction analysis. |
| `openstax-principles-marketing-software-business` (pending) | Complementary on pricing and customer-lifecycle. OpenStax Marketing supplies pricing strategy, service-profit chain, customer-journey mapping; Jones supplies Bass diffusion, CLV under maintenance-payment structures, and the intangible-product cost reframe. | Combine for pricing memos and customer-investment cases: OpenStax for strategy and segmentation, Jones for forecasting and lifetime-value quantification. |
| `openstax-business-ethics-software-business` (pending) | Complementary on AI-ethics and cost-externalisation. OpenStax Business Ethics supplies normative-stakeholder frames, duty-of-care, and the social-contract argument; Jones supplies the cognitive-capitalism extraction analysis and the agency-theory frame. | Combine for AI-integration ethics, externalised-cost analysis, and any decision where the technical and commercial constrain each other through ethical considerations. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** Jones's argument rests on a large bibliography of datasets and studies this corpus does not hold as primary references. Key borrowed-through works cited in the deep ref:

- *Grant and Sackman (1968), the 28:1 productivity study* — origin of the folklore claim; corrected by Dickey (1981) and Prechelt (1999). None held as primary corpus references. Flagged [BT].
- *Jørgensen and Sjøberg — anchoring study on estimates* — professionals' estimates shift toward the customer's offered estimate (Ch 2.2.1, Ch 5.3.1). Flagged [BT].
- *Mohanty (1981) — twelve estimation models* — cited for wide variance across models for the same project (Ch 5.3.1). Flagged [BT].
- *Bass (1969) — diffusion model* — p/q parameter formulation (Ch 3.6.3). Not held as a primary reference. Flagged [BT].
- *Ogden (Google SaaS annual survival rate 0.79) and Tamai (mainframe annual survival rate 0.87)* — cited for software half-life calculations (Ch 3.2.3, Ch 4.2.2). Neither primary dataset is in the corpus. Flagged [BT].
- *Dunn IBM dataset* — cited for the survival-adjusted maintenance-to-development ratio of ~0.8 (Ch 4.5.2). Flagged [BT].
- *Danglot et al. — perturbations having no observed effect* — cited for the claim that many coding mistakes produce no fault experience (Ch 6.3.2). Flagged [BT].
- *NVD (National Vulnerability Database) — 2.6% exploitation rate* — cited for the claim that most NVD-listed vulnerabilities are never actively exploited (Ch 6.2). Primary data outside the corpus. Flagged [BT].

**Named limits of the source.** Jones is explicit about two scope limits. First, the content is dictated by available public data: "Adhering to this rule has led to a very patchy discussion" (Ch 1, "Read me 1st"). Second, Jones disclaims the rigour of his own models: "Most of these models were created by your author after seeing the data, what is sometimes known as HARKing... This is not how rigorous science is done" (Ch 1, "What has been learned?"). Both limits are load-bearing for a practitioner using Jones's empirical corrections: the corrections represent the best available evidence, but they are not immune to the same critique Jones applies to the folklore they displace. The distillation treats them accordingly — as strong-evidence positions, not as settled findings.

**Evidence-marker continuity.** The deep reference carries verbatim claims with [V] markers (the post-1980 evidence collapse quantification; the "intangible goods that are products of cognitive capitalism" framing; the "technical debt... there is no debt" claim; the bi-exponential fault equation description; the waterfall misreading account) and [AR] markers for Jones's own analytical positions (the cognitive capitalism reading of perks; the "social factory" interpretation). This distillation paraphrases [V]-marked content throughout Key Concepts and Questions; no verbatim blockquotes appear here. The 28:1-corrected-to-~6:1 figure is represented as an [AP] claim (Jones's interpretation of the Grant-Sackman reanalysis), not as a [V] verified finding, consistent with the deep ref's evidence classification.

## Trigger extensions surfaced by this source

The seed trigger→response table in task spec §2a already names Jones in 9 rows across Phases 1, 2, 3, and 5. Jones's content extends those triggers in two ways the spec did not anticipate:

| Phase | Trigger extension | Jones content |
|---|---|---|
| Phase 2 | Operator names a measurement-system design decision (KPIs for engineering, OKR for delivery, dashboard design) | Goodhart's Law (Ch 13.1.1) as the structural constraint; formative-vs-summative bifurcation as the design pattern |
| Phase 4 | Operator names a methodology-defence decision against external pressure (board, advisor, vendor advocating a specific methodology) | Post-1980 evidence-collapse (Ch 1) as the empirical context; Royce-1970-misreading (Ch 5.4.1) as the historical-correction; evidence-base critique of Agile (Ch 5.4.3) as the parity argument |
| Phase 6 | Operator names a board-paper decision where folklore claims are likely to be invoked by the audience | Pre-emptive folklore corrections (Grant-Sackman, KLOC, maintenance ratio, cost-of-fix, cone-of-uncertainty) as register-shift mechanism; Paradigm-A landing form per the `business-executive-stakeholder` lens |

The operator may want to fold these extensions back into the task spec §2a in a subsequent `creating-tasks` revision.

## Runtime triggers this source addresses

| Trigger (from task spec §2a) | Content from Jones that addresses it | Teach-in-the-moment script |
|---|---|---|
| Operator names a pricing decision tied to engineering effort | Intangible-product economics (Ch 3.1); price dead zone and pricing-strategy primitives (Ch 3.6.2); Bass diffusion for new-product launches (Ch 3.6.3); CLV calculations (Ch 3.6.4) | "Software has near-zero replication cost — your pricing is value-capture, not cost-recovery. Have you priced against the value-capture mechanism, the price dead zone, and the expected adoption curve?" |
| Operator frames a build-vs-buy decision | Agency theory and moral hazard in vendor-client relations (Ch 3.4.6–3.4.7); information asymmetry as a moat (Ch 3.4.6) | "The build-vs-buy decision is also an information-asymmetry decision. Once you buy, the vendor has the intimate-familiarity moat. What mitigation mechanisms — source escrow, public APIs, transparent change-control, documentation deliverables — are written into the contract?" |
| Operator names market entry or product-portfolio decision | Cognitive-capitalism chapter (Ch 3); ecosystem-dynamics and Arthur lock-in (Ch 4.3); software-development-spend benchmarks (Ch 3.1) | "Software market entry is shaped by network effects and switching costs more than by economies of scale, and the cognitive-capitalism analysis tells you what's being extracted. Where's the Arthur lock-in threshold for this niche?" |
| Operator describes an AI-integration decision | Cognitive-capitalism + agency-theory framing (Ch 3.3, Ch 3.4.7) | "AI integration is a cognitive-capitalism decision: whose labour is being captured, by whom, with what spillover? And it's an agency-theory decision: what are the vendor's incentives, and what mitigation is in place?" |
| Operator names technical-debt remediation against revenue work | Technical-debt-as-not-debt; real-options framing (Ch 3.2.5); survival-adjusted maintenance ratio (Ch 4.5.2); KLOC-power-law mythology (Ch 7.1.4) | "Technical debt isn't debt — it's a call option whose strike price is the rework cost and whose expiry is the system's survival horizon (likely 3–5 years given annual survival rates of 0.79–0.87). Is the option worth exercising at current uncertainty, or worth waiting?" |
| Operator describes a reliability investment against a commercial milestone | Bi-exponential fault-experience pattern (Ch 6.3.1); asymmetric COTS cost (Ch 6.2); NVD-exploitation statistics (Ch 6.2) | "Most fault experiences come from a small set of high-frequency input patterns — bi-exponential. The right investment is shaping the input profile and instrumenting the high-frequency peak, not comprehensive defect-free code. What's the fault-experience profile for this system?" |
| Operator names a capacity-planning decision | Team-communication-overhead Dpeak (Ch 5.5); Brooks's Law quantified (Ch 5.5.1); resource-estimation variance (Ch 5.3) | "Compute Dpeak for the current and proposed team sizes. Above Dpeak, adding people reduces effective output. Are estimates anchored on the customer's number? Round-numbered to the work day? Sensitive to unit-of-measurement?" |
| Operator describes a roadmap-capacity mismatch | Estimation-model variance (Ch 5.3.1, Mohanty 1981); anchoring + round-number preference (Ch 5.3); cone-of-uncertainty as artefact (Ch 5.4.4) | "Different estimation models give widely-varying numbers for the same project. The cone-of-uncertainty graphic is a mathematical artefact, not a planning law. What are the underlying anchoring effects on your roadmap estimates?" |
| Operator names a "speed vs quality" tension | Survival-adjusted maintenance ratio ~0.8 (Ch 4.5.2); Goldratt theory-of-constraints (referenced through OpenStax Accounting Vol 2) | "The 5:1-or-9:1 maintenance-to-development claim collapses to ~0.8 once you adjust for system survival. The 'invest in quality now to save maintenance later' argument doesn't work the way industry-norm framing implies for SaaS systems with 3-year half-lives." |
| Operator names a hiring or role-structure decision | Team-communication-overhead Dpeak (Ch 5.5); Grant-Sackman 28:1 corrected to ~6:1 (Ch 1, Ch 2.8.7) | "Compute Dpeak. Don't justify compensation differentials with 28:1 folklore — the corrected range is closer to 6:1, or even smaller. What does our measurement evidence actually support?" |
| Operator names a contractor / vendor / hybrid-team decision | Agency theory and moral hazard (Ch 3.4.6–3.4.7); social-factory extraction analysis (Ch 3.3) | "Agency theory and moral hazard are the analytic frames. What are the vendor's incentives over a 3-year horizon? What's the information-asymmetry mitigation written into the contract? Which decisions sit with the more-informed party?" |
| Operator names a compliance investment with engineering cost | Cost-as-decision-relative (cross-source with OpenStax Accounting Vol 2); survival-adjusted cost-benefit (Ch 3.2.3, Ch 4.2.2); evidence-base critique (Ch 1) | "Is the compliance period likely to outlast the system itself? Annual survival 0.79–0.87 means the compliance investment must be priced against a likely-shorter system lifetime than the compliance horizon assumes." |
| Operator names a CTO-to-board translation problem | Folklore corrections as register-shift (Ch 1, Ch 4.5.2, Ch 6.6); Paradigm-A landing form via `business-executive-stakeholder` lens; Goodhart's Law as KPI structural constraint (Ch 13.1.1) | "Anchor on the corrected number — 6:1 not 28:1, 0.8 not 5:1, real-options not debt. State the empirical correction as commitment, not as caveat. Make the Paradigm-B reframes once and named; keep the rest of the memo in Paradigm-A operational vocabulary." |
