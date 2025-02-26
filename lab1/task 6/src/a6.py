import os

def largest_number(digits):
    digits.sort(key=lambda x: x * 3, reverse=True)
    return ''.join(digits)

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
        numbers = f.readline().strip().split()

    result = largest_number(numbers)

    with open(os.path.join(txtf_directory, 'output.txt'), 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()