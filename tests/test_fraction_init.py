import unittest

from fraction import Fraction

class TestFractionInit(unittest.TestCase):
    """Tests for the __init__ method of Fraction class."""

    def test_init_default(self):
        result = Fraction()
        self.assertEqual(str(result), "0", "Fraction() should be 0")

    def test_init_single(self):
        result = Fraction(5)
        self.assertEqual(str(result), "5", "Fraction(5) should be 5")

    def test_init_reduce(self):
        result = Fraction(2, 4)
        self.assertEqual(str(result), "1/2", "Fraction(2,4) should reduce to 1/2")

    def test_init_both_negative(self):
        result = Fraction(-2, -3)
        self.assertEqual(str(result), "2/3", "Fraction(-2,-3) should be 2/3")

    def test_init_denom_negative(self):
        result = Fraction(2, -3)
        self.assertEqual(str(result), "-2/3", "Fraction(2,-3) should be -2/3")

    def test_init_non_integer(self):
        with self.assertRaises(TypeError, msg="Fraction(2.4) should lead to TypeError"):
            Fraction(2.4)


if __name__ == '__main__':
    unittest.main()