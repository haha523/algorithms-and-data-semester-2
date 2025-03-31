import os
from collections import defaultdict

def count_components(input_file='input.txt', output_file='output.txt', to_file=True):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as f:
        n, m = map(int, f.readline().strip().split())
        graph = defaultdict(list)

        for _ in range(m):
            u, v = map(int, f.readline().strip().split())
            graph[u].append(v)
            graph[v].append(u)

    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    component_count = 0

    for vertex in range(1, n + 1):
        if vertex not in visited:
            dfs(vertex, visited)
            component_count += 1

    if to_file:
        with open(output_path, 'w') as f:
            f.write(f"{component_count}\n")
    return component_count
