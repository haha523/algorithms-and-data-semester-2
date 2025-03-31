import unittest
import os
import sys
from io import StringIO
from contextlib import redirect_stdout

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c17 import find_min_k

class TestWeakKConnectivity(unittest.TestCase):
    def test_example1(self):
        # given
        find_min_k()

        # when
        output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt'))
        with open(output_path, 'r') as f:
            result = f.read().strip()

        # then
        self.assertEqual(result, "1")

if __name__ == '__main__':
    unittest.main()
