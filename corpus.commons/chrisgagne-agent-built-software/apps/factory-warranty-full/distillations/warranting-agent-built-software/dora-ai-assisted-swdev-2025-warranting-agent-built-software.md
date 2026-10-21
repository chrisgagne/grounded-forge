
# DORA, State of AI-assisted Software Development (2025), Warranting Agent-Built Software Distillation

**Source:** DORA (Google Cloud), *State of AI-assisted Software Development* (2025), v. 2025.2, 142 pages: a global survey of 4,867 respondents fielded 13 June to 21 July 2025, 78 interviews run from July 2024 to July 2025, and signed chapters and sidebars. Licence: CC BY-NC-SA 4.0 (p. 141). Scope: open-nc.

**Licence notice.** This distillation adapts *State of AI-assisted Software Development* (2025) by Google LLC, licensed under CC BY-NC-SA 4.0. It paraphrases and quotes the report, and changes were made. It is shared under the same licence, CC BY-NC-SA 4.0: attribution required, non-commercial use only, and any adaptation of it carries the same licence.

**Applicability gate (Pass G.0): clear yes.** (1) The source speaks to practitioner questions this axis asks: which claims are demonstrated and which only asserted (most respondents perceive AI raised their productivity, the report's own outcomes are self-reports, and it names the biases of self-reported and logs-based measures); what will degrade quietly (higher AI adoption goes with higher delivery instability); and whether success has become the evidence (the summary calls a "trust but verify" approach "a sign of mature adoption" [V], p. 5). (2) Its concepts land in seven of the eight phases, most strongly in Phase 8 (throughput and instability, read against the service's own past), Phase 6 (batch size, review as the constraint, verification as work that needs an owner) and Phase 7 (self-reports, instability booked as the price of speed, rollback offered as the reason a risk is acceptable, skills). (3) Its contrarian positions are the axis's reflexes at the level of the delivery system: instability is not an acceptable price for AI-enabled throughput (p. 41), individual effectiveness is not an end in itself (p. 58), and generating more code into a bottleneck is the wrong use of AI (p. 76). Phase 2, Triaging risk, gets no rows: the report does not sort changes by what they touch, and its theory chapter names service age and criticality only as assumed pathways to delivery outcomes, not as a gate.

**Phase mapping.** Primary: Phase 8, Releasing and operating (the five delivery measures; AI adoption with higher throughput and higher instability; no moderating effect; the service against its own past); Phase 6, Reviewing independently (larger batches hypothesised to be harder to review; local gains absorbed by downstream bottlenecks; friction moving to verification; context the agent could not read); Phase 7, Warranting the change (perception against record; instability as a price; risk compensation; default AI use and skill development). Secondary: Phase 1, Specifying the change (user-centric focus; small batches; outcomes over output); Phase 4, Building in the sandbox (frequent commits and a practised revert; AI-accessible internal data; platforms limiting what AI can do; production data deleted by AI in the foreword's account); Phase 5, Gating deterministically (one automated path for hand- and AI-written code; control systems that keep pace; guardrail friction). Supporting: Phase 3, Locking the tests (tests silently deleted by AI, in the foreword's account; faster feedback loops). Phase 2: none, as above.

**Transfer caveat.** The report is survey research. Its outcomes are respondents' reports, and its results are comparisons, not effects: between two people alike in the traits, environment and processes the model considers, the one with higher AI adoption reports, on average, more or less of an outcome (pp. 37–38; p. 48, notes 20 and 24) [AP]. The estimates come from Bayesian models resting on a stated causal graph, with 89% credible intervals (pp. 116, 123, 127) [AR]. Chat and the IDE were the most common ways respondents used AI, and 61% never use an agentic mode (p. 29) [AP], so the report did not study agents building changes nobody reads line by line, which is this axis's case. Its capabilities are team- and organisation-level conditions that amplify AI's association with outcomes (pp. 50, 80) [AR], and the authors ask readers to treat the findings "not as rigid prescriptions, but as hypotheses for your own experiments" (p. 96) [V]. Where this distillation carries a finding to a small builder's harness and a single change, it says the step is its own inference.

## Warranting Agent-Built Software Relevance

This source tells the accountable builder what AI-assisted delivery looks like at the level of the system that ships it: faster, and less stable. Respondents with higher AI adoption report, on average, higher software delivery throughput and higher delivery instability (pp. 37–38) [AP]; the throughput association turned from negative to positive since 2024 while instability still rises, which the summary reads as teams "adapting for speed" while "their underlying systems have not yet evolved to safely manage AI-accelerated development" (p. 4) [V]. DORA tested whether AI adoption softens instability's harms and "found no evidence of such a moderating effect" (p. 41) [V]. For the warranty, that means a faster harness is not evidence of a safer one, and instability is a cost the builder carries, not a price the speed pays off.

The report also names the conditions under which AI's association with good outcomes is stronger, and several are harness conditions: working in small batches, strong version control (frequent commits, practised rollback), AI-accessible internal data, a user-centric focus, a quality internal platform, and value stream management (pp. 50, 56–62, 77–78) [AR]. It offers explanations, which it hedges, for why individual speed fails to reach delivery: AI "tends to turn up at the keyboard" (p. 39) [V], friction moves from writing code to deciding and verifying it (p. 40) [AR], and local gains are absorbed by queues for testing, review and deployment (pp. 77, 81) [AR]. And it is candid about its own evidence: self-reports carry recall and social-desirability bias, logs-based metrics are not objective (p. 91) [AP] [AR], and more than 80% perceive a productivity gain while the report cites a study in which developers slowed down still believed they were faster (pp. 30, 35) [AP] [BT]. That candour is what the warranty assessor needs when it sorts a pack's evidence into demonstrated and asserted.

## Key Concepts for Warranting Agent-Built Software

1.  **AI as amplifier.** The report's central claim is that "AI’s primary role in software development is that of an amplifier" (Source: DORA, *State of AI-assisted Software Development* 2025, Executive summary, p. 3) [V]: it magnifies the strengths of well-run delivery systems and the dysfunctions of struggling ones [AR]. Without a foundation of platform, workflow and alignment, AI creates local pockets of productivity lost to downstream chaos (p. 3) [AR]. Kalliamvakou calls AI both "a mirror and a multiplier" (p. 87) [V] that shows how a system actually runs.

2.  **Throughput and instability, read against the service's own past.** DORA measures throughput (lead time for changes, deployment frequency, failed deployment recovery time) and instability (change fail rate, meaning deployments that need immediate intervention, likely a rollback or hotfix; and rework rate, unplanned deployments made because of a production incident) (Source: DORA 2025, Harvey, "Understanding your software delivery performance", p. 13) [AP]. The measures say what is happening, not why: "They tell you what is happening, but they don’t explain why." (p. 14) [V]. The most useful comparison is the same application over time (p. 20) [AR].

3.  **Higher AI adoption, higher instability, no moderating effect.** Higher AI adoption goes with higher reported throughput, code quality and individual effectiveness, and with higher instability; burnout and friction stay similar (Source: DORA 2025, DeBellis, "Exploring AI's relationship to key outcomes", pp. 38–39) [AP]. Against the argument that instability is an acceptable price for AI-enabled throughput, DORA found no moderating effect: instability still harms product performance and burnout (p. 41) [AP]. Lacking foundational capabilities "can completely neutralize any gains from AI" (p. 41) [V].

4.  **Trust but verify, and friction that moves to verification.** 30% of respondents report little or no trust in AI-generated code, "indicating a need for critical validation skills" (Source: DORA 2025, Executive summary, p. 4) [V]; the summary calls the "trust but verify" approach "a sign of mature adoption" (p. 5) [V], and the adoption chapter concludes that "absolute trust is not a prerequisite for AI-generated outputs to be useful" (p. 31) [V]. For the individual, "friction doesn’t vanish so much as move" (p. 40) [V], from manual grind to prompt iteration, result vetting and assessing code that looks remarkably like correct code [AR].

5.  **Working in small batches.** Measured by lines per commit, changes per release and time to complete a task, small batches amplify AI's association with product performance and turn its neutral relationship with friction into a decrease, while slightly reducing AI's benefit to individual effectiveness (Source: DORA 2025, Storer, DeBellis and Harvey, "DORA AI Capabilities Model", p. 58) [AP]. The authors hypothesise that AI's association with higher instability is likely, in part, because larger batches of code are harder to review (p. 57) [AR], and argue that "individual effectiveness should not necessarily be pursued as a goal in and of itself" (p. 58) [V].

6.  **Frequent commits and a practised revert.** With high certainty, frequent commits amplify AI's association with individual effectiveness, and more frequent rollback or revert amplifies its association with team performance (Source: DORA 2025, AI Capabilities Model, p. 56) [AP]. Mature version control works as a "psychological safety net" (p. 56) [V]. Rollback reliance does not directly reduce instability; the authors suspect its benefit for AI-assisted teams comes from undoing large batches fast (p. 57) [AR].

7.  **User-centric focus.** With high certainty a user-centric focus amplifies AI's association with team performance, and without it AI adoption has a negative association with team performance (Source: DORA 2025, AI Capabilities Model, p. 60) [AP]. Without that focus developers "may be moving quickly in the wrong direction" (p. 64) [V].

8.  **AI-accessible internal data.** AI tools' access to internal company information amplifies AI's association with individual effectiveness and code quality, with high certainty (Source: DORA 2025, AI Capabilities Model, p. 55) [AP]. In Kalliamvakou's illustration, a working group finds AI output missing "team conventions, architectural history, or past incidents" and recommends exposing internal documentation, decision records and historical tickets to AI securely (Kalliamvakou, "The AI mirror", pp. 85–86) [V] [AE].

9.  **The platform as one automated path, and risk compensation.** The platform applies the same automated testing and deployment to hand- and AI-written code and serves as a risk mitigator and safe space for experiments (Source: DORA 2025, Maxwell and Good, "Platform engineering", p. 72) [AR]. Quality platforms turn AI's neutral relationship with friction harmful, which the authors hypothesise comes from platforms limiting undesired capabilities, "preventing inappropriate use" (p. 62) [V] [AR]. A quality platform also goes with a small but credible rise in instability, read as "risk compensation" (p. 70) [V]: recovery is cheap, so teams accept more minor failures; and "the platform does not eliminate the local impacts of that risk" (p. 72) [V].

10.  **Local gains absorbed by downstream bottlenecks.** Without value stream management, AI's local efficiencies are "simply absorbed by downstream bottlenecks" (Source: DORA 2025, Edwards, "Value stream management", p. 77) [V]; with strong VSM, AI's association with organisational performance is dramatically amplified (p. 78) [AP]. If code review is the bottleneck, apply AI to the review process "rather than using AI to simply generate more code" (p. 76) [V]. Faster coding still meets queues for testing, review and deployment: "The system isn’t designed to carry the gains, let alone amplify them." (Kalliamvakou, p. 81) [V].

11.  **Control systems that keep pace.** In the foreword Kim reports having seen AI cause silently deleted tests, broken functionality and deleted production data, as well as massively improved outcomes (Source: DORA 2025, Kim, Foreword, p. 9) [AE]. When AI speeds up development, "our control systems—that’s us—must also speed up" (pp. 9–10) [V]; he names faster feedback loops, architectures that give independence of action, and a climate for learning (p. 9) [AR].

12.  **Default AI use and skill development.** Beane reports that default use of intelligent automation leaves novices fewer chances for hands-on work, because "Experts can self-serve, so they do." (Source: DORA 2025, Beane, "AI: A skill development threat—and opportunity", p. 88) [V]; the best organisations will "jointly optimize for productivity and skills development" (p. 88) [V]. Verification, orchestration and workflow design become more central roles that need definition, support, aligned incentives and training (Kalliamvakou, p. 86) [AR].

## Questions to Ask During Warranting Agent-Built Software

### Phase 1: Specifying the change

| Need | Question | Source-tag |
|---|---|---|
| Name the user | Who uses this change, and what will they be able to do that they can't now? Is that written in the spec, or only the feature? | p. 60; p. 64 |
| State the outcome, not the output | Is success for this change stated as a user or product outcome, or as output (lines, pull requests, stories closed, agent sessions run)? | p. 58 |
| Size the change | Can this change be split into pieces small enough that each can be reviewed, committed and reverted on its own? | pp. 57–58 |

### Phase 3: Locking the tests

| Need | Question | Source-tag |
|---|---|---|
| Watch the test files | Does the diff delete, skip or weaken any test, and would anyone notice if it did? | p. 9 |
| Keep feedback fast | Do the tests run on every agent commit, or less often than the agent produces changes? | pp. 9–10 |

### Phase 4: Building in the sandbox

| Need | Question | Source-tag |
|---|---|---|
| Limit the reach | Can the agent's environment reach production data, and what limits what it can do there? | p. 9; p. 62 |
| Keep each step revertible | Is the run committed in small steps, and has the team practised reverting to a stable state? | pp. 56–57 |
| Give the agent the history | Can the agent read the team's conventions, decision records and past incident tickets for this area, securely? | p. 55; pp. 85–86 |
| Know the stance | Is it clear which AI tools and uses are permitted on this client's work? | pp. 51–53; p. 64 |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| One path for all code | Does agent-written code reach production through the same automated tests and deployment as hand-written code? | p. 72 |
| Gate at the agent's pace | Do the gates run as often as the agent commits? | pp. 9–10 |
| Read guardrail friction | Is a guardrail being dropped because it slows heavy users down, and is that friction evidence against it? | p. 62 |

### Phase 6: Reviewing independently

| Need | Question | Source-tag |
|---|---|---|
| Find the constraint | Where does work wait between the agent's commit and release? Is review the queue that grows? | pp. 76–77; p. 81 |
| Check batch size | Is this diff larger than a reviewer can follow, and does it carry work the task never named? | p. 57 |
| Own verification | Who verifies this change, with how much time, and is that on the ledger? | p. 40; p. 86 |
| Check what the agent couldn't see | Does the change cross a team convention or a past incident that was not in the agent's context? | pp. 85–86 |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Separate perception from record | Which claims on the pack about speed or quality rest on someone's impression, the builder's or the agent's, and which on a run or a measure? | p. 30; p. 35; p. 91 |
| Name each figure's source | Does every figure on the pack say where it came from and how it was collected, and what bias that method carries? | p. 91 |
| Price the instability | Is a known risk of failure being accepted as the cost of shipping faster? | p. 41 |
| Test the rollback reason | Is "we can roll back" offered as the reason a risk is acceptable, and has the revert been practised? | pp. 56–57; pp. 70, 72 |
| Keep the knowledge human | Who besides the agent works in this area and could explain it? | p. 88 |

### Phase 8: Releasing and operating

| Need | Question | Source-tag |
|---|---|---|
| Watch both factors | Are throughput and instability for this service tracked together since the agents arrived? | p. 13; pp. 38, 41 |
| Count the failures | Do hotfixes and rollbacks count in the change fail rate, and unplanned incident deployments in the rework rate? | p. 13 |
| Compare with the service's past | Is each measure read against this service's own history rather than an industry figure? | p. 20 |
| Review on a date | When will the team next look at these measures, and what did it agree to change? | p. 22 |
| Watch unplanned work | Is unplanned, reactive work crowding out planned work? | p. 17 |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| Deployments rose since agents arrived, and so did hotfixes and rollbacks | The association the report finds between higher AI adoption and higher instability (pp. 38, 41) [AP] | Track change fail rate and rework rate beside throughput; treat a rise as a harness defect to find, not a cost of speed |
| The builder or the pack says the agent made things faster or better, with no record | A perception; more than 80% of respondents perceive a productivity gain, and the report cites a study in which slowed developers believed they were faster (pp. 30, 35) [AP] [BT] | Mark it asserted; ask for a run record or a measure, or drop the claim |
| A diff of dozens of files, including refactors the task never asked for | Larger batches, which the authors hypothesise are harder to review (p. 57) [AR] | Split the unrequested work into its own change; review each on its own |
| The review queue grows while more agent sessions start | Local gains absorbed by a downstream bottleneck (p. 77) [AR] | Find where work waits; put effort, AI included, on the review rather than on more code (p. 76) |
| Verification has no named owner or time, and review is squeezed in | Friction moved to verification without being planned for (p. 40; p. 86) [AR] | Put verification on the ledger with an owner and time |
| The change broke a team convention or repeated a past incident | Context the agent could not read (pp. 85–86) [AE] | Give the agent the decision records and incident tickets, securely; log the gap |
| The pack offers "we can roll back" as the reason a known risk is fine | Risk compensation (p. 70) [AR]; the platform does not remove the risk's local impacts (p. 72) [AR] | Refuse that reason on its own; require the revert to have been practised and the risk to be owned |
| Delivery measures compared with an industry benchmark | The wrong comparison; the useful one is the same application over time (p. 20) [AR] | Compare with the service's own history |
| Only the agent works in an area, and nobody else could explain it | Default AI use blocking skill development (p. 88) [AR] | Name a human who holds this area; pair them on the next change there |

## When to Use This Reference

- Reach for it when the question is what agents are doing to delivery as a whole: throughput and instability for a service over time, and where the gains go.
- Reach for it when a pack, a builder or an agent offers its own sense of speed or quality as evidence, and the assessor needs the report's account of self-report and logs bias.
- Reach for it when a change is large, a review queue is growing, or verification has no owner: it ties batch size, review and downstream bottlenecks to AI's association with instability.
- Reach for it when rollback, or a well-built pipeline, is offered as the reason a risk is acceptable.
- Reach for it when an area of the code has come to be worked only by agents.
- Reach for another source for a measured, controlled result rather than respondents' reports (`becker-metr-ai-developer-productivity-2025`, `he-cursor-velocity-complexity-2025`); for what a change touches and which gates that makes mandatory (the standards and threat lists); for how to lock and judge tests (`egashira-testsuitebench-2026`, `jimenez-swe-bench`); and for how to build the sandbox and human gate (`openssf-finding-fixing-vulnerabilities-ai`). This source sorts no change by risk and studies no single change.

## Worked Example

*Scenario (operator-authored).* A three-person studio maintains a booking app for a client. Two months ago it moved to running several coding agents in parallel. Deployments have roughly doubled; so have hotfixes, and the review queue is longer every week. Today's change touches 38 files: the client's new cancellation flow, plus a refactor of the notification module the agent did "while it was in there". The client wants it live tonight. The builder wants to sign: "the last few weeks have been our fastest ever, and if anything breaks we can roll back." The warranty assessor reads the ledger and the delivery history, not the diff.

*Applying the source.* The assessor starts with the history. Throughput is up and instability is up, the pattern the report finds between higher AI adoption and delivery outcomes (pp. 38, 41) [AP], and the report rejects instability as an acceptable price: DORA "found no evidence of such a moderating effect" (p. 41) [V]. The assessor does not need a dashboard to see it. As Harvey's retrospective example puts it:

> "Precision for these metrics isn’t always required, and teams will generally know how they are changing over time." (Source: DORA 2025, Harvey, p. 22) [V]

Next, the builder's sense that these were the fastest weeks. That is an impression, and the report is candid that its own productivity findings are perceptions, more than 80% of respondents perceiving a gain (p. 30) [AP], while it cites a study in which slowed developers still believed they were faster (p. 35) [BT]. The assessor marks the speed claim asserted and leaves it off the pack.

Then the change itself. Thirty-eight files with an unrequested refactor is a large batch, and the authors hypothesise that larger batches of code are harder to review, which may be part of why AI goes with instability (p. 57) [AR]. The assessor sends the notification refactor back as its own change.

Then the rollback reason. Frequent rollback goes with better team performance for AI-assisted teams, but it does not directly reduce instability (pp. 56–57) [AR]; and the platform chapter reads the instability that comes with cheap recovery as "risk compensation" (p. 70) [V], warning that "the platform does not eliminate the local impacts of that risk" (p. 72) [V]. A booking cancelled wrongly tonight is a customer's problem whether or not the code can be reverted tomorrow. The assessor asks whether the revert has been practised on this service, and who owns the risk until it is.

Last, the queue. The report's account of where AI's gains go is direct:

> "The system isn’t designed to carry the gains, let alone amplify them." (Source: DORA 2025, Kalliamvakou, p. 81) [V]

The studio has been adding agent sessions into a review bottleneck, the use of AI the value stream chapter warns against (p. 76) [AR]. The assessor returns the pack with three asks: the cancellation flow alone, with its run record; a named reviewer with time on the ledger; and a date, a month out, to review change fail rate and rework rate against the months before the agents arrived (p. 22) [AE]. Holding new agent sessions until the queue shrinks is this distillation's inference, not the report's.

## Anti-patterns This Reference Helps Avoid

- **Instability booked as the price of speed.** *Signal:* rising hotfixes explained as the cost of shipping faster. *Why it fails:* the report found no evidence that AI adoption softens instability's harms to product performance and burnout (p. 41) [AP]. *Instead:* treat rising instability as a defect in the harness to find and fix.
- **Rollback as the warrant.** *Signal:* "we can roll back" offered as the reason a known risk is acceptable. *Why it fails:* cheap recovery can lead teams to accept more minor failures, and the platform does not remove the local impacts of that risk (pp. 70, 72) [AR]. *Instead:* require a practised revert and an owner for the risk, and judge the risk on its own.
- **More code into the bottleneck.** *Signal:* more agent sessions while the review queue grows. *Why it fails:* local gains are absorbed by downstream bottlenecks (p. 77) [AR], and the value stream chapter directs AI at the bottleneck rather than at generating more code (p. 76) [AR]. *Instead:* find where work waits and work there.
- **Output as the goal.** *Signal:* a change or a harness judged by lines, pull requests or sessions run. *Why it fails:* individual effectiveness is a means to team, product and organisational outcomes, not an end (p. 58) [AR]. *Instead:* state the user or product outcome the change serves.
- **Speed without a user.** *Signal:* a spec with a feature and no named user or outcome. *Why it fails:* without a user-centric focus, AI adoption goes with worse team performance (p. 60) [AP]. *Instead:* name who the change is for and what they will do with it.
- **Felt speed as evidence.** *Signal:* the pack's case rests on how fast or good the work seemed. *Why it fails:* the report's own productivity and quality findings are perceptions, and self-reports carry recall and social-desirability bias (pp. 30, 91) [AP]. *Instead:* require a record; give every figure its source.
- **Logs taken as objective.** *Signal:* a dashboard figure treated as beyond question because a tool produced it. *Why it fails:* the metrics chapter calls it "a common misconception that logs-based metrics are objective" (p. 91) [V]; instrumentation varies and errors creep in. *Instead:* note how each figure was collected.
- **An area only the agent knows.** *Signal:* nobody but the agent has worked in a part of the code for months. *Why it fails:* default AI use is reported to block skill development (p. 88) [AR]. *Instead:* keep a named human working in each area, and count that as part of the warranty (this distillation's inference).

## Integration with Other References

| Reference | Relationship |
|---|---|
| `becker-metr-ai-developer-productivity-2025` | DORA cites this study [BT] (pp. 35, 48): developers slowed by 19% believed they were 20% more efficient. Becker et al. measured that gap in a randomized trial (Abstract; §3.1) [AE]. DORA shows how widespread the perception of gain is among respondents (p. 30); Becker et al. show how far such a perception can run from the clock. Use them together to treat any self-reported speed on a pack as asserted |
| `he-cursor-velocity-complexity-2025` | He et al. measure project-level velocity rising sharply in the first months after Cursor adoption and then fading, while static-analysis warnings (+30.3%) and complexity (+41.6%) rise and stay (§4.1.1–§4.1.2) [AE]. DORA finds higher AI adoption associated with higher throughput and higher instability across respondents (pp. 38, 41). Both call for the system to adapt: He et al. for quality assurance that scales with AI-era velocity (§1, p. 2) [AR], DORA for "reimagining the system of work it inhabits" (p. 43) [V]. DORA supplies the delivery measures; He et al. the code-quality ones |
| `microsoft-code-with-engineering-playbook` | The playbook holds that "More code there is to review, the higher chances there are letting a bug sneak through." and asks teams to measure time to merge and automate the mechanical checks ("Code Reviews Shouldn't Include too Many Lines of Code"; "Measuring Code Review Process") [V] [AP]. That is the review-level mechanism behind DORA's hypothesis that larger batches are harder to review (p. 57) and its retrospective example of slowing reviews answered with smaller changes (p. 22) |
| `openssf-finding-fixing-vulnerabilities-ai` | DORA's platform chapter applies the same automated testing and deployment to hand- and AI-written code (p. 72), and Kim reports AI deleting production data (p. 9). OpenSSF gives the controls for that reach: a sandbox, a human gate outside the AI, a kill switch, deterministic checks plus AI review on every proposed change, and the warning that agreement among AI reviewers is not proof (§ "Establish a human gate and kill switch"; § "Tips for validation"; § "Repeated application") [AP]. DORA's suggestion of AI first-pass reviews and AI-powered pipeline checks (p. 82) should be read with OpenSSF's limits on what AI review can establish |
| `uk-duck-book-qa-of-code` | The Duck Book's generative AI chapter sets a golden rule that you review LLM code yourself before using or submitting it, and lists risks to on-the-job learning among its cited concerns [BT] (book/generative_ai.md) [AP]. DORA's trust-but-verify stance (p. 5) and Beane's sidebar on skill development (p. 88) carry the same two points from survey and field research: verify what AI writes, and keep people learning the code it writes |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The foreword's company cases come from a book the foreword cites, and its control-system argument rests on an outside engineering criterion; the report also cites outside industry surveys, a study of experienced open-source developers, trust-in-automation and burnout literature, systems-thinking authors, measurement frameworks and statistical texts [BT]. None is held in this corpus except the study of experienced open-source developers, held here as `becker-metr-ai-developer-productivity-2025`. This distillation names none of the others.

**Named limits of the source.** The outcomes are self-reported, and the results are comparisons from a model whose adjustment set blocks biasing pathways only if its causal graph is correct (p. 123) [AP]; the people compared are alike in the aspects the authors considered, not identical (p. 48, note 24) [AP]. The report calls its findings complex and "at times may even appear contradictory" (p. 96) [V]. One such point matters here: on AI, p. 41 rejects instability as an acceptable trade-off for throughput, while the platform chapter calls the instability that comes with a high-quality platform "a manageable tradeoff for higher performance overall" (p. 66) [V]; this distillation follows p. 41 for changes and records the platform reading as risk compensation. The AI Capabilities Model is a first iteration to be validated (pp. 50, 95) [AP], and early standardisation of AI practice "would be premature" (p. 95) [V]. Most respondents did not use agent mode (p. 29). The report does not sort changes by risk and does not study single changes, test design or security controls.

**Evidence-marker continuity.** The report's survey results carry `[AP]`, the authors' readings and hypotheses (batch size and review, risk compensation, platforms preventing inappropriate use, mechanisms) carry `[AR]`, and Kim's observations and Kalliamvakou's working-group illustration carry `[AE]`, as in the deep reference. Verbatim passages are copied from the deep reference's audited `[V]` quotations (pp. 3, 4, 5, 9–10, 14, 22, 31, 39, 40, 41, 55, 56, 58, 62, 64, 66, 70, 72, 76, 77, 81, 85–86, 87, 88, 91, 95, 96); none was re-extracted from the tape. The cited study of experienced developers stays `[BT]`. Cross-references in the integration table cite the sibling deep references' own sections and markers.

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| Nobody can say who will use the change or what they will do with it (Phase 1) | Without a user-centric focus, AI adoption goes with worse team performance (p. 60) [AP]; developers may be moving quickly in the wrong direction (p. 64) [AR] | Name the user and what they'll do before the agent starts. Speed in the wrong direction is still the wrong direction. |
| The spec is long and the change is large (Phase 1) | Small batches amplify AI's association with product performance; larger batches are hypothesised to be harder to review (pp. 57–58) [AP] [AR] | Split it into changes a reviewer can follow and revert one at a time. |
| The agent proposes changing a test so the build goes green (Phase 3) | Kim reports seeing AI silently delete tests (p. 9) [AE] | This happens; the foreword's author has seen it. Block the edit and send the failing test back to a human. Locking the tests is a harness rule. |
| The suite takes minutes, so it runs rarely (Phase 3) | When AI speeds up development, control systems must speed up too, starting with faster feedback loops (pp. 9–10) [AR] | If the agent commits faster than the tests run, the tests are behind. Make them fast enough to run on every change. |
| The agent's environment can reach production credentials or data (Phase 4) | Kim reports seeing AI delete production data (p. 9) [AE]; the authors hypothesise platforms add value by limiting undesired capabilities (p. 62) [AR] | AI has deleted production data. Take away the reach before the run, not after. |
| The agent runs for an hour unattended and reports success (Phase 4) | The summary calls the "trust but verify" approach "a sign of mature adoption" (p. 5) [V]; friction moves to vetting results and assessing code that looks remarkably like correct code (p. 40) [AR] | Useful isn't the same as trusted. Check the run record before you accept the report. |
| The secrets scan or dependency audit is "noisy" so it was turned off (Phase 5) | Quality platforms raise friction for AI users, which the authors hypothesise comes from preventing inappropriate use and need not be bad for the organisation (p. 62) [AR] | Friction from a guardrail isn't evidence against it. Tune the scan; don't drop it. |
| The builder approves because reading the diff is too slow (Phase 6) | Verification is where friction moves (p. 40) [AR]; verification becomes a central role that needs definition and time (p. 86) [AR]; smaller batches are easier to review (p. 57) [AR] | If the diff is too slow to read, it's too big or verification has no time. Split it, or give verification an owner and time. |
| The change "looks fine" but touches something with a history of incidents (Phase 6) | AI output can miss team conventions, architectural history and past incidents; expose decision records and historical tickets to AI securely (pp. 85–86) [AE] | The agent didn't see that history unless someone gave it. Pull the incident tickets into the review, and into the agent's context next time. |
| The client wants it today and the review is still open (Phase 7) | No evidence that AI adoption softens instability's harms to product performance and burnout (p. 41) [AP] | Shipping it open trades stability for speed, and the report found no sign that AI softens what instability costs. Say that trade aloud before signing. |
| Nobody could explain how this part works if the agent were unavailable (Phase 7) | Default AI use leaves fewer chances for people to learn the work; the best jointly optimise productivity and skills (p. 88) [AR] | If only the agent knows this area, nobody does. Name a person to learn it before you sign. |
| The builder signs because the last ten went fine (Phase 7) | More than 80% perceive a productivity gain (p. 30) [AP]; the report cites a study in which slowed developers believed they were faster (p. 35) [BT]; self-reports carry recall bias (p. 91) [AP] | A streak is a feeling about the past. Sign on this change's record. |
| Throughput rose with AI assistance and so did instability (Phase 8) | Higher AI adoption goes with higher throughput and higher instability, with no moderating effect on instability's harms (pp. 38, 41) [AP] | Speed came with breakage, and the breakage still costs. Track change fail rate and rework rate beside throughput, and fix the harness. |

## Trigger extensions surfaced by this source

| Phase | Trigger (what the practitioner notices) | Response (grounded in this source) |
|---|---|---|
| 1 | The story's success measure is output (lines, pull requests, stories closed, agent sessions run), with no user or product outcome named | Rewrite it as an outcome: individual effectiveness is a means to team, product and organisational performance, not a goal in itself (p. 58) [AR] |
| 4 | Nobody can say which AI tools and uses are permitted on this client's work | Settle and state the stance: unclear stances leave some acting too conservatively and others too permissively (p. 53) [AR], and "Ambiguity around AI stifles adoption and creates risk." (p. 64) [V] |
| 4 | A long agent run lands as one large commit with no revert point between steps | Commit each step so it can be reverted: frequent commits and practised rollback amplify AI's association with effectiveness and team performance (p. 56) [AP] |
| 4 | The diff carries work the task never named: refactors, extra files, "while I was in there" | Split it into its own change for a keep-or-drop decision: larger batches are hypothesised to be harder to review (p. 57) [AR] |
| 5 | The gates run less often than the agent commits | Run the gates per commit: control systems must speed up when development does (pp. 9–10) [AR] |
| 5 | Agent-written changes reach production by another route than hand-written ones (a manual deploy, a side branch, a skipped stage) | Route them through the same automated tests and deployment (p. 72) [AR] |
| 6 | Changes waiting for review grow while more agent sessions start | Find where work waits and work on that, not on more code: local gains are absorbed by downstream bottlenecks (pp. 76–77) [AR] |
| 6 | Verification has no owner or time on the ledger | Give it both: friction moves to verifying, and verification is a central role needing definition, support and training (pp. 40, 86) [AR] |
| 6 | The change breaks a team convention or repeats a past incident that the agent had no way to read | Give the agent the decision records and incident tickets, securely (pp. 85–86) [AE]; AI-accessible internal data amplifies AI's association with code quality (p. 55) [AP] |
| 7 | The pack's evidence for speed or quality is an impression, the builder's or the agent's, with no record behind it | Mark it asserted and send it back for a record: the report cites a study in which slowed developers believed they were faster (p. 35) [BT] |
| 7 | A figure on the pack has no source or note of how it was collected | Name its source and likely bias: self-reports carry recall and social-desirability bias, and logs-based metrics are not objective (p. 91) [AP] [AR] |
| 7 | The pack gives "we can roll back" as the reason a known risk is acceptable | Refuse that reason on its own: cheap recovery can lead teams to accept more minor failures, and the platform does not remove the risk's local impacts (pp. 70, 72) [AR] |
| 7 | Instability is booked as the price of speed | Refuse the trade: no evidence that AI adoption softens instability's harms (p. 41) [AP] |
| 8 | A delivery measure is compared with an industry figure or another team's instead of this service's own history | Compare the service with its own past (p. 20) [AR] |
| 8 | Hotfixes or rollbacks are not counted in the service's change fail rate | Count them: change fail rate is deployments needing immediate intervention, likely a rollback or hotfix (p. 13) [AP] |
| 8 | Nobody has looked at the service's delivery measures since it went live | Set a date to review them, as the retrospective example does a month out (p. 22) [AE] |
| 8 | Unplanned, reactive work is crowding out planned work | Read it as instability: the legacy-bottleneck profile pairs frequent instability with a high volume of unplanned, reactive work (p. 17) [AE]; rework rate counts unplanned deployments after incidents (p. 13) [AP] |
