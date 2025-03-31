import os
from collections import deque

def find_min_k():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_path = os.path.join(base_dir, 'txtf', 'output.txt')

    with open(input_path, 'r') as f:
        lines = f.readlines()

    N, M = map(int, lines[0].split())
    adj = [[] for _ in range(N + 1)]
    reverse_adj = [[] for _ in range(N + 1)]

    for line in lines[1:M + 1]:
        u, v = map(int, line.split())
        adj[u].append(v)
        reverse_adj[v].append(u)

    def is_weakly_k_connected(K):
        for start in range(1, N + 1):
            visited = [False] * (N + 1)
            q = deque()
            q.append((start, 0))
            visited[start] = True

            while q:
                node, violations = q.popleft()
                if violations > K:
                    continue

                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((neighbor, violations))

                for neighbor in reverse_adj[node]:
                    if not visited[neighbor] and violations + 1 <= K:
                        visited[neighbor] = True
                        q.append((neighbor, violations + 1))

            for i in range(1, N + 1):
                if i != start and not visited[i]:
                    return False
        return True

    low = 0
    high = N

    while low < high:
        mid = (low + high) // 2
        if is_weakly_k_connected(mid):
            high = mid
        else:
            low = mid + 1

    with open(output_path, 'w') as f:
        f.write(str(low))

if __name__ == "__main__":
    find_min_k()
