import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a19 import read_input, matrix_chain_order, construct_parenthesis

class TestMatrixChain(unittest.TestCase):

    def setUp(self):
        # given
        self.input_data = [
            (3, [(10, 50), (50, 90), (90, 20)]),
            (4, [(10, 20), (20, 30), (30, 40), (40, 30)]),
        ]

        # then
        self.expected_outputs = [
            "((AA)A)",
            "(((AA)A)A)",
        ]

    def test_read_input(self):
        # given
        input_file = os.path.join('..', 'txtf', 'input.txt')
        with open(input_file, 'w') as f:
            f.write("3\n10 50\n50 90\n90 20\n")

        # when
        n, dimensions = read_input(input_file)

        # then
        self.assertEqual(n, self.input_data[0][0])
        self.assertEqual(dimensions, self.input_data[0][1])

    def test_matrix_chain_order(self):
        # given
        n, dimensions = self.input_data[0]
        # when
        dp, split = matrix_chain_order(dimensions)
        # then
        self.assertEqual(len(dp), n)
        self.assertEqual(len(split), n)

    def test_construct_parenthesis(self):
        # given
        n, dimensions = self.input_data[0]
        # when
        _, split = matrix_chain_order(dimensions)
        result = construct_parenthesis(split, 0, n - 1)
        # then
        self.assertEqual(result, self.expected_outputs[0])

if __name__ == '__main__':
    unittest.main()