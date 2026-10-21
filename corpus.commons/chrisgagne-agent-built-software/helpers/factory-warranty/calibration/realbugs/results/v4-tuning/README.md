# Round-two tuning run (development data, not evidence)

Factory `3d12aac` (the round-two fixes), with the corpus, on eight v3 cases the fixes were developed from, two trials
each, graded by Sol. Run 2026-10-16 on mains power.

| Case | v3 corpus arm | This run |
|---|---|---|
| v04 (good change: minified build not regenerated) | stopped 2 of 2 | clean 2 of 2 |
| v12 (good change: checks removed) | stopped 2 of 2 | clean 1, stopped 1 (reviewer high, sort medium; a reviewer's high can't be cleared by the sort) |
| v05 (good change: new file missing from the package's published list) | stopped 2 of 2 | stopped 2 of 2, each finding now naming the failing `require` |
| v10, v11, v14 (bugs; the v3 no-corpus arm timed out on one trial each) | caught 2 of 2 | caught 2 of 2; no review leg ran out of time |
| v20 (bug) | caught 2 of 2 | caught 2 of 2 |
| v25 (bug) | caught 2 of 2 | caught 1, mentioned but not confirmed 1 |

No further tuning: the round-two test (`../../PREREG-v4-false-stops.md`) runs on cases neither version has seen.
