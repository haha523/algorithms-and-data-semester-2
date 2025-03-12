import os

def is_bst(node, min_key, max_key, nodes):
    if node == -1:
        return True

    key, left, right = nodes[node]

    if key < min_key or key >= max_key:
        return False

    return (is_bst(left, min_key, key, nodes) and
            is_bst(right, key, max_key, nodes))

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as file:
        n = int(file.readline().strip())
        nodes = []

        for _ in range(n):
            line = list(map(int, file.readline().strip().split()))
            nodes.append(line)

    if is_bst(0, -2 ** 31, 2 ** 31 - 1, nodes):
        result = "CORRECT"
    else:
        result = "INCORRECT"

    with open(output_path, 'w') as file:
        file.write(result)

if __name__ == '__main__':
    task_scheduler()
