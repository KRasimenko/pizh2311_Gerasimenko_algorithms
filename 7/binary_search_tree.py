class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Средний случай: O(log n)
        # Худший случай (дерево перекошено): O(n)
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        # Средний случай: O(log n)
        # Худший случай: O(n)
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def _deletenode(self, node, value):
        # Средний случай: O(log n)
        # Худший случай: O(n)
        if node is None:
            return None

        if value < node.value:
            node.left = self._deletenode(node.left, value)
        elif value > node.value:
            node.right = self._deletenode(node.right, value)
        else:
            # Случай 1: Нет детей — O(1)

            if node.left is None and node.right is None:
                return None

            # Случай 2: Один ребёнок — O(1)

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Случай 3: Два ребёнка — O(h)
            # где h — высота дерева
            # (нужно найти min в правом поддереве)

            min_node = self.find_min(node.right)
            node.value = min_node.value
            node.right = self._deletenode(node.right, min_node.value)

        return node

    def delete(self, value):
        # Средний случай: O(log n)
        # Худший случай: O(n)
        self.root = self._deletenode(self.root, value)

    def find_min(self, node):
        # Средний случай: O(log n)
        # Худший случай: O(n)
        current = node
        while current.left:
            current = current.left
        return current

    def find_max(self, node):
        # Средний случай: O(log n)
        # Худший случай: O(n)
        current = node
        while current.right:
            current = current.right
        return current

    def inorder(self, node):
        # Левый - Корень - Правый
        # Сложность: O(n)
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def preorder(self, node):
        # Корень - Левый - Правый
        # Сложность: O(n)
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        # Левый - Правый - Корень
        # Сложность: O(n)
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

    def inorder_iterative(self):
        # Сложность: O(n)
        # Мы посещаем каждый узел ровно один раз.
        stack = []
        current = self.root

        while current is not None or stack:
            # Идём в самый левый узел
            while current is not None:
                stack.append(current)
                current = current.left

            # Берём узел из стека
            current = stack.pop()
            print(current.value)

            # Переходим в правое поддерево
            current = current.right

    def height(self, node):
        # Сложность: O(n)
        if node is None:
            return -1  # или 0, если хочешь считать по-другому
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_valid_bst(self):
        return self._validate(self.root, float('-inf'), float('inf'))
    
    def _validate(self, node, low, high):
        if node is None:
            return True

        # Проверка ключевого свойства BST
        if not (low < node.value < high):
            return False

        return (self._validate(node.left, low, node.value) and
                self._validate(node.right, node.value, high))
 
    def print_tree(self, node=None, indent="", is_left=True):
        if node is None:
            node = self.root
            if node is None:
                print("<empty>")
                return

        if node.right:
            self.print_tree(node.right, indent +
                            ("    " if is_left else "│   "), False)

        print(indent + ("└── " if is_left else "┌── ") + str(node.value))

        if node.left:
            self.print_tree(node.left, indent +
                            ("    " if is_left else "│   "), True)
