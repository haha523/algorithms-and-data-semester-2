import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline())
        dimensions = [tuple(map(int, file.readline().split())) for _ in range(n)]
    return n, dimensions

def matrix_chain_order(dimensions):
    n = len(dimensions)
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i][0] * dimensions[k][1] * dimensions[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split

def construct_parenthesis(split, i, j):
    if i == j:
        return "A"
    else:
        return f"({construct_parenthesis(split, i, split[i][j])}{construct_parenthesis(split, split[i][j] + 1, j)})"

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    n, dimensions = read_input(input_path)

    dp, split = matrix_chain_order(dimensions)

    optimal_parenthesis = construct_parenthesis(split, 0, n - 1)

    with open(output_path, 'w') as file:
        file.write(optimal_parenthesis + "\n")

if __name__ == '__main__':
    task_scheduler()