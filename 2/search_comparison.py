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


