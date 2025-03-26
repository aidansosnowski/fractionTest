import unittest

from fraction import Fraction

class TestFractionStr(unittest.TestCase):
    """Tests for the __str__ method of Fraction class."""

    def test_str_standard(self):
        result = Fraction(3, 4)
        self.assertEqual(str(result), "3/4", "Fraction(3,4) should be 3/4")

    def test_str_whole(self):
        result = Fraction(5, 1)
        self.assertEqual(str(result), "5", "Fraction(5,1) should be 5")

    def test_str_negative(self):
        result = Fraction(-3, 4)
        self.assertEqual(str(result), "-3/4", "Fraction(-3,4) should be -3/4")


if __name__ == '__main__':
    unittest.main()
