import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b7 import task_scheduler

def is_bst(node, min_key, max_key, nodes):
    if node == -1:
        return True

    key, left, right = nodes[node]

    if key < min_key or key >= max_key:
        return False

    return (is_bst(left, min_key, key, nodes) and
            is_bst(right, key, max_key, nodes))

def task_scheduler(input_file='input.txt'):
    input_path = os.path.join('..', 'txtf', input_file)

    with open(input_path, 'r') as file:
        n = int(file.readline().strip())
        nodes = []

        for _ in range(n):
            line = list(map(int, file.readline().strip().split()))
            nodes.append(line)

    return is_bst(0, -2 ** 31, 2 ** 31 - 1, nodes)

def measure_performance(input_file='input.txt'):
    start_time = time.time()
    result = task_scheduler(input_file)
    end_time = time.time()
    execution_time = end_time - start_time
    total_size = sys.getsizeof(result)

    print(f"Результаты тестов: {'CORRECT' if result else 'INCORRECT'}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == '__main__':
    measure_performance('input.txt')
