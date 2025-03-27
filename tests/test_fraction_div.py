import unittest
from fraction import Fraction

class TestFractionDiv(unittest.TestCase):
    def setUp(self):
        self.frac_half = Fraction(1, 2)
        self.frac_one = Fraction(1, 1)
        self.frac_neg_half = Fraction(-1, 2)
        self.frac_zero = Fraction(0, 1)

    def test_div_true(self):
        result = self.frac_half / Fraction(1, 4)
        self.assertEqual(result, Fraction(2, 1), "1/2 / 1/4 should be 2/1")

    def test_div_different(self):
        result = self.frac_one / Fraction(1, 4)
        self.assertEqual(result, Fraction(4, 1), "1/1 / 1/4 should be 4/1")

    def test_div_zero_numerator(self):
        result = self.frac_zero / Fraction(1, 4)
        self.assertEqual(result, Fraction(0, 1), "0/1 / 1/4 should be 0/1")

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="Dividing by 0/1 leads to ZeroDivisionError"):
            _ = self.frac_one / Fraction(0, 1)

    def test_div_neg(self):
        result = self.frac_neg_half / Fraction(1, 4)
        self.assertEqual(result, Fraction(-2, 1), "-1/2 / 1/4 should be -2/1")

    def test_div_reduce(self):
        result = Fraction(4, 2) / Fraction(1, 4)
        self.assertEqual(result, Fraction(8, 1), "(4/2) / (1/4) should be 8/1")

    def test_div_invalid(self):
        with self.assertRaises(TypeError, msg="Dividing by a non-Fraction leads to TypeError"):
            _ = self.frac_half / 2

if __name__ == '__main__':
    unittest.main()
