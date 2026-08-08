---
type: Reference
title: Standard Cost Variances Reference
description: Defines the direct-materials, direct-labor, and variable-overhead variance formulas and their interpretation.
resource: https://openstax.org/details/books/principles-managerial-accounting
tags:
  - managerial-accounting
  - standard-costing
  - variance-analysis
  - cost-control
sources:
  - id: openstax-principles-managerial-accounting
    resource: https://openstax.org/details/books/principles-managerial-accounting
    title: "Principles of Accounting, Volume 2: Managerial Accounting"
generated: {by: web-ingestion-instruction/gpt-5.6-sol}
---
# Notation

- `AP`, `SP`: actual and standard input price.
- `AQ`, `SQ`: actual input quantity and standard quantity allowed for actual output.
- `AR`, `SR`: actual and standard labor or overhead rate.
- `AH`, `SH`: actual hours and standard hours allowed for actual output.

With the formulas below, a positive amount is normally unfavorable and a negative amount favorable; reports often present the absolute amount with an `F` or `U` label.

# Direct Materials

```text
Materials price variance
  = AQ purchased × (AP − SP)

Materials quantity variance
  = SP × (AQ used − SQ allowed)

Total direct materials cost variance
  = Materials price variance + Materials quantity variance
```

The price variance is normally recognized at purchase. The quantity variance compares material actually used with the standard amount allowed for the actual output.

# Direct Labor

```text
Labor rate variance
  = AH × (AR − SR)

Labor time variance
  = SR × (AH − SH)

Total direct labor variance
  = Labor rate variance + Labor time variance
```

The rate variance isolates the wage-rate difference for actual hours. The time variance isolates the effect of using more or fewer hours than the standard allowed.

# Variable Manufacturing Overhead

```text
Variable overhead rate variance
  = AH × (Actual variable-overhead rate − Standard variable-overhead rate)

Variable overhead efficiency variance
  = Standard variable-overhead rate × (AH − SH)

Total variable overhead cost variance
  = Rate variance + Efficiency variance
```

The rate variance is also called the spending variance. The efficiency variance reflects use of the allocation base, not necessarily physical efficiency in consuming each overhead item.

# Fixed Manufacturing Overhead

Fixed-overhead analysis compares actual fixed overhead with budgeted and applied fixed overhead. Because total fixed cost does not change with activity within the relevant range, a production-volume difference changes the fixed overhead applied per unit even when total fixed spending is unchanged.

# Interpretation

A favorable variance is not automatically beneficial and an unfavorable variance is not automatically harmful. Lower-priced inputs can cause excess usage, faster labor can require higher wages, and production beyond demand can make overhead application look favorable while creating excess inventory. Variances should be investigated together with operating causes, quality, capacity, and controllability.
