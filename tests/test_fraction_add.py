import unittest
from fraction import Fraction

class TestFractionAdd(unittest.TestCase):
    def setUp(self):
        self.frac_half = Fraction(1, 2)
        self.frac_one = Fraction(1, 1)
        self.frac_neg_half = Fraction(-1, 2)
        self.frac_zero = Fraction(0, 1)

    def test_add_halves(self):
        result = self.frac_half + Fraction(1, 2)
        self.assertEqual(result, Fraction(1, 1), "1/2 + 1/2 should be 1/1")

    def test_add_negatives(self):
        result = self.frac_neg_half + Fraction(-1, 2)
        self.assertEqual(result, Fraction(-1, 1), "-1/2 + -1/2 should be -1/1")

    def test_add_zeros(self):
        result = self.frac_zero + Fraction(0, 1)
        self.assertEqual(result, Fraction(0, 1), "0/1 + 0/1 should be 0/1")

    def test_add_ones(self):
        result = self.frac_one + Fraction(1, 1)
        self.assertEqual(result, Fraction(2, 1), "1/1 + 1/1 should be 2/1")

    def test_add_invalid(self):
        with self.assertRaises(TypeError, msg="Adding a non-Fraction leads to TypeError"):
            _ = self.frac_half + 2

if __name__ == '__main__':
    unittest.main()
