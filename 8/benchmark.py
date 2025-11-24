import random
import sys
import time


sys.path.append(r"D:\3 курс\Алгоритмы\pizh2311_Gerasimenko_algorithms\5")


from sorts import quick_sort, merge_sort

from heap import Heap
from heapsort import heapsort



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
