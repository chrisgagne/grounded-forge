---
id: 05-verbatim-smart-quote-tidy
failure_mode: Verbatim accuracy slip (smart-quote substitution)
severity: correct
expected_finding: "The blockquoted passage replaces the source's straight apostrophe in 'don't' with a curly apostrophe; restore the straight apostrophe to match the source exactly — verbatim means verbatim."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as a deep reference for OpenStax *Organizational Behavior*. One blockquote has a single-character typographic substitution introduced during Pass D; the rest is clean.

---

## Part VIII: Performance appraisal (Ch 8)

### Rater errors in performance evaluation

The text identifies five systematic rater errors that distort performance ratings: central tendency (rating everyone near the midpoint), strictness (rating everyone low), halo (allowing one strong trait to inflate all ratings), recency (over-weighting recent events), and personal bias [AP] (Ch 8.1, "Rater Errors").

The source gives a concrete example of halo error operating in reverse — the "horns effect" — where one observed failing contaminates ratings on unrelated dimensions (Ch 8.1). The practical implication is that appraisers should rate each dimension independently before comparing across dimensions [AR] (Ch 8.1).

On strictness bias, the text quotes a supervisor's reported reasoning:

> "I don’t give high ratings because I don’t want people to think they can stop trying."

This sentence appears at Ch 8.1, "Strictness Bias". The source uses straight apostrophes (ASCII 0x27); the blockquote above carries curly apostrophes (U+2019) introduced during Pass D typographic tidying.

---

**Violation:** the blockquote contains curly right-single-quotation-mark characters (U+2019) in both instances of "don't" where the source has straight ASCII apostrophes (0x27). Pass D's procedure requires character-by-character verification against the source. This is the kind of smart-quote substitution the failure-mode reference lists explicitly. Correct the characters; do not strip the quote.
