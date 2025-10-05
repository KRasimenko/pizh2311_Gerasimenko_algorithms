import timeit
from collections import deque
from linked_list import LinkedList   

def test_list_insert():
    lst = []
    for i in range(1000):
        lst.insert(0, i)   
    #Сложность: O(n)

def test_linkedlist_insert():
    ll = LinkedList()
    for i in range(1000):
        ll.insert_at_start(i)  
    #Сложность: O(1)

def test_list_pop():
    lst = list(range(1000))
    for _ in range(1000):
        lst.pop(0)   
    #Сложность: O(n)

def test_deque_popleft():
    dq = deque(range(1000))
    for _ in range(1000):
        dq.popleft()  
    #Сложность: O(1)


def average_time(stmt, number=5):
    """Запускаем код number раз и возвращаем среднее время"""
    times = timeit.repeat(stmt, globals=globals(), number=1, repeat=number)
    return sum(times) / len(times)


if __name__ == "__main__":
    # Сравнение вставки
    t_list = average_time("test_list_insert()")
    t_ll = average_time("test_linkedlist_insert()")

    # Сравнение удаления
    t_list_pop = average_time("test_list_pop()")
    t_deque = average_time("test_deque_popleft()")

    print("Вставка 1000 элементов в начало:")
    print(f"list.insert(0, x): {t_list:.6f} сек")
    print(f"LinkedList.insert_at_start: {t_ll:.6f} сек")

    print("\nУдаление 1000 элементов из начала:")
    print(f"list.pop(0): {t_list_pop:.6f} сек")
    print(f"deque.popleft(): {t_deque:.6f} сек")
