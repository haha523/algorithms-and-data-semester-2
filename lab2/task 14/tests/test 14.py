import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b14 import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_avl_insert(self):
        # given
        avl_tree = AVLTree()
        avl_tree.insert(3)
        avl_tree.insert(4)

        # when
        avl_tree.insert(5)

        # then
        self.assertEqual(avl_tree.root.key, 4)
        self.assertEqual(avl_tree.root.left.key, 3)
        self.assertEqual(avl_tree.root.right.key, 5)

    def test_empty_tree(self):
        # given
        avl_tree = AVLTree()

        # when
        avl_tree.insert(5)

        # then
        self.assertEqual(avl_tree.root.key, 5)
        self.assertIsNone(avl_tree.root.left)
        self.assertIsNone(avl_tree.root.right)

if __name__ == "__main__":
    unittest.main()
