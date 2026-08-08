---
type: Reference
title: Time Value of Money Reference
description: Present-value and future-value conventions for moving single cash flows across time.
resource: https://openstax.org/details/books/principles-finance
tags:
  - finance
  - valuation
  - time-value-of-money
sources:
  - id: openstax-principles-finance
    resource: https://openstax.org/details/books/principles-finance
    title: Principles of Finance
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Time Value of Money

The time value of money states that money available sooner is worth more than the same nominal amount available later because the earlier amount can earn a return.

For a present amount `PV`, periodic rate `r`, and `n` periods:

```text
FV = PV × (1 + r)^n
PV = FV / (1 + r)^n
```

Compounding moves a cash flow forward in time; discounting moves it backward. The factor `(1 + r)^n` includes interest earned on prior interest as well as on the original principal.

## Calculation conventions

- Put every cash flow on a timeline before calculating.
- Match the rate period to the cash-flow period: a monthly rate with months, a quarterly rate with quarters, and an annual rate with years.
- Treat inflows and outflows with consistent signs.
- Use a discount rate appropriate to the cash flow’s timing and risk.
- For multiple unequal cash flows, discount or compound each cash flow from its own date and add the resulting values at a common date.

Time-value calculations underpin bond pricing, stock valuation, capital budgeting, loan amortization, and retirement planning.
