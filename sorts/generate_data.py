import random
import timeit

from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)


def generate_random_array(size):
    """Создаёт случайный массив заданного размера"""
    return [random.randint(0, 10000) for _ in range(size)]


def generate_sorted_array(size):
    """Создаёт уже отсортированный массив"""
    return list(range(size))


def generate_reversed_array(size):
    """Создаёт массив, отсортированный в обратном порядке"""
    return list(range(size, 0, -1))


def generate_almost_sorted_array(size):
    """
    Создаёт почти отсортированный массив:
    95% элементов отсортированы, 5% — случайно перемешаны
    """
    arr = list(range(size))
    swap_count = int(size * 0.05)
    for _ in range(swap_count):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def is_sorted(arr):
    """Проверяет, отсортирован ли массив по возрастанию"""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
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
    print(pc_info)
    sizes = [100, 1000, 5000, 10000]

    sort_functions = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    for size in sizes:
        print(f"\n=== Размер массива: {size} ===")

        datasets = {
            "Random": generate_random_array(size),
            "Sorted": generate_sorted_array(size),
            "Reversed": generate_reversed_array(size),
            "Almost Sorted": generate_almost_sorted_array(size),
        }

        for dtype, data in datasets.items():
            print(f"\n--- Тип данных: {dtype} ---")

            for name, sort_func in sort_functions.items():
                # Проверяем корректность сортировки перед замерами
                test_array = data.copy()
                sorted_result = sort_func(test_array.copy())

                if not is_sorted(sorted_result):
                    print(f" {name:<15} — сортировка работает НЕПРАВИЛЬНО!")
                    continue  # не замеряем время, если алгоритм некорректен

                # Измеряем среднее время работы (5 прогонов)
                elapsed_time = timeit.timeit(
                    stmt=lambda: sort_func(data.copy()),
                    number=5
                ) / 5

                print(f" {name:<15} => {elapsed_time:.5f} сек.")
