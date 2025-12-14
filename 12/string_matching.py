# Алгоритм Бойера–Мура
def bad_char_table(pattern):
    """
    Таблица плохих символов:
    для каждого символа запоминаем его последнюю позицию в шаблоне
    """
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


def boyer_moore(text, pattern):
    """
    Возвращает список индексов,
    где pattern встречается в text
    """
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return []

    bad_char = bad_char_table(pattern)
    result = []

    shift = 0  # текущий сдвиг шаблона

    while shift <= n - m:
        j = m - 1  # начинаем сравнение с конца шаблона

        # сравниваем справа налево
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            result.append(shift)
            shift += 1
        else:
            bad = text[shift + j]
            last = bad_char.get(bad, -1)
            shift += max(1, j - last)

    return result


def main():
    """
    Ввод:
    1 строка — текст
    2 строка — шаблон
    """
    text = input().strip()
    pattern = input().strip()

    positions = boyer_moore(text, pattern)

    if positions:
        for pos in positions:
            print(pos)
    else:
        print("NO")


if __name__ == '__main__':
    main()
