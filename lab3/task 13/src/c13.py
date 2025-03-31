import os
from collections import deque

def count_gardens():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_path = os.path.join(base_dir, 'txtf', 'output.txt')

    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        with open(output_path, 'w') as f:
            f.write('0')
        return

    N, M = map(int, lines[0].split())
    grid = [list(line.replace(' ', '')) for line in lines[1:N + 1]]

    visited = [[False for _ in range(M)] for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == '#' and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if grid[nx][ny] == '#' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                count += 1

    with open(output_path, 'w') as f:
        f.write(str(count))

if __name__ == "__main__":
    count_gardens()
