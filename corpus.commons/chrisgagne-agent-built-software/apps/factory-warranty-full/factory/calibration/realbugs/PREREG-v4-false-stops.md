# Pre-registration v4: does round two stop fewer good changes without missing more bugs?

**Status:** approved by Chris Gagné (option C, 2026-10-16) and in effect from the commit that adds it, before Sol picks the cases and before any trial runs. Nothing below
may change after that commit; a later change is a dated amendment that judges only later runs.

## Why

In the v3 replay (`results/v3-RESULTS.md`) the factory with the corpus stopped 7 of 16 good-change trials (44%) against
a proposed bar of 20%, and six review legs were killed at the 30-minute leg limit. Round two changed three things
(factory `3d12aac`; no further tuning):

1. Review legs get their own 60-minute limit and one retry on a timeout.
2. The reviewer and sort briefs require a critical or high finding to name the input, call or state that now goes
   wrong, and rate a stale generated file low unless the project shows it must change with the code.
3. A ratchet measurement that errors is measured once more before it counts.

These were developed on v3's cases and checked in a tuning run on eight of them (`results/v4-tuning/`). That run is
development, reported as such, never as evidence. This test uses cases neither version has seen.

## Cases

Picked by Sol (gpt-6.1-sol) with `pick-v4.md` (adapted from `pick-v3.md`): **12 CONTROL and 8 BUG** cases from the same
eight projects, none of the commits in `used-commits-v3.txt` or `v3-cases.json`. Same rules for a bug fix and a clean
change, same size limits, same neutral story. The operator checks only that each case applies.

## Arms

| Arm | Factory | Grounding |
|---|---|---|
| `v3` | `4e4dd14`, the commit v3 ran on, from a separate pinned checkout | the `factory-warranty` app's distillations |
| `v4` | `3d12aac`, the round-two commit | the same app build |

20 cases, 2 trials each, in each arm: 80 trials, the arms interleaved in batches of five cases, on a machine kept
awake on mains power. Scoring as in `PASS-MARK.md` and Amendment 1 (outage re-runs); Sol grades bug trials blind to arm.

## What decides it (primary)

Round two **works** if both hold:

1. **Fewer false stops:** of the 24 good-change trials, the `v4` arm stops at most half as many as the `v3` arm
   (rounded down), and at most 5 (about 20%).
2. **No real loss of catches:** of the 8 bug cases, the `v4` arm catches on both trials at least as many as the `v3`
   arm, less one.

Otherwise it **doesn't work**, and the README says so in these words or plainer: "Round two's changes didn't measurably
cut false stops without costing catches."

**Limits, stated before the run:** 12 good changes and 8 bugs are small samples. The test can show a large drop in
false stops; it can't rule out a small loss of catches.

## Reported, not judged

- Review legs that ran out of time, and retries, per arm.
- The severity of every finding that stopped a good change, and whether it named a trigger.
- The share of confirmed findings naming a standard, a source or a library row, per arm.
- Cost per arm: Claude dollars and Codex tokens.

## Amendment 1, 2026-10-16, before any case was picked

Sol's first pick under `pick-v4.md` returned no cases: the brief required exactly one bug from each of the eight
projects, and decimal.js has no unused bug fix within the limits (Sol's explanation named two decimal.js commits it
rejected, so the operator has seen those two subjects; neither is eligible). The brief now asks for the 8 bugs from as
many different projects as can supply one, at most 2 from any one project. The cases, arms and decision rule above
are unchanged; no case had been picked and no trial run.

## Amendment 2, 2026-10-16 15:00 NZDT, after the Codex usage limit, before any affected trial is re-run

Codex's five-hour usage limit ran out during the second batch. Every trial of cases w06–w10 in both arms failed
closed on it, and the once-only re-run under Amendment 1 ran straight into the same limit, so those 20 trials have no
Codex review at all (0 tokens). Counting them would measure the usage limit, equally in both arms. The run was paused
two trials into the third batch (w11-t1 and w12-t1 in the `v3` arm, also outages, not yet re-run).
**Amendment:** a trial whose Amendment 1 re-run also failed closed on an outage is kept in `infra-failures-repeat/`
and run again once the service answers, up to three more times. Before each batch, and before each repeat, the runner
asks Codex for a one-word reply and waits for the limit to reset if it can't. The decision rule, cases and arms are
unchanged. The operator has read no finding or outcome of the affected trials; which trials were flagged as review malfunctions, their Codex token counts
and the usage-limit message are all that was looked at. The results also give the score by Amendment 1 alone, with
each repeat outage counted as a stop or a miss.
