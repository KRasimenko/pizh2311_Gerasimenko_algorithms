import time
import random
import tracemalloc

from dynamic_programming import fibonacci_cached, fib_tabulation, knapsack_01


def benchmark(func, n):
    print(f"\nТест: {func.__name__}, n={n}")
    tracemalloc.start()
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Результат: {result}")
    print(f"Время: {end - start:.6f} сек")
    print(f"Память (пик): {peak / 1024:.2f} KB")


def benchmark_knapsack():
    ns = [10, 50, 100, 200]       # количество предметов
    Ws = [50, 100, 200, 500]      # вместимость рюкзака

    print("Исследование масштабируемости алгоритма 0-1 рюкзака")
    print("{:<10} {:<10} {:<15}".format("n", "W", "Время (сек)"))

    for n in ns:
        for W in Ws:
            # случайные значения и веса
            values = [random.randint(1, 100) for _ in range(n)]
            weights = [random.randint(1, W//2) for _ in range(n)]

            start = time.perf_counter()
            knapsack_01(values, weights, W)
            end = time.perf_counter()

            print("{:<10} {:<10} {:<15.6f}".format(n, W, end - start))


if __name__ == "__main__":
    N = 35

    benchmark(fibonacci_cached, N)
    benchmark(fib_tabulation, N)
    benchmark_knapsack()
