def factorial(n: int) -> int:
    """
    Рекурсивное вычисление факториала числа n.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    # Временная сложность: O(n)
    # Глубина рекурсии: O(n)


def fibonacci(n: int) -> int:
    """
    Рекурсивное вычисление n-го числа Фибоначчи.
    Последовательность: 0, 1, 1, 2, 3, 5, 8, ...
    в глобальной переменной call_count_naive считает
    количество вызовов функции
    """
    global call_count_naive
    call_count_naive += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    # Временная сложность: O(2^n)
    # Глубина рекурсии: O(n)


def fast_power(a: int, n: int) -> int:
    """
    Быстрое возведение числа a в степень n через деление степени пополам.
    Используется принцип:
        a^n = (a^(n//2))^2  если n чётное
        a^n = a * (a^(n-1)) если n нечётное
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half
    else:
        return a * fast_power(a, n - 1)
    # Временная сложность: O(log n)
    # Глубина рекурсии: O(log n)
