import sys
import unittest
from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.calculate import (
    F0,
    DELTA_T,
    SCALE,
    candidate_frequency,
    propagated_values,
)

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

    def test_scaled_reference(self):
        values = propagated_values()
        self.assertEqual(values["scaled_reference"], Decimal("576480.1"))

    def test_scaled_candidate_prefix(self):
        values = propagated_values()
        self.assertTrue(
            str(values["scaled_candidate"]).startswith(
                "576480.1000001384128720100332329305696"
            )
        )

    def test_residual_propagation_identity(self):
        values = propagated_values()
        self.assertLess(
            abs(values["scaled_residual"] - (SCALE * values["delta_f"])),
            Decimal("1e-74"),
        )


if __name__ == "__main__":
    unittest.main()
