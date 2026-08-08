---
type: Reference
title: Capital Budgeting Reference
description: Decision rules for payback, net present value, internal rate of return, and profitability-index project evaluation.
resource: https://openstax.org/details/books/principles-finance
tags:
  - finance
  - capital-budgeting
  - investment
  - valuation
sources:
  - id: openstax-principles-finance
    resource: https://openstax.org/details/books/principles-finance
    title: Principles of Finance
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Capital Budgeting

Capital budgeting evaluates long-lived investments by comparing their expected incremental cash flows with the resources required to obtain them.

For cash flow `CFt`, project discount rate `r`, and initial investment `I0`:

```text
NPV = -I0 + Σ[t=1..n] CFt / (1 + r)^t
```

Accept an independent project when its NPV is positive and reject it when NPV is negative. For mutually exclusive projects, NPV ordinarily selects the project expected to add the most value.

## Other decision rules

- **Payback period**: time required for undiscounted cash inflows to recover the initial investment; it ignores time value and cash flows after payback.
- **Discounted payback period**: time required for discounted inflows to recover the initial investment.
- **Internal rate of return (IRR)**: the discount rate that makes NPV equal zero; accept when IRR exceeds the required return, subject to the method’s reinvestment and multiple-solution limitations.
- **Modified IRR (MIRR)**: compounds cash flows using the cost of capital and produces one solution.
- **Profitability index**: project value per unit of constrained investment; useful when capital is rationed.

Analysis should use incremental after-tax cash flows and a discount rate appropriate to the project’s risk.
