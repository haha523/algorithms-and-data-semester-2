import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c7 import task_scheduler

class TestBipartiteCheck(unittest.TestCase):

    def test_bipartite_graph(self):
        # given
        input_file = os.path.join('..', 'txtf', 'input.txt')
        output_file = os.path.join('..', 'txtf', 'output.txt')

        # when
        with open(input_file, 'r') as f:
            n, m = map(int, f.readline().strip().split())
            edges = [tuple(map(int, f.readline().strip().split())) for _ in range(m)]

        result = task_scheduler(input_file='input.txt', output_file='output.txt')

        with open(output_file, 'r') as f:
            expected_output = f.read().strip()

        # then
        self.assertIn(result, ['0', '1'])
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
