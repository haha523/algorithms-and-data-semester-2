import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline())
        costs = [int(file.readline()) for _ in range(n)]
    return n, costs

def minimize_cost(n, costs):
    dp = [[float('inf')] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(n + 1):
            if dp[i - 1][j] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + costs[i - 1])
                if costs[i - 1] > 100:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + costs[i - 1])

            if j > 0 and dp[i - 1][j] != float('inf'):
                dp[i][j - 1] = min(dp[i][j - 1], dp[i - 1][j])

    min_cost = float('inf')
    remaining_coupons = 0
    for j in range(n + 1):
        if dp[n][j] < min_cost:
            min_cost = dp[n][j]
            remaining_coupons = j

    used_coupons = []
    j = remaining_coupons
    for i in range(n, 0, -1):
        if j < n and dp[i][j] == dp[i - 1][j + 1]:
            used_coupons.append(i)
            j += 1
        elif dp[i][j] == dp[i - 1][j] + costs[i - 1]:
            pass
        elif costs[i - 1] > 100 and dp[i][j] == dp[i - 1][j - 1] + costs[i - 1]:
            j -= 1

    used_coupons.reverse()
    return min_cost, remaining_coupons, len(used_coupons), used_coupons

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    n, costs = read_input(input_path)

    min_cost, remaining_coupons, used_coupons_count, used_coupons = minimize_cost(n, costs)

    with open(output_path, 'w') as file:
        file.write(f"{min_cost}\n")
        file.write(f"{remaining_coupons} {used_coupons_count}\n")
        for day in used_coupons:
            file.write(f"{day}\n")

if __name__ == '__main__':
    task_scheduler()