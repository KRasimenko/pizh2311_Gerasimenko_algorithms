import time
import random

import matplotlib.pyplot as plt

from dynamic_programming import knapsack_01


def benchmark_knapsack(max_n=100, W=50, step=10):
    ns = list(range(step, max_n + 1, step))
    times = []

    for n in ns:
        values = [random.randint(1, 100) for _ in range(n)]
        weights = [random.randint(1, W//2) for _ in range(n)]

        start = time.perf_counter()
        knapsack_01(values, weights, W)
        end = time.perf_counter()

        times.append(end - start)

    return ns, times



def knapsack_01_visual(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    print("Начальная таблица DP:")
    for row in dp:
        print(row)
    print("\nЗаполнение таблицы DP:")

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

        print(f"\nПосле обработки предмета {i} (value={values[i-1]}, weight={weights[i-1]}):")
        for row in dp:
            print(row)

    selected = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
    selected.reverse()

    print(f"\nМаксимальная ценность: {dp[n][W]}")
    print(f"Выбранные предметы: {selected}")
    return dp[n][W], selected


if __name__ == "__main__":
    # Демонстрация визуализации DP для маленьких данных
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    knapsack_01_visual(values, weights, W)

    ns, times = benchmark_knapsack(max_n=100, W=50, step=10)

    plt.figure(figsize=(8, 5))
    plt.plot(ns, times, marker='o')
    plt.title("Зависимость времени выполнения 0-1 рюкзака от числа предметов")
    plt.xlabel("Количество предметов n")
    plt.ylabel("Время выполнения (сек)")
    plt.grid(True)
    plt.show()
