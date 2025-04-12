import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d7 import find_lcs

class TestLongestCommonSubstring(unittest.TestCase):
    def test_basic_cases(self):
        # given
        self.assertEqual(find_lcs("cool", "toolbox"), (1, 1, 3))
        # when
        self.assertEqual(find_lcs("aaa", "bb"), (0, 0, 0))
        # then
        self.assertEqual(find_lcs("aabaa", "babbaab"), (2, 3, 3))

    def test_empty_strings(self):
        # given
        self.assertEqual(find_lcs("", "abc"), (0, 0, 0))
        # when
        self.assertEqual(find_lcs("abc", ""), (0, 0, 0))
        # then
        self.assertEqual(find_lcs("", ""), (0, 0, 0))

    def test_full_match(self):
        # given
        self.assertEqual(find_lcs("abc", "abc"), (0, 0, 3))
        # then
        self.assertEqual(find_lcs("xyz", "xyz"), (0, 0, 3))

if __name__ == "__main__":
    unittest.main()
