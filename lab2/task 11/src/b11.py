import os

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def exists(self, root, key):
        if not root:
            return False
        if key < root.key:
            return self.exists(root.left, key)
        elif key > root.key:
            return self.exists(root.right, key)
        else:
            return True

    def next(self, root, key):
        succ = None
        while root:
            if root.key > key:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ.key if succ else 'none'

    def prev(self, root, key):
        pred = None
        while root:
            if root.key < key:
                pred = root
                root = root.right
            else:
                root = root.left
        return pred.key if pred else 'none'

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    tree = AVLTree()
    root = None
    results = []

    with open(input_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            command = parts[0]
            if command == 'insert':
                root = tree.insert(root, int(parts[1]))
            elif command == 'delete':
                root = tree.delete(root, int(parts[1]))
            elif command == 'exists':
                results.append("true" if tree.exists(root, int(parts[1])) else "false")
            elif command == 'next':
                results.append(str(tree.next(root, int(parts[1]))))
            elif command == 'prev':
                results.append(str(tree.prev(root, int(parts[1]))))

    with open(output_path, 'w') as f:
        f.write("\n".join(results) + "\n")

if __name__ == '__main__':
    task_scheduler('input.txt', 'output.txt')
