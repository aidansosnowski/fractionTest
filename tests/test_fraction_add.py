import unittest
"Tip: To have more robust tests, it’s essential to first think of edge cases, invalid input, or no"
"input and what the method would return in each of those situations. "
from fraction import Fraction

class TestFractionAdd(unittest.TestCase):
    """Tests for the __add__ method of Fraction class."""

    def setUp(self):
        self.frac_half = Fraction(1, 2)
        self.frac_one = Fraction(1, 1)
        self.frac_neg_half = Fraction(-1, 2)
        self.frac_zero = Fraction(0, 1)

    def test_add_halves(self):
        result = self.frac_half + Fraction(1, 2)
        self.assertEqual(result, Fraction(1, 1), "1/2 + 1/2 should equal 1/1")

    def test_add_negatives(self):
        result = self.frac_neg_half + Fraction(-1, 2)
        self.assertEqual(result, Fraction(-1, 1), "-1/2 + -1/2 should equal -1/1")

    def test_add_zeros(self):
        result = self.frac_zero + Fraction(0, 1)
        self.assertEqual(result, Fraction(0, 1), "0/1 + 0/1 should equal 0/1")

    def test_add_ones(self):
        result = self.frac_one + Fraction(1, 1)
        self.assertEqual(result, Fraction(2, 1), "1/1 + 1/1 should equal 2/1")


if __name__ == '__main__':
    unittest.main()