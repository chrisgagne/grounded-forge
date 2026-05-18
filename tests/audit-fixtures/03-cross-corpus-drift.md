---
id: 03-cross-corpus-drift
failure_mode: Cross-corpus drift
severity: strip
expected_finding: "The sentence connecting equity theory to Kahneman and Tversky's loss-aversion finding makes a cross-corpus connection; the source does not cite Kahneman or Tversky — strip it, the deep ref records what this source cites, not what the ingester knows from other corpus entries."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as a deep reference for OpenStax *Organizational Behavior*. One sentence draws a connection to an author not cited in this source; the rest is clean.

---

## Part VII: Motivation (Ch 7)

### Equity theory and restorative behaviours

Adams's equity theory proposes that individuals compare their input/output ratio to a referent other's ratio and experience tension when the ratios are unequal [AP] (Ch 7.3, "Equity Theory of Motivation"). Under-reward inequity motivates upward restoration; over-reward inequity motivates downward restoration, though the text notes the latter is less common in practice [AR] (Ch 7.3).

Six restorative behaviours are catalogued: altering inputs, altering outcomes, cognitively distorting one's own inputs or outcomes, cognitively distorting the referent's inputs or outcomes, changing the referent, and leaving the field [AP] (Ch 7.3, "Restoring Equity").

The asymmetry between under- and over-reward responses aligns with Kahneman and Tversky's loss-aversion finding — that losses loom larger than equivalent gains — though this connection is the ingester's synthesis; the source does not cite Kahneman or Tversky anywhere in the chapter.

---

**Violation:** the final sentence draws a connection between Adams's equity theory and Kahneman and Tversky's prospect-theory work. The source does not cite Kahneman or Tversky. This is cross-corpus drift: the ingester knows from other corpus entries that loss aversion connects to equity asymmetry, but this source does not make that connection. Strip the sentence.
