import os

def naive_pattern_search(pattern, text):
    occurrences = []
    len_p = len(pattern)
    len_t = len(text)

    for i in range(len_t - len_p + 1):
        match = True
        for j in range(len_p):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i + 1)  

    return occurrences

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    txtf_dir = os.path.join(parent_dir, 'txtf')

    if not os.path.exists(txtf_dir):
        os.makedirs(txtf_dir)

    input_path = os.path.join(txtf_dir, input_file)
    output_path = os.path.join(txtf_dir, output_file)

    with open(input_path, 'r') as f:
        p = f.readline().strip()
        t = f.readline().strip()

    occurrences = naive_pattern_search(p, t)

    with open(output_path, 'w') as f:
        f.write(f"{len(occurrences)}\n")
        if occurrences:
            f.write(" ".join(map(str, occurrences)) + "\n")
        else:
            f.write("\n")

if __name__ == "__main__":
    task_scheduler()
