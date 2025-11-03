import random

# Импортируем наши функции сортировки
from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
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
    swap_count = int(size * 0.05)  # 5% элементов меняем местами случайно
    for _ in range(swap_count):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]

    for size in sizes:
        print(f"\n=== Размер массива: {size} ===")

        datasets = {
            "random": generate_random_array(size),
            "sorted": generate_sorted_array(size),
            "reversed": generate_reversed_array(size),
            "almost_sorted": generate_almost_sorted_array(size)
        }
