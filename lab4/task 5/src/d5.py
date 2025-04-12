import os

def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def process_prefix_function(input_file='input.txt', output_file='output.txt'):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    txtf_dir = os.path.join(parent_dir, 'txtf')

    if not os.path.exists(txtf_dir):
        os.makedirs(txtf_dir)

    input_path = os.path.join(txtf_dir, input_file)
    output_path = os.path.join(txtf_dir, output_file)

    with open(input_path, 'r') as f:
        s = f.readline().strip()

    prefix_func = compute_prefix_function(s)

    with open(output_path, 'w') as f:
        f.write(' '.join(map(str, prefix_func)) + '\n')

if __name__ == "__main__":
    process_prefix_function()
