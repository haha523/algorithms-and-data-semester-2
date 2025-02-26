import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a13 import can_partition

class TestCanPartition(unittest.TestCase):
    def test_partition_not_possible(self):
        # given
        self.assertEqual(can_partition([3, 3, 3, 3]), 0)
        # then
        self.assertEqual(can_partition([40]), 0)

    def test_partition_possible(self):
        # given
        self.assertEqual(can_partition([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]), 1)
        # then
        self.assertEqual(can_partition([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]), 1)

if __name__ == "__main__":
    unittest.main()