---
id: 06-verbatim-capitalisation-tidy
failure_mode: Verbatim accuracy slip (capitalisation tidying)
severity: correct
expected_finding: "The blockquoted passage capitalises 'Behavior' mid-sentence to match the deep ref's surrounding prose; the source uses lowercase 'behavior' there — restore the source's lowercase to keep the quote verbatim."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as a deep reference for OpenStax *Organizational Behavior*. One blockquote has a capitalisation change introduced during Pass D; the rest is clean.

---

## Part IV: Learning and reinforcement (Ch 4)

### Reinforcement schedules

The text catalogues four partial reinforcement schedules — fixed interval, fixed ratio, variable interval, variable ratio — and reports that performance-contingent schedules outperform time-contingent schedules across all four conditions [AP] (Ch 4.2, "Schedules of Reinforcement").

The text takes a clear position on the relative effectiveness of the schedules. From Ch 4.2:

> "The performance-contingent (or ratio) reward schedules generally lead to better Behavior than the time-contingent (or interval) schedules, regardless of whether such schedules are fixed or variable."

This sentence appears at Ch 4.2 ("Schedules of Reinforcement"). The source uses lowercase "behavior"; the blockquote above has been capitalised to "Behavior" to match the surrounding section heading style. Pass D requires verbatim preservation.

---

**Violation:** the blockquote capitalises "Behavior" mid-sentence. The source uses lowercase "behavior" at that position. Capitalisation tidying is a Pass D failure mode listed explicitly in the failure-mode reference. Correct the case; do not strip the quote.
