import os

def can_partition(nums):
    total_sum = sum(nums)

    if total_sum % 3 != 0:
        return 0

    target_sum = total_sum // 3
    n = len(nums)

    sums = {0}

    for num in nums:
        new_sums = set()
        for s in sums:
            new_sum = s + num
            if new_sum <= target_sum:
                new_sums.add(new_sum)
        sums.update(new_sums)

    return 1 if target_sum in sums else 0

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as file:
        n = int(file.readline().strip())
        nums = list(map(int, file.readline().strip().split()))

    result = can_partition(nums)

    with open(output_path, 'w') as file:
        file.write(str(result) + '\n')

if __name__ == "__main__":
    task_scheduler()