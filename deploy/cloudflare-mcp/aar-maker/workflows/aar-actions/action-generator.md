# Action Generator Prompt

Use this prompt when helping users create action items from an AAR.

---

## Connection availability

Before using tracker or chat tools, verify that the relevant connection is available. If it is missing or fails, stop that operation, report the missing data, and offer paste mode: the practitioner pastes ticket details, chat excerpts or action-status data. Do not infer data or claim tickets were created. For action creation without a tracker, return the ticket drafts as markdown for manual entry.

## Library sources

WIP and batch size: open-kanban. Systems archetypes, feedback loops and unintended consequences: ssdl-systems-thinking-foundations (archetypes from Kim, borrowed-through). Hand-offs and local optimisation: org-topologies-primer-2025. Procedures, checklists and controls: doe-hpi-handbook-vol1. Forward accountability: lfuo-learning-review-guide-2024 (forward-looking accountability). Finding who already succeeds: liberating-structures-handbook (Discovery & Action Dialogues).

## Prompt

You are helping generate action items from a completed contributing factor analysis. Actions should address both immediate mitigation and long-term systemic improvement.

**Before generating actions, ensure:**
1. THE constraint has been identified (Goldratt)
2. Actions will be evaluated against the constraint
3. Checklist opportunities will be identified (doe-hpi-handbook-vol1)
4. Hand-offs have been assessed (org-topologies-primer-2025) - is this a flow problem?
5. Systems archetypes have been checked (ssdl-systems-thinking-foundations) - will this fix create new problems?
6. Forward accountability has been assigned (lfuo-learning-review-guide-2024) - who will own fixing this?

---

### Constraint Analysis (Goldratt)

**Before generating any actions, identify THE constraint:**

Every system has ONE constraint that limits throughput. Improving anything else is waste.

**Step 1: What is THE constraint?**
Ask: "If we could magically improve one thing, what would have the biggest impact?"

Name its type in plain words: a resource, a policy, or a paradigm (a belief about what's possible).

**Step 2: Evaluate each proposed action** against the constraint (the exploit, subordinate and elevate steps of Goldratt's Five Focusing Steps):
| Action | Constraint Relation | Priority |
|--------|---------------------|----------|
| [Action] | Gets more from the constraint / Adds capacity at it / Makes other work serve it / Unrelated | High/Med/Low |

**Key Insight:** Actions unrelated to the constraint should be deprioritized or deferred. They may be "good ideas" but won't improve system performance until the constraint is addressed.

---

### Two Categories of Actions

**Short-Term Actions (1-2 weeks)**
- Within current team decision rights and capacity
- Target: tooling, guardrails, runbooks, tactical fixes
- Can be executed without leadership approval
- Should mitigate or contain the failure mode quickly

**Long-Term Actions (Systemic)**
- Require changes to one of the five points: what we optimise for, who owns what, how work moves, what gets measured and rewarded, or who we hire, grow and staff. These five points follow Jay Galbraith's Star Model (strategy, structure, processes, rewards, people), put in plain words.
- Typically need cross-team coordination or leadership authority
- Use the Leadership Request format
- Address contributing factors, not just symptoms

### Short-Term Action Criteria

Good short-term actions are:
- **Specific**: Clear description of what to do
- **Bounded**: Definite scope and completion criteria
- **Actionable**: Can start immediately
- **High-leverage**: Address the most likely failure modes

Examples:
- "Add validation for X input field in API endpoint Y"
- "Create runbook for scenario Z"
- "Add monitoring alert when metric exceeds threshold"
- "Update deployment checklist to include step Q"

### Long-Term Action Criteria

Good long-term actions:
- **Map to one of the five points**: Clearly address one of them (for Complicated/Complex incidents, in Dave Snowden's Cynefin terms). For Clear-domain incidents, long-term actions may be technical (architecture, tooling) rather than organizational.
- **Include hypothesis**: State why this change will help
- **Offer options**: Present 1-3 approaches with trade-offs
- **Have clear ask**: What decision or support is needed from leadership

### Linking to Contributing Factors

Every action should trace back to the CFA:

| Contributing Factor | Action Type |
|-------------------|-------------|
| Missing validation | Short-term: Add validation |
| No quality gate | Short-term: Add gate; Long-term: Review gate coverage |
| Ownership unclear | Long-term: Clarify who owns what |
| Schedule pressure | Long-term: Review what gets measured and rewarded |
| Single expert | Short-term: Document; Long-term: Cross-training plan |

### Avoiding Bad Actions

**Red flags:**
- "Be more careful" → Too vague, person-dependent
- "Add training" without system change → Won't stick
- "We'll remember next time" → Not a forcing function
- "Fix the bug" as the ONLY action → May address symptom without cause. But for Clear-domain incidents, fixing the bug may BE the action — pair with a brief "why did this bug exist?" check.
- "Add monitoring" without response plan → Just noise

**Better:**
- "Add automated check for X" → Forcing function
- "Add training AND update template/checklist" → Embeds in process
- "Create runbook AND alert" → Makes response automatic
- "Add monitoring AND create response checklist" → Complete solution

---

### Cynefin Coherence Check (Snowden)

Actions should match the domain classification from the AAR. Check in both directions:

| Classification | Action Type | Check |
|---------------|------------|-------|
| **Complex** domain, but action is a deterministic check or fixed rule | Is this a deliberate safe-to-fail *probe* (good), or have you inadvertently simplified the domain? Complex problems need sensing mechanisms, not just checks. Name it: "This is our first probe — if the next failure manifests differently, we'll need to sense for semantic inconsistencies, not just check for known mismatches." |
| **Complicated** domain, but action is an exploratory sensing probe | Have you misclassified the domain? Complicated problems have knowable solutions — you shouldn't need to probe. |

**Common failure mode:** Classifying a detection gap as Complex (correct — you don't know what the next failure looks like), then proposing a monitoring solution that treats it as Complicated (a known check on a known interval for a known mismatch). That's fine as a first probe, but say so — and name what you'd do if the probe fails to catch the *next* variant.

---

### Policy-Change Actions

If an action proposes a new decision rule, escalation policy, or classification criteria (e.g., "any parcel with an unreadable label is held at the depot"), it needs more than one sentence:

- **Define key terms:** What counts as "unreadable"? One smudged digit, or no label at all?
- **Edge cases:** What happens at the boundary? Who adjudicates ambiguity?
- **Gaming risks:** Could this rule be gamed or over-triggered? What prevents it from becoming a back-door escalation path?
- **Sunset/review:** When will this rule be re-evaluated?

A one-sentence rule that bypasses existing process needs treatment proportional to its blast radius.

---

### Converting Actions to Procedures and Checklists

When an action involves a repeatable process, write it as a procedure or checklist people can follow and verify. Check it against the DOE handbook's common procedure flaws and its guidance on controls (doe-hpi-handbook-vol1):

- **One action per step.** A step that does two things is a common flaw.
- **Clear expectations.** Each step says exactly what to do and what done looks like.
- **Mark the critical step.** Name the step where an error would cause irreversible harm, in the procedure and in the briefing.
- **Prefer an engineered control where prevention is imperative.** A checklist is an administrative control. If the error must not happen, look for a physical or design control (an interlock, a forcing function, a separation) instead of another step.

**Checklist Template:**
```markdown
## [Checklist Name]

**Use when:** [Trigger condition]
**Owner:** [Role responsible for maintenance]

### Pre-Conditions
- [ ] [Condition that must be true before starting]

### Steps
1. [ ] [Action with exact wording]
2. [ ] [Action with exact wording]
3. [ ] **CRITICAL STEP**: [The step where an error would cause irreversible harm]
4. [ ] [Action]
5. [ ] **VERIFY**: [Expected outcome check]

### If Something Goes Wrong
- Escalation: [Contact path]
- Rollback: [Steps or reference]
```

---

### Avoiding Unintended Consequences (ssdl-systems-thinking-foundations)

Check that proposed actions don't create new problems. Ask which loops each action will strengthen or weaken, and which will push back:

| Proposed Action | Possible Unintended Consequence | Mitigation |
|-----------------|--------------------------------|------------|
| Add process step | Slower → pressure to bypass → worse outcomes | Keep it minimal, automate |
| Add monitoring | Alert fatigue → ignoring alerts | Tune thresholds, ensure response plan |
| Add review gate | Bottleneck at reviewers → skip for "urgent" work | Define bypass criteria upfront |
| Add automation | False confidence → less human oversight | Keep humans in the loop for critical paths |
| Add documentation | Goes stale → misleading info | Assign owner, review cadence |

**Key question:** "How might this action create the conditions for future failure?"

---

### Hand-off Check (org-topologies-primer-2025)

Before adding actions that make individuals faster, check whether the delay lives in the hand-offs between teams. The Org Topologies primer (Krivitsky, Larman and Flemm) treats a cross-silo hand-off a team couldn't avoid as structural, not behavioural, and warns that optimising each element in isolation can make the whole system's flow worse.

**Is this a flow problem or a speed problem?**

| If... | Then... |
|-------|---------|
| Individuals are fast but end-to-end is slow | Focus on reducing hand-offs, broadening team scope |
| Work waits more than it's worked on | Address queue management, not individual speed |
| Multiple specialists must touch every item | Consider a team that owns the whole capability end to end, so the hand-off becomes work inside one team |
| Adding people doesn't help | The constraint is flow, not capacity |

**Actions to consider if hand-offs drive the delay:**
- Broaden team scope to reduce hand-offs
- Collocate dependent specialists
- Establish outcome-based mandates vs. task-based work
- Reduce WIP to improve flow
- Fix the hand-offs before speeding up the individuals
- Look at how the elements fit together: a single new role, policy or committee on its own carries the primer's local-optimisation warning

---

### Systems Archetype Check (ssdl-systems-thinking-foundations; Senge and Kim borrowed-through)

**Fixes that Fail:**
Before implementing, ask: "What might this fix break?"
- Will the fix relieve the problem now but make it worse over time?
- What delayed side effects could feed back into the original problem?
- What happens when this fix stops working?

**Shifting the Burden:**
Ask: "Are we treating the symptom or the cause?"
- Are we creating a dependency on the fix that masks the real problem?
- Is there a "fundamental solution" we're avoiding because it's harder?
- Will this symptomatic solution weaken our ability to implement the fundamental solution?
- Are we building capability or dependency?

**If archetype risk detected:**
- Document the risk explicitly in the action item
- Add a follow-up action to address the fundamental solution
- Set a time limit on symptomatic solutions

---

### Forward Accountability (lfuo-learning-review-guide-2024)

Every action needs an owner, but frame it as forward accountability:

**Not:** "Who caused this and should be held responsible?"
**But:** "Who will take ownership of ensuring this doesn't happen again?"

| Action Type | Forward Accountability Question |
|-------------|--------------------------------|
| Process change | "Who will own implementing and maintaining this?" |
| Training need | "Who will ensure the capability gap is closed?" |
| Tool improvement | "Who will build, deploy, and maintain this?" |
| Structural change | "Who will sponsor and champion this change?" |

**Include in action items:**
- **Owner**: Name/role responsible for completion
- **Accountability**: What success looks like
- **Support needed**: What help they'll need from others

---

### Practical-to-Adopt Test

**Red flags that predict action item failure:**
- "Engineers should remember to..." → Relies on memory. Automate or mandate instead.
- "Improve communication between..." → Too vague to act on. Name who tells whom, when, through which channel, with what content.
- "Be more careful when..." → Not an action item.
- "Add training on..." → Training alone won't hold unless the work itself changes too. For a slip on a familiar task, the DOE handbook calls retraining "a waste of time" (doe-hpi-handbook-vol1).

**Who already does this well?** Before inventing a new fix, ask who here has already overcome the same barriers, and what lets them. Discovery & Action Dialogues put it as "Who/Where have you seen overcome those barriers?" (liberating-structures-handbook). Learn from what already works locally before designing from scratch.

---

### Prioritizing Actions by Urgency

Not all actions are equal. Prioritize by relative urgency.

**Why H/M/L instead of dollar figures:** An individual AAR doesn't generate enough data for credible base rates. Dollar-figure quantification is a *portfolio* tool — useful when sequencing 30 stories in a backlog, misleading when you have one incident and would be fabricating probability estimates from a sample of one. Use the relative ordering.

**Urgency Factors:**
| Factor | Question | High Urgency Signals |
|--------|----------|----------------------|
| Recurrence risk | How likely is this to happen again soon? | Known trigger exists, no mitigation |
| Impact severity | How bad is it when it happens? | Customer-facing, revenue impact, data loss |
| Detection time | How long until we notice next occurrence? | No monitoring, silent failures |
| Recovery time | How long to recover next time? | Manual steps, no runbook, expertise required |

**Prioritization Categories:**

| Category | Urgency / Duration | Action |
|----------|-------------------|--------|
| **Do Now** | High urgency, Short duration | Implement immediately |
| **Schedule** | High urgency, Long duration | Start soon, track progress |
| **Batch** | Low urgency, Short duration | Group with similar work |
| **Deprioritize** | Low urgency, Long duration | Defer or reconsider |

### Batch Size and WIP for Actions (open-kanban)

**Reduce the batch size:** commit to few actions and finish them. A long action list is a large batch (open-kanban, Reduce the Batch Size).

- Break large actions into smaller, independently deployable pieces
- Each piece should be testable and reversible
- Avoid "big bang" implementations that can't be incrementally validated

**WIP Limits:** Limiting the actions in progress follows from reducing the batch size.

- Having 10 actions "in progress" means none complete quickly
- Better: one or two actions in progress, completed before starting new ones

### Design for Fast Feedback

**Actions should be designed for fast feedback:**

| Action Type | Fast Feedback Design |
|-------------|---------------------|
| Process change | Trial with one team first, measure before expanding |
| New tooling | MVP implementation, iterate based on usage |
| Documentation | Publish draft, refine based on questions |
| Monitoring | Alert on first occurrence, tune thresholds with data |

**Key question:** "How will we know if this action is working, and how soon will we know?"

---

### Tracker Ticket Format

For each action, provide:

```markdown
**[Short-term/Long-term] Action: [Title]**
- **Description**: [What needs to happen]
- **Relates to**: Bug #[ID]
- **Owner**: [one person]
- **Checked by**: [who confirms it worked]
- **Target date**: [Date or Quarter]
- **Success criteria**: [How we know it's done]
```

### Leadership Request Format

For long-term systemic actions, use the full Leadership Request template:

```markdown
## Leadership Request: [Brief Title]

**Related Bug**: [ID]
**Context/Impact**: [What happened, why it matters]
**Contributing Factors + Five Points**: [Which factors, and which of the five points they sit in]
**Hypothesis**: [System condition producing the outcome]
**Options**: [1-3 approaches with trade-offs]
**Ask**: [Decision/support needed, by when]
**Success Criteria**: [Measurable outcomes]
```

### Completeness Check

Before finalizing actions:
- [ ] THE constraint has been identified
- [ ] At least one action directly addresses the constraint
- [ ] Actions unrelated to constraint are deprioritized or justified
- [ ] At least one short-term action addresses immediate risk
- [ ] At least one long-term action addresses systemic contributing factors
- [ ] Long-term actions include Leadership Request if one of the five points is outside the team's control
- [ ] All actions link back to original bug
- [ ] No "be more careful" or "add training" without system change
- [ ] Repeatable processes have associated checklists, checked for the common procedure flaws (doe-hpi-handbook-vol1)
- [ ] Actions evaluated for unintended consequences (ssdl-systems-thinking-foundations)
- [ ] Actions prioritized by urgency / duration
- [ ] Large actions broken into smaller batches for fast feedback
- [ ] Feedback mechanism defined: "How will we know this is working?"
- [ ] Hand-offs checked: Are we fixing flow or just speed? (org-topologies-primer-2025)
- [ ] Systems archetypes checked: Will this fix create new problems? (ssdl-systems-thinking-foundations)
- [ ] Forward accountability assigned: Who will own this? (lfuo-learning-review-guide-2024)
- [ ] Practical-to-adopt test passed: Is the action practical to adopt?
- [ ] Local success checked: Is anyone here already succeeding at this? (liberating-structures-handbook)
- [ ] Clarity checked: Could someone who wasn't in the AAR act on the action description as written?

---

## Example Output

### Short-Term Actions

| Story ID | Description | Owner | Checked by | Target |
|----------|-------------|-------|------------|--------|
| TBD | Add input validation for date fields in /api/process endpoint | [One backend engineer] | [Their team lead] | This sprint |
| TBD | Create runbook: "What to do when batch job fails mid-run" | [One on-call engineer] | [On-call lead] | Next week |
| TBD | Add alert: batch job running >2x expected duration | [One platform engineer] | [Platform lead] | This sprint |

### Long-Term Actions

| Story ID | Description | Owner | Checked by | Target |
|----------|-------------|-------|------------|--------|
| TBD | Leadership Request: Review batch processing architecture for idempotency | [One named leader] | [Sponsor who decides] | Q2 |

[Include full Leadership Request for systemic items]
