import os
import sys

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    def find_min_greater_than(self, key):
        return self._find_min_greater_than(self.root, key)

    def _find_min_greater_than(self, node, key):
        if node is None:
            return 0
        if node.key <= key:
            return self._find_min_greater_than(node.right, key)
        left_result = self._find_min_greater_than(node.left, key)
        return node.key if left_result == 0 else left_result

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    bst = BST()
    results = []

    with open(input_path, 'r') as infile:
        for line in infile:
            command = line.strip().split()
            operation = command[0]
            if operation == '+':
                bst.insert(int(command[1]))
            elif operation == '>':
                result = bst.find_min_greater_than(int(command[1]))
                results.append(result)

    with open(output_path, 'w') as outfile:
        for result in results:
            outfile.write(f"{result}\n")

if __name__ == '__main__':
    task_scheduler()
