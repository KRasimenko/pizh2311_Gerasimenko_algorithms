class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
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
        if node is None:
            return None

        if value < node.value:
            node.left = self._deletenode(node.left, value)
        elif value > node.value:
            node.right = self._deletenode(node.right, value)
        else:
            # Случай 1: Нет детей
            if node.left is None and node.right is None:
                return None

            # Случай 2: Один ребёнок
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Случай 3: Два ребёнка
            min_node = self.find_min(node.right)
            node.value = min_node.value
            node.right = self._deletenode(node.right, min_node.value)

        return node

    def delete(self, value):
        self.root = self._deletenode(self.root, value)  

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def find_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current
