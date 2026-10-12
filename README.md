# Portfolio Optimisation & Decision Analytics

Python portfolio-analytics notebook covering return/risk estimation, Monte Carlo portfolio simulation and constrained optimisation.

**Recommended notebook:** [Reviewed and corrected version](portfolio_optimisation_efficient_frontier_REVIEWED.ipynb) — fixes cumulative log-return growth and frontier comparisons, adds input checks and removes historical notebook outputs. The original version remains for source comparison. GitHub CI checks notebook structure and formula conventions offline, not live Yahoo Finance data or investment results.

## Workflow
- Analyses 1,257 trading days across five equities.
- Engineers log returns, annualised expected returns/volatility and covariance/correlation matrices.
- Simulates 5,000 random portfolio allocations.
- Uses constrained SciPy optimisation to construct a 200-point efficient frontier.
- Identifies maximum-Sharpe and minimum-variance allocations and compares them with an existing portfolio.

## Key executed outputs
- Maximum-Sharpe portfolio: expected return 36.38%, volatility 39.63%, Sharpe 0.7919.
- Minimum-variance portfolio volatility: 28.23%.

## Run
```bash
pip install -r requirements.txt
jupyter notebook portfolio_optimisation_efficient_frontier_REVIEWED.ipynb
```

## Important limitations

- Historical Yahoo Finance prices are fetched when run; no independent exchange-feed reconciliation or guaranteed availability.
- Mean/covariance estimates and optimized allocations are **in-sample**, not live or out-of-sample portfolio performance.
- Annualized log-return moments are used as simple-return risk/return proxies; compounding for the displayed growth-of-$1 chart uses the correct exponential of cumulative log returns in the reviewed notebook.
- The modeled universe consists of five selected US equities and illustrative weights, not actual client holdings.
- Trading costs, taxes, corporate-action reconciliation and future market regimes have not been modeled.
