import unittest

from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    # helpers
    def insert_values(self, values):
        for v in values:
            self.tree.insert(v)

    # Проверка свойств BST
    def is_valid_bst(self, node, low=float("-inf"), high=float("inf")):
        if node is None:
            return True
        if not (low < node.value < high):
            return False
        return (self.is_valid_bst(node.left, low, node.value) and
                self.is_valid_bst(node.right, node.value, high))

    # TEST INSERT
    def test_insert(self):
        values = [5, 3, 7, 2, 4]
        self.insert_values(values)

        # Проверяем, что дерево стало корректным BST
        self.assertTrue(self.is_valid_bst(self.tree.root))

        # Проверяем, что можно найти каждое значение
        for v in values:
            self.assertIsNotNone(self.tree.search(v))

    # TEST SEARCH
    def test_search(self):
        self.insert_values([5, 3, 7])
        self.assertIsNotNone(self.tree.search(5))
        self.assertIsNotNone(self.tree.search(3))
        self.assertIsNotNone(self.tree.search(7))
        self.assertIsNone(self.tree.search(10))

    # TEST DELETE — удаление листа
    def test_delete_leaf(self):
        self.insert_values([5, 3, 7])
        self.tree.delete(3)
        self.assertIsNone(self.tree.search(3))
        self.assertTrue(self.is_valid_bst(self.tree.root))

    # TEST DELETE — удаление с одним ребёнком
    def test_delete_one_child(self):
        # У узла 3 есть только левый ребёнок (2)
        self.insert_values([5, 3, 2])
        self.tree.delete(3)
        self.assertIsNone(self.tree.search(3))
        self.assertTrue(self.is_valid_bst(self.tree.root))

    # TEST DELETE — удаление с двумя детьми
    def test_delete_two_children(self):
        # У 5 два потомка (3 и 7)
        self.insert_values([5, 3, 7, 6, 8])
        self.tree.delete(7)
        self.assertIsNone(self.tree.search(7))
        self.assertTrue(self.is_valid_bst(self.tree.root))

    # TEST HEIGHT
    def test_height(self):
        self.insert_values([5, 3, 7, 2, 4])
        h = self.tree.height(self.tree.root)
        self.assertEqual(h, 2)  # 5 → 3 → 2

    # TEST INORDER (sorted)
    def test_inorder(self):
        self.insert_values([5, 3, 7, 2, 4])

        result = []

        def capture_inorder(node):
            if node:
                capture_inorder(node.left)
                result.append(node.value)
                capture_inorder(node.right)

        capture_inorder(self.tree.root)
        self.assertEqual(result, [2, 3, 4, 5, 7])

    # TEST INORDER ITERATIVE
    def test_inorder_iterative(self):
        self.insert_values([5, 3, 7, 2, 4])

        output = []
        # временно переопределим print
        import builtins
        original_print = builtins.print
        builtins.print = lambda v: output.append(v)

        self.tree.inorder_iterative()

        builtins.print = original_print  # вернуть print

        self.assertEqual(output, [2, 3, 4, 5, 7])


if __name__ == '__main__':
    unittest.main()
