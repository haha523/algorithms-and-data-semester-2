import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b3 import BST

class TestBST(unittest.TestCase):
    def setUp(self):
        # given
        self.bst = BST()
        self.test_values = [20, 10, 30, 25, 5, 15]

    def test_insert_and_find_min_greater_than(self):
        # given
        for value in self.test_values:
            self.bst.insert(value)

        # then
        self.assertEqual(self.bst.find_min_greater_than(0), 5)
        self.assertEqual(self.bst.find_min_greater_than(10), 15)
        self.assertEqual(self.bst.find_min_greater_than(20), 25)
        self.assertEqual(self.bst.find_min_greater_than(30), 0)
        self.assertEqual(self.bst.find_min_greater_than(26), 30)

    def test_insert_duplicate(self):
        # given
        self.bst.insert(10)
        # when
        self.bst.insert(10)
        # then
        self.assertEqual(self.bst.find_min_greater_than(9), 10)

if __name__ == '__main__':
    unittest.main()
