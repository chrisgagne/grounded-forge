# NHS Just Culture Guide, Software-Business Distillation

**Source:** NHS Improvement (2018). *A Just Culture Guide*. A3 landscape poster, single page. Open Government Licence v3.0 (CC BY 4.0-equivalent). Based on the work of Professor James Reason and the National Patient Safety Agency's Incident Decision Tree. https://cpcw.org.uk/wp-content/uploads/sites/19/2018/03/180316-NHSi_just_culture_guide_A3.pdf.

**Pass G verdict:** fire-narrow on Phase 5 (Risk, reliability, compliance) with a cross-axis note on Phase 3 (Team and capability building). The source is a domain-specific decision aid for patient-safety incidents; the software-business projection narrows to the analogue case — an engineer is associated with a software incident (security breach, outage, defect with customer impact, data loss, regulator-visible event) and a leader is deciding whether to direct corrective action at the individual or at the system that produced the conditions. The other software-business phases (strategic positioning, product-economics, operations process, stakeholder-communication) are out-of-axis for this source; route them through `decision-making` or `stakeholder-engagement` distillations instead.

## Software-Business Relevance

The NHS Just Culture Guide is the corpus's load-bearing artefact for the *engineer-after-incident* decision: a software incident has occurred, the investigation has begun to surface a concern about an individual action (a bad deployment, a misconfigured permission, a missed pager, a delete-without-confirm), and a leader — typically the CTO, an engineering manager, a head of platform, or a head of security — must decide whether the appropriate response is directed at the individual or at the system that produced the conditions. The source's default-to-system prior — "action singling out an individual is rarely appropriate — most patient safety issues have deeper causes and require wider action" [V] (Source: Preamble, "Purpose and use") — maps cleanly onto software incidents, where the deployment pipeline, observability gap, dependency surprise, on-call rota structure, alert quality, and team supervision can shape the conditions in which an engineer makes the proximate mistake.

The five tests, applied to software, are operationally specific. Q1 (deliberate harm) maps to insider threat, fraud, sabotage, data exfiltration with intent — the rare path where police referral is on the table, alongside regulatory bodies (DPA, GDPR enforcement, sectoral regulators) and disciplinary processes, which the residual G branch can also reach. Q2 (health) maps to engineer burnout, on-call exhaustion, mental-health load, and substance abuse affecting work — to watch for in over-stretched on-call rotations and end-of-quarter delivery crunches; the response is occupational-health and substance-abuse-at-work pathways. Q3 (foresight — agreed protocols, workable, in routine use, knowingly departed from) maps to runbooks, deployment policies, change-management gates, code-review requirements, and on-call procedures — the canonical question is whether the protocol was workable and routinely used, because a runbook can exist yet be unworkable, or a deployment policy can be honoured in the breach. Q4 (substitution — peer behaviour, training gap, supervision absence) maps to the *would-another-engineer-have-done-the-same* test, which sits close to the blameless-postmortem stance the Open Practice Library describes (a distillation-level parallel), plus the structural questions about onboarding, training, and senior on-call coverage. Q5 (mitigating circumstances) maps to the residual: clear protocol, in routine use, knowingly departed from, no peer-behaviour exoneration, no training gap, no supervision absence — and then significant mitigation, or its absence.

The wider-investigation parallel, preserved on every recommendation, aligns with the software-business practice of producing a blameless post-mortem alongside any individual-directed response: "the patient safety incident investigation should indicate the wider actions needed to improve safety for future patients" [V] (Source: Q3, "Recommendation D"; Q4, "Recommendation E"; Q5, "Recommendation F"; Q5, "Recommendation G") becomes, in software, "the incident review should indicate the wider actions needed to improve reliability for future customers". The frame protects against a software-incident failure mode: the visible individual response (PIP, suspension, termination) terminates the corrective work, the wider system fix never lands, and the same incident recurs with a different proximate engineer.

This distillation projects the source onto the software-business task at the engineer-after-incident decision specifically. It does not duplicate the general tree-walking that `decision-making/nhs-just-culture-guide-decision-making.md` covers; for the full decision-tree mechanics, read that distillation. The software-business projection adds the software-specific mapping for each test, the texture of the *engineer-after-incident* leadership decision, and the cross-cut with the corpus's other software-business sources on incident response, organisational structure, and capability-building.

## Key Concepts for Software-Business

1.  **The five sequential tests, applied to software incidents.** Q1 deliberate harm → Q2 health → Q3 foresight → Q4 substitution → Q5 mitigating circumstances. Each test gates the next; only one action (or failure to act) is taken through the tree at a time. The order matters in software too: separate intent from impairment from runbook-contract from peer-behaviour from mitigation before reaching for management action. (Source: Q1-Q5)

2.  **Default to system, not to individual.** "Action singling out an individual is rarely appropriate — most patient safety issues have deeper causes and require wider action" [V] (Source: Preamble, "Purpose and use"). Recommendations D and E explicitly say action singling out the individual is unlikely to be appropriate, with wider actions that may include, but not be limited to, the individual. The default carries over to software by analogy: expect most outages, breaches, and defects with customer impact to have deeper causes (deployment pipeline weaknesses, observability gaps, dependency surprises, on-call structure, alert quality, training gaps, supervision absence) and to require wider action (a distillation-level expectation, not a source finding). The default is a check on the "blame the engineer" reflex that recurs in software incident response. (Source: Preamble, "Purpose and use"; Q1-Q5 recommendations)

3.  **Q1 (deliberate harm) in software: the insider-threat / fraud / sabotage path.** The only branch addressing intent. In software, this maps to deliberate data exfiltration, deliberate sabotage of systems, insider fraud, intentional regulatory violation, theft of trade secrets. A Yes routes to organisational guidance for management action — possibly including regulatory bodies (data-protection authorities, financial regulators, sectoral regulators), suspension, police referral, and disciplinary processes — paired with wider investigation. The wider investigation is preserved even on this branch: how did the system fail to detect or prevent the deliberate harm? (Source: Q1, "Deliberate harm test"; Q1, "Recommendation A")

4.  **Q2 (health) in software: burnout, on-call exhaustion, substance-affecting-work.** Substance abuse (2a), physical ill health (2b), mental ill health (2c). In software, the positive findings to watch for are mental-health load, on-call exhaustion, and burnout from end-of-quarter crunch — and substance abuse where chronic high pressure or shift work contributes. Yes to 2a routes to substance-abuse-at-work guidance (Recommendation B); Yes to 2b or 2c routes to organisational guidance for health issues affecting work, likely occupational-health referral (Recommendation C). Both pair with the backward-looking system question: could the health issue or substance abuse have been recognised and addressed earlier? In software-business terms: could the on-call rota, the alerting load, the deployment cadence, the workload allocation have surfaced the impairment? (Source: Q2, "Health test"; Q2, "Recommendation B"; Q2, "Recommendation C")

5.  **Q3 (foresight) in software: the runbook / deployment-policy / change-management test.** Three sub-questions, all must be Yes to advance: agreed protocols / accepted practice in place (3a — runbook, deployment policy, change-management gate, code-review requirement, on-call procedure), workable and in routine use (3b), knowingly departed from (3c). The 3b condition is load-bearing for software because runbooks that exist but are unworkable, deployment policies honoured in the breach, code-review requirements waived under date pressure, and on-call procedures designed for a smaller system are the cases to watch for. Any No routes to Recommendation D — singling out is unlikely to be appropriate, and the wider actions may include, but not be limited to, the individual. (Source: Q3, "Foresight test"; Q3, "Recommendation D")

6.  **Q4 (substitution) in software: the would-another-engineer-have-done-the-same test.** Three sub-questions, any Yes routes to Recommendation E: peer behaviour (4a — would another engineer with the same context, the same alert flood, the same on-call burden, the same tooling, have made the same decision?), training equity (4b — was the engineer missed out when relevant training was provided to peers — incident-response training, security training, framework-specific upskilling?), supervision adequacy (4c — was senior on-call coverage absent, was a code review skipped, was a senior engineer's review not requested where ordinarily it would be?). The substitution test's operational question is whether substituting another comparable engineer into the same situation would have produced a different outcome; that question sits close to the blameless-postmortem stance the Open Practice Library describes ("Our job is not to point fingers at an unlucky engineer" [BT], OPL, Practice "Blameless Postmortem") — a distillation-level parallel. (Source: Q4, "Substitution test"; Q4, "Recommendation E")

7.  **Q5 (mitigating circumstances) in software: the residual.** Reached only by cases that have cleared deliberate-harm, health, foresight (knowing departure from workable runbook in routine use), and substitution (no peer-behaviour, training-gap, or supervision-failure exoneration). Yes routes to Recommendation F — "action directed at the individual may not be appropriate" [V]; organisational guidance, likely including senior HR advice on the degree of mitigation. No routes to Recommendation G — graduated management action ranging through individual training, performance management, competency assessments, changes to role, increased supervision, on toward regulatory bodies, suspension, and disciplinary processes. In software-business terms the operator should expect the residual to be rare and most cases to exit at D or E (a distillation-level expectation, not a source finding). (Source: Q5, "Mitigating circumstances"; Q5, "Recommendation F"; Q5, "Recommendation G")

8.  **The wider-investigation parallel as blameless-post-mortem alignment.** Every recommendation, including Recommendation A (deliberate harm) and Recommendation G (residual management action), pairs its operational guidance with a directive about wider investigation. In software, this aligns with blameless post-mortem practice: the individual response (where any is directed) does not terminate the system-level corrective work. The wider investigation continues. The frame is a structural check on the failure mode where the visible individual response substitutes for the system fix. (Source: Q1-Q5 recommendations)

9.  **The decomposition discipline for multi-action incidents.** "The guide can only be used to take one action (or failure to act) through the guide at a time. If multiple actions are involved in an incident they must be considered separately" [V] (Source: Preamble, "Please note", bullet 4). Software incidents can involve multiple actions (a bad commit; an inadequate review; a missed alert; a delayed escalation; a botched rollback); the discipline of decomposing into distinct actions and walking the tree separately for each is part of using the source correctly. The deep reference flags this as load-bearing structural caveat. (Source: Preamble, "Please note", bullet 4)

10.  **The re-entrant property as alignment with iterative incident review.** "A just culture guide can be used at any point of an investigation, but the guide may need to be revisited as more information becomes available" [V] (Source: Preamble, "Please note", bullet 2). Software incident reviews can surface new facts after the initial review (a deeper cause analysis turns up an upstream defect; a postmortem-after-the-postmortem changes the picture; the same incident recurs and reframes the original analysis). The re-entrant property means the just-culture decision is not closed by the first walk through the tree. (Source: Preamble, "Please note", bullet 2)

11.  **The dual purpose: protect engineers from unfair targeting; protect customers / users by surfacing system causes.** The source's stated dual end — "protecting staff from unfair targeting" [V] and protecting patients "by removing the tendency to treat wider patient safety issues as individual issues" [V] (Source: Preamble, "Purpose and use") — maps to a dual end in software: protecting engineers from blame-driven incident response, and protecting customers / users / regulators by ensuring the wider system causes are addressed. The two ends are presented as aligned, not in tension. (Source: Preamble, "Purpose and use")

12.  **The transferable pattern: intent → impairment → system contract → peer behaviour → mitigation.** Taken as a sequence, the five tests are a portable pattern for the software-business decision about whether to direct corrective action at an individual engineer or at the engineering system that produced the conditions for error. The pattern is calibrated to patient safety in the source; the order of filters transfers. (This concept 12 is a distillation-level synthesis claim, not stated in the source — the source presents the five tests as patient-safety-specific.)

## Questions to ask during a software-incident just-culture decision

### Phase 5 — Risk, reliability, compliance (the primary fire)

The software-business task spec names this phase explicitly in §2a. The triggers that fire this distillation: incident-response or post-incident-learning concern; security or reliability event with PR + customer dimensions. Use the tables below when one of those triggers names the operator's situation.

#### Phase 5.0: Decide whether the just-culture decision applies

| Need | Question |
|---|---|
| Test the trigger | Has the incident review begun to suggest a concern about an individual engineer's action, beyond the system-level corrective work? If not, do not start the tree — keep the focus on the system. |
| Decompose if needed | Are there multiple distinct actions or omissions in this incident (commit + review + alert + escalation + rollback)? If so, each is a separate trip through the tree. |
| Confirm the conversation | Is this a leader-to-leader conversation (CTO and head of platform; engineering manager and head of HR; head of security and head of legal) that needs structuring? The guide is positioned as a conversation aid. |
| Locate parallel obligations | Have I confirmed the blameless post-mortem is also under way, independent of the just-culture decision? |
| Check HR coupling | Is HR being engaged in parallel? The guide does not replace HR advice on employment-law dimensions. |

#### Phase 5.1: Apply Q1 — deliberate harm test

| Need | Question |
|---|---|
| Test for intent | Was there any intention to cause harm — sabotage, data exfiltration, deliberate regulatory violation, insider fraud? (Q1.1a) |
| Route on Yes | If Yes, follow organisational guidance — potentially regulatory bodies (data-protection authority, sectoral regulator), suspension, police referral, disciplinary processes — and ensure the wider investigation asks how the system failed to detect or prevent the deliberate harm. |
| Proceed on No | If No, move to Q2; do not skip steps. |

#### Phase 5.2: Apply Q2 — health test

| Need | Question |
|---|---|
| Substance abuse | Are there indications of substance abuse affecting work? (Q2.2a) |
| Physical health | Are there indications of physical ill health? (Q2.2b) |
| Mental health | Are there indications of mental ill health — burnout, on-call exhaustion, sustained sleep deprivation, anxiety load? (Q2.2c) |
| Route on substance abuse | If Yes to 2a, follow organisational substance-abuse-at-work guidance; wider investigation should ask whether the substance use could have been recognised and addressed earlier (workload pattern, shift work, on-call burden). |
| Route on ill health | If Yes to 2b or 2c, follow organisational guidance for health issues affecting work (likely to include occupational-health referral); wider investigation should ask whether the impairment could have been recognised — alerting load, deployment cadence, workload allocation, on-call rota structure. |
| Proceed if none | If No to all three, move to Q3. |

#### Phase 5.3: Apply Q3 — foresight test

| Need | Question |
|---|---|
| Protocol existence | Are there agreed runbooks, deployment policies, change-management gates, code-review requirements, or on-call procedures that apply to the action / omission? (Q3.3a) |
| Protocol viability | Were the protocols workable and in routine use? Or were they runbooks that exist but are unworkable, deployment policies honoured in the breach, code-review requirements waived under date pressure, on-call procedures designed for a smaller system? (Q3.3b) |
| Knowing departure | Did the engineer knowingly depart from these protocols — aware of the protocol, aware of the departure, choosing to depart? (Q3.3c) |
| Route on any No | If No to any of 3a, 3b, or 3c, action singling out the engineer is unlikely to be appropriate; the wider investigation should indicate the actions needed — protocol fixes, deployment-pipeline fixes, observability fixes, training fixes — which may include, but not be limited to, the engineer. |
| Proceed only on Yes-to-all | If Yes to all three, move to Q4. (The conjunction is required.) |

#### Phase 5.4: Apply Q4 — substitution test

| Need | Question |
|---|---|
| Peer behaviour | Would another engineer with the same context, the same alert flood, the same on-call burden, the same tooling, the same deployment-pipeline state, have made the same decision? (Q4.4a) |
| Training equity | Was the engineer missed out when relevant training was provided to peers — incident-response training, security training, framework-specific upskilling, runbook-walkthroughs? (Q4.4b) |
| Supervision adequacy | Was senior on-call coverage absent? Was a code review skipped where it would ordinarily have been requested? Was a senior engineer's review not requested where the change's risk-profile warranted it? (Q4.4c) |
| Route on any Yes | If Yes to any of 4a, 4b, or 4c, action singling out the engineer is unlikely to be appropriate; the wider investigation should indicate the actions needed (peers' baseline behaviour, training programme, supervision structure), which may include, but not be limited to, the engineer. |
| Proceed on No-to-all | If No to all three, move to Q5. |

#### Phase 5.5: Apply Q5 — mitigating circumstances

| Need | Question |
|---|---|
| Test for mitigation | Were there significant mitigating circumstances — a personal crisis, a recent role change, a re-org-driven context loss, an unusual external pressure? (Q5.5a) |
| Route on Yes | If Yes, action directed at the engineer may not be appropriate; seek senior HR advice on the degree of mitigation; preserve the wider investigation. |
| Route on No | If No, follow organisational guidance for appropriate management action — graduated from individual training, performance management, competency assessments, changes to role, increased supervision, through to regulatory bodies, suspension, and disciplinary processes. Wider investigation still needed. |

#### Phase 5.6: After the decision

| Need | Question |
|---|---|
| Communicate proportionately | Can the response be explained to the engineering org, the affected customers, the board, and (where relevant) regulators in a way that shows the response was calibrated to the circumstances in which the error was made? |
| Preserve the parallel obligation | Is the blameless post-mortem also producing the wider corrective actions — pipeline fixes, observability fixes, runbook fixes, training fixes — regardless of which branch the individual response sits on? |
| Re-enter if new information surfaces | Have any facts emerged from the deeper investigation, the postmortem-after-the-postmortem, or a recurrence that would change the answer to any of Q1-Q5? If so, walk the tree again. |
| Confirm the recordkeeping | Has the guide's use been documented with reference to organisational HR and incident-reporting policies? |

### Phase 3 cross-axis note — Team and capability building

The task spec's §2a Phase 3 table names `nhs-just-culture-guide` as a cross-axis reference under "engineering-management culture decision" — specifically psychological safety and authority gradient. The just-culture default-to-system prior, with its stated aim of "protecting staff from unfair targeting" [V], bears on how an engineering organisation responds when something goes wrong; its link to psychological safety is a distillation-level reading, not a claim the source makes. An engineering-management culture decision (how do we respond when something goes wrong?) is the standing precondition that the just-culture frame answers. For the team-and-capability projection, use this distillation's concept 2 (default to system) and concept 8 (wider-investigation parallel) as the load-bearing material; route the rest of the team-and-capability framing through `openstax-organizational-behavior` and `openstax-principles-management` distillations, which carry the broader Theory-X-vs-Theory-Y treatment; for psychological-safety practices, see `open-practice-library`.

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| Post-incident chat thread converging on "who pushed the change?" before the investigation has surfaced underlying causes | The blame-the-engineer reflex is recruiting; the conversation has skipped Q3 and Q4 and gone straight to individual response | Pause the thread; route the conversation through the tree; surface the system-level questions the chat has skipped |
| Runbook cited as evidence the engineer "should have known" — but no one has confirmed the runbook is workable or in routine use | Q3.3b has been assumed Yes without testing; the foresight test has been collapsed onto Q3.3a alone | Test 3b: is the runbook workable? Is it in routine use? Or is it a document that exists in the wiki but no one follows? |
| Engineering org talking about "tightening" on-call procedures after an incident where the on-call engineer was clearly impaired by sustained workload | Q2 has been skipped; the conversation has moved to Q3 / Q5 without testing health | Route back to Q2; ask whether the on-call rota, alerting load, and sleep deprivation contributed; if so, the response runs through organisational health guidance (likely occupational-health referral), with the wider investigation alongside |
| Board / exec pressure for a visible individual response after a customer-visible incident | Variance from the source's default-to-system prior; the visible response is being substituted for the system fix | Surface the wider-investigation parallel as the response that addresses future customer outcomes; protect the engineer-after-incident decision from the perception-management pressure |
| Recurrence of the same incident with a different proximate engineer | The first incident's individual response substituted for the system fix; the system condition that produced the original incident has reproduced it | Walk the tree again on the recurrence; the locus is system; the wider investigation from the original incident did not land |
| HR escalation path opens before the just-culture decision has been walked | The guide and HR are running in sequence rather than in conjunction: the just-culture conversation is being skipped | Run the tree alongside the HR process, not after it; the guide does not replace HR advice and should be used in conjunction with organisational policy (Preamble, "Please note", bullet 3) |
| Multi-action incident treated as a single trip through the tree | The decomposition discipline has been skipped; the most-visible action is being treated as the whole incident | Decompose into distinct actions; walk the tree once per action; the recommendations may differ across actions |

## When to Use This Reference

Reach for this distillation when:

- A software incident has occurred (security breach, outage, defect with customer impact, data loss, regulator-visible event) **and** the conversation has begun to surface a concern about an individual engineer's action, beyond the system-level corrective work.
- A leader is deciding whether to direct corrective action at an engineer or at the engineering system that produced the conditions.
- The pressure to "do something visible" (from board, exec, customer, regulator) is recruiting the conversation away from the system-level corrective work.
- A blameless post-mortem is under way and the question of individual response needs a structured frame so the post-mortem's blamelessness is not undermined.
- A recurrence of an incident with a different proximate engineer suggests the first individual response substituted for the system fix.

Do not reach for this distillation when:

- The question is general engineering-management culture — route through `openstax-organizational-behavior` and `openstax-principles-management` distillations; for general psychological-safety design, route through `open-practice-library`.
- The question is about the post-mortem facilitation itself — route through `tc-25-20-army-aar` and `lfuo-learning-review-guide-2024` distillations.
- The question is about the legal-employment frame within which the response is taken (Title VII, ADA, FMLA, at-will doctrine, workplace torts) — route through `openstax-business-law` distillations.
- The question is about general decision-making mechanics — route through `decision-making/nhs-just-culture-guide-decision-making.md` for the full tree-walk.

## Worked Example

A SaaS company runs a deployment-pipeline incident: a deploy from a senior backend engineer pushed a config change that disabled a customer-facing feature for 47 minutes. The change passed code review, but the reviewer was the engineer's manager — the only senior available on a Friday afternoon. The deployment policy required a senior-engineer code review but did not specify the reviewer must be independent of the change author's reporting line. The alerting on the disabled feature had been silenced earlier in the week by the on-call engineer after a flapping-alert storm. The board asked the CTO: "what's the consequence for the engineer who made the change?"

**Walking the tree.** The source frames the tree as a sequential conversation: "This guide supports a conversation between managers about whether a staff member involved in a patient safety incident requires specific individual support or intervention to work safely." [V] The prior is explicit: "action singling out an individual is rarely appropriate — most patient safety issues have deeper causes and require wider action." [V] (Source: NHS Improvement, *A Just Culture Guide*, Preamble, "Purpose and use")

Q1 deliberate harm: No. Q2 health: the engineer had been on a tight delivery sprint; no indications of substance abuse, no indications of mental ill health beyond usual end-of-quarter pressure — No to 2a, 2b, 2c. (Source: Q2, "Health test")

Q3 foresight: 3a (agreed protocol exists — yes), 3b (workable and in routine use — yes, as written). The policy required a senior-engineer code review but the implicit norm about reviewer-independence from the reporting line was not codified; the team had been routinely using manager-as-reviewer when no other senior was available. The safety property the policy aimed to produce had not been delivered. 3c (did the engineer knowingly depart? — no: the change had the senior review the policy required; the policy simply did not require reviewer independence). 3c is No. Any No to 3a, 3b, or 3c routes to Recommendation D: action singling out the engineer is unlikely to be appropriate; the wider actions may include, but not be limited to, the engineer. (Source: Q3, "Foresight test"; Q3, "Recommendation D")

**Wider investigation.** The source directs: the patient safety incident investigation "should indicate the wider actions needed to improve safety for future patients." [V] In software-business terms: wider actions for future customers. (Source: Q3, "Recommendation D") The CTO commits to three fixes with named owners: reviewer-independence requirement codified (deployment team lead, 14 days); alert routing reviewed and flapping-alert handling improved (observability team lead, 30 days); deploy to customer-facing features outside business hours requires explicit risk-acknowledgment (platform team lead, 30 days).

**Board communication.** Lead with the customer-impact summary and 47-minute MTTR; state protocol-and-alerting findings without naming the individual; commit the three fixes. One structural reframe: "the locus of corrective work here is the deployment pipeline, not the engineer who pushed the change" — surfaced as a single Paradigm-B move inside an A-shaped operational envelope.

**Re-entry.** A month later, a deeper review surfaces that the original alerting silencing was a system signal — the flapping alert had been misfiring for six weeks with no owner. The CTO walks the tree again on the silencing action (separate action, separate trip through the tree). The source is explicit: "the guide may need to be revisited as more information becomes available." [V] (Source: Preamble, "Please note", bullet 2) The routing is the same; a fourth wider-action commitment is added: alert ownership at the team level, quarterly tuning review.

## Anti-patterns This Reference Helps Avoid

- **The "fire the engineer" reflex after a customer-visible incident.** Signal: the conversation moves from incident facts to individual response without walking the tree. Diagnosis: variance from the source's default-to-system prior; visible individual response substituting for system fix. Follow-up: route the conversation through Q1-Q5; preserve the wider-investigation parallel; surface the system causes the visible response would conceal.

- **Treating a runbook's existence as evidence of foresight.** Signal: "The engineer should have followed the runbook" cited without anyone confirming the runbook is workable or in routine use. Diagnosis: Q3.3b has been assumed Yes; the foresight test has been collapsed onto Q3.3a alone. Follow-up: test 3b explicitly; if the runbook is unworkable, the locus is the runbook, not the engineer.

- **Skipping Q2 on impaired engineers.** Signal: an engineer who was clearly on an unsustainable on-call rota is routed through Q3 / Q4 / Q5 as if Q2 had returned No. Diagnosis: the health test has been skipped because the impairment is structural (the system has produced the burnout) rather than individual (the engineer arrived burnt out). Follow-up: route back to Q2 if the workload has produced indications of physical or mental ill health (the distillation's reading of Q2); pair it with the source's system question: could the health issue have been recognised and addressed earlier?

- **Multi-action incidents walked as single trips.** Signal: the most-visible action (the bad commit) is treated as the whole incident; the inadequate review, the missed alert, the delayed escalation, the botched rollback are not separately considered. Diagnosis: the decomposition discipline has been skipped. Follow-up: list distinct actions; walk the tree once per action; the recommendations may differ.

- **Conflating the just-culture decision with the legal-employment frame.** Signal: HR escalation opens before the tree is walked, or the tree's verdict is overridden by employment-law concerns without explicit reasoning. Diagnosis: the guide is no longer being used in conjunction with HR advice and organisational policy; HR is standing in for the just-culture conversation. Follow-up: run the tree alongside the HR process, not after it; route HR engagement per the source's caveat — alongside, not instead of, the just-culture decision.

- **Closing the just-culture decision after the first walk-through.** Signal: a deeper post-mortem surfaces new facts (an upstream defect, a second contributing action, a recurrence) and the original individual response is treated as settled. Diagnosis: the re-entrant property has been ignored. Follow-up: walk the tree again on the new facts; the recommendation may change.

- **Substituting the visible individual response for the system fix.** Signal: an engineer is placed on a PIP or suspended; the deployment-pipeline / observability / runbook / training fix is named in the action items but never lands. Diagnosis: the wider-investigation parallel has been treated as ceremonial; the visible response is treated as closure. Follow-up: track the wider-action commitments separately; their delivery is the test of whether the just-culture frame was honoured.

- **Treating the just-culture decision as a perception-management artefact.** Signal: the response is calibrated to what the board, the customer, or the regulator will see, not to what the circumstances require. Diagnosis: the source's "supporting consistent, constructive and fair evaluation" [V] purpose has been inverted into reputational management. Follow-up: surface the perception-management pressure as a separate question; do not let it route the tree.

## Integration with Other References

| Reference | Relationship |
|---|---|
| [decision-making/nhs-just-culture-guide-decision-making.md](../decision-making/nhs-just-culture-guide-decision-making.md) | The lens-neutral decision-making projection of the same source. Read for the general tree-walk mechanics, the patient-safety-specific framing of each test, and the full set of operator anti-patterns. This software-business projection narrows to the engineer-after-incident decision; the decision-making projection is the general companion. |
| [stakeholder-engagement/nhs-just-culture-guide-stakeholder-engagement.md](../stakeholder-engagement/nhs-just-culture-guide-stakeholder-engagement.md) | The stakeholder-engagement projection covers the conversation contexts (manager-to-manager, manager-to-staff, organisation-to-affected-parties, external-stakeholder). Read it for the communication frame around the just-culture decision; this software-business projection covers the decision itself. |
| [decision-making/tc-25-20-army-aar-decision-making.md](../decision-making/tc-25-20-army-aar-decision-making.md) (and stakeholder-engagement projection) | The Army AAR carries the not-a-critique, discovery-by-participants facilitation discipline ("does not grade success or failure" [V]). Use TC 25-20 to facilitate the post-incident review the just-culture frame names as the wider-investigation parallel; use this distillation to decide the individual-response question that runs alongside the post-mortem. |
| [decision-making/lfuo-learning-review-guide-2024-decision-making.md](../decision-making/lfuo-learning-review-guide-2024-decision-making.md) (and stakeholder-engagement projection) | LFUO carries the learning-review discipline specifically calibrated to safety-critical operations. Use LFUO for the technique of the post-incident learning review; use this distillation for the just-culture decision about whether to direct corrective action at the individual. |
| `decision-making/openstax-organizational-behavior-decision-making.md` | OpenStax carries general organisational-behaviour decision frames (programmed vs non-programmed decisions, escalation of commitment, Rest's ethical-decision model). The just-culture frame is the operational decision aid; OpenStax is the cognitive context within which the decision is made. |
| `decision-making/openstax-business-ethics-decision-making.md` | OpenStax distinguishes the moral minimum, ethical minimum and ethical maximum (Ch 3.1, Ch 4); pairing any individual response with a wider system investigation reads as going beyond the minimum (a distillation-level reading). |
| `stakeholder-engagement/openstax-business-law-stakeholder-engagement.md` | The legal-employment frame within which the just-culture decision is taken. The source explicitly notes that the guide does not replace HR advice; the integration is that the just-culture response is taken within the legal frame OpenStax describes (Title VII, ADA, FMLA, at-will doctrine, workplace torts). |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The source cites two primary borrowed-through lineages. First, the poster's footer names "the work of Professor James Reason" [V] as a basis for the guide; no specific work or concept of Reason's is cited, and his publications are not held in this corpus. Second, the National Patient Safety Agency's Incident Decision Tree is cited as the basis from which this guide was developed; the original NPSA document is not held. The A-G recommendation labels used in citations throughout this distillation (and the deep reference) are a citation convenience added at ingestion — they are not in the original single-page poster, which does not letter its recommendations. (Source: NHS Improvement, *A Just Culture Guide*, Footer)

**Named limits of the source.** The source is a single A3 landscape poster designed as a conversation aid for NHS healthcare settings. Four caveats appear explicitly on the poster itself: it is not a replacement for a full investigation; it may need to be revisited as more information becomes available; it does not replace HR advice; and it handles only one action (or failure to act) at a time. The five tests are calibrated to patient-safety incidents involving clinical and operational staff; the software-business projection in this distillation (mapping tests to deployment pipelines, runbooks, alerting systems, on-call rotas) is a distillation-level analogy-transfer, not a claim the source itself makes. Concept 12 of this distillation (the "transferable pattern") is a distillation-level synthesis claim flagged as not in the source. (Source: Preamble, "Please note")

**Evidence-marker continuity.** The source is a single-page normative document; the deep reference classifies its claims as [V] (verbatim), [AP] (author paraphrase), [AR] (author argument: the poster's reasoning as reconstructed at ingestion) and [BT] (the footer lineage). The source's central normative claims — "action singling out an individual is rarely appropriate" and the five sequential tests — are [V] and are presented here as the authors' stated position. The recommendation that routes through Q3.3b if the protocol is "not in routine use" is a structural inference [AR] from the conjunction requirement in Q3; it is a reading of the test's logic, not an additional sentence the poster contains. The wider-investigation directive accompanying each recommendation is [V] and cited accordingly throughout this distillation.

## Trigger extensions surfaced by this source

The source surfaces two triggers the task spec's §2a seed table did not explicitly anticipate, both extending Phase 5:

| Trigger (proposed extension) | Why this source surfaces it |
|---|---|
| Operator names a recurrence of an incident with a different proximate engineer | The just-culture re-entrant property and the wider-investigation parallel together produce the diagnostic: if the same incident has recurred, the first individual response substituted for the system fix; walk the tree again on the recurrence as a system-locus signal. The source does not name "recurrence" explicitly, but the re-entrant property (Preamble, "Please note", bullet 2) and the system-locus default produce this trigger as a clear extension. |
| Operator names a pressure to "do something visible" after a customer-visible incident | The source's "protecting staff from unfair targeting" [V] purpose addresses this directly — the visible-response pressure is the canonical recruitment to unfair targeting. The trigger fires the just-culture frame as the structural check against substituting the visible individual response for the system fix. |

These extensions are logged here so the operator can decide whether to fold them back into the task spec's §2a seed table.
