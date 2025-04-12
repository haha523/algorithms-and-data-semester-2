import os
import sys
import time
import tracemalloc

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d3 import rabin_karp_search

def измерить_производительность():
    образец = "Test"
    текст = "testTesttesT"

    tracemalloc.start()

    начало = time.time()
    результат = rabin_karp_search(образец, текст)
    конец = time.time()
    использование_памяти = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(f"Результат поиска: {результат}")
    print(f"Общий размер памяти: {использование_памяти} байт")
    print(f"Время выполнения: {конец - начало:.6f} секунд")

if __name__ == "__main__":
    измерить_производительность()
