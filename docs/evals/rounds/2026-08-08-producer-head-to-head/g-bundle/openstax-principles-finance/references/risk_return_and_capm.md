---
type: Reference
title: Risk, Return, and CAPM Reference
description: Conventions for measuring investment return, diversification, systematic risk, and risk-adjusted performance.
resource: https://openstax.org/details/books/principles-finance
tags:
  - finance
  - investment
  - risk
  - capm
sources:
  - id: openstax-principles-finance
    resource: https://openstax.org/details/books/principles-finance
    title: Principles of Finance
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Risk, Return, and CAPM

Investment return is the gain or loss relative to the amount invested. In finance, risk commonly means the variability of returns over time.

```text
Holding-period return = (Income + Ending price - Beginning price) / Beginning price
Expected portfolio return = Σ wi × E(Ri)
```

Historical average return is commonly measured with the arithmetic mean, and total volatility with the standard deviation of returns.

## Diversification and beta

Diversification can reduce firm-specific risk when asset returns are not perfectly positively correlated, but it cannot eliminate systematic market risk. Beta measures an asset’s systematic risk relative to a market benchmark.

The capital asset pricing model relates expected return to systematic risk:

```text
E(Ri) = Rf + βi × [E(Rm) - Rf]
```

where `Rf` is the risk-free rate and `E(Rm) - Rf` is the market risk premium.

## Risk-adjusted performance

- **Sharpe ratio** compares excess return with total volatility.
- **Treynor ratio** compares excess return with systematic risk measured by beta.
- **Jensen’s alpha** measures realized or expected return above the return implied by CAPM.

Return alone is therefore insufficient for comparing portfolios with different risk exposures.
