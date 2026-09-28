---
type: distillation
title: "U.S. Marine Corps, MCDP 1: Warfighting"
description: "U.S. Marine Corps, MCDP 1: Warfighting, projected onto the software-business task axis; evidence markers and attribution travel in-band."
resource: https://www.marines.mil/Portals/1/Publications/MCDP%201%20Warfighting.pdf
tags: [distillation, software-business]
task: software-business
scope: open
sources:
  - id: mcdp1-warfighting
    title: "U.S. Marine Corps (Krulak, Charles C., Commandant), MCDP 1: Warfighting. Headquarters United States Marine Corps, Department of the Navy, 1997. PCN 142 000006 00. Supersedes FMFM 1 Warfighting (1989). US Government work, public domain. Scope: open."
    resource: https://www.marines.mil/Portals/1/Publications/MCDP%201%20Warfighting.pdf
generated:
  by: grounded-forge/0.4.0
  at: 2026-09-28T15:12:32+13:00
---
# U.S. Marine Corps, MCDP 1: Warfighting, Software-Business Distillation

**Source:** U.S. Marine Corps (Krulak, Charles C., Commandant), *MCDP 1: Warfighting*. Headquarters United States Marine Corps, Department of the Navy, 1997. PCN 142 000006 00. Supersedes FMFM 1 *Warfighting* (1989). US Government work, public domain. Scope: open.
**Pass G verdict:** fire-narrow on four seed triggers: Phase 2 (roadmap-capacity mismatch), Phase 3 (engineering-management culture decision) and Phase 4 (governance or decision-rights ambiguity; retrospective or learning-loop need). The call was close. MCDP 1 is doctrine for war and says nothing about software, products, markets, pricing or finance. What transfers is its account of how seniors direct and prepare subordinates: task and intent, one main effort, mission tactics as a contract, the treatment of error and dissent, the critique after training, and its warning that information technology tempts leaders to over-control. Phases 1 (strategic positioning), 5 (risk, reliability, compliance) and 6 (stakeholder communication) are out of axis for this source. Its enemy is a hostile, irreconcilable will in a violent struggle (Ch 1, "War defined"), and treating a competitor, customer or regulator as that enemy is an analogy the source does not support; route those phases through the sources the index names.
**Projection:** The engineering leader who owns roadmap commitments and decision rights under commercial pressure. Questions, diagnostic patterns, trigger scripts and the worked scenario are applications written for this task; MCDP 1 is cited only for what the deep reference shows it saying about war and the Marine Corps. No lens variant is applied.

## Software-Business Relevance

MCDP 1 gives an engineering leader a vocabulary for commanding work under uncertainty without trying to control every step of it. Four of its ideas land where engineering capacity meets commercial commitment. Every mission has a task and an intent, and the intent governs because it outlasts the task (Ch 4, "Commander's intent"). One action is named the main effort and gets priority for support, which means strict economy and accepted risk elsewhere (Ch 4, "Main effort"; Ch 2, "Speed and focus"). Mission tactics is a contract in which the senior prescribes method only as far as coordination needs and intervenes only by exception (Ch 4, "Mission tactics"). And the organisation treats errors of overboldness leniently, within limits, while dealing severely with inaction (Ch 3, "Professionalism"). [AR] This projection lands them on a roadmap that exceeds capacity, a decision-rights dispute between leadership and teams, a culture decision about how mistakes are handled, and the review that closes a piece of delivery work.

The doctrine also names information technology as a temptation to over-control. In a software company the dashboards, trackers and telemetry are the equipment, so the passage reads directly onto a tooling or monitoring purchase made in the hope of seeing and steering every piece of work (an application; the doctrine speaks of military equipment and subordinates):

> "Advanced information technology especially can tempt us to try to maintain precise, positive control over subordinates, which is incompatible with the Marine Corps philosophy of command." [V]
>
> (Source: U.S. Marine Corps, MCDP 1, Ch 3, "Equipping")

The doctrine presents itself as guidance, not procedure: *"while authoritative, doctrine is not prescriptive"* [V] (Ch 3, "Doctrine"). The questions below follow suit. They are prompts for judgment, and none of them is a rule MCDP 1 sets for software work.

## Key Concepts for Software-Business

1.  **Task and intent.** Every mission has two parts: the task says what is to be done (and sometimes when and where), the intent says why. Intent lets subordinates depart from the original plan when the unforeseen occurs, in a way consistent with the higher commander's aims. The doctrine asks for a brief, compelling statement of intent and illustrates an *in order to* form: *"Control the bridge in order to prevent the enemy from escaping across the river."* [V] [AP] For a roadmap, the task is the feature and the intent is the commercial purpose it serves. (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Commander's intent")

   > "Of the two, the intent is predominant. While a situation may change, making the task obsolete, the intent is more lasting and continues to guide our actions." [V]
   >
   > (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Commander's intent")

2.  **Shared burden of understanding.** Subordinates *"should understand the intent of the commander at least two levels up"* [V]. *"The burden of understanding falls on senior and subordinate alike"* [V]: seniors must make their purposes clear without inhibiting initiative, and a subordinate given no clear purpose *"should ask for one"* [V]. [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Commander's intent")

3.  **Mission tactics as a contract.** The senior assigns a mission without specifying how it must be done, prescribes method *"only to the degree that is essential for coordination"* [V] and intervenes only by exception. Subordinates adapt to the changing situation: *"They inform the commander of what they have done, but they do not wait for permission."* [V] Unity comes not chiefly from imposed control but from harmonious initiative and lateral coordination within guidance from above. [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Mission tactics")

   > "Mission tactics serves as a contract between senior and subordinate. The senior agrees to provide subordinates with the support necessary to help them accomplish their missions but without unnecessarily prescribing their actions. The senior is obligated to provide the guidance that allows subordinates to exercise proper judgment and initiative. The subordinate is obligated to act in conformity with the intent of the senior. The subordinate agrees to act responsibly and loyally and not to exceed the proper limits of authority." [V]
   >
   > (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Mission tactics")

4.  **Decentralised command, practised in routine work too.** To generate tempo and cope with the uncertainty, disorder and fluidity of combat, command and control must be decentralised: subordinates decide on their own initiative, from their understanding of the senior's intent, rather than passing information up the chain and waiting for the decision to come down. A competent subordinate at the point of decision will better appreciate the true situation than a senior some distance removed. The philosophy applies in preparation as well as in war: *"We cannot rightly expect our subordinates to exercise boldness and initiative in the field when they are accustomed to being oversupervised in garrison."* [V] [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Philosophy of command")

5.  **Main effort.** Of all the actions under way, one is recognised as most critical to success at that moment; the unit responsible is the main effort and receives priority for support of any kind. It gives subordinate initiative a harmonising question: *"How can I best support the main effort?"* [V] The commitment is physical and moral but not irretrievable, and when the main effort shifts, the aim is to exploit success rather than reinforce failure. [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Main effort")

6.  **Economy and prudent risk elsewhere.** Focus at the decisive place and time needs strict economy and the acceptance of risk elsewhere and at other times (Ch 2, "Speed and focus"). Concentrating toward the main effort means accepting prudent risk elsewhere, but accepting risk is not the imprudent willingness to gamble the whole likelihood of success on a single improbable event; and *"Risk is equally common to action and inaction."* [V] [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 1, "Uncertainty"; Ch 2, "Speed and focus")

7.  **Precision falls with the horizon.** The first requirement in shaping the action is to establish what we want to accomplish, why, and how. [AP] Looking forward has a limit: *"The further ahead we think, the less our actual influence can be. Therefore, the further ahead we consider, the less precision we should attempt to impose."* [V] (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Shaping the action")

8.  **Leniency for overboldness, severity for inaction.** Errors by junior leaders that stem from overboldness are a necessary part of learning and are dealt with leniently: *"there must be no 'zero defects' mentality"* [V]. Errors of inaction or timidity are dealt with severely: *"We will not accept lack of orders as justification for inaction"* [V]. The leniency has limits. Commanders still counsel subordinates on mistakes, constructive criticism remains part of learning, and nothing gives subordinates *"free license to act stupidly or recklessly"* [V]. [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 3, "Professionalism")

9.  **Honest dissent before the decision, support after it.** Until a commander has reached and stated a decision, subordinates have a duty to give honest professional opinions, even in disagreement; once it is reached, they support it as if it were their own. *"Ready compliance for the purpose of personal advancement — the behavior of 'yes-men' — will not be tolerated."* [V] Trust runs both ways, must be earned, and is a product of confidence and familiarity. [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 3, "Professionalism")

10.  **The critique.** MCDP 1's word for the review after training is *critique*. Critiques are held immediately after training, before memory fades, in open and frank dialogue in which all hands are encouraged to contribute; we learn as much from mistakes as from things done well, so mistakes must be admitted and discussed; and the focus falls less on the actions taken than on why they were taken and why they brought the results they did. [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 3, "Training")

11.  **Equipment is a means.** The doctrine names two dangers: overreliance on technology and failure to make the most of technological capabilities. *"Better equipment is not the cure for all ills"* [V]; doctrinal and tactical solutions must also be sought, and forces must not become so dependent on equipment that they cannot function when it fails. Information technology in particular tempts precise, positive control over subordinates (see the passage quoted under Software-Business Relevance). [AP] (Source: U.S. Marine Corps, MCDP 1, Ch 3, "Equipping")

## Questions to Ask During Software-Business

The questions apply MCDP 1's command concepts to engineering and roadmap work; the Source-tag names the doctrine passage each one draws on. Phases 1, 5 and 6 carry no table: this source is out of axis there (see the Pass G verdict).

### Phase 2: Product and engineering economics

| Need | Question | Source-tag |
|---|---|---|
| Name the main effort | Of everything on this quarter's roadmap, which one item is most critical to the commitments we have already made, and does it get first call on engineers, reviews and platform support? | [AP] Ch 4, "Main effort" |
| Make the economy explicit | What are we deliberately under-resourcing to fund the main effort, and who has agreed to carry that risk? | [AP] Ch 2, "Speed and focus"; Ch 1, "Uncertainty" |
| Tell prudent risk from a gamble | Does the plan accept risk on the secondary items, or does it stake the whole quarter on one improbable outcome, such as a vendor delivering on time or a migration going cleanly first try? | [AP] Ch 1, "Uncertainty" |
| Write the intent beside each commitment | For each item promised to a customer or the board, what purpose (an *in order to ...* clause) should still guide the team if the planned feature turns out to be the wrong way to get there? | [AP] Ch 4, "Commander's intent" |
| Scale precision to the horizon | Are next year's roadmap items specified at the same level of detail as this month's, even though our influence over them is smaller? | [AP] Ch 4, "Shaping the action" |
| Move support toward success | If the main effort stalls while a secondary item is moving, are we shifting capacity to exploit the progress, or adding more to the stalled work? | [AP] Ch 4, "Main effort" |

### Phase 3: Team and capability building

| Need | Question | Source-tag |
|---|---|---|
| Separate two kinds of error | When an engineer's bold call fails (a shipped experiment, a fast fix that misfired), do we counsel and learn? And do we deal firmly with waiting for orders and with windows missed through timidity? | [AP] Ch 3, "Professionalism" |
| Keep the limits on leniency | Does leniency still come with counselling and constructive criticism, and is a reckless act still named as reckless? | [AP] Ch 3, "Professionalism" |
| Hear dissent before the decision | Before the architecture or roadmap call is stated, has everyone who disagrees given an honest view? After it, are they carrying it out as their own? | [AP] Ch 3, "Professionalism" |
| Check what agreement is rewarded | Do promotions and visibility go to people who agree readily with leadership, or to people who give honest professional opinions? | [AP] Ch 3, "Professionalism" |
| Practise autonomy in routine work | Are teams oversupervised in routine work (sign-off on every merge, daily status to leadership) and then expected to act on their own during an outage or a customer escalation? | [AP] Ch 4, "Philosophy of command" |
| Protect team stability | Does this reorganisation or staffing move break up teams whose stability gives them cohesion, teamwork and implicit understanding? | [AP] Ch 3, "Personnel management" |

### Phase 4: Operations and process

| Need | Question | Source-tag |
|---|---|---|
| State the contract | For this delegated decision (release timing, an architecture choice, a customer fix), what intent and limits has leadership given, and what support has it committed in return? | [AP] Ch 4, "Mission tactics" |
| Prescribe method only for coordination | Which parts of the method are we specifying because another team or a release depends on them, and which only because we are uneasy? | [AP] Ch 4, "Mission tactics" |
| Replace permission with information | Do teams act and then tell leadership what they have done, or queue for approval on decisions within their mission? | [AP] Ch 4, "Mission tactics" |
| Close the intent gap from both ends | Can each team state the purpose two levels up? Where it cannot, has leadership stated it clearly, and has the team asked for it? | [AP] Ch 4, "Commander's intent" |
| Test a tooling purchase | Is this dashboard, tracker or monitoring tool meant to help teams act, or to let leadership keep precise control of their work? What happens to delivery when it is down? | [AP] Ch 3, "Equipping" |
| Critique while memory is fresh | Is the review of this release, launch or incident held soon after, open to everyone involved, and focused on why we acted as we did rather than only on what we did? | [AP] Ch 3, "Training" |
| Make admitting mistakes safe | Does leadership's response to mistakes admitted in the last review make it more or less likely that the next one hears about them? | [AP] Ch 3, "Training" |

## What to Look For

These are task applications of the doctrine, not findings MCDP 1 reports about software organisations.

| Signal | Diagnosis | Follow-up |
|---|---|---|
| The roadmap carries three or four "top priorities" and every team is short-staffed on all of them | No main effort has been named, so nothing receives priority for support and nothing is deliberately economised (Ch 4, "Main effort"; Ch 2, "Speed and focus") | Name one main effort, state what gets economy, and have each team answer how it best supports the main effort |
| A committed feature proves the wrong approach mid-quarter, and the team either ships it anyway or stops to wait for a new instruction | The commitment carried a task but no intent; with the task obsolete, nothing is left to guide the team (Ch 4, "Commander's intent") | Restate the commitment with its purpose, check the team can state it two levels up, and let the team propose another route to it |
| Leaders approve individual deployments, merges or ticket moves, and teams escalate routine choices | Method is being prescribed beyond what coordination needs, and seniors are intervening as a matter of course, not by exception (Ch 4, "Mission tactics") | Separate the coordination constraints (interfaces, release windows, security review) from the rest, and hand the rest back under a stated intent |
| After a failed experiment, the review asks who approved it, and over the next quarters teams stop proposing experiments while nobody is questioned for letting a window pass | The zero-defects mentality the doctrine rejects: boldness is stifled through the threat of punishment, while the errors of inaction it says to treat severely go unexamined (Ch 3, "Professionalism") | Counsel on the failed call as part of learning, and start asking about the decisions that were deferred or never made |
| Design reviews are quiet, then the decision meets passive resistance or rework after it is announced | Dissent was not drawn out before the decision, or ready agreement is what gets rewarded (Ch 3, "Professionalism") | Ask each dissenter for an honest view before the decision is stated; after it, expect support as if it were their own |
| A new engineering-metrics dashboard arrives and, within a quarter, teams wait for leadership to read it before acting | Information technology is being used for precise, positive control, which the doctrine calls incompatible with its philosophy of command (Ch 3, "Equipping") | Keep the tool for what helps teams act; drop the uses that route decisions back up the chain |
| Reviews happen weeks after a launch, a few senior voices dominate, and the write-up lists actions without reasons | The critique discipline is missing: not immediate, not open to all hands, not focused on why (Ch 3, "Training") | Hold the review within days, invite everyone who did the work, and ask why each key choice was made and why it gave the result it did |

## When to Use This Reference

Reach for this distillation when:

- A roadmap commits more work than engineering can carry and the leader needs to decide what gets priority and what gets economy (Ch 4, "Main effort"; Ch 1, "Uncertainty").
- Decision rights between leadership and delivery teams are disputed, and the question is how much method the senior should specify and when to step in (Ch 4, "Mission tactics"; "Commander's intent").
- An engineering leader is deciding how the organisation treats failed bold calls, deferred decisions and dissent (Ch 3, "Professionalism").
- A team needs a discipline for the review that follows a release, launch or incident (Ch 3, "Training").
- A tooling or monitoring investment is being justified as a way to see and steer all of the work (Ch 3, "Equipping").

Do not reach for this distillation when:

- The question is competitive strategy, market entry or a response to a competitor's move. MCDP 1's surfaces and gaps, centers of gravity, surprise and tempo are aimed at an enemy in war; route through `openstax-principles-management` and `openstax-entrepreneurship`.
- The question is pricing, build-vs-buy, finance or legal exposure: the source has nothing on them.
- The question is whether to direct corrective action at an individual after an incident: route through `nhs-just-culture-guide-software-business.md`.
- The question is the general mechanics of deciding under uncertainty with no software-business circumstance: route through `decision-making/mcdp1-warfighting-decision-making.md`.

## Worked Example

**Illustrative scenario authored for this projection:** A 60-person business-software company. Going into the quarter, the CEO has told three enterprise customers that single sign-on (SSO) will ship by quarter end, and their renewals depend on it. The same roadmap carries a usage-based pricing launch, a database migration and a partner integration, all marked top priority. The VP of Engineering finds four teams short-handed on all four items and a queue of routine decisions waiting for her sign-off.

**Naming the main effort.** She designates SSO for the three renewals as the main effort, drawing on the doctrine's definition (an application to roadmap work; the doctrine speaks of units and combat power):

> "Of all the actions going on within our command, we recognize one as the most critical to success at that moment. The unit assigned responsibility for accomplishing this key mission is designated as the main effort — the focal point upon which converges the combat power of the force. The main effort receives priority for support of any kind." [V]
>
> (Source: U.S. Marine Corps, MCDP 1, Ch 4, "Main effort")

Economy follows. The pricing launch moves to the next quarter, and the migration continues with one engineer at a slower pace. She tells the CEO this is a prudent risk on a secondary item, not a gamble of the quarter on one improbable event (Ch 1, "Uncertainty"; Ch 2, "Speed and focus"). The partner-integration team asks how it can best support the main effort and lends its identity-protocol specialist for six weeks (Ch 4, "Main effort").

**Task, intent and the contract.** She writes the commitment as a task with its intent: ship SSO for the three enterprise accounts, in order to secure their renewals this quarter (Ch 4, "Commander's intent"). She states only the limits coordination needs (the security review before release, the shared login service's interface, the date) and leaves the method to the team, committing a security reviewer as her side of the contract (Ch 4, "Mission tactics").

**When the task goes obsolete.** Mid-quarter the team finds that one customer's identity provider does not support the protocol it chose. Because the intent is on the page, the team adds a second connector for that customer instead of shipping an SSO that only two of the three can use, and tells her what it has done instead of waiting for permission (Ch 4, "Mission tactics"; "Commander's intent").

**The critique.** Two days after release, she holds a review open to everyone who worked on SSO, including support. It asks why the team chose the first protocol and why that choice produced the result it did. The engineer who chose it walks through the reasoning, and the room treats the choice as something to learn from, not a fault:

> "Of course, a subordinate's willingness to admit mistakes depends on the commander's willingness to tolerate them. Because we recognize that no two situations in war are the same, our critiques should focus not so much on the actions we took as on why we took those actions and why they brought the results they did." [V]
>
> (Source: U.S. Marine Corps, MCDP 1, Ch 3, "Training")

In the scenario, all three renewals close and the pricing launch ships a quarter late. Those are the scenario's outcomes, written to show the concepts in use; MCDP 1 reports nothing about software companies, and the scenario is not evidence that its doctrine produces them.

## Anti-patterns This Reference Helps Avoid

| Signal | Diagnosis | Follow-up |
|---|---|---|
| A main effort is announced, but every other commitment keeps its full scope and date | Focus without economy. The doctrine ties focus at the decisive place to strict economy and accepted risk elsewhere; without them the main effort is only a label (Ch 2, "Speed and focus"; Ch 4, "Main effort") | List what gets less, tell the owners of those items, and state the risk being accepted |
| Customer and board commitments name features and dates but no purpose | Tasks sold without intent. When the task goes obsolete, the commitment breaks even where its purpose could still be met (Ch 4, "Commander's intent") | Write the purpose into each commitment and renegotiate against it when the planned approach fails |
| "We don't do zero defects" is used to wave through careless or reckless releases | The doctrine's leniency is bounded: counselling and constructive criticism remain, and there is no licence to act stupidly or recklessly (Ch 3, "Professionalism") | Keep leniency for bold calls that failed; treat carelessness as carelessness |
| Teams are told "you own it" with no stated purpose, no committed support and no known limits | Half a contract. Mission tactics obliges the senior to give guidance and support as well as freedom (Ch 4, "Mission tactics") | State the intent, the coordination limits and the support leadership will provide before handing over the decision |
| A new tool is bought as the answer to slow delivery or poor visibility, and nothing else changes | Equipment treated as the cure. The doctrine holds that better equipment is not the cure for all ills and that other solutions must also be sought (Ch 3, "Equipping") | Name the change in practice the tool is meant to support, and check the team can still work when the tool is down |
| Strategy decks speak of destroying a competitor or pushing a rival into panic and paralysis | The war frame imported whole. MCDP 1's maneuver concepts assume a violent struggle between hostile, irreconcilable wills, and the doctrine insists war *"should never be romanticized"* [V] (Ch 1, "War defined"; "Violence and danger") | Keep to the command concepts this distillation projects; take competitive strategy to the sources the index names for Phase 1 |
| "Commander's intent" and "main effort" become template fields that are filled in and never used to decide anything | Doctrine turned into a checklist. MCDP 1 calls its doctrine authoritative but not prescriptive, requiring judgment in application (Ch 3, "Doctrine") | Use the terms in the decisions they are meant to shape: what gets priority, what gets economy, what a team may change without asking |

## Integration with Other References

Each relationship below is a combination made for this projection; none of these sources cites MCDP 1, and MCDP 1 cites none of them.

| Reference | Relationship for software-business work |
|---|---|
| `scrum-guide-2020-software-business.md` | The Scrum Guide makes the Sprint Goal the single objective for the Sprint: a commitment that leaves flexibility in the exact work and creates coherence and focus. Its Scrum Teams are self-managing, deciding internally who does what, when and how. [AP] (Scrum Artifacts, "Sprint Backlog", "Commitment: Sprint Goal"; Scrum Team) At sprint scale a Sprint Goal can carry the intent of the quarter's main effort, and self-management is where mission tactics leaves the method. The Sprint Retrospective, whose purpose is to plan ways to increase quality and effectiveness (Scrum Events, "Sprint Retrospective"), is a natural place to run a review with the critique's discipline. |
| `open-practice-library-software-business.md` | The Open Practice Library defines an OKR's Objective as the what and its Key Result as the how (Practice "Objectives & Key Results (OKRs)", "What is it?"). MCDP 1's intent is the why, so an OKR does not carry intent on its own; state the purpose beside the Objective. The Library's Disagree and Commit moves a team from thinking to committed execution without requiring consensus (Practice "Disagree and Commit", "What is it?"; "Why do it?"), which sits close to MCDP 1's honest opinion before the decision and full support after it. |
| `letaw-handbook-sweng-methods-software-business.md` | Letaw's RACI matrix records who is responsible, accountable, consulted and informed for a task (Ch 2.4.2). RACI settles who holds a decision; MCDP 1 speaks to how the accountable senior directs it: intent, only the method coordination needs, intervention by exception. Use the two together on a decision-rights dispute. |
| `openstax-principles-management-software-business.md` | Principles of Management contrasts control-oriented and involvement-oriented planning and controlling, and holds that as uncertainty, rapid change and turbulence rise, planning and controlling move closer to where plans are carried out (Ch 17.8). A management textbook and a war doctrine point the same way here: move decisions toward the work as uncertainty rises. |
| `nhs-just-culture-guide-software-business.md` | The NHS guide takes one action (or failure to act) at a time through five sequential tests to decide whether a staff member involved in a patient-safety incident needs individual support or intervention, starting from the prior that action singling out an individual is rarely appropriate (Preamble, "Purpose and use"; "Please note"). MCDP 1 sets a standing stance on how bold errors and inaction are treated. Use the NHS guide for the individual-after-incident decision and MCDP 1 for the culture that surrounds it. |
| `jones-evidence-based-sweng-software-business.md` | Jones holds that, at the time of writing, evidence-based software engineering has little to stand on: most existing theories are folklore unsupported by data, and public evidence for current theories of software development is almost non-existent (Ch 1, "History of software engineering research"; Read me 1st). No corpus source tests whether intent, main effort or mission tactics improve software delivery; treat the transfers in this distillation as working hypotheses to check against local results. |
| `../decision-making/mcdp1-warfighting-decision-making.md` | The decision-making projection of the same source. Read it for MCDP 1 on deciding under uncertainty in general; this projection narrows to roadmap commitments, decision rights, engineering culture and delivery reviews. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** MCDP 1 draws on works not held in this corpus: Clausewitz's *On War* (cited in 15 notes), Sun Tzu's *The Art of War*, John Boyd's lecture notes (Notes 18 of Ch 2; Notes 5 of Ch 4), William S. Lind's *Maneuver Warfare Handbook* (Notes 11 of Ch 4), Gelernter's *Mirror Worlds* (Notes 9 of Ch 4) and Joint Pub 1-02 definitions, among others. The deep reference marks the words the pamphlet borrows from them `[BT]`. This distillation quotes none of that borrowed material and rests only on MCDP 1's own text.

**Named limits of the source.** MCDP 1 is doctrine for war. Its Foreword says it contains no specific techniques or procedures, only broad guidance in concepts and values that requires judgment in application. [AP] (Foreword) It does not mention software, products, markets, pricing, finance or any business framework; every software-business application here (the questions, patterns, trigger scripts and the worked scenario) is written for this projection. In the doctrine, intent, main effort and mission tactics serve maneuver warfare against an enemy; the main effort, for example, is directed against a center of gravity through a critical enemy vulnerability (Ch 4, "Main effort"). This projection carries those concepts for the senior-subordinate relationship they describe and leaves the enemy-facing concepts (surfaces and gaps, centers of gravity and critical vulnerabilities, surprise, tempo against an opponent) unprojected. The review the doctrine describes is the critique after training (Ch 3, "Training"); using it after a software release or incident is an application.

**Evidence-marker continuity.** `[V]` marks the pamphlet's own words. The five blockquotes and the short inline quotations are copied from the deep reference's audited `[V]` passages, and each was checked word for word against the converted source, with quotation marks straightened as the deep reference does; none needed an OCR restoration. `[AP]` marks paraphrase of what the doctrine says and `[AR]` a summary of its argument. No `[BT]` material is used. Statements about other corpus sources are paraphrased from their deep references with section pointers.

**Audit trail.** Derived from `mcdp1-warfighting-deep.md` as cleaned on 2026-09-27. The converted source was consulted only to verify `[V]` quotations, not to extract new material. The Integration statements were checked against the deep references of the Scrum Guide 2020, the Open Practice Library, Letaw, OpenStax Principles of Management, the NHS Just Culture Guide and Jones. The nine projection sections are followed by the task's two trigger sections.

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| Operator describes a roadmap-capacity mismatch | Main effort with priority for support of any kind; strict economy and prudent risk elsewhere; less precision the further ahead the plan looks. [AP] Ch 4, "Main effort"; Ch 2, "Speed and focus"; Ch 1, "Uncertainty"; Ch 4, "Shaping the action" | Name the one item that gets first call on people and support this quarter, and list what gets less. Past next quarter, commit to the purpose and keep the detail loose. |
| Operator describes an engineering-management culture decision | Leniency for errors of overboldness within stated limits, severity for inaction and timidity, no zero-defects mentality; honest dissent before a decision and support after it. [AP] Ch 3, "Professionalism" | Decide which errors you will forgive: a bold call that failed gets counselling, waiting for orders gets questioned. Ask for disagreement before you decide, and expect support once you have. |
| Operator names a governance or decision-rights ambiguity | Mission tactics as a contract; method prescribed only as far as coordination needs; intervention by exception; subordinates inform rather than wait for permission; intent understood at least two levels up, and asked for when missing. [AP] Ch 4, "Mission tactics"; "Commander's intent" | Write down the intent, the few limits other teams depend on, and the support you will give. The rest is the team's call, and they tell you what they did instead of asking first. |
| Operator names a retrospective or learning-loop need | The critique: held immediately, open and frank, all hands contributing, focused on why actions were taken and why they gave their results; willingness to admit mistakes depends on the leader tolerating them. [AP] Ch 3, "Training" | Hold the review within days with everyone who did the work. Ask why each key choice was made and why it gave that result, and make admitting a mistake safe. |

## Trigger extensions surfaced by this source

| Trigger (proposed extension) | Why this source surfaces it |
|---|---|
| Operator proposes a tooling, dashboard or monitoring purchase as the way to control or speed up delivery (Phase 4) | MCDP 1 names overreliance on technology as one of two dangers in equipping, holds that better equipment is not the cure for all ills, and says information technology especially tempts precise, positive control over subordinates (Ch 3, "Equipping"). The seed table has no trigger for a tooling decision framed as control. |
| Operator names a roadmap commitment whose planned feature no longer fits while the customer's purpose still stands (Phase 2) | MCDP 1 holds that the intent is predominant because it outlasts a task the situation has made obsolete (Ch 4, "Commander's intent"). The seed table's roadmap trigger covers capacity, not a committed task gone stale. |

These extensions are logged here so the operator can decide whether to fold them into the task spec's §2a seed table.
