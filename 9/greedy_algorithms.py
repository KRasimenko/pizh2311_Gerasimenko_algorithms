import heapq


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
    heap = []

    # Создаём узлы для каждого символа
    for char, freq in freqs.items():
        heapq.heappush(heap, Node(char, freq))

    # Построение дерева
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0]  # корень дерева


def build_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}

    if node is None:
        return codes

    # Если лист — это символ
    if node.char is not None:
        codes[node.char] = current_code
        return codes

    # Идём влево → добавляем "0"
    build_codes(node.left, current_code + "0", codes)
    # Идём вправо → добавляем "1"
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


if __name__ == "__main__":
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10),
                  (8, 11)]
    result = interval_scheduling(intervals)

    print("Выбранные интервалы:", result)

    items = [(60, 10), (100, 20), (120, 30), (25, 5)]  # (стоимость, вес)
    capacity = 50

    result, total_value = fractional_knapsack(items, capacity)
    print("Взятые предметы:", result)
    print("Общая стоимость:", total_value)

    freqs = {
        'A': 5,
        'B': 9,
        'C': 12,
        'D': 13,
        'E': 16,
        'F': 45
    }

    tree = build_huffman_tree(freqs)
    codes = build_codes(tree)

    print("Префиксные коды Хаффмана:")
    for char, code in codes.items():
        print(f"{char}: {code}")
