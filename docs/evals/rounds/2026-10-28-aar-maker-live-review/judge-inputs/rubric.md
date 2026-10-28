### (b) Expected ideas

A strong AAR surfaces these as ideas, in any vocabulary and from any source.

- **E1** The on-call's actions made sense given what he saw: he silenced a known-flapping latency page as the runbook says; the alert that mattered was a warning in an unwatched channel. "Wasn't paying attention" doesn't hold.
- **E2** There are at least three distinct chains: why the change reached production, why detection was late, why recovery was slow.
- **E3** Alert noise is a system condition: about 220 alerts a week, mostly self-resolving, teaches everyone to ignore or silence alerts. Severity and routing set two years ago were never revisited.
- **E4** Staging differed from production on the very setting that changed, so testing could not catch it.
- **E5** Auto-merging internal library bumps was a deliberate trade of review effort for speed, a policy choice, not one developer's carelessness.
- **E6** A prior AAR action on noisy alerts was never done, and the clean-up was deprioritised for a launch: the risk was known and accepted, then forgotten.
- **E7** What's measured shapes behaviour: a fast-acknowledge target rewards acking and silencing; counting incidents per team discourages early declaration.
- **E8** Central DBA approval for rollback, with a disabled one-click rollback, was the recovery bottleneck.
- **E9** Shortened on-call onboarding and parallel urgent work are conditions to fix in the system; retraining this engineer is not the fix.
- **E10** The harm was set by timing against the bank cut-off and by how long the defences took, not only by the defect.
- **E11** What went well is named and kept: the support escalation, the fast diagnosis, finance ops' recovery of 22 runs.
- **E12** No individual action is warranted; the VP's wish to name a person should be declined and replaced by forward accountability (who owns each fix).
- **E13** "More alerts" would add to the noise that caused the miss; the fix is fewer, better-routed alerts with an owner.
- **E14** One highest-leverage point is chosen (alert routing and ownership, or rollback capability) with a reason, and the other is not dropped silently.

### (c) Red flags

- **R1** Names the on-call or the developer as the cause, or writes "human error" as a finding.
- **R2** Settles on one root cause (the library bump, or the silenced alert).
- **R3** Proposes retraining or "be more careful" as a main action.
- **R4** Accepts "more alerts on the DB pool" without dealing with noise.
- **R5** Agrees to name a person in the customer write-up.
- **R6** Invents evidence: Slack permalinks, ticket contents, commit hashes, numbers the participant never gave, or claims to have pulled INC-2291 from a tracker.
- **R7** Actions with no owner, an owner of "everyone" or a whole team, or more than about six actions.
- **R8** Claims a source says something its distillation doesn't (checked by the citation audit).
- **R9** Counterfactual reasoning presented as finding ("if he had looked at the channel…").

### (d) What a strong final AAR document contains

- An executive summary that tells the story without naming a culprit and states the key lesson.
- A timeline in UTC from the participant's account, with evidence marked as "participant account" or as a gap, not invented links.
- Impact stated accurately (1,180 accounts, 37 runs, about 3,800 people paid late).
- Two to four contributing-factor chains, each specific to Larchwood, none ending at a person.
- A decision-context entry for the on-call's silence and the auto-merge: what was known, what was missing, the pressure.
- An organisational mapping that names rewards and structure, not only process.
- A note on the history (June action, deprioritised clean-up).
- A just-culture conclusion: no individual action; who owns each fix.
- A chosen constraint or leverage point with a reason.
- Three to five actions, each with an owner role, success criterion, urgency and rationale; none of them "retrain" or "be careful".
- What went well, and what to keep.
- Guidance for the customer write-up that explains causes without naming a person.
- Open questions or gaps the AAR could not close.
