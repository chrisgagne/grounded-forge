# Real-bug replay: tuning half, after the phase 3 fixes (factory b0eac10)

Cases: `tuning.json` (18), trials per case: 3. Claude review legs $16.70; Codex review tokens 1,166,366.

## Measures

| Measure | Value |
|---|---|
| bug_trials_caught | 34/36 (94%) |
| bug_trials_surfaced | 36/36 (100%) |
| bug_cases_pass_hat_k | 10/12 (83%) |
| bug_cases_pass_at_k | 12/12 (100%) |
| control_trials_false_alarm | 2/18 (11%) |
| control_trials_review_alarm | 2/18 (11%) |
| control_cases_pass_hat_k | 5/6 (83%) |
| errored_trials | 0/54 (0%) |
| grader_errors | 0/36 (0%) |
| infra_reruns | 2/54 (4%) |
| bug_trials_caught_original_rule | 34/36 (94%) |
| control_trials_false_alarm_original_rule | 4/18 (22%) |

## Against the pass mark

| Measure | Pass mark | Result | Meets |
|---|---|---|---|
| bug_trials_caught | >= 50% (PROPOSED) | 94% | yes |
| bug_cases_pass_hat_k | >= 40% (PROPOSED) | 83% | yes |
| bug_trials_surfaced | >= 70% (PROPOSED) | 100% | yes |
| control_trials_false_alarm | <= 10% (PROPOSED) | 11% | no |
| control_cases_pass_hat_k | >= 80% (PROPOSED) | 83% | yes |

Re-run once after an outage (originals in `infra-failures/`): rb05-t3, rb23-t3.

## Per case

| Case | Kind | Project | Trials |
|---|---|---|---|
| rb01 | bug | js-yaml | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb05 | control | yargs-parser | passed clean / passed clean / passed clean |
| rb06 | bug | js-yaml | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb07 | control | jsdiff | false alarm: review / false alarm: review / passed clean |
| rb09 | bug | node-semver | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb11 | control | node-semver | passed clean / passed clean / passed clean |
| rb12 | bug | decimal.js | caught (blocked on the defect) / caught (blocked on the defect) / surfaced to the signer, not blocked |
| rb16 | bug | immutable-js | surfaced to the signer, not blocked / caught (blocked on the defect) / caught (blocked on the defect) |
| rb17 | bug | markdown-it | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb18 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb21 | bug | node-semver | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb22 | bug | decimal.js | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb23 | control | date-fns | passed clean / passed clean / passed clean |
| rb24 | control | immutable-js | passed clean / passed clean / passed clean |
| rb27 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb30 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb31 | control | js-yaml | passed clean / passed clean / passed clean |
| rb35 | bug | date-fns | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
