import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a12 import can_partition

class TestSequencePartition(unittest.TestCase):

    def test_partition_possible(self):
        # given
        self.assertEqual(can_partition([1, 2, 3]), (1, [3]))
        # when
        self.assertEqual(can_partition([1, 1, 2, 2]), (2, [4, 2]))
        # then
        self.assertEqual(can_partition([2, 2, 2, 2]), (2, [4, 3]))

    def test_partition_impossible(self):
        # given
        self.assertEqual(can_partition([1, 2, 5]), (-1, []))
        # when
        self.assertEqual(can_partition([1, 1, 1, 1, 1]), (-1, []))
        # then
        self.assertEqual(can_partition([1, 2, 3, 4]), (2, [4, 1]))

    def test_edge_cases(self):
        # given
        self.assertEqual(can_partition([1]), (-1, []))
        # when
        self.assertEqual(can_partition([2, 2]), (1, [2]))
        # then
        self.assertEqual(can_partition([1, 1, 1, 1, 1, 1]), (3, [6, 5, 4]))

if __name__ == '__main__':
    unittest.main()