from prefix_function import p_fun


def kmp(a, b):
    """ Применение пи фунции для поиска подстроки в строке"""
    res = []
    s = a + '#' + b
    pi = p_fun(s)

    for i in range(len(a) + 1, len(s)):
        if pi[i] == len(a):
            res.append(i - 2 * len(a))

    return res

    # Сложность O(n+m)

