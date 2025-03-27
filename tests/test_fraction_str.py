import unittest
from fraction import Fraction

class TestFractionStr(unittest.TestCase):
    def test_str_standard(self):
        result = Fraction(3, 4)
        self.assertEqual(str(result), "3/4", "Fraction(3,4) should become 3/4")

    def test_str_whole(self):
        result = Fraction(5, 1)
        self.assertEqual(str(result), "5", "Fraction(5,1) should become 5")

    def test_str_negative(self):
        result = Fraction(-3, 4)
        self.assertEqual(str(result), "-3/4", "Fraction(-3,4) should become -3/4")

    def test_str_edge_reduction(self):
        # Testing a reducible fraction that might be an edge case.
        result = Fraction(2, 6)
        self.assertEqual(str(result), "1/3", "Fraction(2,6) should become 1/3")

if __name__ == '__main__':
    unittest.main()
