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

The limits stated before the run still apply: 17 bug cases is a small sample, so a difference of 5 can't rule out
chance, and two trials per case is an easier bar than three.

## Secondary measures (descriptive, no pass mark)

| | No corpus | Corpus |
|---|---|---|
| Bug trials caught | 27 / 34 (79%) | 32 / 34 (94%) |
| Bug trials surfaced to the signer | 28 / 34 (82%) | 32 / 34 (94%) |
| Bug cases caught in at least one trial | 16 / 17 | 16 / 17 |
| Control trials with a false alarm | 6 / 16 (38%) | 7 / 16 (44%) |
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

## What this does and doesn't show

- It shows that, on these 17 real bugs, reviewers given the corpus caught more of them reliably than the same
  reviewers without it, and cited a standard or source in two thirds of their confirmed findings (none did without).
- It costs more: about 2.4 times the Claude review spend and 1.7 times the Codex tokens.
- It doesn't show the factory meets its own false-alarm bar: about four clean changes in ten were stopped, in both
  arms. A signer would spend real time clearing them.
- The gate's semgrep step should pin its registry ruleset so it gives the same answer twice (PROPOSED).
