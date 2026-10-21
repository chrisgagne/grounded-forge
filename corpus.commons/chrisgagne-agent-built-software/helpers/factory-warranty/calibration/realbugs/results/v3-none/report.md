# Real-bug replay: v3, arm: none (2 trials; pass^k read at k = 2)

Cases: `v3-cases.json` (25), trials per case: 2. Claude review legs $13.27; Codex review tokens 1,236,563.

## Measures

| Measure | Value |
|---|---|
| bug_trials_caught | 27/34 (79%) |
| bug_trials_surfaced | 28/34 (82%) |
| bug_cases_pass_hat_k | 11/17 (65%) |
| bug_cases_pass_at_k | 16/17 (94%) |
| control_trials_false_alarm | 6/16 (38%) |
| control_trials_review_alarm | 6/16 (38%) |
| control_cases_pass_hat_k | 5/8 (62%) |
| errored_trials | 0/50 (0%) |
| grader_errors | 0/34 (0%) |
| infra_reruns | 1/50 (2%) |
| bug_trials_caught_original_rule | 26/34 (76%) |
| control_trials_false_alarm_original_rule | 6/16 (38%) |

## Against the pass mark

| Measure | Pass mark | Result | Meets |
|---|---|---|---|
| bug_trials_caught | >= 80% (PROPOSED) | 79% | no |
| bug_cases_pass_hat_k | >= 70% (PROPOSED) | 65% | no |
| bug_trials_surfaced | >= 95% (PROPOSED) | 82% | no |
| control_trials_false_alarm | <= 20% (PROPOSED) | 38% | no |
| control_cases_pass_hat_k | >= 80% (PROPOSED) | 62% | no |

Re-run once after an outage (originals in `infra-failures/`): v24-t1.

## Per case

| Case | Kind | Project | Trials |
|---|---|---|---|
| v01 | bug | date-fns | caught (blocked on the defect) / caught (blocked on the defect) |
| v02 | control | immutable-js | passed clean / passed clean |
| v03 | control | jsdiff | passed clean / passed clean |
| v04 | control | decimal.js | false alarm: review / false alarm: review |
| v05 | control | node-semver | false alarm: review / false alarm: review:malfunction |
| v06 | bug | node-semver | missed / missed |
| v07 | bug | decimal.js | caught (blocked on the defect) / caught (blocked on the defect) |
| v08 | bug | immutable-js | caught (blocked on the defect) / caught (blocked on the defect) |
| v09 | bug | decimal.js | caught (blocked on the defect) / caught (blocked on the defect) |
| v10 | bug | node-semver | caught (blocked on the defect) / missed |
| v11 | bug | js-yaml | caught (blocked on the defect) / missed |
| v12 | control | js-yaml | false alarm: review:malfunction / false alarm: review |
| v13 | bug | js-yaml | caught (blocked on the defect) / caught (blocked on the defect) |
| v14 | bug | markdown-it | caught (blocked on the defect) / missed |
| v15 | control | yargs-parser | passed clean / passed clean |
| v16 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) |
| v17 | control | markdown-it | passed clean / passed clean |
| v18 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) |
| v19 | bug | node-semver | caught (blocked on the defect) / caught (blocked on the defect) |
| v20 | bug | date-fns | caught (blocked on the defect) / surfaced to the signer, not blocked |
| v21 | control | date-fns | passed clean / passed clean |
| v22 | bug | markdown-it | caught (blocked on the defect) / caught (blocked on the defect) |
| v23 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) |
| v24 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) |
| v25 | bug | immutable-js | caught (blocked on the defect) / mentioned, not confirmed |
