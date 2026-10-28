---
name: aar-deep
description: Deep-dive analysis combining contributing factor analysis, drift detection, and constraint identification
argument-hint: "[bug-id or incident description]"
---

# AAR Deep Dive - Contributing Factor, Drift & Constraint Analysis

Combined deep analysis framework for incidents that need more than surface-level investigation. Integrates three complementary lenses:
- **Contributing Factor Analysis** — Why did this happen? (5 Whys + the five organisational points)
- **Drift Detection** — How did we get here gradually? (normalisation of deviance and fading vigilance, from the Columbia report and the DOE handbook)
- **Constraint Identification** — What's THE bottleneck? (Goldratt's Five Focusing Steps)

The five organisational points follow Jay Galbraith's Star Model (strategy, structure, processes, rewards, people), put in plain words.

## Connection availability

Before using tracker or chat tools, verify that the relevant connection is available. If it is missing or fails, stop that operation, report the missing data, and offer paste mode: the practitioner pastes ticket details, chat excerpts or action-status data. Do not infer data or claim tickets were created. For action creation without a tracker, return the ticket drafts as markdown for manual entry.

## Bug ID (optional)

If the practitioner gave a bug ID or incident description, start from it.

## Library sources

Five Whys: open-practice-library. Local rationality: doe-hpi-handbook-vol1 (inside-view questions, via Dekker); doe-hpi-handbook-vol2 (debrief before you know too much). Drift/normalisation: caib-report-vol1 (Concepts 2, 3, 7, 12; the term "normalisation of deviance" is Diane Vaughan's, borrowed-through) and doe-hpi-handbook-vol1 (Concept 11). Whole-system stance: open-kanban (Deming and Goldratt, borrowed-through). The constraint method itself is Goldratt's.

## Instructions

1. **Read the AAR index**: `distillations/aar/AAR-DISTILLATION-INDEX.md` (Phases 2-4)
2. **Read component specs** as needed (in this skill's folder):
   - `cfa-facilitator.md`
   - `drift-analyzer.md`
   - `constraint-analyzer.md`
3. **Start with the failure**: What immediately went wrong?
4. **Choose which lenses fit**: Not every incident needs all three — use judgment
5. **Synthesize across lenses**: The power is in how they connect

## When to Use Each Lens

| Lens | Best For | Key Question |
|------|----------|--------------|
| **Contributing Factors (5 Whys + the five points)** | Any incident — start here | "Why did this happen, and what organizational factors allowed it?" |
| **Drift Detection (caib-report-vol1, doe-hpi-handbook-vol1)** | Recurring problems, gradual erosion | "How did we get from safe to unsafe without anyone noticing?" |
| **Constraint Analysis (Goldratt)** | Performance bottlenecks, action prioritization | "Which ONE thing, if fixed, would have the most impact?" |

**Typical combinations:**
- Acute failure → CFA only
- Recurring problem → CFA + Drift
- Systemic bottleneck → CFA + Constraint
- Safety erosion → All three

---

## Lens 1: Contributing Factor Analysis

### 5 Whys — Keep Going Until You Hit the Organization

Your final "why" should NOT be:
- "No process existed" (WHY didn't it?)
- "Communication gap" (WHY was there a gap?)
- "Human error" (WHAT about the system allowed it?)

Your final "why" SHOULD be:
- Specific to THIS incident
- About the organization, not individuals
- Something that, if fixed, prevents recurrence

### The Five Points — Map Contributing Factors to the Organization

| Point | Questions |
|--------|-----------|
| **What we optimise for** | Was this a conscious tradeoff? What were we optimizing for? |
| **Who owns what** | Who owns this interface? Is ownership clear? |
| **How work moves** | What process should have caught this? Why didn't it? |
| **What gets measured and rewarded** | What happens when someone proposes safeguards here? |
| **Who we hire, grow and staff** | Did people have knowledge, time, authority to prevent this? |

---

## Lens 2: Drift Detection

### Normalisation of Deviance and Fading Vigilance

These checks come from the Columbia Accident Investigation Board's report (caib-report-vol1) and the DOE Human Performance Improvement Handbook (doe-hpi-handbook-vol1). `drift-analyzer.md` (in this skill's folder) has the full checks.

- When was the precursor first accepted, and on what rationale? Did each harmless recurrence make the next one look normal, and did its label soften over time? (caib-report-vol1 Concept 2; doe-hpi-handbook-vol1 Concept 11)
- Which warnings existed but didn't register: looked at one at a time, never trended, not voiced, dropped from briefings? (caib-report-vol1 Concept 3)
- What risk was added a little at a time to hold a schedule or budget? (caib-report-vol1 Concept 7)
- Have earlier fixes or lessons faded or been undone? (caib-report-vol1 Concept 12)

### Key Questions
1. When did we first start doing things this way?
2. Was there a time we would have said "that's too risky"?
3. Did any warnings get ignored or dismissed?
4. Were there "temporary" workarounds that became permanent?

---

## Lens 3: Constraint Analysis

### Goldratt's Insight
Improving non-constraints is waste. Every system has ONE constraint limiting performance.

### Constraint Types

Name what is limiting improvement in plain words: a resource, a policy, or a paradigm (a belief about what's possible).

### Working the Constraint
Use Goldratt's Five Focusing Steps to focus improvement on the bottleneck that limits the whole system. `constraint-analyzer.md` (in this skill's folder) describes each step's job.

### Constraint Test for Actions
For each proposed action: Does this address THE constraint, or does it optimize a non-constraint (waste)?

---

## Synthesis

After applying the relevant lenses, synthesize:

```markdown
## Deep Dive Summary

**Contributing Factors:** [From 5 Whys — the organizational factors]
**Organizational Point:** [What we optimise for / Who owns what / How work moves / What gets measured and rewarded / Who we hire, grow and staff]
**Drift Present:** [Yes/No — if yes, which checks found it and since when]
**THE Constraint:** [The single bottleneck limiting improvement]
**Constraint Type:** [Resource/Policy/Paradigm]

### How the Lenses Connect
[How contributing factors, drift, and constraint relate — e.g., "The contributing factor (unclear ownership)
enabled drift (gradual erosion of review standards) which is sustained by
THE constraint (policy requiring sign-off from a team that no longer exists)"]

### Recommended Actions
[Actions that address the constraint AND the contributing factors, not just symptoms]
```

## Start

If the practitioner gave a bug ID or incident description, pull the bug details and begin analysis.
Otherwise ask: "What incident or recurring problem should we analyze? I'll help determine which analytical lenses fit."
