---
id: 09-verbatim-quote-in-distillation
failure_mode: Verbatim quote in distillation (cross-tier leak)
severity: strip
expected_finding: "The distillation embeds a verbatim blockquote from the source; distillations paraphrase and link back to the deep reference rather than duplicate verbatim text — replace the blockquote with a paraphrase and a link to the corresponding section of the deep ref."
seed_source: openstax-organizational-behavior
tier: distillation
---

# Fixture body (distillation excerpt with one violation)

The following is a synthetic excerpt styled as a decision-making distillation for OpenStax *Organizational Behavior*. Distillations (Pass G outputs) paraphrase; blockquotes belong in the deep reference. One block here duplicates a verbatim quote that should be linked instead.

---

## When to reach for this source

A team has experienced a sharp drop in cohesion after a re-org. The decision in front of the manager is whether to intervene directly in interpersonal dynamics or to redesign the work itself. The text's framing helps clarify which lever is likely to move outcomes.

## What the source contributes

The chapter on conflict offers a distinction between *task conflict* (productive at moderate intensity), *process conflict* (productive when surfaced early), and *relationship conflict* (harmful regardless of intensity). The practical guidance: design conditions that keep conflict in the task and process zones.

The text takes a strong evaluative stance on relationship conflict:

> "Relationship conflict, unlike task and process conflict, tends to corrode the trust that teams depend on, and high-performing teams maintain low levels of it regardless of the intensity of their other disagreements."

This blockquote appears verbatim at Ch 14.1 in the deep reference (see [openstax-organizational-behavior-deep.md](../../corpus.commons/demo/references/openstax-organizational-behavior-deep.md) Part XIV).

## Diagnostic questions

- Is the observed conflict about *what* the team is doing (task), *how* they are doing it (process), or *who they are to each other* (relationship)?
- Which lever — work redesign, role clarification, or relational repair — addresses the dominant mode?

---

**Violation:** the distillation embeds a verbatim blockquote from the source. The failure-mode reference is explicit: "Distillations paraphrase. Blockquotes belong in the deep reference where Pass D exactness verification has run. If the distillation needs the source's own words, link back to the deep ref instead of duplicating." Strip the blockquote; replace with a paraphrase of the evaluative claim ("the text treats relationship conflict as corrosive regardless of intensity") and keep the link to the deep ref section.
