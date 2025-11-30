import os


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Рекурсивный алгоритм бинарного поиска.
    arr      — отсортированный список (по возрастанию)
    target   — искомое значение
    left     — левая граница диапазона поиска
    right    — правая граница диапазона поиска (по умолчанию конец массива)

    Возвращает индекс элемента, если найден, иначе -1.
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)
    # Временная сложность: O(log n)
    # Глубина рекурсии: O(log n)


max_depth = 0


def walk_directory(path: str, indent: int = 0, current_depth: int = 0):
    """
    Рекурсивный обход файловой системы с измерением глубины рекурсии.

    path          — начальный путь
    indent        — отступ для вывода
    current_depth — текущая глубина рекурсии
    """
    global max_depth
    if current_depth > max_depth:
        max_depth = current_depth

    if not os.path.exists(path):
        print("Путь не существует:", path)
        return

    print(" " * indent + f"[{os.path.basename(path) or path}]")

    if os.path.isdir(path):
        for name in os.listdir(path):
            new_path = os.path.join(path, name)
            walk_directory(new_path, indent + 4, current_depth + 1)
    else:
        print(" " * (indent + 4) + os.path.basename(path))


def hanoi(n, source="A", target="C", auxiliary="B", towers=None):
    """
    Рекурсивное решение задачи Ханойские башни с ASCII-визуализацией.

    n         — количество дисков
    source    — стержень, с которого снимаем диск
    target    — стержень, на который ставим диск
    auxiliary — вспомогательный стержень
    towers    — текущее состояние башен (списки дисков)
    """
    if towers is None:
        towers = {
            "A": list(range(n, 0, -1)),
            "B": [],
            "C": []
        }
        print("Начальное состояние:")
        print_towers(towers, n)
        return hanoi(n, source, target, auxiliary, towers)

    if n == 0:
        return

    # 1. Переместить n-1 дисков с source на auxiliary через target
    hanoi(n - 1, source, auxiliary, target, towers)

    # 2. Переместить самый большой диск
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"\nПереместить диск {disk} с {source} на {target}")
    print_towers(towers, max(sum(len(t) for t in towers.values()), n))

    # 3. Переместить n-1 дисков с auxiliary на target через source
    hanoi(n - 1, auxiliary, target, source, towers)


def print_towers(towers, n):
    """Печать текущего состояния стержней в ASCII."""
    if n == 0:
        print("Пусто")
    for level in range(n, 0, -1):
        line = ""
        for peg in "ABC":
            if len(towers[peg]) >= level:
                disk_size = towers[peg][level - 1]
                line += " " * (n - disk_size) + "#" * (disk_size * 2 - 1) + " " * (n - disk_size) + "   "
            else:
                line += " " * (n - 1) + "|" + " " * (n - 1) + "   "
        print(line)
    print("-" * (n * 6 + 9))


if __name__ == "__main__":
    # Задача 1: Бинарный поиск
    print("Задача 1: Бинарный поиск")
    arr = list(range(1, 101))
    target = int(input("Введите число для поиска в массиве 1..100: "))
    index = binary_search_recursive(arr, target)
    if index != -1:
        print(f"Элемент {target} найден на индексе {index}.")
    else:
        print(f"Элемент {target} не найден.")
    # Задача 2: Обход файловой системы
    print("\nЗадача 2: Обход файловой системы")
    path = input("Введите путь для обхода (например, C:/ или ./): ")
    walk_directory(path)
    print(f"Максимальная глубина рекурсии: {max_depth}")
    # Задача 3: Ханойские башни
    print("\nЗадача 3: Ханойские башни")
    n = int(input("Введите количество дисков для Ханойских башен"))
    hanoi(n)
