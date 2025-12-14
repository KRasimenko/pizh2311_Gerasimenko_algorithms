import time
import random
import string

import matplotlib.pyplot as plt

from kmp_search import kmp
from z_function import z_func
from prefix_function import p_fun
from string_matching import boyer_moore


def run_kmp(pattern, text):
    kmp(pattern, text)


def run_z(pattern, text):
    s = pattern + '#' + text
    z_func(s)


def run_bm(pattern, text):
    boyer_moore(text, pattern)


def random_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


def repeated_string(n, ch='a'):
    return ch * n


def periodic_string(n):
    return ('abc' * (n // 3 + 1))[:n]


# Замер врмени

def measure(func, pattern, text, repeat=5):
    total = 0
    for _ in range(repeat):
        start = time.perf_counter()
        func(pattern, text)
        total += time.perf_counter() - start
    return total / repeat


def main():
    N = 100_000
    M = 10

    tests = [
        ("Случайная строка", random_string(N), random_string(M)),
        ("Периодическая строка", periodic_string(N), "abc"),
        ("Повторы (худший случай)", repeated_string(N), repeated_string(M)),
    ]

    for name, text, pattern in tests:
        print(f"\n{name}")
        print("-" * 40)

        print("KMP:", measure(run_kmp, pattern, text))
        print("Z  :", measure(run_z, pattern, text))
        print("BM :", measure(run_bm, pattern, text))
    text_sizes = [1_000, 5_000, 10_000, 20_000, 40_000]
    pattern = "abc"

    kmp_times = []
    z_times = []
    bm_times = []

    for n in text_sizes:
        text = random_string(n)
        kmp_times.append(measure(run_kmp, pattern, text))
        z_times.append(measure(run_z, pattern, text))
        bm_times.append(measure(run_bm, pattern, text))

    plt.figure()
    plt.plot(text_sizes, kmp_times, label="KMP")
    plt.plot(text_sizes, z_times, label="Z-algorithm")
    plt.plot(text_sizes, bm_times, label="Boyer–Moore")
    plt.xlabel("Длина текста")
    plt.ylabel("Время (сек)")
    plt.title("Зависимость времени от длины текста")
    plt.legend()
    plt.grid(True)
    plt.show()


    
    # ГРАФИК 2: ВРЕМЯ vs ДЛИНА ПАТТЕРНА
   

    text = random_string(30_000)
    pattern_sizes = [2, 5, 10, 20, 50]

    kmp_times = []
    z_times = []
    bm_times = []

    for m in pattern_sizes:
        pattern = random_string(m)
        kmp_times.append(measure(run_kmp, pattern, text))
        z_times.append(measure(run_z, pattern, text))
        bm_times.append(measure(run_bm, pattern, text))

    plt.figure()
    plt.plot(pattern_sizes, kmp_times, label="KMP")
    plt.plot(pattern_sizes, z_times, label="Z-algorithm")
    plt.plot(pattern_sizes, bm_times, label="Boyer–Moore")
    plt.xlabel("Длина паттерна")
    plt.ylabel("Время (сек)")
    plt.title("Зависимость времени от длины паттерна")
    plt.legend()
    plt.grid(True)
    plt.show()


    
    # ВИЗУАЛИЗАЦИЯ PREFIX-ФУНКЦИИ
    

    sample = "abacabadabacaba"
    pi = p_fun(sample)

    plt.figure()
    plt.bar(range(len(sample)), pi)
    plt.xlabel("Индекс")
    plt.ylabel("pi[i]")
    plt.title(f"Префикс-функция для строки: {sample}")
    plt.grid(True)
    plt.show()


    
    # ВИЗУАЛИЗАЦИЯ Z-ФУНКЦИИ
    

    z = z_func(sample)

    plt.figure()
    plt.bar(range(len(sample)), z)
    plt.xlabel("Индекс")
    plt.ylabel("z[i]")
    plt.title(f"Z-функция для строки: {sample}")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
