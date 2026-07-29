---
type: Reference
title: Time Value of Money Conventions
description: Defines present- and future-value conventions for lump sums, ordinary annuities, and annuities due.
resource: https://openstax.org/details/books/principles-managerial-accounting
tags:
  - finance
  - time-value-of-money
  - present-value
  - future-value
  - convention
sources:
  - id: openstax-principles-managerial-accounting
    resource: https://openstax.org/details/books/principles-managerial-accounting
    title: "Principles of Accounting, Volume 2: Managerial Accounting"
generated: {by: web-ingestion-instruction/gpt-5.6-sol}
---
# Core Convention

Time value of money recognizes that a dollar available today is worth more than the same nominal dollar received later because current funds can earn a return and future purchasing power is uncertain.

Use:

- `PV` for present value;
- `FV` for future value;
- `PMT` for each equal periodic payment;
- `i` for the interest rate per compounding or discounting period; and
- `n` for the number of periods.

The rate period and payment period must match. If interest compounds more than once a year, convert both the periodic rate and number of periods consistently.

# Lump Sum

A lump sum is a single payment at one point in time.

```text
FV = PV × (1 + i)^n

PV = FV / (1 + i)^n
```

Compounding moves a present amount forward; discounting moves a future amount back to the present.

# Ordinary Annuity

An ordinary annuity is a series of equal payments made at the **end** of each period.

```text
Future value of an ordinary annuity
  = PMT × [((1 + i)^n − 1) / i]

Present value of an ordinary annuity
  = PMT × [(1 − (1 + i)^−n) / i]
```

Use an ordinary-annuity factor only when the payment amount and timing are uniform. Discount unequal cash flows individually as lump sums and add their present values.

# Annuity Due

An annuity due is a series of equal payments made at the **beginning** of each period. Each payment earns or is discounted for one additional period compared with an ordinary annuity:

```text
Annuity-due value
  = Corresponding ordinary-annuity value × (1 + i)
```
