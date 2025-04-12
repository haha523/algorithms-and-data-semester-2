import os
import sys
import time
import tracemalloc

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d7 import find_lcs

def измерить_производительность():
    s = "cool"
    t = "toolbox"

    print(f"Строка s: '{s}' (длина {len(s)})")
    print(f"Строка t: '{t}' (длина {len(t)})")

    tracemalloc.start()

    начало = time.time()
    i, j, l = find_lcs(s, t)
    конец = time.time()
    использование_памяти = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    assert f"{i} {j} {l}" == "1 1 3", "Результат не соответствует ожидаемому"
    if l > 0:
        assert s[i:i + l] == t[j:j + l], "Найденная подстрока не совпадает"

    print("\nРезультат:")
    print(f"{i} {j} {l}")
    print(f"\nПроизводительность:")
    print(f"Общий размер памяти: {использование_памяти} байт")
    print(f"Время выполнения: {конец - начало:.6f} секунд")

if __name__ == "__main__":
    измерить_производительность()
