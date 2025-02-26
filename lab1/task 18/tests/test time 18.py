import sys
import time
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from a18 import minimize_cost

def measure_performance():
    costs = [110, 40, 120, 110, 60]
    n = len(costs)

    start_time = time.time()

    min_cost, remaining_coupons, used_coupons_count, used_coupons = minimize_cost(n, costs)

    end_time = time.time()

    execution_time = end_time - start_time

    total_size = sys.getsizeof(min_cost) + sys.getsizeof(remaining_coupons) + sys.getsizeof(
        used_coupons_count) + sys.getsizeof(used_coupons)
    total_size += sum(sys.getsizeof(item) for item in used_coupons)

    print(f"Минимальная стоимость: {min_cost}")
    print(f"Осталось купонов: {remaining_coupons}")
    print(f"Количество дней использования купона: {used_coupons_count}")
    print(f"Даты использования купона: {used_coupons}")
    print(f"Общий размер памяти: {total_size} байт")
    print(f"Время выполнения: {execution_time:.6f} секунд")

if __name__ == '__main__':
    measure_performance()