import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c13 import count_gardens

class TestCountGardens(unittest.TestCase):
    def setUp(self):
        # given
        self.input_file = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
        self.output_file = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    def test_gardens_count(self):
        # given
        count_gardens()
        # when
        with open(self.output_file, 'r') as f:
            result = f.read().strip()
        # then
        self.assertEqual(result, '3')

if __name__ == '__main__':
    unittest.main()
