---
type: Reference
title: Fuzzy Cognitive Map Parameters
description: Defines Fuzzy Cognitive Map factors, edge weights, and the distinct parameter semantics of causal and dynamical analysis.
resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
tags:
  - fuzzy-cognitive-mapping
  - parameters
  - causal-model
  - glossary
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
sources:
  - id: barbrook-johnson-systems-mapping-2022
    resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
    title: "Systems Mapping: How to Build and Use Causal Models of Systems"
---

# Map fields

- **Factor or concept:** A variable-like node for which an increase or decrease is meaningful. It need not be directly quantifiable or backed by empirical data.
- **Edge:** A directed, direct causal influence between factors.
- **Factor value:** A numerical value assigned to a factor for analysis; its meaning depends on the analysis approach.
- **Edge weight:** A signed numerical value assigned to a causal link; both its magnitude and interpretation depend on the analysis approach.
- **Weight matrix:** A matrix with factors as both rows and columns and edge weights in the cells for connected factor pairs.

# Causal approach

In a causal Fuzzy Cognitive Map:

- Edge values are constrained to the interval `[-1, 1]`.
- Edge magnitude represents certainty that the causal link exists; a magnitude of `1` means certainty.
- Edge sign distinguishes positive causation from suppression.
- Factor values are constrained to `[0, 1]`, or sometimes `[-1, 1]`, and represent how strongly a factor is caused or activated.
- On a `[0, 1]` scale, `0` means not activated, `1` means fully activated, and `0.5` represents maximum ambiguity.

The analysis asks whether changing something in the system makes other factors more or less strongly caused.

# Dynamical approach

In a dynamical Fuzzy Cognitive Map:

- Factor values may take any real value.
- Edge weights may take any real value but are commonly kept in `[-1, 1]` or expressed as weak, medium, and strong.
- Edge magnitude represents the strength of the effect: for example, with a source value of `1`, a weight of `+0.5` increases the target by `0.5`, while `-0.3` decreases it by `0.3`.
- Most factors are commonly initialised at `0`; a driver or factor being changed may be initialised at `1` or less.

Repeated matrix updates propagate changes until values stabilise or enter a repeating cycle. These updates are iterations, not observations through time, so the output should not be interpreted as a time-based simulation.
