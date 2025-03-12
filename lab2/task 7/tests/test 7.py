import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b7 import is_bst

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        # given
        self.nodes_correct = [
            (2, 1, 2),
            (1, -1, -1),
            (3, -1, -1)
        ]

        # then
        self.nodes_incorrect = [
            (1, 1, 2),
            (2, -1, -1),
            (3, -1, -1)
        ]

    def test_bst_correct(self):
        # given
        self.assertTrue(is_bst(0, -2 ** 31, 2 ** 31 - 1, self.nodes_correct))

    def test_bst_incorrect(self):
        # given
        self.assertFalse(is_bst(0, -2 ** 31, 2 ** 31 - 1, self.nodes_incorrect))

if __name__ == '__main__':
    unittest.main()
