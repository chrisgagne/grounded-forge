---
type: Reference
title: System Dynamics Stock-and-Flow Conventions
description: Defines the model elements, diagram notation, and model-assessment terms used in System Dynamics.
resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
tags:
  - system-dynamics
  - stock-and-flow
  - notation
  - glossary
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
sources:
  - id: barbrook-johnson-systems-mapping-2022
    resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
    title: "Systems Mapping: How to Build and Use Causal Models of Systems"
---

# Model elements

- **Stock:** A numerical entity that accumulates or depletes over time.
- **Flow:** The rate of change in a stock, usually represented by a differential equation.
- **Influencing factor:** A variable or parameter that affects a flow equation.
- **Initial value:** A stock’s value at the simulation’s starting point.
- **Time step:** One repeated computation in which flow equations change stock values.
- **Scenario:** A change to model equations, parameters, or structure intended to represent an intervention or a different system condition.

# Diagram notation

Common stock-and-flow diagrams use:

- rectangles for stocks;
- straight hollow arrows with valve-like symbols for flows;
- text labels for factors that affect flows;
- solid, often curved arrows for influences on flows;
- `R` for a reinforcing feedback loop; and
- `B` for a balancing feedback loop.

# Model-assessment terms

- **Parameterisation:** Choosing model parameter values from data or values that are plausible to system experts.
- **Calibration:** Choosing parameter values so the model reproduces a target pattern or output.
- **Validation:** Assessing how well the model reproduces target outputs; this often overlaps with calibration.
- **Sensitivity analysis:** Systematically changing parameters or structural components to assess how sensitive model outputs are to them.

These activities can be performed informally and qualitatively or through more technical quantitative procedures.
