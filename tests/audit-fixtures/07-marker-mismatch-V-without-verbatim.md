---
id: 07-marker-mismatch-V-without-verbatim
failure_mode: Evidence-class marker mismatch ([V] without verbatim text)
severity: correct
expected_finding: "The sentence ending with [V] is a paraphrase, not a direct quotation from the source; either change the marker to [AP] (author paraphrase) or replace the paraphrase with the source's actual wording in quotation marks."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as a deep reference for OpenStax *Organizational Behavior*. One sentence carries a [V] marker without the verbatim text the marker requires; the rest is clean.

---

## Part XIV: Conflict and negotiation (Ch 14)

### Conflict definition and types

The source defines conflict as the process resulting from the tension between team members when their preferred actions or goals are perceived as incompatible [V] (Ch 14.1, "Conflict Definition").

Two functional types are distinguished from one dysfunctional type: process conflict (about how work gets done) and task conflict (about what the work should be) are presented as potentially productive under moderate intensity; relationship conflict (interpersonal animosity) is presented as harmful regardless of intensity [AP] (Ch 14.1, "Types of Conflict").

The source's position is evaluative: managers should not suppress all conflict, but should design conditions that keep conflict in the task and process zones rather than letting it migrate to the relationship zone [AR] (Ch 14.1, "Managing Conflict").

---

**Violation:** the opening sentence ends with `[V]` (verbatim) but is phrased as a paraphrase. There are no quotation marks; the sentence reads like author summary, not author wording. The marker is structurally inconsistent — `[V]` requires verbatim text in quotation marks. Either: (a) change the marker to `[AP]` since the sentence is a paraphrase, or (b) replace the paraphrase with the source's actual wording from Ch 14.1 in quotation marks and keep `[V]`.
