from heap import Heap

def heapsort(array):
    # Шаг 1: строим max-кучу из массива
    heap = Heap(is_min=False)
    heap.build_heap(array)
    
    # Шаг 2: извлекаем элементы из кучи в отсортированном порядке
    sorted_array = []
    while heap.data:
        # Извлекаем корень (максимум) и добавляем в начало списка
        sorted_array.insert(0, heap.extract())  # вставка в начало списка
    
    return sorted_array

def heapsort_inplace(array):
    n = len(array)
    
    # Вспомогательная функция для _sift_down
    def sift_down(arr, start, end):
        root = start
        while True:
            left = 2 * root + 1
            right = 2 * root + 2
            largest = root
            if left <= end and arr[left] > arr[largest]:
                largest = left
            if right <= end and arr[right] > arr[largest]:
                largest = right
            if largest == root:
                break
            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    # Шаг 1: Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n - 1)
    
    # Шаг 2: Сортировка
    for end in range(n - 1, 0, -1):
        # Меняем корень с последним элементом
        array[0], array[end] = array[end], array[0]
        # Погружаем новый корень
        sift_down(array, 0, end - 1)
    
    return array

