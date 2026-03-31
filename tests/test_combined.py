import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from basic_operations import add, multiply
from advanced_operations import sine, power

class TestCombinedOperations(unittest.TestCase):

    def test_add_and_sine(self):
        # sin(0 + 0) = 0
        result = sine(add(0, 0))
        self.assertAlmostEqual(result, 0)

    def test_power_and_add(self):
        # (2^3) + 4 = 12
        result = add(power(2, 3), 4)
        self.assertEqual(result, 12)

    def test_mixed_operations(self):
        # sin(2 * 0) = sin(0) = 0
        result = sine(multiply(2, 0))
        self.assertAlmostEqual(result, 0)

    def test_complex_expression(self):
        # (2^2 + 3) = 7 → sin(7)
        result = sine(add(power(2, 2), 3))
        self.assertAlmostEqual(result, sine(7))

if __name__ == '__main__':
    unittest.main()
