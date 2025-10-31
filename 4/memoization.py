import time

import matplotlib.pyplot as plt
from functools import lru_cache

import recursion
from recursion import fibonacci


def measure_time(func, *args, **kwargs):
    """
    функция-обёртка для измерения времени выполнения функции
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    elapsed = end - start
    return result, elapsed


call_count_memo = 0


@lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    """
    Рекурсивная функция для вычисления n-го числа Фибоначчи.
    Используется мемоизация через @lru_cache, чтобы избежать повторных
    вычислений
    Последовательность: 0, 1, 1, 2, 3, 5, 8, ...
    """
    global call_count_memo
    call_count_memo += 1
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
    # Временная сложность: O(n)
    # Глубина рекурсии: O(n)


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
    ns = [10, 15, 20, 25, 30, 35]
    times_naive = []
    times_memo = []

    for n in ns:
        recursion.call_count_naive = 0
        result_naive, t_naive = measure_time(fibonacci, n)
        times_naive.append(t_naive)

        fibonacci_cached.cache_clear()
        call_count_memo = 0  # сбрасываем перед измерением
        result_memo, t_memo = measure_time(fibonacci_cached, n)
        times_memo.append(t_memo)

        print(f"n={n}: Наивная={t_naive:.8f}s, Мемоизация={t_memo:.8f}s")

    # Построение графика
    plt.plot(ns, times_naive, marker='o', label='Наивная рекурсия')
    plt.plot(ns, times_memo, marker='o', label='Мемоизация')
    plt.xlabel("n (число Фибоначчи)")
    plt.ylabel("Время выполнения, секунд")
    plt.title("Сравнение времени выполнения Фибоначчи")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.show()
