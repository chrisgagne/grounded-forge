---
type: Reference
title: Annuities and Perpetuities Reference
description: Definitions and valuation formulas for level payment streams, annuities due, and constant or growing perpetuities.
resource: https://openstax.org/details/books/principles-finance
tags:
  - finance
  - valuation
  - annuity
  - perpetuity
sources:
  - id: openstax-principles-finance
    resource: https://openstax.org/details/books/principles-finance
    title: Principles of Finance
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Annuities and Perpetuities

An annuity is a fixed stream of periodic payments. An ordinary annuity pays at the end of each period; an annuity due pays at the beginning. A perpetuity is a payment stream that continues indefinitely.

For payment `C`, periodic discount rate `r`, and `n` payments:

```text
PV of ordinary annuity = C × [1 - (1 + r)^(-n)] / r
FV of ordinary annuity = C × [(1 + r)^n - 1] / r
```

An annuity due shifts every ordinary-annuity payment one period earlier:

```text
PV of annuity due = PV of ordinary annuity × (1 + r)
FV of annuity due = FV of ordinary annuity × (1 + r)
```

For a constant perpetuity:

```text
PV = C / r
```

For a perpetuity whose next payment is `C1` and whose payments grow at constant rate `g`, with `r > g`:

```text
PV = C1 / (r - g)
```

Fixed-rate loan payments form an annuity. An amortization schedule divides each payment between interest on the outstanding balance and principal repayment.
