import time
import tracemalloc

from dynamic_programming import fibonacci_cached, fib_tabulation


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


if __name__ == "__main__":
    N = 35

    benchmark(fibonacci_cached, N)
    benchmark(fib_tabulation, N)
