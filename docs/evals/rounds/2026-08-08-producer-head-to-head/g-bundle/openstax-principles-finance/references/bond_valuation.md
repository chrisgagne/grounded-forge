---
type: Reference
title: Bond Valuation Reference
description: Bond cash-flow terms, present-value pricing, yield relationships, and principal sources of bond risk.
resource: https://openstax.org/details/books/principles-finance
tags:
  - finance
  - bond
  - valuation
  - fixed-income
sources:
  - id: openstax-principles-finance
    resource: https://openstax.org/details/books/principles-finance
    title: Principles of Finance
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Bond Valuation

A bond is a debt instrument under which an issuer promises coupon payments and repayment of face value at maturity. Its value is the present value of both cash-flow components.

For face value `F`, coupon payment `C`, required yield per period `r`, and `n` remaining coupon periods:

```text
Bond price = Σ[t=1..n] C / (1 + r)^t + F / (1 + r)^n
```

Use the coupon rate only to determine the coupon payment. Use the yield to maturity or other required return to discount the cash flows. If payments are semiannual, use half the annual coupon and yield with twice the number of years.

## Price and yield

- Required yield equals coupon rate: the bond normally trades at par.
- Required yield exceeds coupon rate: the bond trades at a discount.
- Required yield is below coupon rate: the bond trades at a premium.
- Bond prices and market interest rates move in opposite directions.

The yield curve plots yields on the vertical axis against maturities on the horizontal axis and represents the term structure of interest rates.

Important bond risks include interest-rate, default or credit, liquidity, duration, call, reinvestment, and term risk.
