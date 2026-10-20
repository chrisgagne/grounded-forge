# v5 cost probe (development; never scored)

PREREG-v5's cost probe: the factory reviewed one ReviewBench pull request outside the test set (the first full-set
pull request over 1,000 changed lines in manifest order: AgentParadise/agent-paradise-standards-system #61, Rust,
4,575 changed lines, 56 files), on factory `39a96f3`, grounded in the open (17-source) build, 2026-10-19 14:23–14:26.

- Codex meter (read before and after with one-word calls; Plus plan): 5-hour window 7% → 10%, week 2% → 2%.
- Codex tokens recorded (excluding cached input): 70,871. Claude review legs: $1.92.
- 6 findings (3 medium, 3 low).

**Projection under the pre-registered rule.** The week meter reads in whole percent and didn't move. Earlier that day
two Sol runs moved the 5-hour window 7 points and the week 2, so the week moves about 1 point for every 3.5 in the
5-hour window: about 0.9% of a week per pull request like this one. Two trials of 25 would be about 43% of a week,
over the 25% bar, so **part A runs 1 trial per arm**, as PREREG-v5 says.
