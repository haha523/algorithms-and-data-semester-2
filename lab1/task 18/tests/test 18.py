import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a18 import read_input, minimize_cost

class TestTaskScheduler(unittest.TestCase):

    def test_read_input(self):
        # given
        input_data = "5\n110\n40\n120\n110\n60\n"
        with open('test_input.txt', 'w') as f:
            f.write(input_data)

        # when
        n, costs = read_input('test_input.txt')
        os.remove('test_input.txt')

        # then
        self.assertEqual(n, 5)
        self.assertEqual(costs, [110, 40, 120, 110, 60])

    def test_minimize_cost(self):
        # given
        n = 5
        costs = [110, 40, 120, 110, 60]

        # when
        min_cost, remaining_coupons, used_coupons_count, used_coupons = minimize_cost(n, costs)

        # then
        self.assertEqual(min_cost, 260)
        self.assertEqual(remaining_coupons, 0)
        self.assertEqual(used_coupons_count, 2)
        self.assertEqual(used_coupons, [3, 5])

if __name__ == '__main__':
    unittest.main()