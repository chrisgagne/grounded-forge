---
type: Reference
title: Source-code size units
description: Defines source-line and structural units used to measure software-system size and the scope needed to interpret them.
resource: http://www.knosof.co.uk/ESEUR/
tags:
  - source-code
  - measurement
  - units
  - sloc
sources:
  - id: eseur
    resource: http://www.knosof.co.uk/ESEUR/
    title: Evidence-based Software Engineering based on the publicly available data
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---

Software-system size is often measured in lines of source code (**SLOC**), with **KLOC** or **KSLOC** used for thousands of source lines. Consistency in source layout makes a line a useful approximate unit, but every count needs an explicit scope.

At minimum, record:

- the file types or suffixes counted;
- whether build and configuration files, such as makefiles, are included; and
- the language and revision being measured.

Larger structural units include methods, functions, procedures, subroutines, classes, and files. In many languages a method or function is the smallest self-contained source unit, while classes and files aggregate those units.

SLOC is an approximate size measure, not a direct measure of delivered functionality, developer effort, cost, or defect count. Large variation in the amount of code different developers produce for the same functionality means that size-based comparisons are most credible within the same project team and system, under a consistent counting convention.
