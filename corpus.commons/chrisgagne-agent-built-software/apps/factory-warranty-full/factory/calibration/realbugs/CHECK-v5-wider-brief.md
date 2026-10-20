# Check: does the wider review brief cost catches? (PREREG-v5, before the factory commit is fixed)

**The change.** The reviewer and sort briefs now also ask for what a careful senior reviewer would raise beyond
defects (maintainability, needless work on a hot path, documentation the change makes wrong or leaves missing,
accessibility, awkward public interfaces), always as low, so they never block. The risk: a reviewer asked to notice
everything finds fewer of the defects that matter.

**The check, written before it runs.** The factory with the wider brief (this commit) reviews the 8 bug cases of
`v4-cases.json` once each, grounded in the open (17-source) build, scored as in v4 (Sol grades each bug trial blind
against the fix). It goes into the v5 head-to-head if it **catches at least 6 of the 8** on that trial; the round-two
factory caught 7 of the 8 on both of its trials. Otherwise the head-to-head runs the factory without it.

**Limits.** One trial of 8 bugs can show a large loss, not a small one; these cases have been seen before (development
data). False stops from the new items are measured in v5 part B itself, where every arm's stops on good changes count.
Reported with the count of findings per trial, against round two's.

## Result, 2026-10-19

**Passes: 7 of 8 caught** on factory `95a1a02` (the same seven as round two; w04 missed, as in round two), with no
review malfunctions. Findings per bug trial: 3.25, against 2.75 for round two's factory on the same cases, so the wider
brief added few items. The wider brief goes into the v5 head-to-head. Codex meter: 5-hour window 10% → 23%, week
2% → 4% (8 reviews and their grading). Records in `results/v5-check-wider/`.
