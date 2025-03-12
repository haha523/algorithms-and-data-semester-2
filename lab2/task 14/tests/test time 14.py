import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b14 import AVLTree

def measure_memory_and_time(n):
    avl_tree = AVLTree()

    start_time = time.time()

    for i in range(1, n + 1):
        avl_tree.insert(i)

    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(avl_tree)
    queue = [avl_tree.root]

    while queue:
        node = queue.pop(0)
        total_size += sys.getsizeof(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return total_size, execution_time

if __name__ == "__main__":
    n = 100
    total_size, execution_time = measure_memory_and_time(n)

    print(f"Количество кнопок: {n}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")
