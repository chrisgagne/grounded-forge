---
type: Reference
title: Cost Classification and Behavior Reference
description: Defines the principal managerial-accounting cost classifications, behavior patterns, and mixed-cost estimation conventions.
resource: https://openstax.org/details/books/principles-managerial-accounting
tags:
  - managerial-accounting
  - costs
  - cost-behavior
  - glossary
sources:
  - id: openstax-principles-managerial-accounting
    resource: https://openstax.org/details/books/principles-managerial-accounting
    title: "Principles of Accounting, Volume 2: Managerial Accounting"
generated: {by: web-ingestion-instruction/gpt-5.6-sol}
---
# Behavior Patterns

- **Fixed cost:** remains constant in total within the relevant range, while fixed cost per unit falls as activity rises.
- **Variable cost:** remains constant per unit within the relevant range, while total variable cost changes in direct proportion to its cost driver.
- **Mixed cost:** contains both fixed and variable components.
- **Stepped cost:** remains constant over a band of activity, then changes when activity crosses the band’s relevant range.
- **Relevant range:** the bounded activity interval within which the assumed cost behavior is valid.

For a linear mixed cost:

```text
Y = a + bX
```

where `Y` is total cost, `a` is total fixed cost, `b` is variable cost per unit of activity, and `X` is the activity level.

# Traceability and Financial-Reporting Classifications

- **Direct materials:** material inputs that can be economically traced to a product or service.
- **Direct labor:** labor that can be economically traced to producing the product or service.
- **Manufacturing overhead:** production costs that are not economically traceable as direct materials or direct labor, including indirect materials, indirect labor, factory utilities, and factory depreciation.
- **Product costs:** direct materials, direct labor, and manufacturing overhead; these attach to manufactured inventory.
- **Period costs:** costs associated with a period rather than production of an asset, including many selling and administrative costs.
- **Prime costs:** direct materials plus direct labor.
- **Conversion costs:** direct labor plus manufacturing overhead.

A cost’s classification depends on the decision being made. The same expenditure can, for example, be fixed for cost-behavior analysis and a period cost for financial reporting.

# Per-Unit Measures

```text
Average fixed cost = Total fixed costs / Units produced
Average variable cost = Total variable costs / Units produced
Total cost = Total fixed costs + Total variable costs
```

# High-Low Estimation

Use the observations with the highest and lowest **activity levels**, not necessarily the highest and lowest costs:

```text
b = (Cost at high activity − Cost at low activity)
    / (High activity − Low activity)

a = Total cost − (b × Activity)
```

The high-low method assumes a linear relationship and uses only two observations. A scatter graph can test whether a linear relationship is plausible; least-squares regression uses all observations and generally provides a more precise estimate.
