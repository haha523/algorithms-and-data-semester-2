import os

def fractional_knapsack(n, W, items):
    for i in range(n):
        items[i] = (items[i][0], items[i][1], items[i][0] / items[i][1])

    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    remaining_capacity = W

    for value, weight, unit_value in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += unit_value * remaining_capacity
            remaining_capacity = 0

    return total_value

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

with open(input_file_path, 'r') as file:
    n, W = map(int, file.readline().split())
    items = [tuple(map(int, file.readline().split())) for _ in range(n)]

max_value = fractional_knapsack(n, W, items)

with open(output_file_path, 'w') as file:
    file.write(f"{max_value:.4f}\n")