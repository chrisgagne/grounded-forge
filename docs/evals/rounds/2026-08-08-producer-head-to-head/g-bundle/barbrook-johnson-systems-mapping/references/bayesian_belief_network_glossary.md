---
type: Reference
title: Bayesian Belief Network Glossary
description: Defines the structural and probability terms used in Bayesian Belief Networks.
resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
tags:
  - bayesian-belief-network
  - probability
  - glossary
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
sources:
  - id: barbrook-johnson-systems-mapping-2022
    resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
    title: "Systems Mapping: How to Build and Use Causal Models of Systems"
---

# Structure

- **Node:** A variable, factor, or outcome in the system.
- **State:** One of the values a node can take, such as on or off, high or low, or present or absent. A node’s states should be mutually exclusive and collectively exhaustive.
- **Edge:** A directed causal relationship between nodes.
- **Parent node:** A node with an arrow into another node. The target node’s state probabilities are conditional on the states of its parents.
- **Root node:** A node with no incoming arrows.
- **Child node:** A node receiving an arrow from a parent.
- **Acyclic network:** A directed network with no cycles or feedback loops. Standard Bayesian Belief Networks require this structure.

# Probabilities

- **Conditional probability:** The likelihood that a node takes a particular state given the states of its parent nodes.
- **Conditional probability table:** A table containing a node’s probability distribution for every combination of its parents’ states.
- **Prior probability distribution:** The best estimate of a node’s state probabilities before new evidence or data is considered. Root-node state distributions are priors because they have no incoming conditional information.
- **Posterior probability distribution:** The conditional probability distribution after new evidence or data has been taken into account.

# Practical constraints

Participatory Bayesian Belief Networks commonly limit a node to two or three parents and a small number of states. These are practical elicitation limits: the number of conditional-probability entries grows rapidly as parent nodes and states are added.

A dynamic Bayesian Belief Network can partially represent feedback by creating separate nodes for the same factor at different time points while keeping the overall graph acyclic.
