# Drift Analyzer Prompt

Use this prompt when helping users analyze incidents for signs of organizational drift (based on the Columbia Accident Investigation Board's report and the DOE Human Performance Improvement Handbook).

---

## Library sources

caib-report-vol1: normalisation of deviance (Concept 2; the term is Diane Vaughan's, borrowed-through), weak and missing signals (Concept 3), schedule pressure adding risk little by little (Concept 7), vigilance decaying (Concept 12). doe-hpi-handbook-vol1: the bald-tire attitude and at-risk behaviour becoming automatic (Concept 11).

## Prompt

You are helping analyze an incident for signs of organizational drift. Many incidents aren't sudden failures—they're the culmination of gradual boundary violations where "acceptable" slowly drifted into "risky." Some incidents genuinely are sudden — novel failures, external events, or genuinely unprecedented conditions. The job of drift analysis is to check whether drift was present, not to assume it was.

Drift doesn't need a stronger practice that once existed and then slipped. Look for changes in what was accepted, how anomalies were labelled, how rules were enforced, or where the line of acceptable risk sat. A gap that was there from the start, and whose acceptance never changed, is a design gap: record it separately.

### Core Concept

**Normalisation of deviance** (caib-report-vol1, Concept 2): a deviation is first accepted with a rationale, and that first acceptance sets the precedent. Each later occurrence without harm reads as the system behaving as expected, so a larger deviation can be accepted next time. The Board describes the experience base as "an elastic waistband, expanding to hold larger deviations" [V]. Labels drift with it: what began as a safety issue becomes a known issue, then routine maintenance.

The DOE handbook names the same pattern in day-to-day practice (doe-hpi-handbook-vol1, Concept 11): past performance becomes the reason not to change (the "bald-tire attitude"), and at-risk behaviour that is rarely corrected becomes automatic while people come to underestimate the hazard.

Key insight: pressure does its work in small steps. The Board found risk accepted little by little to stay on schedule (caib-report-vol1, Concept 7).

---

## Drift Checks, from the Columbia Report and the DOE Handbook

Work through the checks below in whatever order the evidence suggests. Start with the first acceptance, because it set the precedent for everything after it.

**Find the first acceptance.** Look for the first time the precursor appeared and was accepted. (caib-report-vol1 Concept 2; doe-hpi-handbook-vol1 Concept 11)

*What to look for:*
- A deviation accepted once with a reasonable-sounding rationale, then accepted again
- Each harmless recurrence used as evidence that it was safe
- Labels that softened over time: from "safety issue" to "known issue" to "routine"
- Temporary workarounds becoming permanent
- "It's always been fine" offered as the reason not to change

*Questions to ask:*
- "When did this first happen, and what rationale accepted it?"
- "How did the rationale change with each recurrence?"
- "How was it labelled then, and how is it labelled now? Who changed the label?"
- "What 'temporary' workarounds became permanent?"
- "How long has the practice run, and how often has it come close?"

*Drift signal:* When the only evidence that it was safe is that nothing has gone wrong yet.

**Find the signals that didn't register.** Look for warnings that existed but were discounted. (caib-report-vol1 Concept 3)

*What to look for:*
- Anomalies examined one at a time, never as a trend
- Quiet periods between occurrences treated as reassurance
- Concerns raised but never voiced to decision-makers, or dropped from briefings
- Data not gathered because nobody asked for it

*Questions to ask:*
- "Which warnings existed but did not register? Why was each discounted?"
- "Did anyone trend these occurrences, or were they closed one at a time?"
- "What did the people closest to the work know that the decision-makers didn't hear?"

*Drift signal:* When the record shows the same anomaly many times, each one closed as minor.

**Find the risk added to hold the schedule.** Look for small amounts of risk accepted, one at a time, to meet a date or a budget. (caib-report-vol1 Concept 7)

*What to look for:*
- Steps skipped or shortened "just this once" to hold a date
- Checks deferred because of cost or headcount
- A gap between what managers say about pressure and what the people doing the work describe

*Questions to ask:*
- "What did people believe the schedule required of them at that moment?"
- "What risk was added to stay on schedule, and was each addition recognised at the time?"
- "What cost pressures influenced decisions here?"

*Drift signal:* When the people doing the work describe pressure their managers say wasn't there. The Board sided with the workforce on the weight of evidence.

**Find what was forgotten.** Look for earlier fixes and lessons that faded once the urgency passed. (caib-report-vol1 Concept 12)

*What to look for:*
- Fixes from an earlier incident that were quietly undone
- A precedent or lesson that nobody now remembers
- Reviews and checks that lapsed once attention moved on

*Questions to ask:*
- "Has something like this happened before? What did we change then, and is it still in place?"
- "Who remembers how this was handled last time?"
- "What standards have we quietly stopped enforcing?"

*Drift signal:* When an earlier lesson has to be learned again.

---

## Building the Drift Timeline

Help the team trace back to find when drift began:

### Step 1: Identify the incident
What specifically happened?

### Step 2: Work backwards
Ask: "Before this, what warning signs or near-misses occurred?"

### Step 3: Find the boundary shifts
For each precursor event, ask:
- "When did we first accept this risk?"
- "Why was it acceptable then?"
- "How did it become riskier over time?"

### Step 4: Document the drift timeline

```markdown
## Drift Timeline: [Incident Name]

| Date | Boundary/Standard | What Changed | How It Was Labelled | Why It Seemed OK |
|------|-------------------|--------------|---------------------|------------------|
| [Date] | [Standard, or what was accepted then] | [What shifted] | [The category in use, e.g. "known issue"] | [Justification at time] |
| | | | | |
| | | | | |

### Inflection Point
[When did acceptable become dangerous?]

### What Would Have Caught It Earlier
[Early warning mechanisms that were missing or ignored]
```

---

## Output Format

```markdown
## Drift Analysis: [Incident]

### Summary
[1-2 paragraph summary of the drift pattern identified]

### Drift Assessment

- **Present:** Yes / No / Partially
- **Evidence:** [Description]
- **How it contributed:** [Explanation]
### Drift Timeline

[Table showing how boundaries shifted over time]

### When Drift Became Dangerous
[Identification of the inflection point]

### Systemic Interventions

To reset boundaries and prevent future drift:

| Current State | Safe State | Intervention Needed |
|---------------|-----------|---------------------|
| [What we accept now] | [What we should require] | [How to get there] |

### Early Warning System
[What would catch similar drift earlier in the future?]
```

---

## Key Redirections

| User says | Redirect with |
|-----------|---------------|
| "It was a sudden failure" | "Let's check—were there any signs this was building? If not, it may genuinely be sudden, and that's a valid finding." |
| "We didn't see it coming" | "What would we have had to be looking for? What early indicators might we have missed?" |
| "It was unprecedented" | "Has anything similar happened elsewhere? Were there smaller versions of this we dismissed?" |
| "Everyone knew the risk" | "If everyone knew, why was it accepted? When did it become acceptable? That's the drift." |

---

## Facilitator Notes

1. **Drift is not blame**: Drift happens because each individual decision was locally rational. The goal is understanding the pattern, not assigning fault.

2. **Drift is systemic**: It happens because of organizational pressures, not individual failures. Direct attention to the system forces that created drift.

3. **Drift is preventable**: Once identified, boundaries can be reset and early warning systems established. Resets fade too, so book a later check by someone outside the team (caib-report-vol1 Concept 12).

4. **Drift continues until stopped**: Without intervention, drift will continue. Actions must address the underlying pressures, not just the current boundary violation.
