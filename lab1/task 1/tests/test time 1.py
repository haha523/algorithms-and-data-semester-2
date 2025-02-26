import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a1 import fractional_knapsack

def generate_items(n):
    items = [(i * 100, i * 10) for i in range(1, n + 1)]
    return items

n = 1000
W = 10000

start_time = time.time()
items_list = generate_items(n)
max_value = fractional_knapsack(n, W, items_list)
end_time = time.time()
execution_time = end_time - start_time

total_size = sys.getsizeof(items_list)
for item in items_list:
    total_size += sys.getsizeof(item)

print(f"Максимальное значение: {max_value:.4f}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.6f} секунд")