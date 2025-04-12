import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d3 import rabin_karp_search

class TestRabinKarp(unittest.TestCase):
    def test_basic_case(self):
        # given
        self.assertEqual(rabin_karp_search("aba", "abacaba"), [1, 5])
        # then
        self.assertEqual(rabin_karp_search("Test", "testTesttesT"), [5])

    def test_overlapping_patterns(self):
        # given
        self.assertEqual(rabin_karp_search("aaaaa", "baaaaaaa"), [2, 3, 4])
        # then
        self.assertEqual(rabin_karp_search("aa", "aaa"), [1, 2])

    def test_case_sensitive(self):
        # given
        self.assertEqual(rabin_karp_search("Ab", "abABab"), [])
        # then
        self.assertEqual(rabin_karp_search("AB", "abABab"), [3])

if __name__ == "__main__":
    unittest.main()
