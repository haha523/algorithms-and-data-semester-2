import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a6 import largest_number

def generate_large_input(n):
    return [str(i) for i in range(n, 0, -1)]

def main():
    n = 1000
    digits = generate_large_input(n)

    start_time = time.time()

    result = largest_number(digits)

    end_time = time.time()
    execution_time = end_time - start_time

    total_size = sys.getsizeof(result)
    for item in digits:
        total_size += sys.getsizeof(item)

    print(f"Результат: {result[:20]}...")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == "__main__":
    main()