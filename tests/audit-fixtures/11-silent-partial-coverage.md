---
id: 11-silent-partial-coverage
failure_mode: Silent partial coverage
severity: flag-and-escalate
expected_finding: "The deep ref's coverage of Ch 17-19 is conspicuously thinner than Ch 1-16, with no Pass A note explaining the gap; this looks like silent partial coverage — escalate to Pass A re-check, do not ship until the gap is either filled or labelled explicitly as partial in the deep ref's source/structure block."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as the closing parts of a deep reference for OpenStax *Organizational Behavior*. Earlier parts (I–XV) cover their chapters in 30–50 lines each. Parts XVI–XIX here collapse into stub-length coverage with no labelled gap. The violation is the absence of a partial-coverage flag, not the brevity itself.

---

## Part XVI: Performance management systems (Ch 16)

The text discusses several performance-management practices in this chapter, including 360-degree feedback, calibration meetings, and the shift away from forced ranking [AP] (Ch 16).

## Part XVII: Organisational change (Ch 17)

The chapter on organisational change covers Lewin's three-stage model and discusses resistance to change [AP] (Ch 17).

## Part XVIII: Stress and well-being (Ch 18)

This chapter addresses workplace stress and its consequences [AP] (Ch 18).

## Part XIX: Entrepreneurship (Ch 19)

The closing chapter introduces entrepreneurship as a topic relevant to organisational behaviour [AP] (Ch 19).

---

**Violation:** Parts I–XV of the deep ref (not shown in this excerpt) average 30–50 lines per chapter; Parts XVI–XIX collapse to 1–2 sentences per chapter and lose all section-level citation, evidence markers, and detail. There is no Pass A note in the deep ref's source/structure block flagging that Ch 17–19 were skimmed rather than deep-read, no `PARTIAL:` label, no record of which sections were skipped. This is silent partial coverage — the audit must reject downstream artefacts that inherited the gap. Escalate to Pass A re-check: either re-ingest Ch 16–19 properly, or amend the source/structure block to label the coverage as partial and constrain downstream consumers accordingly.
