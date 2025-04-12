import os
import sys
import time
import tracemalloc

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d5 import compute_prefix_function

def измерить_производительность():
    тестовые_строки = [
        ("aaaAAA", "Пример 1 (aaaAAA)"),
        ("abacaba", "Пример 2 (abacaba)"),
    ]

    for s, описание in тестовые_строки:
        print(f"\n{описание}:")

        tracemalloc.start()
        начало = time.time()
        результат = compute_prefix_function(s)
        конец = time.time()
        память = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        print(" ".join(map(str, результат)))
        print(f"Общий размер памяти: {память} байт")
        print(f"Время выполнения: {конец - начало:.6f} секунд")

if __name__ == "__main__":
    измерить_производительность()
