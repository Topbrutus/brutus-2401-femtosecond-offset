import sys
import unittest
from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.calculate import F0, DELTA_T, candidate_frequency

getcontext().prec = 80

class FormulaTests(unittest.TestCase):
    def test_defining_equation(self):
        f = candidate_frequency()
        reconstructed = (Decimal(1) / F0) - (Decimal(1) / f)
        self.assertLess(abs(reconstructed - DELTA_T), Decimal("1e-70"))

    def test_expected_prefix(self):
        f = candidate_frequency()
        self.assertTrue(str(f).startswith("240.1000000000576480100000138412872"))

    def test_frequency_increment_is_positive(self):
        self.assertGreater(candidate_frequency() - F0, Decimal(0))

if __name__ == "__main__":
    unittest.main()
