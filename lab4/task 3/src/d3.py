import os

def rabin_karp_search(pattern, text):
    d = 256
    q = 101

    m = len(pattern)
    n = len(text)

    if m == 0 or n == 0 or m > n:
        return []

    h = pow(d, m - 1) % q
    p_hash = 0
    t_hash = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    occurrences = []

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if pattern == text[i:i + m]:
                occurrences.append(i + 1)

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            t_hash = t_hash if t_hash >= 0 else t_hash + q

    return occurrences

def process_files(input_file='input.txt', output_file='output.txt'):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    txtf_dir = os.path.join(parent_dir, 'txtf')

    if not os.path.exists(txtf_dir):
        os.makedirs(txtf_dir)

    input_path = os.path.join(txtf_dir, input_file)
    output_path = os.path.join(txtf_dir, output_file)

    with open(input_path, 'r') as f:
        p = f.readline().strip()
        t = f.readline().strip()

    occurrences = rabin_karp_search(p, t)

    with open(output_path, 'w') as f:
        f.write(f"{len(occurrences)}\n")
        if occurrences:
            f.write(" ".join(map(str, occurrences)) + "\n")

if __name__ == "__main__":
    process_files()
