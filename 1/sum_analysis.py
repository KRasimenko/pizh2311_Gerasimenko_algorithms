import random
import time

import matplotlib
import matplotlib
import random
import time

import matplotlib.pyplot as plt
matplotlib.use("TkAgg")


def sum_from_file(filename: str) -> int:
    """
    Считывает два числа из файла и возвращает их сумму.

    Args:
        filename (str): Имя файла, содержащего два числа в одной строке.

    Returns:
        int: Сумма двух чисел.
    """
    # O(1) — открытие файла
    with open(filename, "r", encoding="utf-8") as file:
        # O(1) — чтение одной строки
        line = file.readline()

        # O(k) — split разбивает строку на части по пробелам,
        # где k — количество элементов в строке (в нашем случае k = 2).
        numbers = line.split()

        # O(1) — преобразование строк в числа и их сложение
        a = int(numbers[0])
        b = int(numbers[1])
        return a + b
    # Общая сложность: O(1)


def sum_array(arr: list[int]) -> int:
    """
    Суммирует все элементы массива.

    Args:
        arr (list[int]): Список чисел.

    Returns:
        int: Сумма элементов.
    """
    # O(n) — проход по всем элементам массива
    return sum(arr)


def measure_time(func, *args, repeats: int = 5) -> float:
    """
    Замеряет среднее время выполнения функции в миллисекундах.

    Args:
        func (Callable): Функция для замера.
        *args: Аргументы, передаваемые в функцию.
        repeats (int): Количество повторов (по умолчанию 5).

    Returns:
        float: Среднее время выполнения в мс.
    """
    times: list[float] = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        times.append((end - start) * 1000)  # в миллисекундах

    avg_time = sum(times) / repeats
    print(f"Результат: {result}")
    print(f"Среднее время выполнения ({repeats} запусков): {avg_time:.4f} мс")
    return avg_time


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

    # Массивы разного размера
    small = [random.randint(1, 100) for _ in range(1000)]        # 1k чисел
    medium = [random.randint(1, 100) for _ in range(100000)]     # 100k чисел
    large = [random.randint(1, 100) for _ in range(1000000)]     # 1M чисел

    sizes = [1000, 100000, 1000000]  # размеры массивов для анализа
    times: list[float] = []

    print("=== (1k элементов) ===")
    time1 = measure_time(sum_array, small)
    times.append(time1)

    print("\n=== (100k элементов) ===")
    time2 = measure_time(sum_array, medium)
    times.append(time2)

    print("\n=== (1M элементов) ===")
    time3 = measure_time(sum_array, large)
    times.append(time3)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker="o", linestyle="-", color="blue")
    plt.title("Зависимость времени суммирования массива от его размера")
    plt.xlabel("Размер массива (число элементов)")
    plt.ylabel("Время выполнения (мс)")
    plt.grid(True)

    # Подписи к точкам
    labels = ["1K", "100K", "1M"]
    for size, time_val, label in zip(sizes, times, labels):
        plt.annotate(
            f"{label}\n{time_val:.4f} мс",
            (size, time_val),
            textcoords="offset points",
            xytext=(0, 15),
            ha="center",
        )

    plt.show()
