import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a13 import can_partition

def measure_performance(numbers):
    start_time = time.time()
    result = can_partition(numbers)
    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(result)
    total_size += sys.getsizeof(numbers)

    print(f"Результаты дивизиона: {result}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == '__main__':
    numbers = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    measure_performance(numbers)