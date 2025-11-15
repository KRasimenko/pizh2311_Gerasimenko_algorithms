import time
import random
import string
import matplotlib.pyplot as plt

from hash_table_chaining import HashTableChaining
from hash_function import simple_hash, poly_hash, djb2


# -----------------------------
# Генерация случайных строк
# -----------------------------
def random_string(n=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


# ============================================================
# 1. Замер времени вставки/поиска + графики
# ============================================================
def benchmark_time(table_class, name):
    print(f"\n=== {name} ===")

    capacities = [10000]
    load_factors = [0.1, 0.5, 0.7, 0.9]

    results_insert = []
    results_find = []

    for lf in load_factors:
        cap = capacities[0]
        n = int(cap * lf)

        ht = table_class(size=cap)
        keys = [random_string() for _ in range(n)]

        # Вставка
        start = time.time()
        for i, key in enumerate(keys):
            ht.insert(key, i)
        insert_time = time.time() - start
        results_insert.append(insert_time)

        # Поиск
        start = time.time()
        for key in keys:
            ht.find(key)
        find_time = time.time() - start
        results_find.append(find_time)

        print(f"  LF={lf}: insert={insert_time:.4f}s  find={find_time:.4f}s")

    # -----------------------------
    # Построение графиков
    # -----------------------------
    plt.figure(figsize=(10, 5))
    plt.plot(load_factors, results_insert, marker='o')
    plt.title("Время вставки vs коэффициент заполнения")
    plt.xlabel("Load factor")
    plt.ylabel("Время вставки (сек)")
    plt.grid(True)
    plt.savefig("time_insert_vs_load.png")

    plt.figure(figsize=(10, 5))
    plt.plot(load_factors, results_find, marker='o')
    plt.title("Время поиска vs коэффициент заполнения")
    plt.xlabel("Load factor")
    plt.ylabel("Время поиска (сек)")
    plt.grid(True)
    plt.savefig("time_find_vs_load.png")

    print("Графики сохранены: time_insert_vs_load.png, time_find_vs_load.png")


# ============================================================
# 2. Исследование коллизий + гистограммы
# ============================================================
def benchmark_collisions():
    print("\n=== Сравнение количества коллизий ===")

    hash_funcs = [
        ("simple_hash", simple_hash),
        ("poly_hash", poly_hash),
        ("djb2", djb2),
    ]

    size = 10000
    keys = [random_string() for _ in range(20000)]

    for name, func in hash_funcs:
        buckets = [0] * size

        for key in keys:
            h = func(key) % size
            buckets[h] += 1

        collisions = sum(1 for b in buckets if b > 1)

        print(f"{name:12}  коллизий = {collisions}")

        # -----------------------------
        # Строим гистограмму коллизий
        # -----------------------------
        plt.figure(figsize=(10, 5))
        plt.hist(buckets, bins=50)
        plt.title(f"Распределение коллизий: {name}")
        plt.xlabel("Количество элементов в корзине")
        plt.ylabel("Количество корзин")
        plt.grid(True)
        fname = f"collisions_{name}.png"
        plt.savefig(fname)
        print(f"Гистограмма сохранена: {fname}")


# ============================================================
# Запуск
# ============================================================
if __name__ == "__main__":
    # 1) сравнение времени
    benchmark_time(HashTableChaining, "Метод цепочек")

    # 2) коллизии у хеш-функций
    benchmark_collisions()
