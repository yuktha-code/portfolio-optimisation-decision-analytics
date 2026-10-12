"""Offline correctness and notebook provenance checks; no market-data downloads."""
import json
import math
import unittest
from pathlib import Path


NOTEBOOK = Path(__file__).resolve().parents[1] / "portfolio_optimisation_efficient_frontier_REVIEWED.ipynb"


class PortfolioNotebookChecks(unittest.TestCase):
    def setUp(self):
        self.nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        self.source = "\n".join("".join(c.get("source", [])) for c in self.nb["cells"])

    def test_log_growth_formula(self):
        # True log-return compounding: product of gross simple returns.
        prices = [100., 98., 101.5, 103.]
        log_returns = [math.log(prices[i] / prices[i-1]) for i in range(1, len(prices))]
        self.assertAlmostEqual(math.exp(sum(log_returns)), prices[-1] / prices[0], places=12)
        self.assertIn("np.exp(log_returns.cumsum())", self.source)
        self.assertNotIn("(log_returns + 1).cumprod()", self.source)

    def test_frontier_upper_branch(self):
        self.assertIn("np.linspace(r_mv, float(expected_returns.max()), 200)", self.source)
        self.assertNotIn("Your portfolio is ABOVE the simulated frontier (excellent!)", self.source)
        self.assertIn("In-sample", self.source)

    def test_clean_notebook(self):
        self.assertTrue(all(c.get("execution_count") is None for c in self.nb["cells"] if c["cell_type"] == "code"))
        self.assertTrue(all(not c.get("outputs") for c in self.nb["cells"] if c["cell_type"] == "code"))
        self.assertEqual(self.nb["nbformat"], 4)


if __name__ == "__main__":
    unittest.main()
