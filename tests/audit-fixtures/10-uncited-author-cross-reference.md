---
id: 10-uncited-author-cross-reference
failure_mode: Cross-reference to an author the source does not cite
severity: strip
expected_finding: "The connections bullet attributing transformational leadership to Bass with a [BT] marker fails the trace test — the source's leadership chapter discusses transformational vs transactional leadership without naming Bass or Burns; strip the [BT] attribution, keep [AP] for the framework itself."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as a deep reference for OpenStax *Organizational Behavior*. The "Connections" section of a deep ref records [BT] citation chains where the source itself names another author. One bullet here records a chain the source does not in fact make; the rest is clean.

---

## Connections to other authors and frameworks

The text repeatedly intersects with named authors elsewhere in the corpus:

- *Hofstede's cultural dimensions*: cited extensively in Ch 2.6 as the framework for cross-cultural analysis of work behaviour [BT].
- *Maslow's hierarchy*: cited in Ch 7.2 as a foundational motivation framework that the text then qualifies as not strictly supported by research [BT].
- *Bass's transformational leadership*: cited in Ch 11.4 as the framework distinguishing inspirational, charismatic leadership from transactional exchange-based leadership [BT].
- *French and Raven's five bases of power*: cited in both Ch 12.3 and Ch 13.1 as the canonical taxonomy of power sources [BT].

---

**Violation:** the third bullet attributes the transformational/transactional distinction to Bass with a `[BT]` marker. The source's leadership chapter (Ch 11.4) discusses these two leadership styles as named constructs but does not cite Bass or Burns by name. The ingester knows from training data that Bass formalised transformational leadership; the source does not record that connection. Strip the Bass attribution. Either rewrite the bullet to describe the framework without naming an originator (and keep the marker as `[AP]` since the framework as a framework is the source's paraphrase), or drop the bullet entirely if it adds nothing without the attribution.
