import timeit

import matplotlib.pyplot as plt
import pandas as pd

from generate_data import (
    generate_random_array,
    generate_sorted_array,
    generate_reversed_array,
    generate_almost_sorted_array,
    is_sorted,
)

from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)


def measure_sort_times():
    """Замеряет время выполнения сортировок на разных данных"""
    sizes = [100, 1000, 5000, 10000]
    data_generators = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reversed": generate_reversed_array,
        "Almost Sorted": generate_almost_sorted_array,
    }
    sort_functions = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    results = []

    for size in sizes:
        for dtype, generator in data_generators.items():
            data = generator(size)

            for name, sort_func in sort_functions.items():
                sorted_result = sort_func(data.copy())
                if not is_sorted(sorted_result):
                    print(f"❌ {name} неправильно сортирует ({dtype}, n={size})")
                    continue


                elapsed = timeit.timeit(
                    stmt=lambda: sort_func(data.copy()),
                    number=5
                ) / 5

                results.append({
                    "Algorithm": name,
                    "DataType": dtype,
                    "Size": size,
                    "Time": elapsed,
                })

    return pd.DataFrame(results)


def plot_results(df):
    """Строит графики и выводит таблицу"""
    # === 1. Время от размера массива (Random) ===
    random_df = df[df["DataType"] == "Random"]

    plt.figure(figsize=(10, 6))
    for algo in random_df["Algorithm"].unique():
        subset = random_df[random_df["Algorithm"] == algo]
        plt.plot(subset["Size"], subset["Time"], marker="o", label=algo)

    plt.title("Зависимость времени от размера массива (Random)")
    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время (сек.)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # === 2. Время от типа данных при фиксированном размере ===
    fixed_size = 5000
    fixed_df = df[df["Size"] == fixed_size]

    plt.figure(figsize=(10, 6))
    width = 0.15
    data_types = fixed_df["DataType"].unique()

    for i, algo in enumerate(fixed_df["Algorithm"].unique()):
        subset = fixed_df[fixed_df["Algorithm"] == algo]
        plt.bar(
            [p + i * width for p in range(len(subset))],
            subset["Time"],
            width=width,
            label=algo
        )

    plt.xticks(
        [p + 2 * width for p in range(len(data_types))],
        data_types
    )
    plt.title(f"Зависимость времени от типа данных (n={fixed_size})")
    plt.xlabel("Тип данных")
    plt.ylabel("Время (сек.)")
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()

    # === 3. Сводная таблица ===
    summary = df.groupby(["Algorithm", "DataType"])["Time"].mean().unstack()
    print("\nСводная таблица среднего времени (сек):\n")
    print(summary.round(5))


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
    print("Проводим измерения\n")
    df = measure_sort_times()
    print("Измерения завершены!\n")
    plot_results(df)
