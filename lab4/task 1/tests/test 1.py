import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d1 import naive_pattern_search

class TestSubstringSearch(unittest.TestCase):
    def test_basic_cases(self):
        # given
        self.assertEqual(naive_pattern_search("aba", "abaCaba"), [1, 5])
        # when
        self.assertEqual(naive_pattern_search("abc", "abcdefabc"), [1, 7])
        # then
        self.assertEqual(naive_pattern_search("a", "aaaaa"), [1, 2, 3, 4, 5])

    def test_no_match(self):
        # given
        self.assertEqual(naive_pattern_search("xyz", "abcdef"), [])
        # then
        self.assertEqual(naive_pattern_search("long", "short"), [])

    def test_case_sensitive(self):
        # given
        self.assertEqual(naive_pattern_search("Ab", "abABab"), [])
        # then
        self.assertEqual(naive_pattern_search("AB", "abABab"), [3])

if __name__ == "__main__":
    unittest.main()
