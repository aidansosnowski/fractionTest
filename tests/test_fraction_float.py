import unittest
from fraction import Fraction

class TestFractionFloat(unittest.TestCase):
    def setUp(self):
        self.frac_half = Fraction(1, 2)
        self.frac_one = Fraction(1, 1)
        self.frac_neg_half = Fraction(-1, 2)
        self.frac_zero = Fraction(0, 1)

    def test_float_true(self):
        self.assertEqual(float(self.frac_half), 0.5, "float(1/2) should be 0.5")

    def test_float_whole(self):
        self.assertEqual(float(Fraction(5, 1)), 5.0, "float(5/1) should be 5.0")

    def test_float_neg(self):
        self.assertEqual(float(self.frac_neg_half), -0.5, "float(-1/2) should be -0.5")

    def test_float_zero(self):
        self.assertEqual(float(self.frac_zero), 0.0, "float(0/1) should be 0.0")

    def test_float_type(self):
        self.assertIsInstance(float(self.frac_half), float, "float() should return a float")

if __name__ == '__main__':
    unittest.main()
