import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a15 import find_max_valid_subsequence

def measure_performance(input_string):
    start_time = time.time()
    result = find_max_valid_subsequence(input_string)
    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(result)
    total_size += sys.getsizeof(input_string)

    print(f"Строка ввода: {input_string}")
    print(f"Результат: {result}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == '__main__':
    input_string = "([)]"
    measure_performance(input_string)