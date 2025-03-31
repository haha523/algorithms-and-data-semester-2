import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c2 import count_components

class TestCountComponents(unittest.TestCase):
    @patch('sys.stdin', new_callable=StringIO)
    def test_components(self, mock_stdin):
        # given
        mock_stdin.write('4 2\n1 2\n3 2\n')
        mock_stdin.seek(0)
        # when
        result = count_components(input_file='input.txt', output_file='output.txt', to_file=False)
        # then
        self.assertEqual(result, 2)

    @patch('sys.stdin', new_callable=StringIO)
    def test_no_edges(self, mock_stdin):
        # given
        mock_stdin.write('5 0\n')
        mock_stdin.seek(0)
        # when
        result = count_components(input_file='input.txt', output_file='output.txt', to_file=False)
        # then
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
