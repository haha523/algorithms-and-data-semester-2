import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a12 import can_partition

def measure_performance(numbers):
    start_time = time.time()
    count, indices = can_partition(numbers)
    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(indices)
    for item in indices:
        total_size += sys.getsizeof(item)

    print(f'Индексный список: {indices}')
    print(f'Общий размер памяти: {total_size} байт')
    print(f'Время выполнения: {execution_time:.6f} секунд')

if __name__ == '__main__':
    n = 200
    numbers = [min(i, n // 2) for i in range(1, n + 1)]
    measure_performance(numbers)