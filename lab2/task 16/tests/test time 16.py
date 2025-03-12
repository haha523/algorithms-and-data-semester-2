import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b16 import KthMaximum

def measure_memory_and_time(n):
    kth_maximum = KthMaximum()

    start_time = time.time()

    for i in range(1, n + 1):
        kth_maximum.add(i)

    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(kth_maximum)
    queue = [kth_maximum.max_heap]

    for item in kth_maximum.max_heap:
        total_size += sys.getsizeof(item)

    total_size += sys.getsizeof(kth_maximum.elements)

    return total_size, execution_time

if __name__ == "__main__":
    n = 100
    total_size, execution_time = measure_memory_and_time(n)

    print(f"Количество элементов: {n}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")
