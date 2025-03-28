import unittest
from fraction import Fraction

class TestFractionSub(unittest.TestCase):
    def test_sub_basic(self):
        result = Fraction(3, 4) - Fraction(1, 4)
        self.assertEqual(result, Fraction(1, 2), "Fraction(3,4) - Fraction(1,4) should be Fraction(1,2)")

    def test_sub_diff(self):
        result = Fraction(1, 2) - Fraction(1, 3)
        self.assertEqual(result, Fraction(1, 6), "Fraction(1,2) - Fraction(1,3) should be Fraction(1,6)")

    def test_sub_negative(self):
        result = Fraction(1, 4) - Fraction(3, 4)
        self.assertEqual(result, Fraction(-1, 2), "Fraction(1,4) - Fraction(3,4) should be Fraction(-1,2)")

    def test_sub_zero(self):
        result1 = Fraction(3, 4) - Fraction(0, 1)
        result2 = Fraction(0, 1) - Fraction(3, 4)
        self.assertEqual(result1, Fraction(3, 4), "Fraction(3,4) - Fraction(0,1) should be Fraction(3,4)")
        self.assertEqual(result2, Fraction(-3, 4), "Fraction(0,1) - Fraction(3,4) should be Fraction(-3,4)")

    def test_sub_invalid(self):
        with self.assertRaises(TypeError, msg="Subtracting a non-Fraction should be a TypeError"):
            _ = Fraction(1, 2) - 1

if __name__ == '__main__':
    unittest.main()
