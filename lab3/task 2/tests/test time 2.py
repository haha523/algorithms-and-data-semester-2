import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c2 import count_components

def measure_time_and_memory(input_file, output_file):

    start_time = time.time()
    result = count_components(input_file=input_file, output_file=output_file, to_file=False)
    end_time = time.time()
    execution_time = end_time - start_time
    total_size = sys.getsizeof(result)
    total_size += sys.getsizeof(input_file) + sys.getsizeof(output_file)

    print(f"Количество подключенных компонентов: {result}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    input_file = '../txtf/input.txt'
    output_file = '../txtf/output.txt'

    with open(input_file, 'w') as f:
        f.write("4 2\n1 2\n3 2\n")

    measure_time_and_memory(input_file, output_file)
