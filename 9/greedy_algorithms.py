import heapq
import random
import time
import matplotlib.pyplot as plt
import networkx as nx


# ------------------- Interval Scheduling -------------------
def interval_scheduling(intervals):
    # Шаг 1: сортируем по времени окончания
    intervals.sort(key=lambda x: x[1])

    selected = []
    last_end = float('-inf')

    # Шаг 2-3: выбираем интервалы жадно
    for start, end in intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected
# ---------------- Задача о выборе заявок (Interval Scheduling) ----------------
# Временная сложность: O(n log n)
# Основная часть времени уходит на сортировку интервалов по времени окончания.
# Жадный выбор корректен, потому что выбирая интервал, который заканчивается раньше всех,
# мы оставляем максимум свободного времени для следующих интервалов,
# что гарантирует наибольшее количество непересекающихся интервалов.

# ------------------- Fractional Knapsack -------------------


def fractional_knapsack(items, capacity):
    # items: список кортежей (value, weight)
    # capacity: вместимость рюкзака

    # Шаг 1: сортируем по удельной стоимости (value/weight)
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    result = []

    for value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # Берём предмет целиком
            total_value += value
            capacity -= weight
            result.append((value, weight, 1.0))  # 100%
        else:
            # Берём часть предмета
            fraction = capacity / weight
            total_value += value * fraction
            result.append((value, weight, fraction))
            capacity = 0
            break

    return result, total_value
# ---------------- Задача о дробном рюкзаке (Fractional Knapsack) ----------------
# Временная сложность: O(n log n)
# Время уходит на сортировку предметов по убыванию удельной стоимости (цене за единицу веса).
# Жадный выбор корректен, потому что мы всегда берём самый выгодный предмет на единицу веса.
# Так как можно брать дробные части предметов, алгоритм всегда приводит к оптимальному решению,
# максимизируя общую стоимость при заданной вместимости рюкзака.

# ------------------- Huffman Coding -------------------


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # Для работы в куче сравниваем по частоте

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freqs):
    # Создание кучи из узлов
    heap = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(heap)

    # Построение дерева
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0]


def build_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.char is not None:
        codes[node.char] = current_code
        return codes

    build_codes(node.left, current_code + "0", codes)
    build_codes(node.right, current_code + "1", codes)
    return codes
# ---------------- Оптимальный префиксный код (Алгоритм Хаффмана) ----------------
# Временная сложность: O(n log n)
# Построение кода включает многократные операции в приоритетной очереди,
# которые выполняются logarithмически, а всего таких операций порядка n.
# Жадный выбор корректен, потому что объединение двух самых редких символов
# минимизирует вклад этих символов в общую длину кодируемого сообщения.
# В итоге получаем оптимальное префиксное дерево, где редко встречающиеся символы
# имеют более длинные коды, что уменьшает итоговую стоимость кодирования по частотам.

# ------------------- Замер времени Хаффмана -------------------


def huffman_time_test(num_symbols):
    # Генерация случайных частот для символов
    symbols = [chr(i % 256) for i in range(num_symbols)]
    freqs = {s: random.randint(1, 1000) for s in symbols}
    start = time.time()
    tree = build_huffman_tree(freqs)
    end = time.time()
    return end - start

# ------------------- Визуализация дерева Хаффмана -------------------


def visualize_huffman_tree(root):
    G = nx.Graph()
    labels = {}

    def add_edges(node, parent=None, edge_label=""):
        if node is None:
            return
        name = f"{node.char if node.char else ''}\n{node.freq}"
        labels[name] = name
        G.add_node(name)
        if parent:
            G.add_edge(parent, name, label=edge_label)
        add_edges(node.left, name, "0")
        add_edges(node.right, name, "1")

    add_edges(root)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=1500, node_color="lightblue")
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Дерево Хаффмана")
    plt.show()

# ------------------- Main -------------------


if __name__ == "__main__":
    # Interval Scheduling
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
    result = interval_scheduling(intervals)
    print("Выбранные интервалы:", result)

    # Fractional Knapsack
    items = [(60, 10), (100, 20), (120, 30), (25, 5)]
    capacity = 50
    result, total_value = fractional_knapsack(items, capacity)
    print("Взятые предметы:", result)
    print("Общая стоимость:", total_value)

    # Huffman Coding
    freqs = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
    tree = build_huffman_tree(freqs)
    codes = build_codes(tree)
    print("Префиксные коды Хаффмана:")
    for char, code in codes.items():
        print(f"{char}: {code}")

    # Визуализация дерева Хаффмана
    visualize_huffman_tree(tree)

    # Замер времени Хаффмана для разных размеров
    sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    times = []
    for size in sizes:
        t = huffman_time_test(size)
        times.append(t)
        print(f"Символов: {size}, Время: {t:.6f} сек")

    # Построение графика зависимости времени
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, marker='o')
    plt.title("Зависимость времени работы алгоритма Хаффмана от размера входных данных")
    plt.xlabel("Количество символов")
    plt.ylabel("Время работы (сек)")
    plt.grid(True)
    plt.show()
