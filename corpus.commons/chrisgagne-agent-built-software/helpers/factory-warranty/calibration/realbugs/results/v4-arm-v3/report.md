# Real-bug replay: v4, arm: v3 (2 trials; pass^k read at k = 2)

Cases: `v4-cases.json` (20), trials per case: 2. Claude review legs $22.68; Codex review tokens 1,734,413.

## Measures

| Measure | Value |
|---|---|
| bug_trials_caught | 14/16 (88%) |
| bug_trials_surfaced | 15/16 (94%) |
| bug_cases_pass_hat_k | 7/8 (88%) |
| bug_cases_pass_at_k | 7/8 (88%) |
| control_trials_false_alarm | 2/24 (8%) |
| control_trials_review_alarm | 2/24 (8%) |
| control_cases_pass_hat_k | 11/12 (92%) |
| errored_trials | 0/40 (0%) |
| grader_errors | 0/16 (0%) |
| infra_reruns | 17/40 (42%) |
| bug_trials_caught_original_rule | 7/16 (44%) |
| control_trials_false_alarm_original_rule | 12/24 (50%) |

## Against the pass mark

| Measure | Pass mark | Result | Meets |
|---|---|---|---|
| bug_trials_caught | >= 80% (PROPOSED) | 88% | yes |
| bug_cases_pass_hat_k | >= 70% (PROPOSED) | 88% | yes |
| bug_trials_surfaced | >= 95% (PROPOSED) | 94% | no |
| control_trials_false_alarm | <= 20% (PROPOSED) | 8% | yes |
| control_cases_pass_hat_k | >= 80% (PROPOSED) | 92% | yes |

Re-run once after an outage (originals in `infra-failures/`): w06-t1, w06-t2, w07-t1, w07-t2, w08-t1, w08-t2, w09-t1, w09-t2, w10-t1, w10-t2, w11-t1, w12-t1, w16-t2, w17-t2, w18-t2, w19-t2, w20-t2.

## Per case

| Case | Kind | Project | Trials |
|---|---|---|---|
| w01 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) |
| w02 | control | immutable-js | passed clean / passed clean |
| w03 | control | yargs-parser | passed clean / passed clean |
| w04 | bug | node-semver | mentioned, not confirmed / surfaced to the signer, not blocked |
| w05 | control | immutable-js | passed clean / passed clean |
| w06 | bug | markdown-it | caught (blocked on the defect) / caught (blocked on the defect) |
| w07 | bug | date-fns | caught (blocked on the defect) / caught (blocked on the defect) |
| w08 | control | yargs-parser | passed clean / passed clean |
| w09 | control | decimal.js | passed clean / passed clean |
| w10 | control | js-yaml | passed clean / passed clean |
| w11 | control | node-semver | passed clean / passed clean |
| w12 | control | jsdiff | false alarm: review / false alarm: review |
| w13 | control | date-fns | passed clean / passed clean |
| w14 | control | date-fns | passed clean / passed clean |
| w15 | bug | js-yaml | caught (blocked on the defect) / caught (blocked on the defect) |
| w16 | control | js-yaml | passed clean / passed clean |
| w17 | control | markdown-it | passed clean / passed clean |
| w18 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) |
| w19 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) |
| w20 | bug | immutable-js | caught (blocked on the defect) / caught (blocked on the defect) |
