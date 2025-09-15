import time
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def sum_from_file(filename):
    # O(1) — открытие файла 
    with open(filename, "r") as file:
        
        # O(1) — чтение одной строки 
        line = file.readline()
        
        # O(k) — split разбивает строку на части по пробелам, 
        # где k — количество элементов в строке.
        # В нашем случае k = 2, фактически O(1).
        numbers = line.split()
        
        # O(1) — обращение к первому элементу списка
        a = int(numbers[0])  # O(1) — преобразование строки в число
        
        # O(1) — обращение ко второму элементу списка
        b = int(numbers[1])  # O(1) — преобразование строки в число
        
        # O(1) — сложение двух чисел
        return a + b
    # общая сложность: O(1)


"""def measure_time1(func, *args):
    
    start = time.perf_counter()   # старт замера
    result = func(*args)          # выполняем функцию
    end = time.perf_counter()     # конец замера
    elapsed_ms = (end - start) * 1000  # перевод секунд в миллисекунды
    print(f"Результат: {result}")
    print(f"Время выполнения: {elapsed_ms:.4f} мс")"""

def sum_array(arr):
    # O(n) — проход по всем элементам массива и их сложение
    return sum(arr)

def measure_time(func, *args, repeats=5):
    """Замеряет среднее время выполнения функции в миллисекундах"""
    times = []
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


    
    

    small = [random.randint(1, 100) for _ in range(1000)]       # 1k элементов
    medium = [random.randint(1, 100) for _ in range(100000)]    # 100k элементов
    large = [random.randint(1, 100) for _ in range(1000000)]    # 1M элементов
    
    
    sizes = [1000, 100000, 1000000] # размеры массивов для анализа
    times = [] # массив для хранения времени выполнения
    
    print("=== (1k элементов) ===")
    time1 = measure_time(sum_array, small) # вызываем функцию замера времени
    times.append(time1) # сохраняем результат в список
    
    print("\n=== (100k элементов) ===")
    time2 = measure_time(sum_array, medium)
    times.append(time2)
    
    print("\n=== (1M элементов) ===")
    time3 = measure_time(sum_array, large)
    times.append(time3)

    
    plt.figure(figsize=(10, 6)) # создаём фигуру с размерами 10x6 дюймов
    plt.plot(sizes, times, marker='o', linestyle='-', color='blue') # строим график
    plt.title("Зависимость времени выполнения суммирования массива от размера массива")
    plt.xlabel("Размер массива (число млн элементов)") # подпись оси X
    plt.ylabel("Время выполнения (мс)") # подпись оси Y
    plt.grid(True) # включаем сетку 
    
    
    # Подписи к точкам
    labels = ['1K', '100K', '1M']
    for i, (size, time_val, label) in enumerate(zip(sizes, times, labels)):
        plt.annotate(f'{label}\n{time_val:.4f}мс', 
                    (size, time_val), # координаты точки
                    textcoords="offset points",  #смещение подписи относительно точки
                    xytext=(0,15), #сдвиг по вертикали
                    ha='center') #выравнивание по горизонтали
    plt.show()
    
    
  

