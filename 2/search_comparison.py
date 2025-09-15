import time

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
    return sum(times) / runs    # считает среднее время выполнения    

if __name__ == '__main__':

    sizes = [1000, 2000, 5000, 10000, 50000, 
             100000, 500000, 1000000, 5000000, 10000000] # массив размеров

    for size in sizes:
        arr = list(range(size))  # создаём отсортированный массив
        targets = [arr[0], arr[-1], arr[size // 2], size + 1]  
        # первый, последний, средний, отсутствующий элемент

        print(f"\n--- Размер массива: {size} ---")
        for target in targets:
            lin_time = measure_time(linear_search, arr, target)
            bin_time = measure_time(binary_search, arr, target)
            print(f"Цель: {target} | Linear: {lin_time:.8f} c | Binary: {bin_time:.8f} c")

