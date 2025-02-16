import unittest
from main import *

class my_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=10, cat=11), 21)

    def test_mix(self):
        self.assertEqual(adder(1, r=45), 46)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual((adder(0, -5, y, a=x)), 5)

    def test_type(self):
        self.assertEqual(adder("5", "abc", 10), 15)


if __name__ == "__main__":
    unittest.main()