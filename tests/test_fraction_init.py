import unittest
from fraction import Fraction

class TestFractionInit(unittest.TestCase):
    def test_init_default(self):
        result = Fraction()
        self.assertEqual(str(result), "0", "Fraction() should be represented as '0' (i.e., 0/1)")

    def test_init_single(self):
        result = Fraction(5)
        self.assertEqual(str(result), "5", "Fraction(5) should be represented as '5' (i.e., 5/1)")

    def test_init_reduce(self):
        result = Fraction(2, 4)
        self.assertEqual(str(result), "1/2", "Fraction(2,4) should reduce to 1/2")

    def test_init_both_negative(self):
        result = Fraction(-2, -3)
        self.assertEqual(str(result), "2/3", "Fraction(-2,-3) should become 2/3")

    def test_init_denom_negative(self):
        result = Fraction(2, -3)
        self.assertEqual(str(result), "-2/3", "Fraction(2,-3) should become -2/3")

    def test_init_non_integer(self):
        with self.assertRaises(TypeError, msg="Fraction(2.4) should lead to TypeError"):
            Fraction(2.4)

    def test_init_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError, msg="Fraction(1,0) should lead to ZeroDivisionError"):
            Fraction(1, 0)

    def test_init_non_integer_denominator(self):
        with self.assertRaises(TypeError, msg="Fraction(1, 2.5) should lead to TypeError"):
            Fraction(1, 2.5)

if __name__ == '__main__':
    unittest.main()
