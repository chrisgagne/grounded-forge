---
type: Reference
title: Causal Loop Diagram Notation
description: Defines the variables, causal-link polarities, feedback-loop labels, and delay marks used in Causal Loop Diagrams.
resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
tags:
  - causal-loop-diagram
  - feedback
  - notation
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
sources:
  - id: barbrook-johnson-systems-mapping-2022
    resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
    title: "Systems Mapping: How to Build and Use Causal Models of Systems"
---

# Elements

- **Variable:** A node expressed as something that can increase or decrease along a meaningful scale.
- **Causal link:** A directed edge representing influence from one variable to another.
- **Feedback loop:** A closed chain of causal links. Feedback loops are the method’s organising structure and are made conspicuous in the map.
- **Core system engine:** The set of central variables and feedbacks treated as the system’s main driver.

# Link polarity

- **Positive (`+`) or same-direction (`s`) link:** The source and target change in the same direction: an increase in the source tends to increase the target, while a decrease tends to decrease it.
- **Negative (`-`) or opposite-direction (`o`) link:** The source and target change in opposite directions: an increase in the source tends to decrease the target, and vice versa.

Polarity describes the direction of causal influence, not whether a change is desirable.

# Loop and delay marks

- **`R`:** Reinforcing feedback loop.
- **`B`:** Balancing feedback loop.
- **`//` on a link:** A time delay in the causal influence.

Curved arrows, colour, and small polarity symbols may also be used to make feedback loops visible.
