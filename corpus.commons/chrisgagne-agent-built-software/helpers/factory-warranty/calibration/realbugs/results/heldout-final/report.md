# Real-bug replay: HELD-OUT half, final (factory d67c073)

Cases: `heldout.json` (18), trials per case: 3. Claude review legs $17.06; Codex review tokens 1,247,105.

## Measures

| Measure | Value |
|---|---|
| bug_trials_caught | 36/36 (100%) |
| bug_trials_surfaced | 36/36 (100%) |
| bug_cases_pass_hat_k | 12/12 (100%) |
| bug_cases_pass_at_k | 12/12 (100%) |
| control_trials_false_alarm | 9/18 (50%) |
| control_trials_review_alarm | 6/18 (33%) |
| control_cases_pass_hat_k | 3/6 (50%) |
| errored_trials | 0/54 (0%) |
| grader_errors | 0/36 (0%) |
| infra_reruns | 3/54 (6%) |
| bug_trials_caught_original_rule | 34/36 (94%) |
| control_trials_false_alarm_original_rule | 10/18 (56%) |

## Against the pass mark

| Measure | Pass mark | Result | Meets |
|---|---|---|---|
| bug_trials_caught | >= 50% (PROPOSED) | 100% | yes |
| bug_cases_pass_hat_k | >= 40% (PROPOSED) | 100% | yes |
| bug_trials_surfaced | >= 70% (PROPOSED) | 100% | yes |
| control_trials_false_alarm | <= 10% (PROPOSED) | 50% | no |
| control_cases_pass_hat_k | >= 80% (PROPOSED) | 50% | no |

Re-run once after an outage (originals in `infra-failures/`): rb10-t1, rb13-t1, rb26-t1.

## Per case

| Case | Kind | Project | Trials |
|---|---|---|---|
| rb02 | bug | markdown-it | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb03 | bug | immutable-js | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb04 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb08 | bug | date-fns | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb10 | bug | js-yaml | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb13 | bug | immutable-js | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb14 | control | markdown-it | passed clean / passed clean / passed clean |
| rb15 | bug | decimal.js | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb19 | bug | jsdiff | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb20 | bug | node-semver | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb25 | control | decimal.js | passed clean / passed clean / passed clean |
| rb26 | control | yargs-parser | false alarm: gate:sast / false alarm: gate:sast / false alarm: gate:sast |
| rb28 | control | js-yaml | false alarm: review / false alarm: review / false alarm: review |
| rb29 | bug | markdown-it | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb32 | control | date-fns | passed clean / passed clean / passed clean |
| rb33 | bug | yargs-parser | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb34 | bug | date-fns | caught (blocked on the defect) / caught (blocked on the defect) / caught (blocked on the defect) |
| rb36 | control | node-semver | false alarm: review / false alarm: review / false alarm: review |
