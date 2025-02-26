import os

def can_partition(numbers):
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return -1, []

    target_sum = total_sum // 2
    n = len(numbers)

    dp = [False] * (target_sum + 1)
    dp[0] = True

    for num in numbers:
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    if not dp[target_sum]:
        return -1, []

    subset = []
    w = target_sum
    for i in range(n - 1, -1, -1):
        if w >= numbers[i] and dp[w - numbers[i]]:
            subset.append(i + 1)
            w -= numbers[i]

    return len(subset), subset

def main():
    txtf_directory = os.path.join(os.path.dirname(__file__), '..', 'txtf')

    if not os.path.exists(txtf_directory):
        os.makedirs(txtf_directory)

    input_file_path = os.path.join(txtf_directory, 'input.txt')

    if not os.path.exists(input_file_path):
        print(f"File {input_file_path} не найдено. Создайте файл с входными данными.")
        return

    with open(input_file_path, 'r') as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split()))

    count, indices = can_partition(numbers)

    output_file_path = os.path.join(txtf_directory, 'output.txt')
    with open(output_file_path, 'w') as f:
        if count == -1:
            f.write("-1\n")
        else:
            f.write(f"{count}\n")
            f.write(" ".join(map(str, indices)))

if __name__ == "__main__":
    main()