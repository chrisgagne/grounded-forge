# Pre-registration: does making reviewers show their work clear false stops without losing catches?

**Status:** in effect from the commit that adds it, before the reproduction step is run on any recorded finding.
Nothing below may change after that commit; a later change is a dated amendment that judges only later runs. Chris
Gagné approved building and testing this step on 2026-10-19 ("what would fix the root issue?").

## Why

In round two (`results/v4-RESULTS.md`) every false stop came from one jsdiff change: reviewers named a concrete input
that "now breaks", rated it critical, and the input worked fine when run. A person who doesn't read code can't tell a
right argument from a wrong one, and a second model grading the argument doesn't help either. They can tell whether a
test the factory ran failed.

## The step

For each finding that blocks a change, a Claude leg gets the finding (claim, evidence, file, line), the change's base
tree and head tree, and a shell with no network. It does one of two things:

- **Writes a check:** a test or script, and the command that runs it, meant to fail on the head because of the
  finding's problem. The factory runs that command itself in both trees. **Shown** if it fails on the head and passes
  on the base (or, where the base can't run it because the code is new, if it fails on the head for the reason the
  finding gives, as the leg must state in one sentence that the factory records). **Not shown** if it doesn't fail on the
  head.
- **Says the finding can't be shown by running code** (a removed security check, a race, a licence or design question),
  in one sentence. **Argued.**

A shown or argued finding keeps blocking, labelled as such on the sheet; a not-shown finding stops blocking and appears
as "raised but not shown". The leg's test files never enter the change.

## The test, offline, on recorded findings

Every blocking finding recorded in these runs, on the trees the replay built for it:

- `results/v4-arm-v3/` and `results/v4-arm-v4/`: bug trials that caught their bug, and control trials stopped by review;
- `results/v3-distillations/`: the same;
- `results/v5-b-factory/`: control trials stopped by review, once that run is complete.

Each finding goes through the step once. The operator prepares each project's base and head trees with their
dependencies installed (`npm ci --ignore-scripts` or the project's equivalent, before the leg starts; the leg itself has
no network) and reads nothing else about the cases.

**What decides it.** The step goes into the factory if both hold:

1. **Catches kept:** of the bug trials that caught their bug, at least 90% still have a blocking finding that describes
   the bug (the same grade as before) after the step, shown or argued.
2. **False stops cleared:** of the control trials stopped by review, at least half no longer have any blocking finding
   after the step.

Otherwise the factory ships without it, and the README says the step was tried and what it did.

**Reported, not judged:** how many blocking findings were shown, not shown and argued, in bug trials and in control
trials; how many argued findings look like they could have been run (the operator's reading, labelled as such); cost
per finding; and every control stop the step didn't clear, with the reason.

**Limits.** These findings come from runs already seen, including the jsdiff stop the step was designed against, so
this is development evidence. A fresh test needs fresh cases; the next replay would run the factory with the step.
