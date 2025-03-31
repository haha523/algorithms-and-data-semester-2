import os
from collections import defaultdict, deque

def is_bipartite(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = {}

    def bfs(start):
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for vertex in range(1, n + 1):
        if vertex not in color:
            if not bfs(vertex):
                return 0

    return 1

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as f:
        n, m = map(int, f.readline().strip().split())
        edges = [tuple(map(int, f.readline().strip().split())) for _ in range(m)]

    result = is_bipartite(n, edges)

    with open(output_path, 'w') as f:
        f.write(f"{result}\n")

    return str(result)

if __name__ == "__main__":
    task_scheduler(input_file='input.txt', output_file='output.txt')
