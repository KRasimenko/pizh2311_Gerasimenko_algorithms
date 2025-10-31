def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Асимптотическая сложность:
# Худший случай: O(n²)
# Средний случай: O(n²)
# Лучший случай (уже отсортированный массив): O(n)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Асимптотическая сложность:
# Худший случай: O(n²)
# Средний случай: O(n²)
# Лучший случай: O(n²)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Асимптотическая сложность:
# Худший случай: O(n²)
# Средний случай: O(n²)
# Лучший случай (если массив отсортирован): O(n)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Асимптотическая сложность:
# Худший случай: O(n log n)
# Средний случай: O(n log n)
# Лучший случай: O(n log n)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Опорный элемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Асимптотическая сложность:
# Худший случай: O(n²)
# Средний случай: O(n log n)
# Лучший случай: O(n log n)

