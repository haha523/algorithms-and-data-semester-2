import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c13 import count_gardens

def measure_time_and_memory(input_file, output_file):

    start_time = time.time()
    count_gardens()
    end_time = time.time()
    execution_time = end_time - start_time

    with open(output_file, 'r') as f:
        result = f.read().strip()

    total_size = sys.getsizeof(result)

    print(f"Количество: {result}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    input_file = '../txtf/input.txt'
    output_file = '../txtf/output.txt'

    measure_time_and_memory(input_file, output_file)
