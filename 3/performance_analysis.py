import timeit
from collections import deque

import matplotlib.pyplot as plt

from linked_list import LinkedList


def test_list_insert(n):
    lst = []
    for i in range(n):
        lst.insert(0, i)  # O(n)


def test_linkedlist_insert(n):
    ll = LinkedList()
    for i in range(n):
        ll.insert_at_start(i)  # O(1)


def test_list_pop(n):
    lst = list(range(n))
    for _ in range(n):
        lst.pop(0)  # O(n)


def test_deque_popleft(n):
    dq = deque(range(n))
    for _ in range(n):
        dq.popleft()  # O(1)


def average_time(stmt_func, n, repeat=5):
    """Замер времени для функции stmt_func с n элементами"""
    def stmt():
        return stmt_func(n)
    times = [timeit.timeit(stmt, number=1) for _ in range(repeat)]
    return sum(times) / repeat


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
    sizes = [1000, 5000, 10000, 20000, 50000]  # размеры данных
    times_list_insert = []
    times_ll_insert = []
    times_list_pop = []
    times_deque_popleft = []

    for n in sizes:
        times_list_insert.append(average_time(test_list_insert, n))
        times_ll_insert.append(average_time(test_linkedlist_insert, n))
        times_list_pop.append(average_time(test_list_pop, n))
        times_deque_popleft.append(average_time(test_deque_popleft, n))

    plt.figure(figsize=(12, 6))

    # Вставка в начало
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times_list_insert, marker='o', label='list.insert(0, x)')
    plt.plot(sizes, times_ll_insert, marker='o',
             label='LinkedList.insert_at_start')
    plt.title("Вставка в начало")
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (сек)")
    plt.legend()
    plt.grid(True)

    # Удаление из начала
    plt.subplot(1, 2, 2)
    plt.plot(sizes, times_list_pop, marker='o', label='list.pop(0)')
    plt.plot(sizes, times_deque_popleft, marker='o', label='deque.popleft()')
    plt.title("Удаление из начала")
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (сек)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
