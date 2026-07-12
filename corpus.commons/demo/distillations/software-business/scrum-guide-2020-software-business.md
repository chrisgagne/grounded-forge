# Schwaber & Sutherland, The Scrum Guide — Software-Business Distillation

**Source:** Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. November 2020 edition. scrumguides.org. Licence: CC BY-SA 4.0. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf.

## Software-Business Relevance

The Scrum Guide is methodology, not business prescription, but it is methodology *with software-business decisions wired into its structure*. The Product Owner accountability is the most direct software-business artefact in the corpus: a role explicitly responsible for maximising product value, ordering the work, and absorbing stakeholder pressure into a single ordered backlog (Source: *Scrum Guide* 2020, "Scrum Team", "Product Owner"). The Product Goal is a long-term strategic-positioning artefact; the Sprint Goal is a delivery-cadence commitment; the Definition of Done is a quality-vs-speed bargain encoded into a release gate; the cancel-Sprint authority is a governance constraint that names a single decision-right owner for the most disruptive product decision available.

The Guide is also the operating spec that produces a class of software-business decisions the practitioner needs to be ready for. Pricing decisions show up in Sprint Planning Topic One ("why is this Sprint valuable?") when a Sprint commits engineering to a feature whose monetisation isn't yet decided. Build-vs-buy decisions show up when refining a Product Backlog item that could be sourced externally. Compliance-and-reliability investment decisions show up when the Definition of Done is being authored or updated — the DoD is the structural place where "reliability is a financial decision" lands in the team's daily work. Board-and-exec reporting decisions show up when Sprint Review attendance is set and when the Product Owner has to translate the Product Backlog ordering rationale for stakeholders who are not in the room.

A third software-business contribution is the Guide's stance on framework immutability versus local adaptation. The framework "is immutable. While implementing only parts of Scrum is possible, the result is not Scrum" (Source: *Scrum Guide* 2020, "End Note"). But the local tactics — meeting format, story decomposition, refinement cadence, specific Definition of Done — are explicitly the team's to set. This maps onto the software-business question of when to standardise (across teams, across products, for compliance reasons) versus when to localise (for context-fit, for team-level capability, for product-stage reasons). The DoD has both flavours encoded: organisational-standard DoD when standards exist (compliance, security, multi-team coordination); team-authored DoD otherwise.

A fourth contribution is the explicit refusal of certain software-business patterns the consultant-derivative cluster surfaces. The Product Owner is "one person, not a committee" (Source: "Scrum Team", "Product Owner") — a structural refusal of decision-by-committee on product value. The Sprint Review "should never be considered a gate to releasing value" (Source: "Scrum Artifacts", "Increment") — a refusal of release-cadence-tied-to-inspection-cadence. Forecasting tools "do not replace the importance of empiricism" (Source: "Scrum Events", "The Sprint") — a refusal of the burn-down-chart-as-truth pattern that often shapes board reporting.

This distillation gathers these threads: how the Scrum framework structures software-business decisions across the six task phases; where the framework's accountabilities and artefacts encode specific decision rights; and where the Guide's refusals discipline software-business practitioners against the consultant-frequency-mean framings.

## Key Concepts for Software-Business

1. <!-- concept: product-owner --> **Product Owner accountability as the software-business primary role.** The Product Owner "is accountable for maximizing the value of the product resulting from the work of the Scrum Team" (Source: *Scrum Guide* 2020, "Scrum Team", "Product Owner"). The role is structural: ordering the Product Backlog, communicating the Product Goal, deciding trade-offs, absorbing stakeholder pressure into a single ordering decision. The PO is the role through which software-business decisions enter the team's daily work.

2. <!-- concept: product-goal --> **Product Goal as long-term strategic-positioning artefact.** The Product Goal "describes a future state of the product which can serve as a target for the Scrum Team to plan against... It is the long-term objective for the Scrum Team. They must fulfill (or abandon) one objective before taking on the next" (Source: "Scrum Artifacts", "Product Backlog", "Commitment: Product Goal"). For the software-business practitioner, the Product Goal is where market-entry, portfolio, and AI-integration decisions land in the team's operating frame.

3. <!-- concept: sprint-goal --> **Sprint Goal as the delivery-cadence commitment.** The Sprint Goal is "the single objective for the Sprint... Although the Sprint Goal is a commitment by the Developers, it provides flexibility in terms of the exact work needed to achieve it" (Source: "Scrum Artifacts", "Sprint Backlog", "Commitment: Sprint Goal"). It is the place where the practitioner balances roadmap commitments against engineering capacity each cycle — the "what can be done this Sprint" question is a delivery-cadence economic decision, not a planning hygiene exercise.

4. <!-- concept: definition-of-done --> **Definition of Done as the quality-and-compliance gate.** "The Definition of Done is a formal description of the state of the Increment when it meets the quality measures required for the product" (Source: "Scrum Artifacts", "Increment", "Commitment: Definition of Done"). Items failing the DoD "cannot be released or even presented at the Sprint Review." For the software-business practitioner, the DoD is where reliability investment, security investment, compliance posture, and "speed vs quality" economics land as a daily release gate, not as quarterly governance theatre.

5. <!-- concept: org-vs-team-dod --> **Organisational-vs-team DoD split.** "If the Definition of Done for an increment is part of the standards of the organization, all Scrum Teams must follow it as a minimum. If it is not an organizational standard, the Scrum Team must create a Definition of Done appropriate for the product" (Source: "Scrum Artifacts", "Increment", "Commitment: Definition of Done"). This is the standardise-vs-localise hinge for software-business: organisation-level DoD is the place where compliance-and-reliability investment becomes binding across the engineering org.

6. <!-- concept: sprint-cancellation --> **Sprint cancellation as a Product-Owner-only decision right.** "A Sprint could be cancelled if the Sprint Goal becomes obsolete. Only the Product Owner has the authority to cancel the Sprint" (Source: "Scrum Events", "The Sprint"). The most disruptive software-business decision available in Scrum — abandoning a Sprint's commitments — is reserved to a single accountable owner, not to the team or the executive chain.

7. <!-- concept: sprint-planning --> **Sprint Planning's three Topics as embedded software-business decisions.** Topic One: why is this Sprint valuable? (a value-and-positioning question). Topic Two: what can be done this Sprint? (a capacity-and-scope decision). Topic Three: how will the work get done? ("at the sole discretion of the Developers" — a build-decision-right boundary) (Source: "Scrum Events", "Sprint Planning"). The order matters: value before scope before plan.

8. <!-- concept: sprint-review --> **The Sprint Review as the regular board-and-stakeholder engagement.** The Sprint Review "is a working session and the Scrum Team should avoid limiting it to a presentation" (Source: "Scrum Events", "Sprint Review"). For the software-business practitioner, this is the structural moment where engineering outputs meet stakeholder absorption — a place where the practitioner translates technical work into business consequence in a regular cadence, not in crisis-driven board memos.

9. <!-- concept: release-vs-inspection-decoupling --> **Decoupling release from inspection.** "An Increment may be delivered to stakeholders prior to the end of the Sprint. The Sprint Review should never be considered a gate to releasing value" (Source: "Scrum Artifacts", "Increment"). Software-business consequence: release cadence is a business decision; inspection cadence is a process discipline. They should not be conflated.

10. <!-- concept: scrum-immutability --> **The framework is immutable; local tactics are the team's.** "The Scrum framework, as outlined herein, is immutable" (Source: "End Note"); but the format of the Daily Scrum, the team's specific Definition of Done where no organisational standard applies, and the decomposition of Product Backlog items are local-context decisions. Software-business consequence: the standardise-vs-localise hinge is built into the framework.

11. <!-- concept: empiricism --> **Empiricism over forecasting in commitment.** "Various practices exist to forecast progress, like burn-downs, burn-ups, or cumulative flows. While proven useful, these do not replace the importance of empiricism. In complex environments, what will happen is unknown. Only what has already happened may be used for forward-looking decision making" (Source: "Scrum Events", "The Sprint"). Software-business consequence: when the practitioner is asked to report a fixed-date commitment to a board, the framework's stance is that forecasts are inputs, not decisions; what has actually shipped is the evidence base.

12. <!-- concept: scrum-team-size --> **Scrum Team size and structure as a hiring constraint.** The Scrum Team is "typically 10 or fewer people... smaller teams communicate better and are more productive" (Source: "Scrum Team"). When teams "become too large, they should consider reorganizing into multiple cohesive Scrum Teams, each focused on the same product. Therefore, they should share the same Product Goal, Product Backlog, and Product Owner." Software-business consequence: team-structure decisions for software work have a default upper bound the framework names.

13. <!-- concept: cross-functional-self-management --> **Cross-functional self-management as the implicit hire criterion.** "Scrum Teams are cross-functional, meaning the members have all the skills necessary to create value each Sprint. They are also self-managing, meaning they internally decide who does what, when, and how" (Source: "Scrum Team"). Software-business consequence: the framework requires hiring for cross-functionality and self-management, not for purely-specialist or purely-managed work. Hiring patterns that select for narrow specialism create framework-fit problems.

14. <!-- concept: scrum-master --> **The Scrum Master as the organisational-engagement role.** The Scrum Master is responsible for "Leading, training, and coaching the organization in its Scrum adoption; Planning and advising Scrum implementations within the organization; Helping employees and stakeholders understand and enact an empirical approach for complex work; and, Removing barriers between stakeholders and Scrum Teams" (Source: "Scrum Team", "Scrum Master"). Software-business consequence: when the executive chain or board needs translation work to engage with engineering, the framework names the Scrum Master as a structural conduit alongside the Product Owner.

## Questions to Ask During Software-Business Work

### Phase 1: Strategic positioning (pricing, market entry, build-vs-buy, portfolio, AI integration)

| Need | Question |
|---|---|
| Locate the decision in the framework | Is this strategic decision being made by the Product Owner (where it structurally belongs), by a committee dressed as the Product Owner role, or by the executive chain operating around the Product Owner? "The Product Owner is one person, not a committee." |
| Anchor pricing/market-entry against the Product Goal | What is the Product Goal this decision serves or revises? "The Product Goal describes a future state of the product which can serve as a target for the Scrum Team to plan against." A pricing or market-entry decision that doesn't tie to a Product Goal is a free-floating commitment. |
| Frame the Sprint Planning Topic One question | If the strategic decision implies a Sprint commitment in the near term, what does the Product Owner propose for "why is this Sprint valuable?" — the value proposition the Sprint Goal will encode? |
| Sequence build-vs-buy against Product Backlog refinement | Is the build-vs-buy decision being resolved during Product Backlog refinement (where it belongs structurally) or improvised at Sprint Planning under timebox pressure? "Product Backlog refinement is the act of breaking down and further defining Product Backlog items into smaller more precise items." |
| Honour Product Owner authority on portfolio decisions | "For Product Owners to succeed, the entire organization must respect their decisions." Is the organisation overriding Product Owner ordering decisions, or working through the Product Owner? |
| Test the AI-integration question against the framework | Does the AI capability being integrated fit Scrum's "complex work" framing — where empiricism and inspect-and-adapt are the right disciplines? Or is it a routine deterministic capability where a different operating model applies? |

### Phase 2: Product and engineering economics (technical-debt, capacity, ROI, reliability-as-business-decision)

| Need | Question |
|---|---|
| Locate technical-debt remediation in Product Backlog ordering | Is technical-debt remediation being weighed against revenue work in the Product Backlog ordering decision (where it belongs), or being run as a separate parallel track outside the framework? The Product Owner orders the single backlog; trade-offs land there. |
| Encode reliability/quality investment in the Definition of Done | Is reliability or security investment being expressed as a Definition-of-Done bar (where it becomes a daily gate) or as a parallel commitment that doesn't bind the team's release decisions? "Work cannot be considered part of an Increment unless it meets the Definition of Done." |
| Distinguish org-standard vs team DoD | If the reliability/compliance investment must apply across teams, is it being authored as an organisational-standard DoD? "If the Definition of Done for an increment is part of the standards of the organization, all Scrum Teams must follow it as a minimum." |
| Read forecasting outputs as inputs, not decisions | Are burn-downs, burn-ups, or cumulative flow charts being used as decision inputs, or are they being treated as the decision? "These do not replace the importance of empiricism." |
| Set the Sprint Goal to discipline scope under pressure | When the work turns out different than expected, are Developers "negotiating the scope of the Sprint Backlog within the Sprint without affecting the Sprint Goal"? The Sprint Goal is the discipline that protects against scope creep eating quality. |
| Anchor capacity decisions in past-Sprint empirical data | "Only what has already happened may be used for forward-looking decision making." Is the capacity-planning decision being made on empirical Sprint output, or on theoretical capacity that hasn't been validated? |

### Phase 3: Team and capability building (hiring, structure, levelling, culture)

| Need | Question |
|---|---|
| Set hiring against the cross-functional self-managing criterion | "Scrum Teams are cross-functional, meaning the members have all the skills necessary to create value each Sprint. They are also self-managing, meaning they internally decide who does what, when, and how." Is the hire being scoped for both cross-functionality and self-management, or for narrow specialism the framework cannot absorb? |
| Bound team size at the framework's guideline | "The Scrum Team is small enough to remain nimble and large enough to complete significant work within a Sprint, typically 10 or fewer people." If the team is approaching the upper bound, is the next move a split into "multiple cohesive Scrum Teams, each focused on the same product"? |
| Test for hierarchies the framework refuses | "Within a Scrum Team, there are no sub-teams or hierarchies." Is the proposed team structure recreating the hierarchies the framework refuses, regardless of what the org chart looks like above the team? |
| Honour the three role accountabilities cleanly | Is the proposed role decomposing into Developers / Product Owner / Scrum Master in a way that aligns with each accountability? Or is a single person carrying multiple accountabilities in a way that creates structural conflict (e.g., the Scrum Master also being the Product Owner for the same team)? |
| Locate the Scrum Master in the organisational change posture | "The Scrum Master serves the organization in several ways, including: Leading, training, and coaching the organization in its Scrum adoption; Planning and advising Scrum implementations within the organization." For an org-level capability shift, is the Scrum Master being positioned to do this organisational work? |
| Source contractor/vendor relationships through the Product Owner | If contractors or vendor teams are involved, are they engaging with the Scrum Team through the Product Owner, or are they negotiating directly with Developers in a way that bypasses the single-accountable-owner constraint? |

### Phase 4: Operations and process (delivery cadence, governance, decision rights, change management)

| Need | Question |
|---|---|
| Set the Sprint length as a deliberate cadence decision | Sprints are "fixed length events of one month or less to create consistency." What Sprint length is right for this product's commercial cadence — given that "shorter Sprints can be employed to generate more learning cycles and limit risk of cost and effort to a smaller time frame"? |
| Lock decision rights to the framework's accountabilities | Who has the formal decision right for each operational question: Product Owner for ordering and Sprint cancellation; Developers for sizing, how-to-build, Daily Scrum format; the team collectively for Sprint Goal definition; team-or-organisation for DoD? Are operating decisions respecting these boundaries? |
| Run the Sprint Planning event as designed | Is Sprint Planning running through the three Topics in order — Why valuable, What can be done, How will it get done — and concluding with "the Sprint Goal must be finalized prior to the end of Sprint Planning"? An 8-hour timebox for a one-month Sprint. |
| Run the Daily Scrum at Developers' discretion | "The Developers can select whatever structure and techniques they want, as long as their Daily Scrum focuses on progress toward the Sprint Goal and produces an actionable plan for the next day of work." Is the Daily Scrum format being mandated by managers above the team, or is it the Developers' to set? |
| Run the Sprint Review as a working session, not a presentation | "The Sprint Review is a working session and the Scrum Team should avoid limiting it to a presentation." Are stakeholders engaging in a collaborative what-to-do-next conversation, or watching a demo? |
| Run the Sprint Retrospective to produce committed change | "The most impactful improvements are addressed as soon as possible. They may even be added to the Sprint Backlog for the next Sprint." Is the Retrospective producing committed change in the next Sprint Backlog, or producing wishlist items with no commitment? |
| Detect partial-implementation drift | Is the team quietly dropping events, watering down accountabilities, or weakening the DoD? "Implementing only parts of Scrum is possible, the result is not Scrum." Partial implementation reads to leadership as "Scrum isn't working" rather than as "Scrum was abandoned in pieces." |

### Phase 5: Risk, reliability, compliance (incidents, security, legal, regulatory, ethics)

| Need | Question |
|---|---|
| Express reliability investment as Definition-of-Done changes | "The Definition of Done creates transparency by providing everyone a shared understanding of what work was completed as part of the Increment." For a reliability incident, is the durable fix being encoded as a DoD change (where it gates future work) or as a one-off remediation that won't bind subsequent work? |
| Author cross-team compliance posture as organisational-standard DoD | "If there are multiple Scrum Teams working together on a product, they must mutually define and comply with the same Definition of Done." Is the cross-team compliance posture being expressed as a shared DoD, or as a separate compliance regime running outside the framework? |
| Locate cancel-Sprint authority for a regulatory shift | "A Sprint could be cancelled if the Sprint Goal becomes obsolete. Only the Product Owner has the authority to cancel the Sprint." If a regulatory event obsoletes the Sprint Goal mid-Sprint, is the cancellation decision being made by the Product Owner, or by the executive chain (which has no Sprint-cancellation authority in the framework)? |
| Use the Sprint Retrospective for incident-derived process change | The Sprint Retrospective inspects "individuals, interactions, processes, tools, and their Definition of Done." For a post-incident review, is the Retrospective the place where the process change lands, or is it being routed through a parallel incident-management process that doesn't bind the team's daily work? |
| Distinguish ethics-of-Scrum-application from Scrum's silence on ethics | The Guide is silent on the ethics of *what* a Scrum Team should build. The Product Owner's value-maximisation accountability does not authorise unethical product choices. For software-business AI-ethics or extractive-cost questions, the Guide hands off to other corpus references; it does not arbitrate. |
| Test for "release cadence equals inspection cadence" conflation | "An Increment may be delivered to stakeholders prior to the end of the Sprint. The Sprint Review should never be considered a gate to releasing value." For a time-pressured security or reliability fix, can the Increment ship before the next Sprint Review? The framework permits it. |

### Phase 6: Stakeholder communication (board, exec, investor, customer)

| Need | Question |
|---|---|
| Route board and exec engagement through the Product Owner | "The Product Owner may represent the needs of many stakeholders in the Product Backlog. Those wanting to change the Product Backlog can do so by trying to convince the Product Owner." Is the board's product-direction influence flowing through the Product Owner, or being lobbed at the Developers, the CTO, or the Scrum Master? |
| Use the Sprint Review as the regular stakeholder engagement | The Sprint Review is the structural moment where stakeholders engage with what was actually shipped. For a board engagement on product progress, is this the cadence — or are board members getting custom one-off updates that pull engineering attention away from the work? |
| Translate forecasts honestly to the board | "What will happen is unknown. Only what has already happened may be used for forward-looking decision making." If the board wants a fixed delivery date, is the practitioner offering an empirically-grounded forecast with crisp uncertainty, or treating the burn-down as a commitment? |
| Position the Product Goal as the long-term board narrative | "The Product Goal is the long-term objective for the Scrum Team. They must fulfill (or abandon) one objective before taking on the next." For board reporting, is the Product Goal the unit of narrative — or is the narrative shaped per board meeting in ways the team cannot deliver against? |
| Set Sprint Review attendees deliberately | Who needs to be in the Sprint Review for it to remain a working session and not a status performance? The wrong attendees (too senior, too many, wrong roles) collapse the engagement to a presentation, which the framework explicitly refuses. |
| Hold the cross-function negotiation between PO and other functions | When engineering, product, and sales are negotiating priorities, is the negotiation happening between the Product Owner and the other functions, or are sales/marketing/operations going directly to engineering and creating commitments the Product Backlog ordering doesn't reflect? |

## What to Look For

**Pattern: Product Owner role being run by committee.**

- *Signal:* Backlog ordering changes after every executive meeting; the Product Owner's stated priorities don't match the team's actual work; "we made a decision" but no individual carries the accountability.
- *Diagnosis:* The single-accountable-owner constraint the framework requires has been replaced by committee politics. "The Product Owner is one person, not a committee."
- *Follow-up:* Name the committee-run pattern explicitly; identify which one person carries the Product Owner accountability; route influence attempts to that person rather than to the team's daily work.

**Pattern: Definition of Done being eroded under date pressure.**

- *Signal:* Items being released that "meet the spirit of the DoD" without meeting the DoD; arguments about whether something is "really done" appearing mid-Sprint; "we'll fix that next Sprint" becoming a recurring concession.
- *Diagnosis:* The DoD is being treated as aspiration rather than as a release gate. "Work cannot be considered part of an Increment unless it meets the Definition of Done." DoD erosion is a quality-and-compliance debt that accumulates invisibly.
- *Follow-up:* Audit the last three Sprints for DoD compliance; either tighten the DoD enforcement or update the DoD (with organisational sign-off if it is an organisational standard) so the gate matches what's actually being released.

**Pattern: Sprint Review collapsing into a status presentation.**

- *Signal:* The Sprint Review is one-way (team presents, stakeholders receive); no Product Backlog adjustments are made in the room; attendance has crept up to a level where collaborative working is impossible.
- *Diagnosis:* The framework's collaborative-engagement design has been replaced by performance theatre. "The Sprint Review is a working session and the Scrum Team should avoid limiting it to a presentation."
- *Follow-up:* Set attendee criteria deliberately; reframe the Sprint Review purpose at the opening; make at least one Product Backlog adjustment in the room to re-establish the working-session pattern.

**Pattern: Forecasting artefacts being read as commitments.**

- *Signal:* The burn-down chart becomes "the plan"; the board asks why the team is "behind" because the burn-down line doesn't track linearly to zero; the team starts gaming the burn-down to appear on track.
- *Diagnosis:* Forecasting tools are being treated as decisions rather than as inputs. "What will happen is unknown. Only what has already happened may be used for forward-looking decision making."
- *Follow-up:* Reframe the artefact for the board as a forecast with uncertainty; report what has actually shipped against the Product Goal as the primary signal; degrade the burn-down to a secondary input.

**Pattern: Partial Scrum implementation framed as "Scrum isn't working."**

- *Signal:* The team has quietly dropped the Sprint Retrospective; the Daily Scrum has become a status meeting for managers; the Sprint Goal is being skipped; the Definition of Done is informal; nonetheless, "Scrum" is being credited or blamed for outcomes.
- *Diagnosis:* "Implementing only parts of Scrum is possible, the result is not Scrum." The framework has been abandoned in pieces but the label persists, creating attribution errors at the leadership level.
- *Follow-up:* Either restore the framework's components and re-test, or explicitly retire the Scrum label and adopt a different method honestly. The most damaging position is partial Scrum that gets reported up as full Scrum.

**Pattern: Cancel-Sprint authority being exercised by the executive chain.**

- *Signal:* A senior executive (not the Product Owner) decides to cancel a Sprint or rework its commitments mid-Sprint; the Product Owner is consulted but not the decider.
- *Diagnosis:* "Only the Product Owner has the authority to cancel the Sprint." The framework's most concentrated decision right has been overridden by hierarchy.
- *Follow-up:* Either ratify the cancellation by routing it through the Product Owner (and naming the executive's influence as influence, not authority), or accept that this is no longer a Scrum operating model and adjust the labelling accordingly.

**Pattern: Release cadence collapsing into Sprint Review cadence.**

- *Signal:* "We can't ship until the Sprint Review"; demo-ready Increments are being held back from customers for inspection-ceremony reasons; release frequency is artificially capped at one-per-Sprint.
- *Diagnosis:* The framework explicitly decouples release from inspection: "an Increment may be delivered to stakeholders prior to the end of the Sprint. The Sprint Review should never be considered a gate to releasing value." Conflating the two creates artificial release latency.
- *Follow-up:* Audit the release calendar; identify Increments that could ship before their Sprint Review; separate the release-decision (commercial) from the inspection-cadence (process).

## When to Use This Reference

- A *software-business decision* is being made and the question is whether the Scrum framework names a structural place for it (it usually does: PO for ordering, Sprint Planning for commitment, DoD for quality bar, Sprint Cancel for major reset, Sprint Review for stakeholder engagement).
- A *Product Owner role* is being scoped, debated, or being treated as a committee — the Guide's single-accountable-owner constraint is the source.
- A *Definition of Done* is being authored, updated, or eroded — the Guide names the DoD as the release gate, with organisational-vs-team scoping rules.
- A *Sprint cancellation* question is on the table — only the PO can; only if the Sprint Goal is obsolete.
- A *Sprint Review* is being treated as a status-report ceremony rather than a collaborative working session — the Guide is explicit on the distinction.
- A *standardise-vs-localise* question for software methodology — the Guide's "immutable framework, local tactics" stance is the hinge.
- A *board-reporting* question about engineering progress — the framework's empiricism stance is a discipline against burn-down-chart-as-commitment.
- A *partial-Scrum* drift is being labelled as Scrum at the leadership level — the immutability claim is the source for naming the gap.
- An *AI-integration* question about whether the work fits Scrum's "complex work" framing — the Guide's empiricism stance applies where inspect-and-adapt is the right discipline.

## Worked Example

A founder is preparing a board memo on a quarterly product slip. The product is a B2B SaaS platform; the team has been running Scrum for fourteen months. The slip is real: a feature committed for end-of-Q3 has moved to mid-Q4, with implications for two enterprise customer contracts.

The founder's first instinct is to write the memo around the burn-down chart and a recovery plan with new dates. The Scrum Guide pushes back on this in two specific ways.

First, the Sprint Review history is the more honest evidence base than the burn-down. "Only what has already happened may be used for forward-looking decision making." The founder rewrites the memo to lead with what has shipped against the Product Goal across the last quarter — three Increments delivered, two of which are revenue-active — and treats the burn-down only as a forecast input with crisp uncertainty.

Second, the cancel-Sprint and Product-Goal revision questions belong to the Product Owner, not the founder writing the memo. The founder consults with the Product Owner on whether the Product Goal is being abandoned (it is not — the goal is the same, the path has shifted) and whether any Sprint should be cancelled (no — the current Sprint Goal still serves the revised path). The memo names these decisions as PO decisions, communicated through the founder, rather than as founder decisions imposed on the PO. This protects the structural accountability the framework requires for product value.

Third, the founder uses the Definition of Done as the durable artefact for the reliability commitment to the enterprise customers. Rather than promising "we'll be more careful next quarter," the founder commits to a DoD update that names the reliability bar as an organisational standard, with the Product Owner authoring the specific change at the next refinement session. This makes the commitment binding on the team's daily work rather than aspirational. The board memo names the DoD change as the structural intervention, not the new date.

The memo lands with the board as crisper than the founder's instinct: empirical evidence base, named accountable owner (the PO), structural intervention (DoD update), and a forecast with uncertainty rather than a commitment masquerading as a plan.

## Anti-patterns This Reference Helps Avoid

**Anti-pattern: Treating Scrum as one of several "agile flavours" that can be partially adopted.**

- *Signal:* "We do Scrum, but we've adapted it" turns out to mean the Retrospective is skipped, the Sprint Goal is implicit, the DoD is informal, and the PO is a committee.
- *Diagnosis:* The Guide is explicit: "the Scrum framework, as outlined herein, is immutable. While implementing only parts of Scrum is possible, the result is not Scrum." Partial Scrum is a label-vs-implementation gap that misleads leadership decisions about what's working.
- *Follow-up:* Either restore the framework's components and run them honestly, or explicitly retire the Scrum label and adopt a different operating model. Hybrid in-between is the most expensive position because it attracts Scrum-attributed blame for outcomes the framework wasn't allowed to produce.

**Anti-pattern: Backlog grooming as a substitute for prioritisation gates.**

- *Signal:* The backlog count grows without bound; refinement is an endless triage task; "we'll prioritise it in the next refinement" becomes the default response to new requests.
- *Diagnosis:* The framework names refinement as "the act of breaking down and further defining Product Backlog items into smaller more precise items" — a sharpening operation for ready items, not a holding area for unprioritised work. The PO's ordering decision is the prioritisation gate; refinement is downstream of it.
- *Follow-up:* Audit the backlog for items that have not made it to "ready" status across three or more Sprints; either order them into upcoming work or archive them. Distinguish the PO's prioritisation decision (ordering) from the team's refinement work (sharpening) explicitly.

**Anti-pattern: Cancel-Sprint authority being treated as a board or executive decision.**

- *Signal:* A board member tells the founder "we should cancel this Sprint and redirect the team"; the founder agrees and instructs the Product Owner to execute.
- *Diagnosis:* "Only the Product Owner has the authority to cancel the Sprint." The framework concentrates the most disruptive product decision in one role for a reason: the cancellation has implications for product value the PO is accountable for. Routing the decision through the founder or board breaks the accountability chain.
- *Follow-up:* Either route the influence through the PO (the board tells the PO; the PO decides), or accept that this is no longer a Scrum operating model and adjust the framework expectations accordingly. Honour the framework boundary or change it openly.

**Anti-pattern: Sprint Review attendance creep collapsing the working session.**

- *Signal:* The Sprint Review has grown to 30+ attendees; the team performs a polished demo; no Product Backlog adjustments are made in the room; the event is described as "going well" because no one objects.
- *Diagnosis:* "The Sprint Review is a working session and the Scrum Team should avoid limiting it to a presentation." Attendance creep is the mechanism by which Sprint Reviews degrade to presentations: above a working-session attendee count, collaborative work becomes impossible.
- *Follow-up:* Set deliberate attendee criteria for the next Sprint Review; the question is "who needs to be in this working session," not "who wants visibility." Visibility-only attendees get the Sprint Review notes, not seats.

**Anti-pattern: DoD weakened to "make the date."**

- *Signal:* Items released as "done" but with caveats; "we'll add the test coverage next Sprint"; "the security review is queued for follow-up."
- *Diagnosis:* "If a Product Backlog item does not meet the Definition of Done, it cannot be released or even presented at the Sprint Review. Instead, it returns to the Product Backlog for future consideration." Weakening the DoD to make a date is the mechanism by which reliability and compliance debt accumulates without showing up in the team's metrics.
- *Follow-up:* Either hold the DoD and let the date slip (the framework's stance), or update the DoD explicitly so the bar matches what's being shipped (transparent). The covert weakening is the position to avoid.

**Anti-pattern: Sprint Goal as a list of items rather than a single objective.**

- *Signal:* "Our Sprint Goal is to deliver stories A, B, C, D, and E"; the goal is the Sprint Backlog rephrased.
- *Diagnosis:* "The Sprint Goal is the single objective for the Sprint. Although the Sprint Goal is a commitment by the Developers, it provides flexibility in terms of the exact work needed to achieve it." A list of items doesn't provide the flexibility the Guide intends; the team can't negotiate scope without affecting the goal because the items *are* the goal.
- *Follow-up:* Rewrite the Sprint Goal as a single objective that the items collectively serve; the items become negotiable scope, the objective stays fixed. Test by asking: if we couldn't deliver item B but could deliver A, C, D, E, would the Sprint Goal still be met?

## Through the cto lens

For the AI-native, opportunity-first, constraint-disciplined CTO at enterprise mid-modernisation scale, the Scrum Guide reads as a constraint-as-mechanism source — sharply useful in places, demanding interrogation in others.

**What the lens reweights:**

- *The Product Owner accountability* is the framework's clearest constraint-as-mechanism artefact: owner + capability gap (value maximisation) + repeatable gate (Product Backlog ordering decision). The lens elevates the PO question above every other Scrum question. If the PO is a committee, no other Scrum discipline can hold. The constraint-and-mechanism question is *who is the PO, what is their capability gap, what is the repeatable gate they own?*
- *The Definition of Done* is the framework's most direct demand-governance gate at the work-unit level. The lens reads the DoD not as a quality bar but as the team's repeatable gate against backlog grooming becoming the operating model. A team with a sharp DoD has the prioritisation gate at the right structural level; a team with a fuzzy DoD has displaced prioritisation into backlog accumulation.
- *The Sprint cancellation authority* is the framework's most concentrated decision right. The lens reads this as the explicit prioritisation gate for the most disruptive product reset — a CTO-comfortable structural pattern that the consultant-derivative cluster will frame as "the team needs more agility" instead of as "we have a named owner for this specific decision."
- *Empiricism over forecasting* maps directly onto the CTO's preference for signal quality over volume. The lens reads burn-down-as-truth as a signal-quality failure and replaces it with empirical Sprint output as the primary evidence base.

**What the lens flags as a missing dimension:**

- *The AI-native angle* is structurally absent from the Scrum Guide (the 2020 edition predates the AI-substrate question being load-bearing). The lens flags this as a gap to be filled by other sources, not as a Scrum failure. Specifically: the framework's "complex work" framing applies, but the role-bifurcation question (AI-platform-expert vs deep-domain-expert, with the generalist middle disappearing) is not addressed. The CTO reaches outside Scrum for this.

**What the lens treats as Past-tempo:**

- *Methodology purity arguments* about whether something "is Scrum" or "isn't Scrum." The lens reads these as Past-tempo discussions that don't advance the constraint — the load-bearing question is whether the team has the mechanism the work needs, not whether the label is correctly applied. The Guide's immutability claim is useful for naming partial-Scrum drift; it's Past-tempo when used to police method preference.

**The lens's native vocabulary applied to this distillation:**

- *Constraint as mechanism:* the PO accountability, the DoD, the Sprint Goal, the cancel-Sprint authority — each is a mechanism with owner-and-gate.
- *The lever:* the PO role is the single lever that unlocks the most Scrum value; without it, no other Scrum mechanism holds.
- *Demand choking:* the DoD is the framework's most direct demand-choking mechanism at the work-unit level.
- *Signal quality:* empiricism over forecasting; what has shipped over what is projected.
- *Capability not productivity:* hiring for cross-functional self-management (capability) rather than for narrow specialism (productivity-of-current-roles).

## Through the business-executive-stakeholder lens

For the Paradigm-A-operating, occasionally-Paradigm-B-espousing business executive at enterprise software-product-delivery, the Scrum Guide reads as both useful Paradigm-A vocabulary (named owner, KPI delta, timeboxed action, decision rights) and as a source of opportunistic Paradigm-B surface (system-shape role discipline, structural-acknowledgment).

**What the lens reweights as Paradigm-A load-bearing:**

- *The Product Owner as named accountable owner* — the framework's most direct Paradigm-A artefact. The stakeholder reads this as the answer to *who is accountable for product value?* with no committee diffusion. Use this vocabulary directly.
- *The Definition of Done as a KPI-delta mechanism* — items either meet the DoD or they don't; release decisions hinge on it; this is the variance-against-plan discipline the stakeholder reads as rigour.
- *The Sprint Goal as a commitment artefact* — the team's single objective for the Sprint, finalised at Sprint Planning. Paradigm-A vocabulary. Use directly.
- *The Sprint Review as a quarterly-business-review-style stakeholder cadence* — but framed as a working session, not a presentation. The stakeholder reads "working session" with some skepticism; the lens supplies the rigour by naming the structural design.
- *Sprint cancellation as a decision-rights artefact* — the PO has the authority; the framework names the decision right. Paradigm-A vocabulary; the lens reads this as the place where governance is encoded into the framework rather than diffused.

**The one parsimonious Paradigm-B move per artefact, applied to this distillation:**

- *The structural acknowledgment that role discipline is system-shaped, not individual-shaped.* The lens names this once: "The PO-as-single-accountable-owner is a structural design that prevents committee diffusion of product-value decisions. When ordering is contested across stakeholders, the durable fix is not to make the PO more 'aligned' but to honour the structural decision right the framework provides." This B-move is named once and not repeated; the rest of the lens-section stays in A-vocabulary.

**What recedes when this lens reads:**

- *Pure-system-thinking framings* of Scrum that downplay individual accountability. The Scrum Guide is rigorous about role accountabilities (Developers / PO / Scrum Master); Paradigm-B sermons that read Scrum as "team-collective accountability without individual roles" misrepresent the framework. The lens reads through these to the framework's actual structural design.
- *Hedged language about "Scrum maturity"* and "agile journey." The framework is either being run or not; partial implementation has consequences the framework names. The lens reads "Scrum maturity" hedges as Paradigm-B sympathy-performance and strips them.

**B-vocabulary the artefact can quote opportunistically:**

- *"Role clarity protects everyone"* — the framework's named accountabilities give every stakeholder a clear address. The stakeholder's espoused-B value of "role clarity" gets ratified by the framework's structural design.
- *"Single owner, system-protected"* — the PO-as-single-accountable-owner is both the named individual (Paradigm-A) and the structural protection against committee diffusion (Paradigm-B opportunistic surface).

**Decision the stakeholder will reach for:** approve / decline a specific Scrum implementation decision — DoD content, PO assignment, Sprint Review attendee list, Sprint length. The lens makes the decision crisp by naming the framework's structural place for the decision and the accountable owner.

## Through the pm-bounded-by-ba-role lens

For the PM whose title implies product authority but whose role is bounded by BA-shaped coordination work, the Scrum Guide reads as a *naming source for the authority gap*. The framework explicitly assigns the Product Owner accountability to a single person; the PM-bounded-by-BA's role frequently lives in the gap between this PO accountability and the actual exercise of it.

**What the lens reweights as load-bearing:**

- *The PO accountability as the destination for product-authority asks the PM cannot carry.* When an artefact lands in the PM's queue asking them to "decide priorities," "drive product strategy," or "shape demand," the lens routes the actual ask to where the framework places the authority: the PO. If the PM is also the named PO, the role's coordination work needs to be costed honestly; if the PM is not the PO, the artefact has misdirected the ask.
- *The single-accountable-owner constraint as the structural argument against committee-PO patterns.* The framework refuses committee Product Ownership: "The Product Owner is one person, not a committee." When the PM is being asked to coordinate among multiple "product owners" or "stakeholders-as-co-POs," the lens names this as a structural violation, not as a coordination challenge to be solved by harder absorption.
- *The Product Backlog refinement work as substantive PM activity.* "Product Backlog refinement is the act of breaking down and further defining Product Backlog items into smaller more precise items. This is an ongoing activity..." The lens reads this as substantive product work — not as overhead to be eliminated by AI tooling or process simplification — and protects time for it.

**What the lens flags as authority-vs-coordination-gap:**

- Artefacts that ask the PM to "prioritise the backlog" without naming who has the actual ordering authority (the PO). If the PM is the PO, the ask is in-role. If the PM is not the PO and the ask is being directed at them anyway, the authority gap is the load-bearing fact.
- Artefacts that ask the PM to "decide trade-offs" between competing stakeholder demands. The framework concentrates this decision at the PO. If the PM is being asked to make this decision without the PO accountability, the artefact has either confused the PM's role or is asking the PM to absorb the trade-off invisibly.
- Artefacts that ask the PM to "drive the Sprint Goal" or "drive the Sprint Review outcome." Sprint Goal definition is whole-team; Sprint Review collaborative work is whole-team; the framework does not assign these to the PM specifically. "Drive" verbs in this domain typically signal authority-assumption beyond the actual role.

**What the lens reads as protective for the PM:**

- *The PO accountability gives the PM a structural address for influence attempts.* When stakeholders pressure the PM directly, the framework supplies the script: "Those wanting to change the Product Backlog can do so by trying to convince the Product Owner." The PM can route the stakeholder to the PO rather than absorbing the pressure silently.
- *The Developers' authority over how-to-build* protects the PM from being asked to direct technical decisions outside their role. "How this is done is at the sole discretion of the Developers. No one else tells them how to turn Product Backlog items into Increments of value." The PM does not have to absorb how-to-build asks; the framework names the boundary.
- *The Scrum Master's role in "removing barriers between stakeholders and Scrum Teams"* gives the PM a partner for the organisational coordination work that often accumulates silently on the PM's desk.

**Coordination cost the artefact creates:**

- When the framework's role discipline is being violated in practice (committee POs, executive-cancellation of Sprints, Sprint Review attendance creep), the PM frequently absorbs the structural mismatch as additional coordination work. The lens names this absorption rather than treating it as the PM's natural role. The cost is real: PM time, stakeholder soothing, framework-translation labour.
- When AI tooling rollouts assume the PM will operate the new tools without the framework adjustments needed (e.g., new prioritisation tooling that doesn't change the underlying authority of who orders the backlog), the lens names the gap between tool-rollout and role-rollout.

**The lens does not perform sympathy.** The structural consequence: when the framework's accountabilities are honoured, the PM's coordination work is bounded and clear; when they are violated, the PM absorbs the violation invisibly. The framework provides language for naming the violation. The lens surfaces this consequence and stops.

## Integration with Other References

| Reference | Relationship |
|---|---|
| Letaw, *Handbook of Software Engineering Methods* | Letaw operationalises Scrum at the methods level (story points, ideal days, planning poker, INVEST, RACI, Tuckman team stages, decision-rights mechanics). The Scrum Guide is the framework; Letaw is one fill-in of how to populate it. For software-business: use the Scrum Guide for the framework constraints (PO accountability, DoD as release gate, Sprint Goal discipline); use Letaw for the methods that operate inside those constraints (specifically RACI for cross-team coordination, INVEST for story-readiness criteria, Tuckman for team-stage assessment in capability-building decisions). |
| Jones, *Evidence-based Software Engineering* | Jones reads Agile and Scrum critically: the post-1980 evidence collapse means many software-engineering claims (including Agile claims) are folklore-laden. For software-business: use the Scrum Guide for what the framework actually requires; use Jones for the empirical evidence base on cost, quality, and reliability statistics that should inform the DoD content and the capacity-planning decisions inside the framework. Specifically Jones on the bi-exponential fault-report pattern, the post-1980 evidence collapse, and resource estimation under uncertainty. |
| OpenStax, *Principles of Management* | Provides the broader management theory within which Scrum's team-level structure sits. PDCA maps onto Scrum's Sprint cycle; Mintzberg's six organisational structures cover the cross-team and cross-product structures Scrum's "multiple cohesive Scrum Teams" framing hands off to. For software-business: use the Scrum Guide for team-level structural decisions; use *Principles of Management* for organisational-structure decisions above the team. |
| OpenStax, *Accounting Vol 2* | Carries cost-classification primitives, make-or-buy relevant-cost analysis, theory of constraints, and CVP. The Scrum Guide is silent on cost economics; the DoD content for compliance and reliability investment should be informed by *Accounting Vol 2*'s cost-as-decision-relative framing. For build-vs-buy decisions that the PO is ordering in the Product Backlog, *Accounting Vol 2* supplies the relevant-cost analysis the Guide does not. |
| OpenStax, *Organizational Behavior* | Provides group dynamics, communication networks, conflict, and negotiation theory. The Scrum Guide names role accountabilities but does not analyse the power dynamics or group-decision patterns inside the team. For software-business: use the Scrum Guide for the role structure; use *Organizational Behavior* for the dynamics inside the structure (groupthink, conflict types, communication network patterns). |
| OpenStax, *Business Ethics* | Carries stakeholder theory (Mitchell-Agle-Wood salience, Freeman) and the normative-vs-instrumental-vs-descriptive stakeholder distinction. The Scrum Guide assigns the PO to represent stakeholders without offering a theory of stakeholder prioritisation. For software-business: combine — the PO orders the Product Backlog (Guide); Mitchell-Agle-Wood salience informs which stakeholders the PO prioritises representing (*Business Ethics*). |
| OpenStax, *Principles of Marketing* | Provides 5A customer journey, service-profit chain, RATER, and B2B buying centre. The Scrum Guide is silent on customer engagement methodology; the PO's stakeholder representation work for customer-facing products is informed by *Principles of Marketing*'s customer-engagement vocabulary. |
| OpenStax, *Business Law* | Carries the ADR-tier framework (negotiation / mediation / arbitration / litigation) and contract law. When stakeholder engagement at Sprint Review reaches contractual escalation, the Scrum framework hands off to formal escalation. The Sprint Review is upstream of formal negotiation; when collaboration fails, the engagement has moved out of Scrum's territory. |
| OpenStax, *Entrepreneurship* | Carries the lean-startup build-measure-learn cycle and the entrepreneurship funding-ladder. Scrum's inspect-and-adapt cycle is conceptually adjacent to build-measure-learn at the venture level. For software-business: use *Entrepreneurship* for venture-level pivots and funding decisions; use the Scrum Guide for product-development cadence inside an established venture. |
| `approach-perfect-field-guide-scrum-events` | The field guide operationalises each Scrum event at the facilitation level (specific protocols, agendas, edge cases). The Scrum Guide is the framework spec; the field guide is the practitioner runbook. Use the Scrum Guide for what each event must accomplish; use the field guide for how to run it well. |
| `open-kanban` | Kanban offers flow primitives (WIP limits, cycle time, cumulative flow diagrams) that Scrum's iteration model can incorporate (Scrum's reference to cumulative flows already anticipates this). For software-business: Scrum's iteration model is the cadence; Kanban's flow primitives are diagnostic tools for delivery economics within or alongside the cadence. |
| `nhs-just-culture-guide`, `tc-25-20-army-aar`, `lfuo-learning-review-guide-2024` | Incident-response and post-incident-learning sources. The Scrum Guide names the Sprint Retrospective as the team's structural learning event; for incidents that cross into individual-vs-system attribution (NHS Just Culture), severe consequence (TC 25-20), or learning-loop design (LFUO), these sources extend the Retrospective's discipline beyond what the Guide specifies. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The Scrum Guide (2020 edition) is notable for citing no external sources within its body — it does not reference the Agile Manifesto, prior Scrum literature, Sutherland's or Schwaber's earlier writings, or the broader iterative-development literature. The deep reference confirms this explicitly: the Guide "does not cite Agile, the Agile Manifesto, Sutherland's earlier writings, Schwaber's earlier writings, or any of the broader iterative-development literature within its body." There are therefore no [BT]-marked borrowed-through gaps in this source's own claims; the framework presents itself as a self-contained canonical statement.

The sole external influence the deep reference records is directional — Letaw's *Handbook of Software Engineering Methods* cites the Scrum Guide, not the reverse. The VersionOne "State of Agile" surveys and derivative adoption-statistics claims that appear in third-party Scrum commentary are not in the Guide itself and are not present in this distillation.

**Named limits of the source.** The Guide is explicit about what it does not prescribe: "The Scrum framework is purposefully incomplete, only defining the parts required to implement Scrum theory" (Scrum Definition). Specific named limits relevant to software-business work:

- *Pricing methodology, market-entry analysis, build-vs-buy decision frameworks.* The Scrum Guide encodes where these decisions land (PO accountability, Product Backlog ordering, Product Goal alignment) but does not arbitrate them. Route to OpenStax *Principles of Marketing*, *Accounting Vol 2*, and Jones's *Evidence-Based Software Engineering* for the decision frameworks.
- *Estimation methods.* Story points, ideal days, planning poker — not addressed. Route to Letaw's *Handbook of Software Engineering Methods*.
- *Organisational structures above the team level.* The Guide names "multiple cohesive Scrum Teams" but does not specify SAFe, LeSS, Nexus, or Scrum-of-Scrums coordination patterns. Route to OpenStax *Principles of Management* for Mintzberg's six structures.
- *Stakeholder typology and prioritisation theory.* The Guide uses "stakeholders" without offering Mitchell-Agle-Wood salience or any other prioritisation framework. Route to `openstax-business-ethics`.
- *Hiring strategy, team composition, levelling, and compensation.* The Guide names cross-functionality and self-management as criteria but does not specify role mixes. Route to `openstax-principles-management` and `openstax-organizational-behavior`.
- *Ethics of what to build.* The Guide does not arbitrate what a Scrum Team should build. "The Product Owner's value-maximisation accountability does not authorise unethical product choices" is a distillation-level inference, not a Guide claim.
- *Specific compliance, security, and regulatory content.* The DoD is where these land; the Guide does not prescribe content. Route to industry-specific sources.
- *Negotiation theory for cross-function conflicts.* TKI five modes, BATNA, principled negotiation — these live in OpenStax *Organizational Behavior* (Ch 14.4) and *Business Law*. The Scrum Guide names the structural roles for negotiation but does not supply the negotiation theory.

**Evidence-marker continuity.** The Scrum Guide is a brief primary source (14 pages); virtually all substantive claims in the deep reference carry [V] markers from direct quotation or close paraphrase. This distillation paraphrases [V]-marked content throughout and cites by section name (e.g., "Scrum Artifacts, 'Increment', 'Commitment: Definition of Done'"). The framework's key structural claims — Product Owner as single accountable owner, Sprint Goal as the single objective, DoD as release gate, cancel-Sprint authority residing only with the PO, empiricism over forecasting — are all [V]-grounded in the deep reference and are cited by section name in this distillation. No claims have been smuggled in from the broader Scrum ecosystem (SAFe, LeSS, Nexus, derivative coaching frameworks) without explicit attribution.
