from binary_search_tree import BinarySearchTree

if __name__ == '__main__':
    pc_info = """
    Конфигурация ПК:
    - Процессор: 11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50 GHz
    - Оперативная память: 16,0 ГБ (доступно: 15,8 ГБ)
    - Тип системы: 64-разрядная операционная система, процессор x64
    - ОС: Windows 11 Pro
    - Версия: 24H2
    - Сборка ОС: 26100.4946
    - Python: 3.13.3
    """
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)

    tree.inorder(tree.root)
    print("\n")
    tree.preorder(tree.root)
    print("\n")
    tree.postorder(tree.root)
    print("\n")
    tree.inorder_iterative()
