---
type: Reference
title: UML Sequence Diagram Notation
description: A glossary of common notation used to show interactions among sequence-diagram participants.
resource: https://open.oregonstate.education/setextbook/
tags:
  - uml
  - sequence-diagrams
  - notation
  - glossary
sources:
  - id: handbook-of-software-engineering-methods
    resource: https://open.oregonstate.education/setextbook/
    title: Handbook of Software Engineering Methods
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Elements

- **Participant** — a column representing an object, user, database, or other entity involved in the interaction.
- **Lifeline** — a vertical dashed line representing the participant's lifespan, with time progressing downward.
- **Message** — a solid line with an arrow showing an interaction from one participant to another, often a method call.
- **Activation bar** — a box on a lifeline showing when the participant is active, such as when a method is on the call stack.
- **Return** — a dashed line with an arrow showing a method return; include it when it communicates important information.
- **Self-call** — a solid message arrow that returns to the sender's own lifeline.
- **Deletion** — an `X` on the lifeline marking the end of the participant's life.
