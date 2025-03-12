import sys
import time
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b3 import BST

def measure_performance():
    bst = BST()
    test_values = random.sample(range(1, 1000001), 100000)

    start_time = time.time()

    for value in test_values:
        bst.insert(value)

    end_time = time.time()
    execution_time_insert = end_time - start_time
    total_size = sys.getsizeof(bst)

    start_time = time.time()
    result = bst.find_min_greater_than(50000)
    end_time = time.time()
    execution_time_search = end_time - start_time

    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения вставки: {execution_time_insert:.6f} секунд")
    print(f"Время выполнения поиска: {execution_time_search:.6f} секунд")
    print(f"Результат поиска: {result}")

if __name__ == '__main__':
    measure_performance()
