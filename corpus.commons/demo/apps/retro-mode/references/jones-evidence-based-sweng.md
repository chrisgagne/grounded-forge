
# Jones, Evidence-based Software Engineering (light reference)

**Source:** Derek M. Jones (2020). *Evidence-based Software Engineering: based on the publicly available data*. Version 1.0. ISBN 978-1-8382913-0-3. http://www.knosof.co.uk/ESEUR/. Licence: **CC BY-SA 4.0** (copyleft — derivatives carry the SA obligation).
**Structure:** Two-part book. Part I (software engineering: Ch 1 Introduction, Ch 2 Human cognition, Ch 3 Cognitive capitalism, Ch 4 Ecosystems, Ch 5 Projects, Ch 6 Reliability, Ch 7 Source code, Ch 8 Stories told by data). Part II (data analysis methods: Ch 9 Probability, Ch 10 Statistics, Ch 11 Regression modeling, Ch 12 Miscellaneous techniques, Ch 13 Experiments, Ch 14 Data preparation, Ch 15 Overview of R). 628 figures, 2,035 bibliography entries, ~600 publicly-available datasets cited.

## Author's thesis (condensed)

The book takes the explicit position that, at the time of writing, evidence-based software engineering is essentially a blank slate. Software development has progressed as a craft rather than an engineering discipline because building software has been a seller's market — customers pay what it takes, and in a competitive market paying people to learn from mistakes that have already been made by many others is an unaffordable luxury. The book's organising claim is that software engineering should be analysed as an economically motivated cognitive activity occurring within one or more ecosystems, with three load-bearing inputs: human cognition (the labour of the cognitariate is the means of production), cognitive capitalism (the economics of intangibles differs fundamentally from the economics of tangible goods because the cost of replicating software is effectively zero), and ecosystems (software wears out and breaks through ecosystem change rather than through use).

A second load-bearing claim is that the dearth of evidence-based research has filled the field with folklore — the 28-to-1 productivity claim (Grant-Sackman 1968) and Halstead/McCabe complexity metrics are the canonical examples. A systematic review of 5,453 software-engineering papers (1993–2002) found 2% reported experiments and 72.6% of those used students as the only subjects. A third claim is that the contents of the book are dictated by what public data exists, not by what topics are important — leading to a deliberately patchy discussion that highlights how thin the evidence is for much current software-engineering theory. A fourth claim is that human cognitive characteristics — operating limits of brains that evolved in stone-age ecosystems — constrain software development more than the formal mathematical ideals researchers have historically applied to it.

## Software engineering as evidence-blind craft

Software ecosystems have been continually disrupted by hardware-cost decline averaging 17.5% per year. The three commercial eras are the IBM (mainframe) era, the Wintel era, and the Internet era. Until the early 1980s most software systems were developed for large organisations, with over 50% of US government research funding for mathematics and computer science coming from the DOD; the legacy of this first 30 years was a research agenda oriented towards building large software systems. After ~1980, very little published software-engineering research has been evidence-based, with academic publishing incentivising paper count and impact factor rather than rigour. Jones argues that researchers in computing departments tend to be more interested in algorithms and mathematics than the human factors and economic issues that dominate commercial software development, and that researchers with a talent for software engineering tend to leave the field. The Grant-Sackman 28-to-1 productivity claim is a casual reading of a table from a 1968 paper; the corrected ratio for individual subject performance is closer to 1:5 or 6-to-1.

## Human cognition as binding constraint

The collection of cognitive characteristics in *Homo sapiens* is the end-result of evolutionary survival pressures over millions of years. Software developers should not be expected to behave according to mathematical ideals; techniques must be fitted to the cognitive characteristics actually present in the human brain. Cognition and the environment are like two blades of a pair of scissors — both blades must mesh together. Most cognitive-psychology research is done on Western Educated Industrialised Rich Democratic (WEIRD) subjects; this is acceptable for software-engineering work because developers are typically WEIRD-educated. Short-term memory capacity is approximately two seconds of sound rather than 7±2 items (Chinese speakers can hold ~9.9 digits, English ~6.6, Welsh ~5.8). Expertise requires roughly 10,000 hours of deliberate practice; expertise in one domain does not transfer to another. Human reasoning is best understood as story processing rather than logic processing. Anchoring and confirmation bias shape estimation. Overconfidence is evolutionarily stable. Hyperbolic discounting (not exponential) describes time-variable preferences.

## Cognitive capitalism

Software systems are intangible goods that are products of cognitive capitalism; human cognition is the means of production. Software-development costs run around 19% of revenue at software companies; sales and marketing 22–40%; general and admin 11–22%. Creating software is an irreversible investment — incomplete software has little resale value. The survival-adjusted break-even ratio for development-time investments aimed at reducing future maintenance costs must factor in the risk that the system has no future. Annual application survival rate is approximately 0.87 for mainframe systems (Tamai 1991) and 0.79 for Google SaaS (Ogden 2020), giving half-lives of roughly 5 years and 2.9 years respectively. The Black-Scholes equation cannot be validly applied to software development because software production does not create liquid assets and the historical data needed is not available. *Technical debt* is rejected as a misuse of financial vocabulary — there is no debt because there may not be any need for more work in the future.

Organisations whose income is derived from cognitive output are "social factories"; free meals and laundry are not perks but a means of bringing employees together and reducing knowledge spillover. US software patents grew from 0 (before 1995) to 109,281 granted in 2014 (36% of all utility patents). Open-source-licence proliferation, the OSI vetting process, and the survival curve of approved licences are catalogued. Group-dynamics analysis: team communication overhead bounds effective team size at roughly 5 people for a 10%-per-pair communication overhead; Brooks's Law has a quantitative form that depends on training cost, training duration, and the production rate of the new team member.

## Ecosystems

Software ecosystem evolution is Lamarckian (acquired traits passed by copy-and-modify) rather than Darwinian, and replication is free. Software has unlimited lifetime in theory but depends on ecosystem stability in practice. Venture capital is a hits business — VC fees average 2% + 20% carry, and most public-market index investors over 20 years would have done better. Hardware diversity historically drove software diversity; the rise of Wintel and later open-source compilers eliminated most of it. Software-system lifespans have half-lives of years, not decades. Market-entry barriers analysed include economies of scale (which don't apply well to software), network effects (which do), and switching costs. The Arthur lock-in analysis governs technology-vs-technology competition with increasing returns. Closed-population mark-recapture (Chapman estimator) and open-population CJS/JS models from ecology are applied to estimate remaining fault populations.

The text takes the explicit position that mean total maintenance-to-development cost ratio is *less than one* when adjusted for survival — approximately 0.8 — contradicting the widely-cited claim that maintenance dominates over development. The correlation between development and maintenance man-hours is 0.5 (95% CI 0.38–0.63).

## Projects

Most software projects complete in under a year, contain less than 40 KSLOC, and use significant external-contractor effort. Project-success criteria are role-dependent — only *user happiness with the system* is common to all roles. Bidding decisions are driven by factors with little or no connection to technical aspects: keeping staff busy, bidding the maximum the client will pay, bidding low to recoup losses during maintenance. Standard form contracts almost universally favour the software company that wrote them. 90% of transportation projects under-estimate costs with average overrun 28%; software is similarly under-estimating. Multiple estimation models give widely-varying estimates for the same project. Function-point analysis methods are widely used but the function-point-to-cost mapping is highly variable. For multiple implementations of the same specification, the standard deviation in LOC is approximately one quarter of the mean.

Software development is a *punctuated information arrival process*. The Royce 1970 paper that "gave birth" to the waterfall demon actually warned against it; DoD-Std-2167 then enshrined the warned-against approach as the recommended technique. Iterative development has been independently discovered many times. The OSI seven-layer model is held up as the largest waterfall failure (documented first, vendor-implemented later) versus the IETF's rough-consensus-and-running-code iterative model. The widely-cited cone-of-uncertainty curve is a mathematical artefact of the choice of axis (plotting Actual/Estimated against percentage-complete) — at best useless as a project-management guide.

## Reliability

People are willing to continue using software containing faults if it delivers a worthwhile benefit. Software systems containing likely fault experiences are shipped because it is not economically worthwhile fixing all mistakes. Two events are required for a fault to occur: a mistake in the source, and input values that exercise the code containing the mistake. With COTS the cost asymmetry is that the customer bears the cost of the fault experience while the vendor chooses whether to fix and ship an update. Only 2.6% of NVD-listed vulnerabilities have been actively exploited in attacks.

Bi-exponential models fit the rank-ordered count of duplicate fault reports across many programs — possibly because two independent processes (input distribution and mistake distribution) must interact to produce a fault. Over 80% of code-level bit-flips have no detectable impact on program behavior. Halstead's volume and McCabe's complexity both scale as power laws of LOC; both metrics are easily manipulated by refactoring without changing the underlying logic ("software accounting fraud"). Hardware (radiation-induced soft errors) is a significant source of unreliability in modern memory — commodity DRAM has 1000 FIT/Mb, giving 4 GB systems an MTBF of approximately 33 hours; even ECC-corrected supercomputers see occasional uncorrected errors. Manual code review has diminishing returns — 50% of issues are found by only one reviewer in many studies. Combinatorial testing covers most faults: 90%+ of detected faults require interactions of fewer than 6 factors.

## Source code

Source code is a form of communication, but communicating with a computer is a take-it-or-leave-it transaction — Grice's cooperative-principle assumptions don't apply between developer and compiler. The text takes a cognitive-linguistics approach rather than a Chomskyan formal-syntax approach to source code. Most Java methods are very short (50% of all Java source lives in methods of ≤ 4 LOC); C functions are larger on average (50% of C source in functions ≤ 114 LOC). Halstead's metric and McCabe's complexity persist as folklore despite empirical work showing them comparable in predictive performance to LOC and easily manipulated. Identifier names represent ~40% of non-whitespace characters in C visible source; identifiers occurring in any two systems with the same spelling rarely exceed 12% of all identifiers, and 18% of the time two free-association subjects produce the same word for the same cue. Embedded C software has substantially fewer function parameters than desktop C software (Poisson λ ≈ 0.8 vs ≈ 2) because parameter-passing overhead matters on resource-limited hardware. Software changes only when developers have an incentive to spend time making the changes. Most files are only ever edited by one person.

## Stories told by data

The chapter is a methodology chapter on communicating numeric findings. Color is essential for plot information density. Logarithmic axes are appropriate when values span orders of magnitude but can hide useful information by spreading data out. Quantities plotted on each axis must be carefully analysed to avoid generating artificial relationships — the *defect-density-vs-LOC U-shape*, popularly cited to argue for an optimal function length, is a mathematical artefact of plotting F/LOC against LOC.

## Statistics, regression, and the toolkit

Regression modeling is the default hammer; the book prefers `glm()` over `lm()` because `glm` makes fewer assumptions about sample characteristics. The bootstrap is used everywhere closed-form alternatives are not available. The frequentist approach is used throughout, with explicit acknowledgement that "the p-value is the fall-guy of the frequentist approach". Bayesian methods are mentioned but not deployed — prior selection opens the door to bias from opinion and policy. Many software-engineering measurements fit Poisson, Exponential, or Negative Binomial distributions. Bi-exponential regressions fit fault-report duplicates well; cross-correlation reveals lag relationships in time-series data. Survival analysis (Cox proportional-hazards) is recommended when the parametric hazard distribution is uncertain.

Experimental design requires randomisation, careful subject selection, ecologically valid tasks, and control of confounding variables. Students are not representative of professional developers: students typically have 50–150 hours of programming experience vs 1,000–10,000 for professionals, and academic studies often call final-year undergraduates "experts" while industry would call them novices. Mechanical Turk subjects can stop at any time so attrition bias is a real concern. Benchmarking is full of measurement variability — SSD performance varies across runs, environment-variable size changes Perlbench performance, object-link order changes execution time, gcc release affects measured performance non-monotonically, and EC2 cloud instances show bimodal performance distributions. Goodhart's Law: any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes.

Data preparation often consumes 80%+ of analysis effort. Domain knowledge is essential to cleaning. The NASA MDP dataset, used by 58 of 208 fault-prediction papers (2000–2010), has many known quality problems including all-same-value columns and lines-of-code as fractional values.

## Key statistics

| Metric | Value |
|---|---|
| Hardware-cost decline per year | 17.5% |
| Software-engineering papers (1993–2002) reporting experiments | 2% / 1.9% (controlled) |
| Of which used students only as subjects | 72.6% |
| Annual application survival rate, mainframe (Tamai 1991) | 0.87 |
| Annual application survival rate, Google SaaS (Ogden 2020) | 0.79 |
| Mean total maintenance-to-development cost ratio (survival-adjusted) | ~0.8 |
| Correlation between development and maintenance man-hours | 0.5 (95% CI 0.38–0.63) |
| Short-term memory capacity in spoken digits (English) | 6.6 avg |
| Hours of deliberate practice at top violinist level by age 20 | 10,000 |
| % of NVD-listed vulnerabilities actively exploited | 2.6% |
| % of bit-flips with no detectable program-behavior impact | > 80% |
| % of Java source in methods of ≤ 4 LOC | 50% |
| % of C source in functions ≤ 114 LOC | 50% |
| Mean uniqueness of free-association responses across 5,018 cue words | 18% |
| Empirical PSP-trainee variation in problem-solution time | ~10× |
| Grant-Sackman 28:1 corrected to individual-subject ratio | ~6:1 or 1:5 |
| MC/DC min probability of detecting an incorrect condition | 93.75% |

## Key connections

- Cognitive psychology: Anderson and Newell (cognitive architecture), Baddeley (working memory), Gigerenzer (fast-and-frugal heuristics), Ericsson (deliberate practice and the 10,000-hours claim).
- Economics: Tockey on return-on-software, Brealey and Myers on corporate finance, behavioural economics applied to estimation.
- Probability and statistics: Feller, Grinstead and Snell, Olive, Crawley, Kuhn and Johnson, Box-Hunter-Hunter on experiments.
- Software-engineering process: Brooks's Law derived quantitatively (not as a maxim); the Royce 1970 waterfall paper read as a warning that was inverted in DoD-Std-2167; the Standish CHAOS report dismissed as failure-biased; Halstead and McCabe as folklore.
- Open data and reproducibility: Jones's own data-request experiment — of 574 requests, 26% received data, 35% no reply, 4% bounced email.

## Signature contrarian positions

1. **Evidence-based software engineering is a blank slate.** Most theories are folklore unsupported by data.
2. **Programmers should not be modelled as omnipotent logicians.** This view is driven by human self-image, a counter-productive mindset.
3. **Halstead and McCabe metrics are not useful.** Both scale with LOC and are easily manipulated by trivial refactoring.
4. **The 28-to-1 productivity range is a misreading.** The corrected figure is roughly 6-to-1 or smaller.
5. **Cost-of-fixing-faults grows by orders of magnitude with development phase is overstated.** The 1:10:100 figures are NASA/DOD artefacts of extreme hardware costs.
6. **The cone of uncertainty is at best useless.** It's a mathematical artefact of the plotting choice.
7. **Royce 1970 warned against the waterfall.** The same paper that introduced the diagram dismissed the approach; DoD-Std-2167 enshrined the warned-against design.
8. **Maintenance is not typically 5× development.** Survival-adjusted, the ratio is below 1 (~0.8).
9. **Strong typing improves reliability evidence is weak.** Where effects exist they are dwarfed by between-subject variation.
10. **The CHAOS report is not representative.** It explicitly asked subjects for failure stories.
11. **Bayesian methods inherit bias through the prior.** Frequentist methods are used throughout for practical reasons.
12. **Static-analysis false-positive rates determine tool adoption.** Developers stop using tools when false-positive rates exceed a threshold; this is modelled through the Ballot Theorem and hot-hand-style consecutive-false-positive analysis.

**Distribution note:** This light reference is a derivative of a CC BY-SA 4.0 source. Any further derivative carries the same CC BY-SA 4.0 obligation.
