def coin_change(coins, amount):
    # "бесконечное" значение для инициализации
    INF = float('inf')

    # dp[x] = минимальное количество монет для суммы x
    dp = [INF] * (amount + 1)
    dp[0] = 0

    # строим dp снизу вверх
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # если сумма не достижима
    return dp[amount] if dp[amount] != INF else -1


def lis(nums):
    n = len(nums)

    if n == 0:
        return 0, []

    # dp[i] = длина LIS, заканчивающейся на nums[i]
    dp = [1] * n

    # prev[i] = индекс предыдущего элемента в LIS
    prev = [-1] * n

    # Заполнение DP (восходящий подход)
    for i in range(1, n):
        for j in range(0, i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Длина LIS — максимум в dp[]
    lis_length = max(dp)

    # Находим последний элемент LIS
    end_index = dp.index(lis_length)

    # Восстановление LIS
    lis_seq = []
    while end_index != -1:
        lis_seq.append(nums[end_index])
        end_index = prev[end_index]

    lis_seq.reverse()

    return lis_length, lis_seq

    # Временная сложность: O(n^2)
    # Пространственная сложность: O(n)


if __name__ == "__main__":
    print("=== Демонстрация coin_change ===")
    coins = [1, 3, 4]
    amount = 6
    result = coin_change(coins, amount)
    print(f"Монеты: {coins}")
    print(f"Сумма: {amount}")
    print(f"Минимальное количество монет: {result}")

    print("\n=== Демонстрация LIS ===")
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    length, sequence = lis(arr)
    print(f"Массив: {arr}")
    print(f"Длина LIS: {length}")
    print(f"LIS: {sequence}")
