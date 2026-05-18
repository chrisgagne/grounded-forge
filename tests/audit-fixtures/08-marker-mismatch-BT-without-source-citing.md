---
id: 08-marker-mismatch-BT-without-source-citing
failure_mode: Evidence-class marker mismatch ([BT] without source citing the other author)
severity: correct
expected_finding: "The sentence attributing the Hawthorne studies to Mayo carries a [BT] (borrowed-through) marker, but the source does not cite Mayo — change the marker to [AP] (author paraphrase) or strip the Mayo attribution; [BT] requires the source itself to cite the named author."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as a deep reference for OpenStax *Organizational Behavior*. One sentence carries a `[BT]` marker that the source does not earn; the rest is clean.

---

## Part I: The nature of work and management (Ch 1)

### Origins of organisational behaviour as a field

The text traces organisational behaviour to the human-relations movement of the 1920s and 1930s, framing it as a corrective to the engineering-led scientific management of the prior generation [AP] (Ch 1.2, "Origins of Organizational Behavior").

The Hawthorne studies at Western Electric — productivity changes that persisted across both improved and worsened lighting conditions — are presented as the empirical anchor of the human-relations turn, with the studies attributed to Elton Mayo and his Harvard collaborators [BT] (Ch 1.2, "The Hawthorne Studies").

The text positions Mary Parker Follett as a contemporaneous voice who anticipated many of the human-relations themes from a management-theory angle rather than an experimental one [AP] (Ch 1.3, "Mary Parker Follett").

---

**Violation:** the second paragraph attributes the Hawthorne studies to Mayo with a `[BT]` (borrowed-through) marker. `[BT]` is the marker for "this source cites another author, and the deep ref records the citation chain." But the source does not name Mayo — it refers to "researchers at Western Electric" and to "the Hawthorne studies" without naming the lead investigator. The Mayo attribution is ingester knowledge, not source-cited material. Either: (a) strip the Mayo name and keep `[AP]` since the studies-without-naming is what the source actually says, or (b) confirm by re-checking the source whether Mayo is in fact named somewhere in Ch 1.2 and re-anchor the citation precisely.
