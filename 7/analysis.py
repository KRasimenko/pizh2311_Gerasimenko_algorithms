import random
import time

import matplotlib.pyplot as plt

from binary_search_tree import BinarySearchTree


def build_balanced_tree(n):
    """Строит дерево, вставляя элементы в случайном порядке."""
    values = list(range(n))
    random.shuffle(values)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


def build_degenerate_tree(n):
    """Строит дерево, вставляя элементы в отсортированном порядке."""
    tree = BinarySearchTree()
    for v in range(n):
        tree.insert(v)
    return tree


def measure_search_time(tree, n_search=1000):
    """Замеряет время поиска случайных элементов."""
    values = [random.randint(0, 10**9) for _ in range(n_search)]

    start = time.time()
    for v in values:
        tree.search(v)
    end = time.time()

    return end - start


# ДОБАВЛЯЕМ print_tree В КЛАСС

def bst_print_tree(self, node=None, indent="", is_left=True):
    """Текстовая визуализация дерева."""
    if node is None:
        node = self.root
        if node is None:
            print("<empty>")
            return

    if node.right:
        bst_print_tree(self, node.right, indent +
                       ("    " if is_left else "│   "), False)

    print(indent + ("└── " if is_left else "┌── ") + str(node.value))

    if node.left:
        bst_print_tree(self, node.left, indent +
                       ("    " if is_left else "│   "), True)


BinarySearchTree.print_tree = bst_print_tree


def run_experiment():
    sizes = [1000, 5000, 10000, 50000]

    print(f"{'Размер':10} {'Сбалансированное':20} {'Вырожденное':20}")
    print("-" * 55)

    for n in sizes:
        balanced = build_balanced_tree(n)
        t_bal = measure_search_time(balanced)

        degenerate = build_degenerate_tree(n)
        t_deg = measure_search_time(degenerate)

        print(f"{n:<10} {t_bal:<20.6f} {t_deg:<20.6f}")


def build_graphs():
    sizes = [1000, 5000, 10000, 20000, 30000]

    balanced_times = []
    degenerate_times = []

    for n in sizes:
        balanced = build_balanced_tree(n)
        degenerate = build_degenerate_tree(n)

        t_bal = measure_search_time(balanced)
        t_deg = measure_search_time(degenerate)

        balanced_times.append(t_bal)
        degenerate_times.append(t_deg)
        print(f"n={n}: balanced={t_bal:.6f}, degenerate={t_deg:.6f}")

    plt.figure(figsize=(10, 5))

    plt.semilogy(sizes, balanced_times, marker='o',
                 label="Сбалансированное дерево (O(log n))")
    plt.semilogy(sizes, degenerate_times, marker='o',
                 label="Вырожденное дерево (O(n))")

    plt.title("Зависимость времени поиска от количества элементов (log scale)")
    plt.xlabel("Количество элементов")
    plt.ylabel("Время поиска 1000 операций (сек.) — лог шкала")
    plt.grid(True, which="both")
    plt.legend()

    plt.tight_layout()
    plt.show(block=True)


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
    values = list(range(1, 16))
    random.shuffle(values)

    tree_balanced = BinarySearchTree()
    for v in values:
        tree_balanced.insert(v)

    print("Случайный порядок:", values)
    print("Высота:", tree_balanced.height(tree_balanced.root))

    sorted_values = list(range(1, 16))

    tree_degenerate = BinarySearchTree()
    for v in sorted_values:
        tree_degenerate.insert(v)

    print("Отсортированный порядок:", sorted_values)
    print("Высота:", tree_degenerate.height(tree_degenerate.root))

    run_experiment()

    print("\nСбалансированное дерево:")
    tree_balanced.print_tree()

    print("\nВырожденное дерево:")
    tree_degenerate.print_tree()

    print("\nГРАФИКИ")
    build_graphs()
