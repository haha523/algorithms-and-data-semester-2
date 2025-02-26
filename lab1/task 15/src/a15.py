import os

def is_matching_pair(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '[' and closing == ']') or \
           (opening == '{' and closing == '}')

def find_max_valid_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if is_matching_pair(s[i], s[j]):
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    result = []
    i, j = 0, n - 1
    while i <= j:
        if is_matching_pair(s[i], s[j]):
            result.append(s[i])
            result.append(s[j])
            i += 1
            j -= 1
        elif dp[i][j] == dp[i + 1][j]:
            i += 1
        else:
            j -= 1

    return ''.join(result)

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as file:
        s = file.read().strip()

    result = find_max_valid_subsequence(s)

    with open(output_path, 'w') as file:
        file.write(result)

task_scheduler()