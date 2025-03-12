import os
from collections import deque

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = AVLNode(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def level_order_traversal(self):
        if not self.root:
            return []

        result = []
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = os.path.join(base_dir, '..', 'txtf')

    os.makedirs(txtf_dir, exist_ok=True)

    input_path = os.path.join(txtf_dir, input_file)
    output_path = os.path.join(txtf_dir, output_file)

    with open(input_path, 'r') as f:
        N = int(f.readline())
        nodes = []
        for _ in range(N):
            K, L, R = map(int, f.readline().split())
            nodes.append((K, L, R))
        X = int(f.readline())

    avl_tree = AVLTree()
    for node in nodes:
        avl_tree.insert(node[0])

    avl_tree.insert(X)
    level_order = avl_tree.level_order_traversal()

    node_to_index = {node: i + 1 for i, node in enumerate(level_order)}

    with open(output_path, 'w') as f:
        f.write(f"{len(level_order)}\n")
        for node in level_order:
            left_index = node_to_index.get(node.left, 0)
            right_index = node_to_index.get(node.right, 0)
            f.write(f"{node.key} {left_index} {right_index}\n")

if __name__ == "__main__":
    task_scheduler()
