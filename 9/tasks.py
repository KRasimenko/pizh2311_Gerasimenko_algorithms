def min_coins_greedy(amount):
    # Стандартная система монет (рубли/копейки)
    coins = [10, 5, 2, 1]  # можно менять на другую стандартную систему
    result = []
    remaining = amount

    for coin in coins:
        count = remaining // coin
        if count > 0:
            result.append((coin, count))
            remaining -= coin * count

    return result


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[u_root] += 1
        return True


# Алгоритм Краскала
def kruskal(n, edges):
    """
    n - количество вершин
    edges - список рёбер (u, v, вес)
    Возвращает список рёбер MST и общую сумму веса
    """
    edges.sort(key=lambda x: x[2])  # сортировка по весу
    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


if __name__ == "__main__":
    # Пример использования
    amount = 139
    change = min_coins_greedy(amount)

    print(f"Сумма сдачи: {amount}")
    print("Монеты для выдачи:")
    for coin, count in change:
        print(f"{coin}-рублевая монета: {count} шт.")

    n = 5
    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]

    mst, total = kruskal(n, edges)

    print("Рёбра минимального остовного дерева:")
    for u, v, w in mst:
        print(f"{u} - {v} (вес {w})")
    print("Общий вес MST:", total)
