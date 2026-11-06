# opennotebook-demo-C1-1

Converted sources: corpus.commons/demo/sources/converted

## Question

I'm CTO at a 140-person logistics SaaS. Three product lines, one engineering group of about 60 in nine squads. Every sprint overflows: we plan around 40 points, ship 25, and carry the rest into the next one. Marketing wants a feature a week for the growth push and says quality is engineering's problem; engineering says the churn numbers come from bugs. My head of engineering has set a "stretch" target of 40% more throughput by Q1 and tied the squad leads' bonus to it. Most developers sit on two or three squads at once, because the CEO's rule is that nobody is idle. Last month a bad release took the customer portal down for four hours; the postmortem named the developer who merged it, and he's now on a performance plan. The CEO's answer to all of this is to buy AI coding tools so we can "do both".

I need a two-page memo for the CEO that says what's actually going on here, what to change first and why that first, and where the thinking you're drawing on disagrees with itself.

## Answer

Each [slug] marks a citation of that whole source; Open Notebook cites sources, not passages.

# Memo to the CEO

**From:** CTO
**Re:** Why we ship less than we plan, what to change first, and where the advice disagrees

**How to read this memo.** Sentences with a bracketed citation report only what that passage says. Sentences that begin "My inference:" are my own reading and carry no citation. No source in this notebook covers four topics: whether our churn is caused by bugs, AI *coding* tools specifically (the AI material is about generative AI and automation in general), any measured cost of splitting people across squads, and blame-naming postmortems in software teams in particular.

---

## 1. What is actually going on

**We overload people, and work gets stuck.** The Open Practice Library describes how people "take on all new tasks that come in." When several of those tasks can resume at once, "the person gets overloaded, nobody knows how the progress is, and tasks get stuck in a progressed state where nobody else can help" [open-practice-library]. It says that working on one task, then the next, means "the person stays responsive, flexible and the status stays visible" [open-practice-library]. It also names "carried over stories" as a cause of "a loss of context" [open-practice-library].

My inference: Putting most developers on two or three squads is this overload pattern applied across the whole organisation. Our 15 points of carry-over each sprint add to the lost context.

**We plan past what we deliver.** The library lists "Velocity – How much has the team been able to produce recently" as a sprint-planning input [open-practice-library]. A Scrum guide in the notebook says planning should "Realistically forecast what Increment can be delivered in the upcoming Sprint" [approach-perfect-field-guide-scrum-events].

My inference: We ship about 62% of what we plan (25 of 40 points), so every sprint starts with a forecast that fails that test.

My inference: Even if we hit the full 40% stretch target, 25 points becomes 35, which is still below the 40 we plan. The target would not end the carry-over.

**The bonus rewards the wrong number.** A management text says hard goals help, but "If goals are perceived as too difficult or impossible, however, they lose their motivating effectiveness." It also says goals fail "when managers assign them without making sure that workers have accepted or committed to the goals" [openstax-principles-management].

An accounting text describes a manager whose decision "was based on his bonus being tied to his profitability and not linked to other factors such as dealership profitability or dealership reputation (customer satisfaction)" [openstax-accounting-vol2]. Our software-engineering source warns that "Performance need not be correlated with productivity" [jones-evidence-based-sweng].

My inference: A squad-lead bonus paid on story-point throughput has the same structure as that manager's bonus. Story points are the teams' own estimates, so the bonus invites inflated estimates and cut corners rather than more delivered value.

**Quality is being treated as one department's job.** A business text says "Successful businesses recognize that quality and productivity must go hand in hand." It also says quality control "requires a company-wide dedication" [openstax-introduction-business]. The software source notes that whether behaviour counts as "a fault, or a feature, can depend on the person doing the classification" [jones-evidence-based-sweng].

My inference: "Quality is engineering's problem" is the position the business text argues against. Part of the marketing–engineering dispute may simply be that the two sides define "bug" differently.

**The outage review punished a person, not the process.** An incident handbook describes a newer view that "human error is not the cause of failure, but a symptom of failure—trouble deeper inside the system." It says investigations should "prevent recurrence, not simply to find people to punish" [doe-hpi-handbook-vol2]. The library's blameless postmortem rests partly on "Psychological safety of all participants that promotes speaking up openly" [open-practice-library].

My inference: Naming the developer and putting him on a performance plan teaches everyone that surfacing risk is dangerous. It also leaves open how one merge could take the portal down for four hours.

## 2. What to change first, and why that first

**First change: stop over-committing the system.**

My inference: This has three parts.
- Give each developer one home squad.
- Have each squad set a work-in-progress (WIP) limit.
- Plan sprints to recent velocity, roughly 25 points, not 40.

The library's method is to "determine the amount of in-progress work you want to be your maximum at any given time" and to "Review WIP Limit at the end of the sprint and adjust if needed" [open-practice-library].

My inference: This comes first for three reasons.
1. **It costs nothing and takes effect next sprint.**
2. **It makes status visible.** Without that, we cannot judge any later change, including AI tools.
3. **It is the change that addresses the overload the other symptoms sit on.**

**Two moves that must happen in the same week:**

My inference: First, suspend the link between squad-lead bonuses and the 40% target. A paid incentive to push more points would directly fight a plan to commit to fewer.

My inference: Second, redo the portal postmortem as a blameless, system-focused review, and pause the developer's performance plan while it runs. Until we do, I would expect honest estimates and early warnings to be filtered.

The library advises that key business stakeholders not attend the postmortem, "as their very presence can prevent others from speaking freely" [open-practice-library].

My inference: You and I should read the draft afterwards rather than sit in the room.

**Next: a shared quality measure with marketing.** The library describes a North Star metric as "connective tissue between the product and the broader business" [open-practice-library].

My inference: Marketing's feature cadence and engineering's defect work should feed one shared customer-outcome number. Before that, both teams should agree on a single definition of "defect."

**Then: AI tools.** The library cites a framework, attributed to George Westerman of MIT, that says generative AI automation makes sense when "(Cost of Using AI + Cost of Adaptation + Cost of Detecting and Fixing Errors) < Cost of Manual Process." It notes that generative AI "can produce hallucinations" [open-practice-library]. The Org Topologies primer advises focusing on "that big bottleneck, over a generic 'adopt AI'" [org-topologies-primer-2025].

My inference: Our weakest point is the error-detection term in that formula: reviewers split across squads, and a release process that already lets outages through. More code, generated faster, into the current system would mostly produce more unchecked code. I would pilot AI tools in one squad, aimed at a named bottleneck, after the changes above.

## 3. Where the thinking disagrees with itself

**Hard goals versus realistic plans.** The management text says "People with difficult goals perform better than those with easy goals." It then adds the conditions on difficulty and acceptance quoted above [openstax-principles-management]. The Scrum guide asks for a "Realistically forecast" increment [approach-perfect-field-guide-scrum-events].

My inference: The head of engineering can fairly cite the first half of the goal-setting claim. The real dispute is whether 40% is challenging or impossible, and whether the squads accept it.

**Bonuses work, and backfire.** The business text says bonuses are "replacing the raise" as the way companies reward and motivate. It also reports that at Google, award sizes "created jealousy instead of fostering better teamwork" [openstax-introduction-business]. An organisational-behaviour text says rewards should be "as closely tied to actual job performance as possible" [openstax-organizational-behavior].

My inference: The sources argue for changing what the bonus measures, not necessarily for abolishing it.

**Blameless review versus individual accountability.** Another handbook says "Managers and supervisors must provide specific feedback when at-risk behavior is observed" and that "Competence does not guarantee positive control" [doe-hpi-handbook-vol1]. The library, by contrast, promotes "the safe culture of 'it's alright to fail'" [open-practice-library].

My inference: One way to reconcile them is that honest error leads to a system fix, while knowingly skipping an existing safeguard leads to direct feedback. No retrieved passage states this distinction. The review should still ask whether a check was bypassed, but only after the system questions.

**Busy people versus on-time delivery.** The software text says a company with fixed headcount "may seek to schedule work so that employees always have something productive to do." It says a company with a delivery date "may seek to schedule staff to optimise for delivery dates" [jones-evidence-based-sweng].

My inference: "Nobody is idle" serves the first objective, and a feature a week assumes the second. We have to choose between them deliberately.

**AI optimism versus error cost.** The Org Topologies primer says AI "Ensures consistent execution quality" and suggests "Spin up another 10,000 agents" [org-topologies-primer-2025]. Westerman's framework treats error correction as a standing cost [open-practice-library]. Accenture, as reported in an ethics text, says AI could "increase labor productivity by as much as 40 percent," and adds "When implemented holistically" [openstax-business-ethics]. The software text says that until effort across activities "is quantified, it is not possible to estimate developer productivity" [jones-evidence-based-sweng].

My inference: Accenture's macroeconomic "40 percent" is not evidence that our nine squads can reach a 40% throughput gain by Q1. Even that optimistic claim depends on the organisation being changed as a whole.

**Technical debt: sometimes necessary, sometimes fatal.** The library says debt "is not necessarily a bad thing." It also says the debt cycle can "become the death of a product or company" [open-practice-library].

My inference: Some shortcuts for the growth push may be defensible, provided they are tracked and paid down.

**Advice versus evidence.** My inference: The WIP-limit and blameless-postmortem passages I retrieved are practitioner reasoning with no measured data attached. We should run the first change as an experiment and track three numbers: planned-versus-shipped, carry-over, and incidents per release.

## Quotation locations

35 quotations, 32 found
  found    open-practice-library:3789                    take on all new tasks that come in.
  found    open-practice-library:3792                    the person gets overloaded, nobody knows how the progress is, and tasks get stuck in a progressed st
  found    open-practice-library:3797                    the person stays responsive, flexible and the status stays visible
  found    open-practice-library:20897                   Velocity – How much has the team been able to produce recently
  found    approach-perfect-field-guide-scrum-events:195 Realistically forecast what Increment can be delivered in the upcoming Sprint
  found    openstax-principles-management:25283          If goals are perceived as too difficult or impossible, however, they lose their motivating effective
  found    openstax-principles-management:25294          when managers assign them without making sure that workers have accepted or committed to the goals
  found    openstax-accounting-vol2:25593                was based on his bonus being tied to his profitability and not linked to other factors such as deale
  found    jones-evidence-based-sweng:16236              Performance need not be correlated with productivity
  found    openstax-introduction-business:29705          Successful businesses recognize that quality and productivity must go hand in hand.
  found    openstax-introduction-business:29721          requires a company-wide dedication
  MISSING                                                a fault, or a feature, can depend on the person doing the classification
  MISSING                                                Quality is engineering's problem
  found    doe-hpi-handbook-vol2:2803                    human error is not the cause of failure, but a symptom of failure—trouble deeper inside the system.
  found    doe-hpi-handbook-vol2:2809                    prevent recurrence, not simply to find people to punish
  found    open-practice-library:19817                   Psychological safety of all participants that promotes speaking up openly
  found    open-practice-library:3804                    determine the amount of in-progress work you want to be your maximum at any given time
  found    open-practice-library:3810                    Review WIP Limit at the end of the sprint and adjust if needed
  found    open-practice-library:19820                   as their very presence can prevent others from speaking freely
  found    open-practice-library:13463                   connective tissue between the product and the broader business
  found    open-practice-library:11469                   (Cost of Using AI + Cost of Adaptation + Cost of Detecting and Fixing Errors) < Cost of Manual Proce
  found    org-topologies-primer-2025:1456               that big bottleneck, over a generic 'adopt AI'
  found    openstax-principles-management:25282          People with difficult goals perform better than those with easy goals.
  found    openstax-introduction-business:27169          created jealousy instead of fostering better teamwork
  found    openstax-organizational-behavior:12880        as closely tied to actual job performance as possible
  found    doe-hpi-handbook-vol1:2264                    Managers and supervisors must provide specific feedback when at-risk behavior is observed
  found    doe-hpi-handbook-vol1:2783                    Competence does not guarantee positive control
  found    open-practice-library:19808                   the safe culture of 'it's alright to fail'
  found    jones-evidence-based-sweng:21547              may seek to schedule work so that employees always have something productive to do.
  found    jones-evidence-based-sweng:21549              may seek to schedule staff to optimise for delivery dates
  found    org-topologies-primer-2025:1439               Spin up another 10,000 agents
  found    openstax-business-ethics:14946                increase labor productivity by as much as 40 percent,
  MISSING                                                is quantified, it is not possible to estimate developer productivity
  found    open-practice-library:22180, openstax-business-ethics:5734 is not necessarily a bad thing.
  found    open-practice-library:22186                   become the death of a product or company

