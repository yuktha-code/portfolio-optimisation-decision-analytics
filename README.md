# Portfolio Optimisation & Decision Analytics

Python portfolio-analytics notebook covering return/risk estimation, Monte Carlo portfolio simulation and constrained optimisation.

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
jupyter notebook portfolio_optimisation_efficient_frontier.ipynb
```
