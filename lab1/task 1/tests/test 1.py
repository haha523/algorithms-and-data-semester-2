import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a1 import fractional_knapsack

class TestFractionalKnapsack(unittest.TestCase):

    def test_case_1(self):
        # given
        items = [(60, 20), (100, 50), (120, 30)]
        result = fractional_knapsack(3, 50, items)
        # then
        self.assertAlmostEqual(result, 180.0000, places=4)

    def test_case_2(self):
        # given
        items = [(500, 30)]
        result = fractional_knapsack(1, 10, items)
        # then
        self.assertAlmostEqual(result, 166.6667, places=4)

    def test_case_3(self):
        # given
        items = [(100, 10), (200, 20), (300, 30)]
        result = fractional_knapsack(3, 50, items)
        # then
        self.assertAlmostEqual(result, 500.0000, places=4)

if __name__ == '__main__':
    unittest.main()