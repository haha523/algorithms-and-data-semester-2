import unittest
import os

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a6 import largest_number

class TestLargestNumber(unittest.TestCase):

    def test_largest_number(self):
        # given
        self.assertEqual(largest_number(['21', '2']), '221')
        # when
        self.assertEqual(largest_number(['23', '39', '92']), '923923')
        self.assertEqual(largest_number(['3', '30', '34', '5', '9']), '9534330')
        # then
        self.assertEqual(largest_number(['1', '10', '100']), '110100')

    def test_empty_input(self):
        # given
        self.assertEqual(largest_number([]), '')

if __name__ == '__main__':
    unittest.main()
