import time
import tracemalloc

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if len(lines) == 2:
            return int(lines[0]), list(map(int, lines[1].split()))

def write_to_file(data, file_name):
    with open(file_name, 'w') as file:
        if isinstance(data, (list, tuple)):
            if isinstance(data, tuple):
                file.write(' '.join(map(str, data[0])) + '\n')
                file.write(' '.join(map(str, data[1])))
            elif isinstance(data[0], list):
                for row in data:
                    file.write(' '.join(map(str, row)) + '\n')
            else:
                file.write(' '.join(map(str, data)))
        else:
            file.write(str(data))

def measure_performance(func, *args):
    start_time = time.perf_counter()
    tracemalloc.start()

    result = func(*args)

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f'Execution time: {time.perf_counter() - start_time:.6f} seconds')
    print(f'Memory usage: {peak_memory / 1024 ** 2:.6f} MB')

    return result

def display_input_output(inputs, result):
    print(f'Input data:\n{inputs}')
    print(f'Result:\n{result}')