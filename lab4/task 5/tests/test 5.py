import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d5 import compute_prefix_function

class TestPrefixFunction(unittest.TestCase):
    def test_basic_cases(self):
        # given
        self.assertEqual(compute_prefix_function("aaaAAA"), [0, 1, 2, 0, 0, 0])
        # then
        self.assertEqual(compute_prefix_function("abacaba"), [0, 0, 1, 0, 1, 2, 3])

    def test_single_character(self):
        # given
        self.assertEqual(compute_prefix_function("a"), [0])
        # then
        self.assertEqual(compute_prefix_function("z"), [0])

    def test_repeated_patterns(self):
        # given
        self.assertEqual(compute_prefix_function("aaaaa"), [0, 1, 2, 3, 4])
        # then
        self.assertEqual(compute_prefix_function("ababab"), [0, 0, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
