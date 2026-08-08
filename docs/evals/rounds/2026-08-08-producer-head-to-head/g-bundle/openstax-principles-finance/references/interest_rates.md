---
type: Reference
title: Interest Rate Conventions Reference
description: Definitions and relationships among nominal, real, stated, effective, and risk-adjusted interest rates.
resource: https://openstax.org/details/books/principles-finance
tags:
  - finance
  - interest-rate
  - convention
sources:
  - id: openstax-principles-finance
    resource: https://openstax.org/details/books/principles-finance
    title: Principles of Finance
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Interest Rate Conventions

An interest rate is the rental price of money: it compensates a lender for postponing consumption and accepting risk.

## Rate types

- **Nominal rate**: the quoted or stated rate, before removing inflation.
- **Real rate**: the nominal rate adjusted for inflation. A common approximation is `real rate ≈ nominal rate − inflation rate`.
- **Risk premium**: an increment above a lower-risk base rate that compensates a lender or investor for additional risk.
- **Stated annual rate**: an annual quotation that does not by itself reflect the effect of compounding within the year.
- **Effective annual rate (EAR)**: the annual rate after intra-year compounding is recognized.

For a stated annual rate `r` compounded `m` times per year:

```text
EAR = (1 + r / m)^m - 1
```

More frequent compounding raises the effective rate when the stated rate is positive. When using a rate to value cash flows, the rate per period and the number of periods must use the same time unit.
