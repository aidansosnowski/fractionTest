import unittest
from fraction import Fraction

class TestFractionMul(unittest.TestCase):
    def setUp(self):
        self.frac_half = Fraction(1, 2)
        self.frac_one = Fraction(1, 1)
        self.frac_neg_half = Fraction(-1, 2)
        self.frac_zero = Fraction(0, 1)

    def test_mul_true(self):
        result = self.frac_half * self.frac_half
        self.assertEqual(result, Fraction(1, 4), "1/2 * 1/2 should be 1/4")

    def test_mul_zero(self):
        result = self.frac_zero * self.frac_one
        self.assertEqual(result, Fraction(0, 1), "0/1 * 1/1 should be 0/1")

    def test_mul_half_neg(self):
        result = self.frac_neg_half * self.frac_one
        self.assertEqual(result, Fraction(-1, 2), "-1/2 * 1/1 should be -1/2")

    def test_mul_both_neg(self):
        result = self.frac_neg_half * self.frac_neg_half
        self.assertEqual(result, Fraction(1, 4), "-1/2 * -1/2 should be 1/4")

    def test_mul_reduce(self):
        result = self.frac_half * Fraction(8, 2)
        self.assertEqual(result, Fraction(2, 1), "1/2 * 8/2 should be 2/1")

    def test_mul_invalid(self):
        with self.assertRaises(TypeError, msg="Multiplying by a non-Fraction should be a TypeError"):
            _ = self.frac_half * 2

if __name__ == '__main__':
    unittest.main()
