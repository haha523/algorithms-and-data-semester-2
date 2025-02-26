import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a19 import read_input, matrix_chain_order, construct_parenthesis

def measure_performance(dimensions):
    start_time = time.time()

    dp, split = matrix_chain_order(dimensions)
    optimal_parenthesis = construct_parenthesis(split, 0, len(dimensions) - 1)

    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(dp) + sys.getsizeof(split) + sys.getsizeof(optimal_parenthesis)

    for item in dp:
        total_size += sys.getsizeof(item)
    for item in split:
        total_size += sys.getsizeof(item)

    print(f"Оптимальные скобки: {optimal_parenthesis}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == '__main__':
    dimensions = [(10, 50), (50, 90), (90, 20)]
    measure_performance(dimensions)