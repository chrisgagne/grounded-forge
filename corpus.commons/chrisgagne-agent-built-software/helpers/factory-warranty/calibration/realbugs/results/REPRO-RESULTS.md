# Reproduction step: offline test results (PREREG-reproduce.md)

Run 2026-10-19 on factory `0bd42ef`, every blocking finding recorded in `v3-distillations`, `v4-arm-v3` and
`v4-arm-v4` (70 findings in 70 trials; one v3 control stopped only by a reviewer timing out, with no finding to test,
counts as not cleared). Leg: Claude (Opus) in Claude Code's sandbox with no network; checks run by the factory under
`sandbox-exec`, no network, on fresh copies of each tree. Records: `results/repro/`. Cost: $10.95 of Claude in all
(about $0.16 a finding).

## As registered

| | Result | Rule | Met |
|---|---|---|---|
| Caught bug trials that keep a blocking finding describing the bug | 60 of 60 | at least 90% | yes |
| Review-stopped good-change trials cleared | 2 of 10 | at least half | no |

**The step does not go into the factory**, as pre-registered.

## What it found

- **Real bugs show.** 58 of the 60 bug-describing findings were shown: a check that passed before the change and failed
  after it, for the reason the finding gave. The other 3 got no usable answer from the leg (kept blocking, fail-closed).
  None came out "not shown".
- **Most stops on "good" changes pointed at a real change in behaviour.** 7 of the 9 findings on stopped good changes
  were shown, each with a concrete before-and-after:
  - decimal.js (v04, both trials): the source now accepts `'+1'`, but the shipped minified build wasn't rebuilt and still
    throws, so the two builds disagree.
  - node-semver (v05): the new `preload.js` isn't in the package's `files` list, so `require('semver/preload')` would
    fail in the published package.
  - js-yaml (v12, both trials): an event stream cut short now returns an empty result with no error, where it used to
    throw.
  - jsdiff (w12, two of four trials): a patch object built by hand with line 0 now puts the line at the end. Patches
    the library parses itself aren't affected, which is why the other two trials came out not shown: those legs tested
    only the input the reviewer named.
- The cases were picked as good changes because nothing later reverted or fixed them. The step shows that "never
  reverted" and "changes no behaviour anyone would object to" are different things: these upstream projects accepted
  the changes (for example, rebuilding minified files at release time), and a reviewer flagging them wasn't wrong about
  the code, only about whether it mattered.

## What that means for the factory

The registered rule asked the step to clear false stops, and it didn't. What it did instead is turn an argument the
signer can't check into a fact they can: "after this change, this input does that; before, it did this". Whether that
change is wanted is the signer's call, and now they can make it without reading code. A next version would show the
check's before-and-after on the sheet and let the signer clear a shown finding as intended, rather than clearing
findings automatically; that is a design change, to be tested on fresh cases.

**Limits.** Development evidence: these findings come from runs already seen, including the jsdiff stop the step was
designed against. The legs were inconsistent on w12 (two shown, two not), so one run per finding understates how often
a real change gets shown.
