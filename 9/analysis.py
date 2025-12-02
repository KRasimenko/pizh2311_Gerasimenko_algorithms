import random
import itertools

# Fractional knapsack (жадный алгоритм для дробного рюкзака)
def fractional_knapsack(items, capacity):
    items_sorted = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0
    taken = []
    remaining = capacity
    for value, weight in items_sorted:
        if remaining == 0:
            break
        if weight <= remaining:
            total_value += value
            taken.append((value, weight, 1.0))
            remaining -= weight
        else:
            fraction = remaining / weight
            total_value += value * fraction
            taken.append((value, weight, fraction))
            remaining = 0
            break
    return total_value, taken

# Greedy 0/1 knapsack
def greedy_01_knapsack(items, capacity):
    indexed = list(enumerate(items))
    indexed.sort(key=lambda iv: iv[1][0] / iv[1][1], reverse=True)
    total_value = 0
    remaining = capacity
    taken_indices = []
    for i, (value, weight) in indexed:
        if weight <= remaining:
            remaining -= weight
            total_value += value
            taken_indices.append(i)
    return total_value, taken_indices

# Exact 0/1 knapsack by brute-force
def exact_01_knapsack_bruteforce(items, capacity):
    n = len(items)
    best_value = 0
    best_subset = []
    for r in range(n + 1):
        for combination in itertools.combinations(range(n), r):
            weight_sum = sum(items[i][1] for i in combination)
            if weight_sum <= capacity:
                value_sum = sum(items[i][0] for i in combination)
                if value_sum > best_value:
                    best_value = value_sum
                    best_subset = list(combination)
    return best_value, best_subset

def demonstrate_example():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50

    frac_val, frac_taken = fractional_knapsack(items, capacity)
    greedy_val, greedy_taken = greedy_01_knapsack(items, capacity)
    exact_val, exact_taken = exact_01_knapsack_bruteforce(items, capacity)

    print("Предметы (стоимость, вес):", items)
    print("Вместимость рюкзака:", capacity)
    print()
    print("Результат дробного жадного алгоритма:")
    print("Стоимость =", frac_val)
    print("Взято:", frac_taken)
    print()
    print("Результат жадного алгоритма 0/1:")
    print("Стоимость =", greedy_val)
    print("Взято:", [items[i] for i in greedy_taken])
    print()
    print("Точное оптимальное решение 0/1:")
    print("Стоимость =", exact_val)
    print("Взято:", [items[i] for i in exact_taken])
    print()
    print("Вывод: жадный 0/1 дал", greedy_val,
          "а оптимальный дал", exact_val)
    print("То есть жадный 0/1 не всегда находит лучшее решение!")
    print("Дробный дает", frac_val, "что еще лучше, так как можно брать части предметов.")

def random_trials(trials=200, n_items=6, max_weight=10, max_value=30):
    failures = 0
    for _ in range(trials):
        items = [(random.randint(1, max_value), random.randint(1, max_weight)) for _ in range(n_items)]
        capacity = sum(w for _, w in items) // 2
        greedy_val, _ = greedy_01_knapsack(items, capacity)
        exact_val, _ = exact_01_knapsack_bruteforce(items, capacity)
        if greedy_val < exact_val:
            failures += 1
    print("\nПроверка на случайных данных:")
    print("Жадный 0/1 ошибся в", failures, "из", trials, "случаев.")
    print("Доля ошибок =", failures / trials)

if __name__ == "__main__":
    demonstrate_example()
    random_trials()
