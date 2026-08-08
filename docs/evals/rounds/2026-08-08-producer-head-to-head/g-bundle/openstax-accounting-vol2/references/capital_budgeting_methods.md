---
type: Reference
title: Capital Budgeting Methods Reference
description: Defines payback, accounting rate of return, net present value, profitability index, and internal rate of return methods.
resource: https://openstax.org/details/books/principles-managerial-accounting
tags:
  - managerial-accounting
  - capital-budgeting
  - discounted-cash-flow
  - investment-analysis
sources:
  - id: openstax-principles-managerial-accounting
    resource: https://openstax.org/details/books/principles-managerial-accounting
    title: "Principles of Accounting, Volume 2: Managerial Accounting"
generated: {by: web-ingestion-instruction/gpt-5.6-sol}
---
# Non-Time-Value Methods

**Payback period** measures how long cumulative net cash inflows take to recover the initial investment.

```text
Payback period for equal annual cash flows
  = Initial investment / Annual net cash inflow
```

For uneven cash flows, accumulate each period’s cash flow until recovery; the fractional final period equals the unrecovered amount at the start of that period divided by that period’s cash inflow. Payback emphasizes liquidity and risk but ignores the time value of money, profitability, and cash flows after recovery.

**Accounting rate of return (ARR)** compares incremental accounting income with the investment:

```text
ARR
  = Incremental annual net income
    / (Initial investment − Salvage value)
```

Incremental net income includes incremental revenue and cost savings less incremental expenses, including depreciation. ARR uses income rather than cash flow and does not discount future amounts.

# Discounted Cash Flow Methods

**Net present value (NPV)** discounts project cash flows at the required rate of return:

```text
NPV
  = Present value of future net cash flows
  − Initial investment
```

A positive NPV indicates the project exceeds the required return; zero meets it; negative falls short.

**Profitability index** scales present value to the investment:

```text
Profitability index
  = Present value of net cash inflows / Initial investment
```

An index above `1` corresponds to a positive NPV. It is useful when comparing projects of different sizes under capital constraints.

**Internal rate of return (IRR)** is the discount rate that makes NPV zero:

```text
0
  = Present value of future net cash flows at IRR
  − Initial investment
```

A project passes the IRR screen when its IRR meets or exceeds the required rate of return.

# Selection Conventions

A screening decision eliminates projects that fail minimum criteria; a preference decision ranks acceptable projects. For mutually exclusive projects, only one can be selected. NPV states expected value creation in currency, while IRR states a percentage return; project scale and cash-flow timing can cause the methods to rank alternatives differently.
