---
id: 05-apostrophe-style-control
failure_mode: None (control: apostrophe and quote-mark style)
severity: none
expected_finding: "No violation. The blockquote's straight apostrophes stand where the source prints curly ones; apostrophe and quote-mark style is typography, not the author's words, so the quotation is verbatim. The auditor should not flag it."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt, clean except for apostrophe style)

The following is an excerpt styled as a deep reference for OpenStax *Organizational Behavior*. Its one blockquote is the source's sentence word for word, with straight apostrophes (ASCII 0x27) where the converted source has curly ones (U+2019). Pass I should read it and produce no findings. An auditor that flags the apostrophes is over-flagging: correcting them changes no word, letter, case or punctuation mark of the author's.

---

## Part VII: Work motivation (Ch 7)

### Expectancy theory: weak effort-performance expectancies

The text gives two reasons employees develop weak effort-performance expectancies (E1s): they lack the internal or external resources to perform, or the organisation fails to measure performance accurately [AP] (Ch 7.3, "Expectancy Theory").

On inaccurate measurement, the text puts the problem plainly:

> "That is, performance ratings don't correlate well with actual performance levels."

(Ch 7.3, "Expectancy Theory")

---

**Violation:** none. The quotation matches the source's words, case and punctuation; only the apostrophe glyph differs. `scripts/check-verbatim.py` reports it as `apostrophe`, which does not fail the check.
