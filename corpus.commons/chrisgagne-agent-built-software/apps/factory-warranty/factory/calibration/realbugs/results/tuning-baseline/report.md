# Real-bug replay: tuning half, baseline (factory ca5646f)

Cases: `tuning.json` (18), trials per case: 3. Claude review legs $15.88; Codex review tokens 976,273.

## Measures

| Measure | Value |
|---|---|
| bug_trials_caught | 32/36 (89%) |
| bug_trials_surfaced | 36/36 (100%) |
| bug_cases_pass_hat_k | 10/12 (83%) |
| bug_cases_pass_at_k | 11/12 (92%) |
| control_trials_false_alarm | 0/18 (0%) |
| control_trials_review_alarm | 0/18 (0%) |
| control_cases_pass_hat_k | 6/6 (100%) |
| errored_trials | 0/54 (0%) |
| grader_errors | 0/36 (0%) |

## Against the pass mark

| Measure | Pass mark | Result | Meets |
|---|---|---|---|
| bug_trials_caught | >= 50% (PROPOSED) | 89% | yes |
| bug_cases_pass_hat_k | >= 40% (PROPOSED) | 83% | yes |
| bug_trials_surfaced | >= 70% (PROPOSED) | 100% | yes |
| control_trials_false_alarm | <= 10% (PROPOSED) | 0% | yes |
| control_cases_pass_hat_k | >= 80% (PROPOSED) | 100% | yes |

## Per case

| Case | Kind | Project | Trials |
|---|---|---|---|
| rb01 | bug | js-yaml | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb05 | control | yargs-parser | passed clean / passed clean / passed clean |
| rb06 | bug | js-yaml | caught (blocked on the defect) / surfaced to the signer, not blocked / caught (blocked on the defect) |
| rb07 | control | jsdiff | passed clean / passed clean / passed clean |
| rb09 | bug | node-semver | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb11 | control | node-semver | passed clean / passed clean / passed clean |
| rb12 | bug | decimal.js | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb16 | bug | immutable-js | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb17 | bug | markdown-it | surfaced to the signer, not blocked / surfaced to the signer, not blocked / surfaced to the signer, not blocked |
| rb18 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb21 | bug | node-semver | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb22 | bug | decimal.js | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb23 | control | date-fns | passed clean / passed clean / passed clean |
| rb24 | control | immutable-js | passed clean / passed clean / passed clean |
| rb27 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb30 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb31 | control | js-yaml | passed clean / passed clean / passed clean |
| rb35 | bug | date-fns | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
