import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c14 import task_scheduler

def measure_time_and_memory(input_file, output_file):

    start_time = time.time()
    task_scheduler(input_file=input_file, output_file=output_file)
    end_time = time.time()
    execution_time = end_time - start_time

    with open(output_file, 'r') as f:
        result = f.read()

    total_size = sys.getsizeof(result) + sys.getsizeof(input_file) + sys.getsizeof(output_file)

    print(f"Результат: {result.strip()}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    input_file = '../txtf/input.txt'
    output_file = '../txtf/output.txt'

    with open(input_file, 'w') as f:
        f.write("3\n1 3\n4\n1 0 2 5\n1 1 2 3\n2 3 3 5\n1 1 3 10\n")

    measure_time_and_memory(input_file, output_file)
