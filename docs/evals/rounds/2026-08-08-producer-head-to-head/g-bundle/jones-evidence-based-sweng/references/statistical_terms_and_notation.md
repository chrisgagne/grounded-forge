---
type: Reference
title: Statistical terms and notation
description: Defines the experimental terminology and mathematical notation used in evidence-based software engineering analysis.
resource: http://www.knosof.co.uk/ESEUR/
tags:
  - statistics
  - probability
  - notation
  - convention
sources:
  - id: eseur
    resource: http://www.knosof.co.uk/ESEUR/
    title: Evidence-based Software Engineering based on the publicly available data
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---

## Experimental terms

- **Group:** another name for a sample.
- **Treatment:** an operation or process performed on subjects.
- **Explanatory variable:** a variable used to explain, predict, or stimulate the value of a response variable. Depending on context, it may also be called an independent, stimulus, predictor, or control variable.
- **Response variable:** a variable believed to respond to or depend on explanatory variables; also called a dependent variable.
- **Truncated data:** values below or above a threshold are unobserved or removed from the dataset.
- **Censored data:** values below or above a threshold are set equal to that threshold.
- **Between-subjects comparison:** samples come from different groups of subjects, often under different experimental conditions.
- **Within-subjects comparison:** samples come from the same subjects, often after those subjects perform tasks under multiple experimental conditions.
- **Parametric test:** a statistical technique that assumes the sample has a known probability distribution.
- **Nonparametric test:** a distribution-free technique that makes no assumption about the sample distribution.

## Notation

- \(n!\) means \(n(n-1)(n-2)\ldots 1\).
- \(\binom{n}{r} = \frac{n!}{r!(n-r)!}\).
- A hat, as in \(\hat{y}\), denotes an estimate of the corresponding value.
- \(\mu\) commonly denotes a mean.
- \(\sigma\) commonly denotes a standard deviation.
- \(n \to \infty\) means that \(n\) becomes arbitrarily large; \(n \to 0\) means that it approaches zero.
- \(P(x)\) denotes the probability of \(x\), while \(P(D \mid S)\) denotes the probability of \(D\) given \(S\).
- Conditional probability is \(P(D \mid S) = \frac{P(D \cap S)}{P(S)}\).
- \(\prod_{i=1}^{n} a_i\) denotes a product, and \(\sum_{i=1}^{n} a_i\) denotes a sum.

The probabilities of all mutually exclusive outcomes of an action sum to one. If events \(D\) and \(S\) are independent, then \(P(D \cap S)=P(D)P(S)\).

A function is **convex** on an interval when every chord between points on the function lies above it; it is **concave** when every such chord lies below it.
