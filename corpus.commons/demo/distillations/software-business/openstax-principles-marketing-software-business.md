# OpenStax, Principles of Marketing, Software-Business Distillation

**Source:** OpenStax (2023). *Principles of Marketing*. CC BY-NC-SA 4.0.

## Software-Business Relevance

*Principles of Marketing* is one of the few sources in this corpus that prices the commercial side of software-business decisions in marketing's own working vocabulary. It lands hardest where the software company is making a *pricing decision* (Ch 12 — the canonical software-business question, especially for SaaS), a *customer-lifetime-value-versus-acquisition-cost* judgement (Ch 2.4), a *new-product cadence* decision that intersects with engineering capacity (Ch 10), or a *customer-experience and board-reporting* question that turns on service quality the engineering org has to deliver (Ch 11, 13.4). The text is pedagogical and templated, which makes it especially well-suited as a software-business reference: each commercial decision is decomposed into named steps, criteria, and worked examples that a founder, CTO, or product leader can adopt directly.

The source is less useful for the software-internal questions the corpus catches better elsewhere — team-structure decisions (route to `openstax-principles-management`, `letaw-handbook-sweng-methods`), engineering-economics-and-technical-debt judgements (route to `openstax-accounting-vol2`, `jones-evidence-based-sweng`), and AI-integration ethics (route to `openstax-business-ethics`, the architecture's `llm-epistemology.md`). What this source contributes that no other reference in the corpus does: a structured way to price an offering, a structured way to forecast customer-lifetime-value as a business decision, a stage-gated process for product development that maps onto release cadence, and a structured framework for diagnosing where customer-experience promises break down between marketing, engineering, and frontline service.

## Verbatim anchors from the source

Customer value — the price-value frame for any SaaS pricing decision — is defined as "the ratio between the perceived benefits and costs incurred by the customer in acquiring your products or services" [V] (OpenStax, *Principles of Marketing*, Ch 1.1, "Step 3: Deliver High Customer Value").

A value proposition — the compressed statement of a tier's promise — is "a promise of value that communicates the benefits of your company's products or services" [V] (Ch 1.1, "Step 2").

Advertising — the largest single line item in most software-business GTM budgets — is "paid communication messages that identify a brand or organization and is intended to reach a large number of recipients" [V] (Ch 14.1, "Advertising and its Importance").

The Iceberg of Ignorance statistic that anchors the service-profit-chain frontline-feedback argument: "4 per cent of frontline problems known by top management, 9 per cent middle, 74 per cent supervisors, 100 per cent employees" [V] (Ch 11.2, citing Yoshida).

## Key Concepts for Software-Business

1. <!-- concept: five-cs-of-pricing --> **The Five Cs of pricing.** Cost, customers, channels of distribution, competition, compatibility with brand strategy. The checklist a software business runs before setting or revising a price. (Source: OpenStax, *Principles of Marketing*, Ch 12.2, "The Five Cs of Pricing")
2. <!-- concept: pricing-objectives --> **Seven pricing objectives.** Customer value-based (GoToMeeting's "$49 all-you-can-meet" — directly applicable to SaaS), cost-based, sales-oriented, market-share-oriented, target return, competition-based (Amazon's algorithmic just-below-competitor model), customer-driven. The choice space for a software-business pricing decision. (Source: Ch 12.3, "Pricing Objectives")
3. <!-- concept: new-product-pricing-strategies --> **Three new-product pricing strategies.** Price skimming (Sony PlayStation 3 from $599 to $299), penetration pricing (Netflix subscription), break-even pricing (formula: fixed costs ÷ (unit price − unit variable cost)). The choice for launching a new software product, feature, or tier. (Source: Ch 12.4, "New Product Pricing Strategies")
4. <!-- concept: price-value-equation --> **The price-value equation.** Value = perceived benefits − perceived costs. The frame for any software-business pricing decision: customer willingness-to-pay is bounded by the *perceived* value, not the engineering-effort cost. (Source: Ch 12.1, "Price as an Indicator of Value")
5. <!-- concept: customer-lifetime-value --> **Customer lifetime value (CLV) as decision metric.** CLV = annual profit per customer × average years retained − CAC. The text's worked example computes CLV across four customer segments ($66K to $215K range), showing that retention and CAC, not gross margin alone, drive customer profitability. The load-bearing metric for any SaaS unit-economics decision. (Source: Ch 2.4, "Examples of Customer Support KPIs"; Table 2.1)
6. <!-- concept: cac-and-retention --> **CAC + retention as joint software-business levers.** Customer acquisition cost without retention is a leak; retention without acquisition is a ceiling. Marketing KPIs cluster around the CLV-CAC engine: Average Revenue per Customer, customer retention rates, CSAT, CES. (Source: Ch 2.4, "Marketing Metrics Explained")
7. <!-- concept: new-product-development-process --> **The nine-stage NPD process.** Idea generation → idea screening → concept development and testing → market strategy → business analysis (payback, break-even) → product development (prototype) → test-marketing → commercialisation → evaluation. Maps onto a software release cadence with explicit stage gates between commitment levels. (Source: Ch 10.2, "Stages of the New Product Development Process")
8. <!-- concept: new-product-success-factors --> **Five new-product success factors.** Unique benefits to users (cited 5× success rate vs me-too products); planning before development (raised success rate from ~31% to 75%); technological synergy; marketing synergy (2.3× success rate when present); market attractiveness. The pre-commitment diagnostic for a new software offering. (Source: Ch 10.4, "Factors Contributing to a Product's Success")
9. <!-- concept: service-profit-chain --> **Service-profit chain.** Internal service quality → employee satisfaction → loyalty/productivity → external value proposition → customer satisfaction → customer loyalty → profit. For SaaS, the chain runs through engineering and frontline support and is broken if any link fails. (Source: Ch 11.2, "The Service-Profit Chain Model")
10. <!-- concept: gap-model --> **The Gap Model of service quality.** Five gaps: knowledge gap (what customers expect vs what management thinks they expect), policy gap (understanding vs delivery standards), delivery gap (specs vs actual delivery), communication gap (delivery vs what's communicated), customer gap (expectation vs perception of experience). The diagnostic catalogue for a SaaS reliability-or-service incident report. (Source: Ch 11.3, "The Gap Model of Service Quality")
11. <!-- concept: rater-framework --> **RATER framework.** Reliability (cited as 3× more important than equipment or uniforms), Assurance, Tangibles, Empathy, Responsiveness. The dimensions a board memo on customer-experience metrics should report against. (Source: Ch 11.3, "The RATER Framework")
12. <!-- concept: 5a-customer-journey --> **5A customer journey.** Aware, Appeal, Ask, Act, Advocacy. The sequencing template for SaaS customer-communication decisions — from cold prospect to advocate. (Source: Ch 13.4, "The 5A Framework")
13. <!-- concept: integrated-marketing-communications --> **Integrated Marketing Communications (IMC).** A single, consistent message across six promotion-mix elements (advertising, sales promotion, personal selling, public relations, direct marketing, digital/Internet) — load-bearing for SaaS because customers encounter the product across product UI, sales touches, support, content marketing, and community simultaneously. (Source: Ch 13.3, "Integrated Marketing Communications")

## Questions to Ask During Software-Business Work

### Phase 1: Strategic positioning

| Need | Question |
|---|---|
| Frame the pricing decision | Which of the seven pricing objectives are we serving — customer-value (GoToMeeting all-you-can-meet model), cost-based, sales-volume, market-share, target-return, competition-based, or customer-driven (auction/usage-based)? Does the objective match the engineering-cost reality and the competitor's pricing? (Source: Ch 12.3) |
| Run the Five Cs of pricing | Cost (variable + fixed engineering cost per unit), customers (willingness to pay; segment differences), channels (direct, partner, marketplace), competition (where we sit on the price band), compatibility (does the price match the brand position)? (Source: Ch 12.2) |
| Choose new-product pricing strategy | Skimming (high initial price, gradual reduction — defensible if the offering is novel or premium-positioned), penetration (low price to capture share fast — defensible if the unit economics work at scale and the competitive window is closing), or break-even (cover costs, no profit — defensible only as a deliberate market-entry stance)? (Source: Ch 12.4) |
| Test the price-value frame | Have we measured the customer's *perceived* value of the offering, not just our engineering effort? Where does our offering land on a perceived-benefits-minus-perceived-costs comparison vs the next-best alternative? (Source: Ch 12.1) |
| Calculate CLV for the target segment | What's the annual profit per customer, average years retained, and CAC for this segment? Does the resulting CLV justify the acquisition spend and retention investment? (Source: Ch 2.4, Table 2.1) |
| Test CAC discipline | Is CAC trending up or down? Is retention trending up or down? Are we acquiring expensive customers and losing them faster than we acquire? (Source: Ch 2.4) |
| Frame the product-portfolio decision | Where do our offerings sit on the BCG matrix — star, cash cow, question mark, dog? Does the resource allocation match the matrix position? (Source: Ch 2.2) |

### Phase 2: Product and engineering economics

| Need | Question |
|---|---|
| Test new-product-launch viability | Have we passed the five success-factor tests — unique benefits, predevelopment planning, technological synergy, marketing synergy, market attractiveness? Without these, failure rate runs 35–49% (PDMA) to 95% (Christensen estimate). (Source: Ch 10.4) |
| Test demand elasticity | Are we pricing into elastic demand (many substitutes — penetration likely; price sensitivity high) or relatively inelastic demand (few substitutes — pricing power; skimming defensible)? For SaaS: switching costs, integration depth, and network effects shape elasticity. (Source: Ch 12.3) |
| Run the break-even formula | Break-even units = fixed costs ÷ (unit price − unit variable cost). For a SaaS feature: what's the monthly break-even subscriber count? Does the addressable market support it? (Source: Ch 12.4) |
| Pick existing-product pricing tactics | Product line pricing (tier structure — Free / Pro / Enterprise), captive pricing (low base with paid add-ons — the printer-and-ink pattern), bundle pricing (suite vs point-product), economy pricing (price-leader tier to defend share)? (Source: Ch 12.5) |

### Phase 3: Team and capability building

| Need | Question |
|---|---|
| Test the service-profit chain | Is internal service quality (engineering tooling, ops support, working conditions) high enough to drive employee satisfaction → productivity → customer-facing value delivery? For SaaS where engineers are inseparable from product quality, the chain runs through engineering. (Source: Ch 11.2) |
| Diagnose the broken chain link | If customer satisfaction is declining without an obvious cause, which link is broken — internal service quality, employee satisfaction, employee loyalty/productivity, external value proposition, or customer-loyalty mechanism? (Source: Ch 11.2) |
| Test the empowerment level | Can frontline support staff deviate from the script to solve a customer problem (the Zappos call-centre model)? For SaaS: can support engineers ship a hotfix without escalation when the customer's working hours are different from the engineering team's? (Source: Ch 11.2, "Empowerment") |
| Test for the Iceberg of Ignorance | Yoshida's estimate: 4% of frontline problems known by top management, 100% by employees. What feedback channel brings frontline knowledge upward — and is it actually used in product and engineering decisions? (Source: Ch 11.2) |

### Phase 4: Operations and process

| Need | Question |
|---|---|
| Map release cadence to NPD stages | Which of the nine NPD stages applies to this release — concept testing (Stage 3), business analysis (Stage 5), prototype/MVP (Stage 6), test-marketing (Stage 7 — beta cohort), commercialisation (Stage 8), or evaluation (Stage 9)? Are stage gates being enforced or skipped? (Source: Ch 10.2) |
| Test stage-gate discipline | Is business analysis (Stage 5: payback, break-even) actually being done before product development (Stage 6), or are we shipping features without unit-economics validation? Maxwell House case: four months of formulation, then cheaper substitute, then flop. (Source: Ch 10.2) |
| Sequence adoption work | For a new product launch: are we mapping the five-stage consumer adoption process (awareness → interest → evaluation → trial → adoption)? Are we targeting innovators and early adopters first (per Rogers), or pushing to the late majority before the early-adopter signal has been validated? (Source: Ch 10.5) |
| Choose innovation-type framing | Continuous (no behavioural change required — UI polish, performance improvement), dynamically continuous (workflow shift — adopting a new IDE), or discontinuous (radical behavioural change — agentic AI replacing manual workflow)? Higher disruption demands more behavioural-change support in onboarding, training, and customer-success engagement. (Source: Ch 10.1) |

### Phase 5: Risk, reliability, compliance

| Need | Question |
|---|---|
| Test the customer gap on reliability | When a reliability event happens, how big is the gap between what the customer expected from us (the SLA, the marketing promise, the perceived reliability) and what they actually experienced? (Source: Ch 11.3, "Customer Gap") |
| Test the communication gap on incidents | Did our marketing or sales promises overshoot what engineering delivers, even when engineering is performing well? The communication gap is between what we delivered and what we communicated we'd deliver. (Source: Ch 11.3, "Communication Gap") |
| Test PR-crisis preparation | Do we have a Tylenol-1982-style crisis comms plan ready — direct, transparent, costly when needed? For software incidents (breach, outage, defect): are we prepared to face the issue head-on with the same discipline? (Source: Ch 13.1, "Public Relations") |

### Phase 6: Stakeholder communication

| Need | Question |
|---|---|
| Frame the customer-experience board memo | Are we reporting on RATER (Reliability, Assurance, Tangibles, Empathy, Responsiveness) with metrics for each dimension? Reliability is 3× more important than equipment/uniforms per the source — for software, reliability is the load-bearing dimension. (Source: Ch 11.3) |
| Diagnose where CX is breaking | Where in the five Gap Model gaps is the failure — knowledge (we misunderstand the customer), policy (our policies don't translate the understanding), delivery (the engineering team isn't shipping to spec), communication (our marketing overshoots delivery), or customer (the customer's expectation has drifted)? (Source: Ch 11.3) |
| Map the customer journey for comms | At which stage of the 5A journey is this customer or cohort — Aware (paid search, content, PR), Appeal (value-prop testing, comparisons), Ask (chatbot, support, sales), Act (purchase friction reduction), Advocacy (loyalty, referrals, ambassadorship)? Is the communication appropriate to the stage? (Source: Ch 13.4) |
| Test for IMC across the company | Are product UI, sales touches, support conversations, content marketing, in-app messaging, and community engagement all carrying the same message — or is the customer encountering a fragmented company? (Source: Ch 13.3) |
| Choose the appeal | Rational (capabilities, ROI, performance benchmarks), emotional (the story of what becomes possible), or moral (the responsibility argument — AI safety, data sovereignty, sustainability)? Does the appeal match the segment's psychology and our positioning? (Source: Ch 13.4) |

## What to Look For

- **Pattern: Pricing set by engineering-cost markup, not by customer value.** Signal: pricing discussions inside engineering using cost-of-build as the anchor; no measurement of customer willingness-to-pay. Diagnosis: cost-based pricing dominating to the exclusion of value-based or competitive objectives — common when engineering leads the pricing decision. Follow-up: complete the Five Cs (Ch 12.2); rerun the price-value equation; pick a pricing objective consistent with strategic position (Ch 12.3).
- **Pattern: SaaS unit economics tracked by ARR alone, not CLV-CAC.** Signal: ARR growing while CAC and retention are not tracked or are diverging. Diagnosis: the CLV-CAC engine is invisible; the company may be acquiring expensive customers and losing them faster than they pay back. Follow-up: build the four-segment CLV table (Ch 2.4, Table 2.1); set retention and CAC as core KPIs alongside ARR.
- **Pattern: NPD process skipping the business-analysis stage.** Signal: a feature ships from idea to prototype to launch without explicit payback or break-even calculation. Diagnosis: NPD Stage 5 skipped — the Maxwell-House failure mode (Ch 10.2). Follow-up: enforce stage gates; insist on business analysis before development resources commit.
- **Pattern: Reliability events handled as engineering problems, not customer-experience problems.** Signal: incident write-up names the technical root cause without naming the customer-gap (where the customer's expectation diverged from the experience). Diagnosis: the Gap Model isn't being applied to the incident — only the technical defect is in scope. Follow-up: extend the incident write-up to name all five Gap Model gaps (Ch 11.3); the technical defect is usually one of them, but not all of them.
- **Pattern: Customer-success metrics tracked only as engineering uptime, not RATER.** Signal: board CX report shows 99.x% uptime, no measurement of Assurance (does the customer trust our team's competence), Empathy (do they feel heard), or Responsiveness (how quickly do we resolve). Diagnosis: tangibles-and-reliability reporting that misses the other three RATER dimensions where customer-perception lives. Follow-up: instrument Assurance, Empathy, Responsiveness measurement; report all five RATER dimensions to the board (Ch 11.3).
- **Pattern: Customer-acquisition spend without 5A-stage segmentation.** Signal: same marketing message, same content, same channels for Aware-stage prospects, Appeal-stage evaluators, and Advocacy-stage existing customers. Diagnosis: 5A-stage mismatch — every dollar spent on the wrong stage is partly wasted. Follow-up: segment by stage; build stage-appropriate content; track conversion between stages (Ch 13.4).
- **Pattern: Fragmented customer messaging across product, sales, support, content.** Signal: sales says "premium", product UI says "self-serve", support says "we'll customise", content marketing says "biggest discount". Diagnosis: IMC failure — the company shows up as multiple personalities to a single customer. Follow-up: align on a single message strategy; audit every touchpoint for consistency (Ch 13.3).
- **Pattern: Service-profit chain broken at the engineering link in a SaaS company.** Signal: support tickets rising, frontline burnout, customer satisfaction declining, engineering velocity dropping in parallel. Diagnosis: internal service quality has degraded — the engineering org's working conditions are propagating downstream to customer experience. Follow-up: invest in internal service quality (tooling, on-call rotation, technical-debt servicing); the customer-experience metric will follow (Ch 11.2).

## When to Use This Reference

- *Pricing-policy review* for a new feature, product, tier, or SaaS plan — especially when engineering effort and competitor effort are uneven.
- *Unit-economics modelling* for a new customer segment — CLV-CAC for SaaS, marketplace, or freemium offerings.
- *Product-launch decision gates* — when applying NPD stage discipline to a software release.
- *Customer-experience board memo preparation* — when reporting CX metrics to a board that doesn't read code.
- *Incident or reliability post-mortem* — when extending an engineering-side write-up into a customer-experience-side write-up.
- *Service-profit chain diagnostic* — when customer satisfaction is declining without obvious cause and the chain may be broken at an internal link.
- *Customer-communication strategy* — when building or refreshing the 5A journey across SaaS marketing, sales, product, and customer success.
- *Customer-success / loyalty programme design* — for retention and advocacy work.

## Worked Example

A 60-engineer B2B SaaS company is preparing to launch a new "AI co-pilot" tier alongside its existing Standard and Pro tiers. The CEO wants to price it; the CTO is worried about engineering capacity for the build; the head of customer success is worried about how to communicate the new tier to existing customers without cannibalising Pro upgrades; the board wants a customer-experience report at next quarter's meeting.

Apply the Five Cs of pricing (Ch 12.2): cost (the AI infrastructure spend is high and variable per user — variable-cost frame); customers (willingness-to-pay testing with 12 design-partner accounts before commit); channels (direct sales for enterprise, self-serve for SMB — different prices may make sense); competition (two competitors at $99/user/month, three at $199); compatibility (the AI tier must read as premium to support the brand position).

Apply the seven pricing objectives (Ch 12.3): the most defensible objective is customer-value-based — the AI tier should price into the value it delivers (productivity hours saved × loaded rate), not into the cost of GPU inference. Reject the cost-plus default the CFO is gravitating toward.

Apply the three new-product pricing strategies (Ch 12.4): skimming makes sense — high initial price ($299/user/month for the design-partner cohort, $249 at general availability, $199 at one-year mark as competitors enter). The PlayStation 3 pattern, applied to AI.

Apply CLV calculation (Ch 2.4, Table 2.1): for the existing Pro segment, average years retained is 4.2, annual profit per customer is $14K, CAC is $3.2K — CLV is $55.6K. The AI tier needs to clear this bar to justify the build. Modelling at $299/user/month with 15% incremental gross margin and a 4-year retention assumption shows ~$120K CLV at 10-seat average — clears the bar.

Apply the nine-stage NPD process (Ch 10.2): the team is at Stage 3 (concept development and testing with design partners). Stage 5 (business analysis) is the next gate — the CTO's capacity concern lands here. Force the business analysis before the team commits to the full build. The Maxwell House failure mode is the warning.

Apply the five new-product success factors (Ch 10.4): unique benefits (the AI co-pilot does something the Pro tier cannot — clear yes); predevelopment planning (design-partner cohort + business analysis — in progress); technological synergy (uses the existing data platform — yes); marketing synergy (the existing customer success motion can carry the launch — partial — the team needs training); market attractiveness (B2B SaaS AI tier market is hot — yes). 4.5 out of 5 — success-factor signal is strong if the marketing-synergy gap closes.

Apply the service-profit chain (Ch 11.2): the AI tier adds support load. Internal service quality (the engineering team's working conditions during the build) and customer-success team capacity (the frontline who'll absorb the load) must be invested in before launch — or the chain will break at the employee-satisfaction link.

Apply the 5A customer journey (Ch 13.4) for customer comms: existing Pro customers are at Advocacy stage; the AI tier is a new "Aware" intro. The cannibalisation concern dissolves if the message frames the AI tier as additive (not as a Pro replacement). Build stage-appropriate content.

Apply the Gap Model (Ch 11.3) for the board CX report: report all five gaps quarterly. Reliability (RATER) is the dimension to lead with; AI features are *high-variance reliability* and the board will notice if the AI tier's uptime is lower than the Pro tier's. Be ahead of the question.

Decision: launch the AI tier at $299/user/month for design partners, $249 at GA, with enforced NPD stage gates, with explicit investment in customer-success team capacity, and with a board CX report that names the AI tier's reliability profile separately from the Pro tier. Cancel the lower-priced "AI Lite" alternative; the price compression would push the offering into penetration-pricing territory the unit economics don't support.

## Anti-patterns This Reference Helps Avoid

- *"Cost-plus pricing for a SaaS tier"* — engineering effort sets the price, customer perceived-value is ignored. Predictable result: undercharging where the value is high; overcharging where the value is low.
- *"ARR is the only metric that matters"* — acquiring expensive customers and losing them faster than they pay back. The CLV-CAC engine catches this; ARR-only reporting hides it.
- *"Ship the feature, then figure out the business model"* — NPD Stage 5 skipped; payback and break-even calculated *after* the build. The Maxwell-House failure mode applied to software.
- *"The engineering team will absorb the AI infrastructure cost"* — variable cost ignored in the pricing model. SaaS gross margin compression follows in the second year.
- *"Customer success will handle it"* — internal service quality not invested in before a launch that adds support load. The service-profit chain breaks at the frontline link.
- *"Reliability is an engineering metric, not a customer-experience metric"* — RATER's other four dimensions (Assurance, Tangibles, Empathy, Responsiveness) ignored. The board sees uptime; the customer feels something else.
- *"The same marketing message works at every stage"* — 5A-stage segmentation missing. The Aware-stage prospect, the Appeal-stage evaluator, and the Advocacy-stage existing customer all get the same content.
- *"Sales says X, product says Y, support says Z, content says W"* — IMC failure. The customer encounters multiple companies and trusts none of them.
- *"Cancel the feature when CSAT drops"* — Gap Model not applied. Often the technical delivery is fine and the failure is upstream (knowledge or policy gap) or downstream (communication gap). Cancelling the feature treats the symptom.

## Through the cto lens

A CTO reading a software-business question this reference would land on reads for the *constraint* in the pricing or product-economics decision and the *mechanism* — owner, capability gap, repeatable gate — that captures the opportunity. Three diagnostic reweightings:

1. **Pricing as constraint mechanism, not as marketing decision.** The CTO reads the Five Cs (Ch 12.2) primarily through *cost* (variable-cost discipline against engineering reality) and *compatibility* (brand-strategy match), and reads the seven objectives (Ch 12.3) primarily as *which one is the constraint mechanism that unlocks the AI-native or modernisation thesis*. Customer-value-based pricing is the lever this CTO would reach for because it ties price to capability-built rather than to engineering hours, which is the AI-substrate frame, not the productivity-tool frame.
2. **CLV-CAC as the demand-governance unit of measure.** The CTO reads CLV (Ch 2.4) as the priority-gate criterion: every new story enters the queue under an explicit prioritisation gate, and the gate weights CLV-impact against engineering-cost. Backlog grooming is replaced by ranked-list-of-actual-work where the rank is CLV-justified. The CTO reads ARR-only reporting as a Past-tempo signal — analysis-first, not constraint-first.
3. **Service-profit chain as engineering-org operating-model question.** The CTO reads the service-profit chain (Ch 11.2) as a load-bearing claim about the engineering org being inseparable from customer experience — and reads the AI-native transition through this frame. AI as substrate redesigns the chain: who's the new role bifurcation (AI-platform-expert vs deep-domain-expert), how does on-call shift, how does internal service quality scale when agent fleets carry support load. The CTO would not read this chapter as a customer-success problem; they would read it as an org-redesign opportunity.

The CTO's native vocabulary for this reference: *the pricing lever, CLV-justified queue position, capability-built-not-hours-spent, the AI tier's variable-cost discipline, the on-call mechanism, the bifurcation in customer-success engineering, what unlocks the next $10M of ARR.*

## Through the business-executive-stakeholder lens

A business-executive stakeholder reading customer-experience or pricing artefacts heading into a board or peer-C-suite meeting reads in Paradigm-A register (commitment, accountability, KPI, named owner) with occasional Paradigm-B language surfacing in low-heat moments. Three reweightings:

1. **The board CX memo opens with the operational situation, then the variance, then the named owner.** The Gap Model (Ch 11.3) is the analytical backbone the artefact uses, but the artefact does not lead with it. It leads with the KPI delta (RATER scores quarter-on-quarter, customer NPS, churn rate) and the named accountable owner. The Gap Model surfaces as one Paradigm-B move inside the artefact — a structural reframe offered as a choice ("This pattern reads as a communication-gap issue, not a delivery-gap issue; the structural fix is to align marketing claims with engineering capacity at the message-design stage") — not as the artefact's organising frame.
2. **CLV is the KPI; CAC is the discipline; retention is the variance.** This stakeholder reads CLV-CAC (Ch 2.4) in Paradigm-A vocabulary — commitment, ROI, accountability — and reads the four-segment table (Table 2.1) as the format the artefact should use. The artefact must supply named owners for each segment's CLV target, KPI deltas against last quarter, and a timeboxed action with measurable success criteria. The B-move available here: occasional acknowledgment that retention investments are slack-against-utilisation moves (sustainable-pace vocabulary the stakeholder espouses in retros).
3. **The service-profit chain as accountability surface.** The stakeholder reads the service-profit chain (Ch 11.2) in Paradigm-A register: each link is an accountability surface with a named owner. The B-move available: the chain breaks at *internal* service quality long before customer-satisfaction signals show up — the structural fix is upstream investment, not downstream apology. One B-move per artefact; the artefact closes with named owners, KPI deltas, and the decision being requested.

The artefact opens with 1-2 sentences of acknowledgment when post-event (the team's CX work or the engineering team's reliability investment); shifts to Paradigm-A operational analysis for the substance; offers one Paradigm-B reframe as a choice (Gap Model attribution, or service-profit-chain upstream investment, or sustainable-pace-as-retention-investment — pick one per artefact); closes with named owner, KPI, timeboxed first step, decision being requested.

## Through the pm-bounded-by-ba-role lens

A PM bounded by a BA role would absorb significant coordination cost from this reference's frames if applied as-leadership-directed. The lens surfaces what the artefacts created by this reference take from the PM that the artefact doesn't acknowledge. Three structural surfacings:

1. **The nine-stage NPD process (Ch 10.2) creates stage-gate coordination work no artefact budgets for.** If leadership directs "enforce NPD stage discipline on the next release," the PM absorbs the coordination cost — writing the business-analysis ask, escalating to finance, sequencing the stage gates against external commitments already made, herding the test-marketing cohort, composing the commercialisation handover. None of this appears in the leadership directive. The lens names the coordination cost and asks *where this time will come from* — usually from the PM's already-full backlog.
2. **The 5A customer journey (Ch 13.4) and IMC (Ch 13.3) create cross-team coordination at the PM's structural position.** If leadership directs "align messaging across product, sales, marketing, and customer success," the PM is structurally between sales (Directing archetype, demanding compelling promises), engineering (Doing archetype, delivering specific capabilities), marketing (their own register), and customer success (frontline reality). The PM coordinates the artefacts but does not have authority to refuse the misaligned demands. The lens names the label-vs-authority gap and the absorption.
3. **Service-profit chain (Ch 11.2) and Gap Model (Ch 11.3) read as structural diagnoses the PM can surface but cannot fix.** When leadership asks "diagnose the customer-satisfaction drop using the Gap Model," the PM does the diagnostic work — coordinating with engineering, customer success, marketing — and identifies the structural fix (often upstream in marketing-claims or in engineering-staffing decisions). The fix requires authority the PM doesn't have. The lens names this: the PM does the diagnostic work; the structural fix routes back up to leadership; the artefact often does not name this routing explicitly, leaving the PM to herd it.

The lens surfaces (structural voice, no first-person, no sympathy-performance) that this reference's frameworks — when adopted as organisational discipline — create real coordination cost in the PM's day. Naming the cost is not a refusal to adopt; it is naming what the adoption takes, so leadership can decide whether to invest in coordination capacity (a dedicated launch coordinator, a PM operations role) or to accept the cost as PM absorption.

## Integration with Other References

| Reference | Connection |
|---|---|
| `openstax-accounting-vol2` | Relevant-cost discipline and cost-classification primitives are the prerequisite for the Five Cs *cost* element and the break-even formula (Ch 12.4). Pair when running a software-business pricing or build-vs-buy analysis. |
| `jones-evidence-based-sweng` | Resource estimation under uncertainty, KLOC mythology, and the cone of uncertainty supply the engineering-cost side of the pricing decision the marketing source frames. Pair when the pricing question turns on engineering-effort uncertainty. |
| `openstax-principles-management` | Strategic-environment-scan (PESTLE, five forces) and organisational design supply the *competitive-positioning* and *team-structure* sides of the software-business question the marketing source addresses commercially. Pair for portfolio decisions. |
| `openstax-organizational-behavior` | The service-profit chain's *internal service quality → employee satisfaction* link is the OB literature on engagement applied through the service lens. Pair when the customer-experience problem traces back to employee-engagement issues. |
| `openstax-business-ethics` | The stakeholder approach to sustainability (Ch 19.2) is operationally adopted from stakeholder theory — pair with Business Ethics for the AI-ethics and externalised-cost framings. |
| `openstax-principles-finance` | The CAC + CLV unit-economics frame is the marketing-side of the financial-decision discipline the Finance text covers — pair for SaaS-investor-update preparation. |
| `letaw-handbook-sweng-methods` | NPD stage-gate discipline (Ch 10.2) is the marketing-side parallel to Letaw's process discipline in software engineering — pair when product development needs both commercial and engineering-process discipline simultaneously. |
| `scrum-guide-2020`, `approach-perfect-field-guide-scrum-events` | The 5A customer journey (Ch 13.4) and NPD test-marketing stage (Ch 10.2) map onto Scrum sprint-review and beta-cohort patterns — pair when sequencing customer-discovery work against sprint cadence. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The source draws on several foundational marketing researchers and practitioners this corpus does not hold as primary references.

- *Valarie Zeithaml, A. Parasuraman, and Leonard Berry, Delivering Quality Service* — the RATER framework (Reliability, Assurance, Tangibles, Empathy, Responsiveness) and the Gap Model of service quality are sourced [BT] (Ch 11.3). The primary research monograph is not in this corpus; this text is the corpus's only treatment of both frameworks.
- *Christopher Lovelock* — the four-category service taxonomy is cited [BT] (Ch 11.1).
- *Everett Rogers, Diffusion of Innovations* — the five adopter categories (innovators through laggards) and the two-step personal-influence model are cited [BT] (Ch 10.5).
- *Clayton Christensen* — the estimate that approximately 95 per cent of roughly 30,000 new product launches per year fail is attributed to Christensen [BT] (Ch 10.4). The PDMA failure-rate studies (35-49 per cent by product category) are also cited [BT].
- *Tony Hsieh, Zappos, Delivering Happiness* — the Zappos frontline-empowerment model and the Zappos call-centre examples are cited [BT] (Ch 11.2).
- *Philip Kotler and Kevin Lane Keller* — the 5A customer journey framework (Aware, Appeal, Ask, Act, Advocacy) is attributed to this tradition [BT] (Ch 13.4).
- *Abraham Maslow* — hierarchy of needs used to anchor motivation analysis in consumer psychology is cited [BT] (Ch 3.2).
- *Geert Hofstede* — cultural dimensions frame for segmentation is cited [BT] (Ch 5.3; Ch 8.3).
- *Theodore Levitt* ("Marketing Myopia") — cited approvingly twice [BT] (Ch 1.4; Ch 5.2).
- Irina Simmons (consumer-income interview), Rebecca Henderson (shared-value orientation), Harvard Business Review global-competitiveness criteria — cited [BT] in various chapters; none held as primary references.

**Named limits of the source.** The text is a general undergraduate marketing textbook; it is not calibrated to B2B SaaS, marketplace, or AI-native software business models specifically. The Gap Model's five gaps and RATER apply to service delivery broadly; software-specific adaptations (API reliability as "Reliability", developer-experience as "Assurance") are inference territory, not source claims. The nine-stage NPD process is presented as a general product-development template; agile-adjacent adaptations (sprint as stage, beta as test marketing) are distillation-level inferences. CLV calculation (Ch 2.4, Table 2.1) uses a simplified formula; practitioners building financial models should cross-reference with `openstax-principles-finance` for discount-rate treatment.

**Evidence-marker continuity.** The RATER framework and Gap Model are [BT] in the deep reference (sourced from Zeithaml, Parasuraman, and Berry) and are attributed to those authors in this distillation. The CLV formula and the five-success-factor list are [V]-marked content in Ch 2.4 and Ch 10.4 respectively and are cited by chapter. The Christensen failure-rate figure is [BT] and is attributed as such. The worked example (AI co-pilot tier pricing) is operator-authored; its framework applications trace back to Ch 12.2 (Five Cs), Ch 12.3 (pricing objectives), Ch 2.4 (CLV), Ch 10.2 (NPD stages), Ch 10.4 (success factors), Ch 11.2 (service-profit chain), and Ch 11.3 (Gap Model) with source citations throughout.
