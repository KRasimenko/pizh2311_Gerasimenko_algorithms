import random
import time
import matplotlib.pyplot as plt

from sorts import quick_sort, merge_sort
from heap import Heap
from heapsort import heapsort


def experiment_heap_building():
    sizes = [1000, 5000, 10000, 20000, 50000, 100000]
    t_insert_list = []
    t_build_list = []

    for n in sizes:
        t_insert, t_build = measure_heap_building(n)
        t_insert_list.append(t_insert)
        t_build_list.append(t_build)
        print(f"[Heap] n={n}: insert={t_insert:.4f}, build={t_build:.4f}")

    plt.figure()
    plt.plot(sizes, t_insert_list, label="Вставка по одному")
    plt.plot(sizes, t_build_list, label="build_heap()")
    plt.xlabel("Количество элементов")
    plt.ylabel("Время (сек)")
    plt.title("Построение кучи")
    plt.legend()
    plt.show()


def print_heap_tree(heap):
    """Печатает бинарную кучу в виде дерева (для малых размеров)."""
    arr = heap.data  # предполагается, что элементы кучи хранится в heap.data
    n = len(arr)

    if n == 0:
        print("<empty>")
        return

    max_width = 2 ** (_arr_level(n) - 1) * 4
    level = 0
    index = 0

    while index < n:
        start = 2 ** level - 1
        end = min(2 ** (level + 1) - 1, n)
        elems = arr[start:end]
        spacing = max_width // (2 ** (level + 1))
        line = (" " * spacing).join(f"{x:3}" for x in elems)
        print(" " * spacing + line)
        level += 1
        index = end


def _arr_level(n):
    level = 0
    while (1 << level) <= n:
        level += 1
    return level


def measure_heap_building(n=100000):
    array = [random.randint(0, 1_000_000) for _ in range(n)]

    # Метод 1: последовательные вставки
    heap1 = Heap(is_min=True)
    t1_start = time.perf_counter()
    for x in array:
        heap1.insert(x)
    t1 = time.perf_counter() - t1_start

    # Метод 2: build_heap
    heap2 = Heap(is_min=True)
    t2_start = time.perf_counter()
    heap2.build_heap(array)
    t2 = time.perf_counter() - t2_start

    return t1, t2


def measure_sorts(n=50000):
    base = [random.randint(0, 1_000_000) for _ in range(n)]

    t_h_start = time.perf_counter()
    heapsort(base.copy())
    t_h = time.perf_counter() - t_h_start

    t_q_start = time.perf_counter()
    quick_sort(base.copy())
    t_q = time.perf_counter() - t_q_start

    t_m_start = time.perf_counter()
    merge_sort(base.copy())
    t_m = time.perf_counter() - t_m_start

    return t_h, t_q, t_m


if __name__ == "__main__":
    print("\n=== Построение кучи ===")
    t_insert, t_build = measure_heap_building(100000)
    print(f"Последовательные вставки: {t_insert:.4f} сек")
    print(f"build_heap():             {t_build:.4f} сек")
    print("Ускорение:", f"{t_insert / t_build:.2f}x")

    print("\n=== Сравнение сортировок (n = 50000) ===")
    t_h, t_q, t_m = measure_sorts(50000)
    print(f"Heapsort:      {t_h:.4f} сек")
    print(f"Quicksort:     {t_q:.4f} сек")
    print(f"Merge sort:    {t_m:.4f} сек")

    # Тест: визуализация маленькой кучи
    heap = Heap(is_min=True)
    heap.build_heap([10, 4, 7, 2, 8, 1, 3, 9, 13])
    print("\n=== Дерево кучи ===")
    print_heap_tree(heap)

    experiment_heap_building()
