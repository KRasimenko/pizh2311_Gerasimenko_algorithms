from prefix_function import p_fun
from z_function import z_func


# 1. Найти все вхождения паттерна в тексте
def find_pattern_kmp(pattern, text):
    """
    Возвращает список индексов, где pattern встречается в text
    """
    s = pattern + '#' + text
    pi = p_fun(s)
    result = []
    plen = len(pattern)
    for i in range(len(pattern) + 1, len(s)):
        if pi[i] == plen:
            result.append(i - 2 * plen)
    return result


def find_pattern_z(pattern, text):
    """
    Альтернатива через Z-функцию
    """
    s = pattern + '#' + text
    z = z_func(s)
    result = []
    plen = len(pattern)
    for i in range(plen + 1, len(s)):
        if z[i] == plen:
            result.append(i - plen - 1)
    return result


# 2. Найти минимальный период строки
def minimal_period(s):
    """
    Возвращает длину минимального периода строки
    """
    pi = p_fun(s)
    n = len(s)
    if n == 0:
        return 0
    period = n - pi[-1]
    if n % period == 0:
        return period
    return n


# 3. Проверка циклического сдвига
def is_cyclic_shift(s1, s2):
    """
    Проверяет, является ли s2 циклическим сдвигом s1
    """
    if len(s1) != len(s2):
        return False
    doubled = s1 + s1
    return s2 in doubled


if __name__ == '__main__':
    text = "abcabcabcabc"
    pattern = "abc"
    print("Вхождения (KMP):", find_pattern_kmp(pattern, text))
    print("Вхождения (Z):", find_pattern_z(pattern, text))

    s = "abcabcabc"
    print("Минимальный период:", minimal_period(s))

    a = "abcd"
    b = "cdab"
    print(f"'{b}' циклический сдвиг '{a}'?", is_cyclic_shift(a, b))
