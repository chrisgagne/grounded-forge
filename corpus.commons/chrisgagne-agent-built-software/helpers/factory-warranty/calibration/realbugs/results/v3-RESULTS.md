# Replay v3 results: does the corpus help the reviewers?

Pre-registered in `../PREREG-v3-grounding.md` (`457abd9`) before any case was picked; cases `../v3-cases.json`
(`42d52a3`), picked by Sol and committed before any trial; scoring script `../compare_v3.py` (`390f2e2`), committed
before any trial was graded. Run 2026-10-15 17:50 to 2026-10-16 09:05 on factory `4e4dd14` (later commits touch docs
only), the corpus arm reading the `factory-warranty` app built from grounded-forge `77c6c4d1`. 25 cases (17 bug, 8
control), 2 trials each, in each arm, the arms interleaved in batches of five cases. Graded blind by Sol (gpt-6.1-sol)
against each bug's fix. Reported as it stands.

## The pre-registered test

| | No corpus (`none`) | Corpus (`distillations`) | Difference | Rule |
|---|---|---|---|---|
| Bug cases caught every time (2 of 2) | 11 / 17 | 16 / 17 | +5 | +3 or more |
| Control cases with a false alarm in any trial | 3 / 8 | 4 / 8 | +1 | at most +1 |

**Criterion (a) is met.** With the corpus, the reviewers caught 5 more of the 17 real bugs on both trials, and flagged
one more clean change. The +1 on controls is the most the rule allows, and that one extra case was a gate flake, not
the review (below).

**How much of the +5 rests on review malfunctions.** Three of the five extra cases (v10, v11, v14) are ones where the
no-corpus arm caught the bug on one trial, and on the other its review leg malfunctioned (the Codex reviewer ran past
its 30-minute limit and was killed, so the factory failed closed and stopped the change without naming the defect). All three review malfunctions on bug trials
fell in the no-corpus arm; the corpus arm had none. Scored as registered, a malfunction is not a catch, and the
criterion is met. Counting only reviews that completed, the corpus arm caught 16 of 17 on every completed review and
the no-corpus arm 14 of 17: a difference of 2, which would not meet the +3 rule. Whether the corpus makes a review leg
less likely to malfunction, or the three fell on that arm by chance, these 100 trials can't say. This count is descriptive,
not the registered rule: it lets three no-corpus cases qualify on one completed review while every corpus case needed
two.

The limits stated before the run still apply: 17 bug cases is a small sample, so a difference of 5 can't rule out
chance, and two trials per case is an easier bar than three.

## Secondary measures (descriptive, no pass mark)

| | No corpus | Corpus |
|---|---|---|
| Bug trials caught | 27 / 34 (79%) | 32 / 34 (94%) |
| Bug trials surfaced to the signer | 28 / 34 (82%) | 32 / 34 (94%) |
| Bug cases caught in at least one trial | 16 / 17 | 16 / 17 |
| Control trials with a false alarm | 6 / 16 (38%) | 7 / 16 (44%) |
| Review malfunctions (bug trials / control trials) | 3 / 2 | 0 / 1 |
| Confirmed findings citing a standard, a corpus source or an axis row | 0 of 64 (0%) | 56 of 82 (68%) |
| Errored trials / grader errors | 0 / 0 | 0 / 0 |
| Outage re-runs (Amendment 1) | 1 | 2 |
| Claude review legs | $13.27 | $32.00 |
| Codex review tokens | 1,236,563 | 2,112,700 |

Against pass mark v2 (PROPOSED; pass^k read at k = 2, which doesn't compare directly with three-trial runs): the
corpus arm meets the two catch measures (94% of trials, 94% of cases every time) and misses the surfacing measure by a
hair (94% against 95%); neither arm meets the false-alarm measures (38% and 44% of control trials against at most 20%).

## What the false alarms were

The same three control cases were flagged in both arms, so they are not the corpus's doing:

- **v04 (decimal.js), both trials, both arms:** the reviewers confirmed that the change edits the source but not the
  committed minified build, which still behaves the old way. A real inconsistency, scored as a false alarm because the
  case was picked as a clean change.
- **v05 (node-semver), both arms:** a new file left out of the package's published-file list, rated high and
  confirmed.
- **v12 (js-yaml), both arms:** the reviewers read the change's removed checks as a regression, rated high.

Three trials failed closed on a malfunctioning review leg (v05 t2 in both arms, v12 t1 without the corpus). One trial in
the corpus arm (v17 t1, markdown-it) was blocked by the gate's semgrep ratchet, not by review: a deterministic gate that
behaved differently across runs, most likely because the registry ruleset (`p/default`) is fetched fresh each run. That
is the one extra control case in the corpus arm.

The fresh-controls run of 2026-10-14 had no false alarms on 12 different controls. Whether v04, v05 and v12 are
reviewers being too strict or real problems the projects later fixed out of view, these results don't say; they are
scored as the pre-registration says.

## What the malfunctions were (found after the results, 2026-10-16)

Every review malfunction in v3 was the Codex reviewer killed at the review stage's 30-minute limit (`killed after 30
min` in each run's ledger, 0 Codex tokens recorded): five of 50 trials without the corpus (v05 t2, v10 t2, v11 t2,
v12 t1, v14 t2) and one of 50 with it (v05 t2). Long Codex legs cluster in the same arm: 11 of the no-corpus legs ran
10 minutes or more, against 4 with the corpus, from the leg durations in each run's ledger. A reading consistent with
this, not tested here: with the corpus the reviewer gets a focused packet and finishes sooner; without it, it explores
the repository and runs out of time. Whether a longer limit would have let the no-corpus arm catch v10, v11 and v14 on
both trials, these runs can't say. The outage rule (Amendment 1) doesn't cover a timeout, so these stay scored.

## What this does and doesn't show

- The cases are small, reverted logic fixes and clean changes in eight JavaScript and TypeScript libraries, with the
  projects' own test suites replaced by a passing stub: it measures the review stage, not the whole factory.
- Catches are graded by a model (Sol), blind to arm and severity; no human has checked the grader against human
  judgement. Sol also picked the cases and is one of the two reviewers.
- It shows that, on these 17 real bugs, reviewers given the corpus caught more of them reliably than the same
  reviewers without it, and cited a standard or source in two thirds of their confirmed findings (none did without).
- It costs more: about 2.4 times the Claude review spend and 1.7 times the Codex tokens.
- It doesn't show the factory meets its own false-alarm bar: about four clean changes in ten were stopped, in both
  arms. A signer would spend real time clearing them.
- The gate's semgrep step should pin its registry ruleset so it gives the same answer twice (PROPOSED).
