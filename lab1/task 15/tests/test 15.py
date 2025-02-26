import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a15 import find_max_valid_subsequence

class TestMaxValidSubsequence(unittest.TestCase):

    def test_valid_subsequence(self):
        # given
        self.assertEqual(find_max_valid_subsequence("()"), "()")
        # when
        self.assertEqual(find_max_valid_subsequence("{[()]}"), "{}[]()")
        self.assertEqual(find_max_valid_subsequence("(()())"), "()()")
        # then
        self.assertEqual(find_max_valid_subsequence("{[()]}()"), "{}[]()")

    def test_empty_input(self):
        # given
        self.assertEqual(find_max_valid_subsequence(""), "")

    def test_mixed_input(self):
        # given
        self.assertEqual(find_max_valid_subsequence("([{}])"), "()[]{}")
        # when
        self.assertEqual(find_max_valid_subsequence("([)]"), "[]")
        # then
        self.assertEqual(find_max_valid_subsequence("abc[()]xyz"), "[]()")

    def test_long_input(self):
        # given
        self.assertEqual(find_max_valid_subsequence("()()()()()"), "()()()")
        # when
        self.assertEqual(find_max_valid_subsequence("[({})]"), "[](){}")
        # then
        self.assertEqual(find_max_valid_subsequence("((((((()))))))"), "()()()()()()()")

if __name__ == "__main__":
    unittest.main()