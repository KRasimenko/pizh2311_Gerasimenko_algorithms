from functools import lru_cache


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


@lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    """
    Рекурсивная функция для вычисления n-го числа Фибоначчи.
    Используется мемоизация через @lru_cache, чтобы избежать повторных
    вычислений
    Последовательность: 0, 1, 1, 2, 3, 5, 8, ...
    """
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
    # Временная сложность: O(n)
    # Глубина рекурсии: O(n)


def fib_tabulation(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
    # Временная сложность: O(n)
    # Простронственная сложность: O(n)


def knapsack_01(values, weights, W):
    n = len(values)
    # создаём таблицу dp размером (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # заполняем таблицу
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                # Берём максимум: либо не берём предмет, либо берём его
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] +
                               values[i - 1])
            else:
                # Не можем взять предмет, оставляем предыдущий максимум
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]  # максимальная ценность для всех предметов и веса W
    # Временная слольность: O(n * W)
    # Простронственная сложность: O(n * W)


def lcs(X, Y):
    m, n = len(X), len(Y)

    # Таблица DP
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Заполняем DP (восходящий подход)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Восстановление LCS
    i, j = m, n
    lcs_seq = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            # Символ входит в LCS
            lcs_seq.append(X[i - 1])
            i -= 1
            j -= 1
        else:
            # Идём туда, где значение dp больше
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    lcs_seq.reverse()
    return dp[m][n], "".join(lcs_seq)
    # Временная слольность: O(m * n)
    # Простронственная сложность: O(m * n)


def levenshtein_distance(X, Y):
    m = len(X)
    n = len(Y)

    # создаём таблицу dp размером (m+1) x (n+1)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # инициализация: расстояние от пустой строки
    for i in range(m + 1):
        dp[i][0] = i  # нужно i удалений
    for j in range(n + 1):
        dp[0][j] = j  # нужно j вставок

    # заполняем таблицу
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # символы совпадают
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # удаление
                    dp[i][j - 1],    # вставка
                    dp[i - 1][j - 1]  # замена
                )

    return dp[m][n]
    # Временная слольность: O(m * n)
    # Простронственная сложность: O(m * n)


if __name__ == '__main__':
    print(fib_tabulation(30))
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    print(knapsack_01(values, weights, W))
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(lcs(X, Y))
    X = "kitten"
    Y = "sitting"
    print(levenshtein_distance(X, Y))
