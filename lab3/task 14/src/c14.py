import os
import heapq

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as f:
        N = int(f.readline().strip())
        d, v = map(int, f.readline().strip().split())
        R = int(f.readline().strip())

        bus_routes = []
        for _ in range(R):
            start, dep_time, end, arr_time = map(int, f.readline().strip().split())
            bus_routes.append((start, dep_time, end, arr_time))

    graph = {i: [] for i in range(1, N + 1)}
    for start, dep_time, end, arr_time in bus_routes:
        graph[start].append((dep_time, end, arr_time))

    min_time = {i: float('inf') for i in range(1, N + 1)}
    min_time[d] = 0
    priority_queue = [(0, d)]

    while priority_queue:
        current_time, current_village = heapq.heappop(priority_queue)

        if current_time > min_time[current_village]:
            continue

        for dep_time, next_village, arr_time in graph[current_village]:
            if current_time <= dep_time:
                if arr_time < min_time[next_village]:
                    min_time[next_village] = arr_time
                    heapq.heappush(priority_queue, (arr_time, next_village))

    result = min_time[v]
    with open(output_path, 'w') as f:
        f.write(str(result) if result != float('inf') else '-1')

if __name__ == "__main__":
    task_scheduler()
