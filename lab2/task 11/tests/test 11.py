import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b11 import AVLTree, TreeNode

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        # given
        self.tree = AVLTree()
        self.root = None

    def test_insert_and_exists(self):
        # given
        self.root = self.tree.insert(self.root, 10)
        self.root = self.tree.insert(self.root, 20)
        self.root = self.tree.insert(self.root, 5)
        # then
        self.assertTrue(self.tree.exists(self.root, 10))
        self.assertTrue(self.tree.exists(self.root, 20))
        self.assertTrue(self.tree.exists(self.root, 5))
        self.assertFalse(self.tree.exists(self.root, 15))

    def test_delete(self):
        # given
        self.root = self.tree.insert(self.root, 10)
        self.root = self.tree.insert(self.root, 20)
        self.root = self.tree.insert(self.root, 5)
        self.root = self.tree.delete(self.root, 10)
        # then
        self.assertFalse(self.tree.exists(self.root, 10))
        self.assertTrue(self.tree.exists(self.root, 20))
        self.assertTrue(self.tree.exists(self.root, 5))

    def test_next_and_prev(self):
        # given
        self.root = self.tree.insert(self.root, 10)
        self.root = self.tree.insert(self.root, 20)
        self.root = self.tree.insert(self.root, 15)
        # then
        self.assertEqual(self.tree.next(self.root, 10), 15)
        self.assertEqual(self.tree.prev(self.root, 20), 15)
        self.assertEqual(self.tree.next(self.root, 30), 'none')
        self.assertEqual(self.tree.prev(self.root, 5), 'none')

if __name__ == '__main__':
    unittest.main()
