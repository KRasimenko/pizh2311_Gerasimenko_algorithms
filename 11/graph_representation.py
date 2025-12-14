from collections import deque


class AdjacencyMatrixGraph:
    def __init__(self):
        # Матрица хранится как список списков
        # Память: O(V^2), где V — число вершин
        self.matrix = []

    def add_vertex(self):
        """
        Добавление вершины.
        Сложность: O(V), потому что нужно добавить 1 столбец в каждую строку.
        """
        V = len(self.matrix)
        for row in self.matrix:
            row.append(0)  # расширяем каждую строку
        self.matrix.append([0] * (V + 1))  # добавляем новую строку нулей

    def remove_vertex(self, v):
        """
        Удаление вершины по индексу v.
        Сложность: O(V^2), так как нужно удалить строку и столбец.
        """
        self.matrix.pop(v)
        for row in self.matrix:
            row.pop(v)

    def add_edge(self, u, v):
        """
        Добавление ребра (u, v).
        Сложность: O(1).
        """
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # если граф неориентированный

    def remove_edge(self, u, v):
        """
        Удаление ребра (u, v).
        Сложность: O(1).
        """
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0  # если граф неориентированный


class AdjacencyListGraph:
    def __init__(self):
        # Список: у каждой вершины свой список соседей
        # Память: O(V + E), где E — число рёбер
        self.adj = []

    def add_vertex(self):
        """
        Добавление вершины.
        Сложность: O(1).
        """
        self.adj.append([])

    def remove_vertex(self, v):
        """
        Удаление вершины v.
        Сложность: O(V + E).
        """
        self.adj.pop(v)
        for neighbors in self.adj:
            # удаление: O(deg), в сумме O(E)
            while v in neighbors:
                neighbors.remove(v)
            # уменьшение индексов вершин > v
            for i in range(len(neighbors)):
                if neighbors[i] > v:
                    neighbors[i] -= 1

    def add_edge(self, u, v):
        """
        Добавление ребра (u, v).
        Сложность: O(1) амортизированно.
        """
        self.adj[u].append(v)
        self.adj[v].append(u)  # если граф неориентированный

    def remove_edge(self, u, v):
        """
        Удаление ребра (u, v).
        Сложность: O(deg(u) + deg(v)).
        """
        if v in self.adj[u]:
            self.adj[u].remove(v)
        if u in self.adj[v]:
            self.adj[v].remove(u)


# ---------------- BFS ---------------- #

def bfs_with_paths(adj, start):
    """
    BFS с расстояниями и родителями для восстановления пути.
    Время:  O(V + E)
    Память: O(V)
    """

    n = len(adj)
    dist = [-1] * n
    parent = [-1] * n

    dist[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for to in adj[v]:
            if dist[to] == -1:      # ещё не посещён
                dist[to] = dist[v] + 1
                parent[to] = v
                queue.append(to)

    return dist, parent


def restore_path(parent, target):
    """
    Восстановление пути по массиву parent.
    Время: O(L), где L — длина пути.
    """
    path = []
    v = target
    while v != -1:
        path.append(v)
        v = parent[v]
    return path[::-1]


# DFS (recursive)

def dfs_recursive(adj, start, visited=None):
    """
    Рекурсивный DFS.
    Время:  O(V + E)
    Память: O(V) из-за глубины рекурсии
    """

    if visited is None:
        visited = [False] * len(adj)

    visited[start] = True

    for to in adj[start]:
        if not visited[to]:
            dfs_recursive(adj, to, visited)

    return visited


# DFS (iterative)

def dfs_iterative(adj, start):
    """
    Итеративный DFS на стеке.
    Время:  O(V + E)
    Память: O(V)
    """

    visited = [False] * len(adj)
    stack = [start]

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = True

            for to in reversed(adj[v]):
                if not visited[to]:
                    stack.append(to)

    return visited


def main():
    # создаём граф
    g = AdjacencyListGraph()

    # добавим 5 вершин
    for _ in range(5):
        g.add_vertex()

    # добавим рёбра
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("Список смежности:", g.adj)

    # BFS
    dist, parent = bfs_with_paths(g.adj, 0)
    print("\nBFS расстояния:", dist)
    print("BFS родители:", parent)

    # восстановление пути 0 → 4
    path = restore_path(parent, 4)
    print("Путь 0 → 4:", path)

    # ---- DFS recursive ----
    visited_rec = dfs_recursive(g.adj, 0)
    print("\nDFS (рекурсивный):", visited_rec)

    # ---- DFS iterative ----
    visited_it = dfs_iterative(g.adj, 0)
    print("DFS (итеративный):", visited_it)


# Запуск
if __name__ == "__main__":
    main()
