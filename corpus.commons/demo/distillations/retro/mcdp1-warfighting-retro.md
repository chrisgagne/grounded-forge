<!-- derived-from-deep: sha256:72550dcb4a79df378ed7b1441f68804581317c24bb6c65b51c20104d797fb0c4 -->
# U.S. Marine Corps, MCDP-1 Warfighting — Retrospective Distillation

**Source:** U.S. Marine Corps (1997). *MCDP 1: Warfighting*. Headquarters United States Marine Corps, Department of the Navy, 20 June 1997. PCN 142 000006 00. Supersedes FMFM 1 Warfighting (1989). **Licence:** Public domain (US Government work product). **Scope:** open.

## Retro Relevance

MCDP-1 is a high-tempo / high-uncertainty / decentralised-execution doctrinal pamphlet. For software / product / SRE teams operating in similar conditions, the document is unusually directly usable. Where the Scrum Guide and Field Guide supply the *cadence* of team retrospection, MCDP-1 supplies the *philosophy* — particularly four threads that recur in team-level retros.

### 1. Doctrine is a way of thinking, not a checklist (Ch 3)

Teams treating runbooks / playbooks / standards as scripts rather than as ways of thinking will drift; the runbook will be executed but the underlying judgment will atrophy. Retro question: *what is the underlying thinking that produced our current procedures? Is the thinking still right? Have the conditions changed?*

Runbooks executed mechanically without the underlying thinking produce drift. The retro action item is rarely *update the runbook* — it is *refresh the thinking, then let the runbook follow*.

### 2. The main effort / Schwerpunkt (Ch 4)

MCDP-1 names the disciplinary requirement: every subordinate's standing question is *how can I best support the main effort?* The main effort is one — one team / one objective. Everything else is supporting effort.

Retro question: *what is our team's main effort right now? Could every team member state it in one sentence? If you asked each person, would the answers agree?* The variance in answers is data. High variance means the team's *Schwerpunkt* discipline is missing and prioritisation decisions are unanchored.

### 3. Commander's intent must be understood two levels up (Ch 4)

Senior commanders give *what* and *why* (intent), never *how*. Subordinates execute within intent. Intent must be understood *two levels up*. If the sharp-end team does not know the intent two levels up, the senior leaders' communication is the upstream cause, not the team's compliance.

Retro pattern this surfaces: chronic *we never know what management actually wants* surfaces as a leadership-level action item, not a team-level one.

### 4. The OODA loop and tempo (Ch 2 Notes 18)

For SRE / incident-response / agile-delivery / startup teams, the diagnostic question is *what is our team's OODA tempo relative to the market / threat / customer's?* The team that completes the cycle faster, or that operates in a way the adversary cannot orient to, wins. Boyd's insight (via Coram's biography, where Orient is the load-bearing node): the improvements that actually matter are usually orientation improvements (better mental models, faster cultural pattern-recognition) — not just faster Observe / Decide / Act.

For agile teams: if your sprint cadence is shorter than the requirements-change cadence, your sprint plan is obsolete by mid-sprint; the requirements are inside your team's OODA loop. The retro question: *where can we cut our Observe-Orient-Decide-Act cycle in half? Is the bottleneck in Orient?*

### 5. Attrition vs maneuver (Ch 2)

Teams in chronic *more hours / more headcount / more meetings / more rigour* response mode are operating in attrition mode. MCDP-1 distinguishes attrition (cumulative damage / production) from maneuver (shatter cohesion through rapid, focused, surprising action). Retro question: *is our team currently in attrition mode or maneuver mode? Does the situation reward the mode we're in?* Mismatching the mode to the situation is the failure.

### 6. Severity on errors of inaction, leniency on overbold errors (Ch 3)

The zero-defects mentality is directly rejected. For teams in chronic fear-of-mistakes / fear-of-blame patterns, the retro move is to make the leniency / severity asymmetry explicit: *we will be lenient on errors of commission, severe on errors of omission*. Without this asymmetry, the team optimises for *don't be the one blamed*, which produces inaction.

## Retro Cautions

The doctrinal pamphlet is dense; for teams unfamiliar with military / strategic vocabulary, reach instead for Scrum Guide (slug 00m), Field Guide (slug 000), or Liberating Structures (slug 006) for the retro mechanics. MCDP-1 is the *philosophical companion*, not a how-to manual.

## Connections to other corpus sources

- **Scrum Guide (slug 00m); Field Guide (slug 000)** — the procedural / cadence companions.
- **Liberating Structures (slug 006); Open Practice Library (slug 009)** — facilitation methods that operationalise MCDP-1's *doctrine-as-way-of-thinking* discipline.
- **TC 25-20 (slug 00o)** — military AAR procedure that operates within MCDP-1's doctrinal frame.
- **Barbrook-Johnson & Penn, Systems Mapping (slug 001)** — for retros that need to read the structural / dynamical context, complementing MCDP-1's tempo / Schwerpunkt vocabulary.
- **Open Kanban (slug 008)** — flow / WIP discipline as a tempo-management practice.
