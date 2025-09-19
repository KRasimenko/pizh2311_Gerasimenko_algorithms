import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:   # O(1)
            return i         # O(1)
    return -1                  # O(1)
# Общая сложность: O(n)

def binary_search(arr, target):
    left = 0                  # O(1)
    right = len(arr) - 1    #O(1)

    while left <= right:     #O(log n) (цикл делит массив пополам)
        mid = (left + right) // 2   # O(1)
        if arr[mid] == target:    # O(1)
            return mid            # O(1)
        elif arr[mid] < target:   # O(1)
            left = mid + 1       # O(1)
        else:
            right = mid - 1         # O(1)

    return -1                  # O(1)
# Общая сложность: O(log n)

def measure_time(search_func, arr, target, runs=5):
    times = []
    for _ in range(runs):  
        start = time.perf_counter()  # Засекаем время
        search_func(arr, target)     # Запускаем поиск
        end = time.perf_counter()    # Останавливаем
        times.append(end - start)    
    return (sum(times) / runs) * 1000    # считает среднее время выполнения в мс

if __name__ == '__main__':

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

    sizes = [1000, 2000, 5000, 10000, 50000, 
             100000, 500000, 1000000, 5000000, 10000000] # массив размеров
    linear_times = { "Первый": [], "Последний": [], "Средний": [], "Отсутствующий": [] } # словарь для хранения времён
    binary_times = { "Первый": [], "Последний": [], "Средний": [], "Отсутствующий": [] } 
    for size in sizes:
        arr = list(range(size))  # создаём отсортированный массив
        targets = {
            "Первый": arr[0],
            "Последний": arr[-1],
            "Средний": arr[size // 2],
            "Отсутствующий": size + 1
        }

        print(f"\n--- Размер массива: {size} ---")
        for case, target in targets.items():
            lin_time = measure_time(linear_search, arr, target)
            bin_time = measure_time(binary_search, arr, target) 

            linear_times[case].append(lin_time)
            binary_times[case].append(bin_time)

            print(f"Цель: {case} ({target}) | Линейный: {lin_time:.8f} мc | Бинарный: {bin_time:.8f} мc")
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    cases = ["Первый", "Последний", "Средний", "Отсутствующий"]
    for ax, case in zip(axs.flat, cases):
        ax.plot(sizes, linear_times[case], marker="o", label="Линейный")
        ax.plot(sizes, binary_times[case], marker="s", label="Бинарный")
        ax.set_title(case)
        ax.set_xlabel("Размер массива (n)")
        ax.set_ylabel("Время (мс)")
        ax.grid(True)
        ax.legend()
    plt.tight_layout()
    plt.show()

   
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    cases = ["Первый", "Последний", "Средний", "Отсутствующий"]
    for ax, case in zip(axs.flat, cases):
        ax.plot(sizes, linear_times[case], marker="o", label="Линейный")
        ax.plot(sizes, binary_times[case], marker="s", label="Бинарный")
        ax.set_title(case)
        ax.set_xlabel("Размер массива (n)")
        ax.set_ylabel("Время (мс, лог-шкала)")
        ax.set_yscale("log")  # логарифмическая шкала по Y
        ax.grid(True, which="both")  # сетка для минорных и мажорных делений
        ax.legend()
    plt.tight_layout()
    plt.show()
    
