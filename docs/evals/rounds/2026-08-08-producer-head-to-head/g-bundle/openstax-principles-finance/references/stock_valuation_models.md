---
type: Reference
title: Stock Valuation Models Reference
description: Relative, dividend-discount, and discounted-cash-flow methods for estimating common-stock value.
resource: https://openstax.org/details/books/principles-finance
tags:
  - finance
  - stock
  - valuation
  - equity
sources:
  - id: openstax-principles-finance
    resource: https://openstax.org/details/books/principles-finance
    title: Principles of Finance
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Stock Valuation Models

Stock valuation estimates intrinsic value from comparable market multiples, expected dividends, or enterprise cash flows.

## Relative multiples

Common ratios include price-to-earnings, price-to-book, price-to-sales, and price-to-cash-flow. A multiple is meaningful only when its accounting basis, growth expectations, and risk are comparable across the firms being evaluated.

## Dividend discount models

The dividend discount model treats stock value as the present value of expected future dividends. For next-period dividend `D1`, required return `r`, and constant dividend growth `g`, with `r > g`:

```text
P0 = D1 / (r - g)
```

If dividends never grow:

```text
P0 = D / r
```

Variable-growth and two-stage models discount the dividends during each explicit growth stage and add the discounted terminal value at the point stable growth begins.

## Discounted cash flow

A discounted-cash-flow model values the company from forecast cash flows and a terminal value:

```text
Enterprise value = Σ[t=1..n] CFt / (1 + r)^t + Terminal value / (1 + r)^n
```

Equity value is derived from enterprise value after accounting for claims such as debt; per-share value divides equity value by shares outstanding. Results are highly sensitive to cash-flow forecasts, terminal assumptions, and the discount rate, so multiple valuation methods should be compared.
