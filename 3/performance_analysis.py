

import time
import statistics
import matplotlib.pyplot as plt
from collections import deque
from linked_list import LinkedList


def bench_list_insert_start(n: int) -> float:
    """Вставка n элементов в начало Python list: insert(0, item) -> O(n) per op."""
    lst = []
    t0 = time.perf_counter()
    for i in range(n):
        lst.insert(0, i)
    t1 = time.perf_counter()
    return t1 - t0


def bench_linkedlist_insert_start(n: int) -> float:
    """Вставка n элементов в начало LinkedList -> O(1) per op."""
    ll = LinkedList()
    t0 = time.perf_counter()
    for i in range(n):
        ll.insert_at_start(i)
    t1 = time.perf_counter()
    return t1 - t0


def bench_list_pop0(n: int) -> float:
    """Удаление из начала списка поп(0) — O(n) per op."""
    lst = list(range(n))
    t0 = time.perf_counter()
    while lst:
        lst.pop(0)
    t1 = time.perf_counter()
    return t1 - t0


def bench_deque_popleft(n: int) -> float:
    """Удаление из начала deque — O(1) per op."""
    dq = deque(range(n))
    t0 = time.perf_counter()
    while dq:
        dq.popleft()
    t1 = time.perf_counter()
    return t1 - t0


def run_and_plot():
    sizes = [1000, 2000, 4000, 8000]  # можно увеличить; сначала попробуй такие
    repeats = 3  # среднее по 3 запускам

    # Вставка в начало: list vs linked list
    list_times = []
    ll_times = []
    for n in sizes:
        lt = [bench_list_insert_start(n) for _ in range(repeats)]
        llt = [bench_linkedlist_insert_start(n) for _ in range(repeats)]
        list_times.append(statistics.mean(lt))
        ll_times.append(statistics.mean(llt))
        print(f"Insert-start n={n} -> list: {list_times[-1]:.4f}s, linked: {ll_times[-1]:.4f}s")

    plt.figure()
    plt.plot(sizes, list_times, marker="o", label="list.insert(0, x)")
    plt.plot(sizes, ll_times, marker="o", label="LinkedList.insert_at_start")
    plt.xlabel("n")
    plt.ylabel("time (s)")
    plt.title("Insert at start: list vs LinkedList")
    plt.legend()
    plt.grid(True)
    plt.savefig("insert_start_comparison.png")
    print("Saved insert_start_comparison.png")

    # Очередь: pop(0) vs deque.popleft()
    list_times = []
    deque_times = []
    for n in sizes:
        lt = [bench_list_pop0(n) for _ in range(repeats)]
        dt = [bench_deque_popleft(n) for _ in range(repeats)]
        list_times.append(statistics.mean(lt))
        deque_times.append(statistics.mean(dt))
        print(f"Queue-pop n={n} -> list.pop(0): {list_times[-1]:.4f}s, deque.popleft: {deque_times[-1]:.4f}s")

    plt.figure()
    plt.plot(sizes, list_times, marker="o", label="list.pop(0)")
    plt.plot(sizes, deque_times, marker="o", label="deque.popleft()")
    plt.xlabel("n")
    plt.ylabel("time (s)")
    plt.title("Queue removal: list vs deque")
    plt.legend()
    plt.grid(True)
    plt.savefig("queue_comparison.png")
    print("Saved queue_comparison.png")


if __name__ == "__main__":
    run_and_plot()
