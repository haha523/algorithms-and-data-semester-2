import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b11 import AVLTree

def measure_performance(n):
    tree = AVLTree()
    root = None

    start_time = time.time()

    for i in range(n):
        root = tree.insert(root, i)

    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(tree)
    total_size += sys.getsizeof(root)
    for node in traverse_tree(root):
        total_size += sys.getsizeof(node)

    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время вставки {n} элементов: {execution_time:.6f} секунд")

def traverse_tree(node):
    if node is None:
        return []
    return traverse_tree(node.left) + [node] + traverse_tree(node.right)

if __name__ == '__main__':
    n = 100
    measure_performance(n)
