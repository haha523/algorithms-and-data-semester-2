import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b16 import KthMaximum

class TestKthMaximum(unittest.TestCase):
    def setUp(self):
        # given
        self.kth_maximum = KthMaximum()

    def test_add_and_get_kth_maximum(self):
        # given
        self.kth_maximum.add(5)
        self.kth_maximum.add(3)
        self.kth_maximum.add(7)

        # then
        self.assertEqual(self.kth_maximum.get_kth_maximum(1), 7)
        self.assertEqual(self.kth_maximum.get_kth_maximum(2), 5)
        self.assertEqual(self.kth_maximum.get_kth_maximum(3), 3)

    def test_remove_and_get_kth_maximum(self):
        # given
        self.kth_maximum.add(5)
        self.kth_maximum.add(3)
        self.kth_maximum.add(7)
        self.kth_maximum.remove(5)

        # then
        self.assertEqual(self.kth_maximum.get_kth_maximum(1), 7)
        self.assertEqual(self.kth_maximum.get_kth_maximum(2), 3)

    def test_multiple_operations(self):
        # given
        self.kth_maximum.add(10)
        self.kth_maximum.add(20)
        self.kth_maximum.add(30)
        self.kth_maximum.add(40)

        # when
        self.kth_maximum.remove(20)

        # then
        self.assertEqual(self.kth_maximum.get_kth_maximum(1), 40)
        self.assertEqual(self.kth_maximum.get_kth_maximum(2), 30)
        self.assertEqual(self.kth_maximum.get_kth_maximum(3), 10)

if __name__ == '__main__':
    unittest.main()
