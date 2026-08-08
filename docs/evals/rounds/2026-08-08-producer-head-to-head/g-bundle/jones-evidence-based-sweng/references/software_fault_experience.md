---
type: Reference
title: Software fault experience
description: Defines a software fault experience as the interaction of an implementation mistake with activating program input.
resource: http://www.knosof.co.uk/ESEUR/
tags:
  - software-reliability
  - fault
  - terminology
sources:
  - id: eseur
    resource: http://www.knosof.co.uk/ESEUR/
    title: Evidence-based Software Engineering based on the publicly available data
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---

A software fault experience requires two events:

1. A mistake exists in the software.
2. The program processes input that executes the affected code in a way that makes the fault observable.

This separates a latent implementation mistake from an experienced fault. A program can contain many mistakes yet appear reliable when typical input does not activate them; a program with few mistakes can appear unreliable when those mistakes are activated frequently.

The likelihood of a fault experience therefore depends on both the mistakes present and the operational input distribution. More users generally increase the volume and variety of input, the pool of possible reporters, and consequently the number of reported faults.

A fault report is evidence of a reported experience, not a one-to-one count of underlying mistakes. Reports may be duplicated, omit experiences that were never submitted, or describe enhancement requests rather than faults. Reliability comparisons based on reports should account for usage volume, input diversity, reporting practices, and the possibility that multiple reports trace to the same mistake.
