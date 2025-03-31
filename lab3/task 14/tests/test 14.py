import unittest
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c14 import task_scheduler

class TestBusRoutes(unittest.TestCase):

    def run_task_scheduler(self, input_data):
        # given
        original_stdin = sys.stdin
        sys.stdin = StringIO(input_data)

        # when
        try:
            task_scheduler()
            with open('../txtf/output.txt', 'r') as f:
                result = f.read().strip()
                return int(result)

        # then
        finally:
            sys.stdin = original_stdin

    def test_case_1(self):
        # given
        input_data = "3\n1 3\n4\n1 0 2 5\n1 1 2 3\n2 3 3 5\n1 1 3 10\n"
        # when
        expected_output = 5
        # then
        self.assertEqual(self.run_task_scheduler(input_data), expected_output)

    def test_case_2(self):
        # given
        input_data = "3\n1 3\n0\n"
        # when
        expected_output = 5
        # then
        self.assertEqual(self.run_task_scheduler(input_data), expected_output)

    def test_case_3(self):
        # given
        input_data = "4\n1 4\n5\n1 0 2 5\n2 5 3 10\n3 11 4 15\n1 6 4 20\n1 3 4 25\n"
        # when
        expected_output = 5
        # then
        self.assertEqual(self.run_task_scheduler(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()
