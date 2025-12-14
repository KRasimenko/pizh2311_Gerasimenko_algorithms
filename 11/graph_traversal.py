import time
import random
import matplotlib.pyplot as plt
import networkx as nx
from graph_representation import AdjacencyListGraph
from heapq import heappush, heappop


def connected_components(adj):
    n = len(adj)
    visited = [False] * n
    components = []

    for v in range(n):
        if not visited[v]:
            stack = [v]
            comp = []
            visited[v] = True

            while stack:
                u = stack.pop()
                comp.append(u)
                for to in adj[u]:
                    if not visited[to]:
                        visited[to] = True
                        stack.append(to)
            components.append(comp)
    return components


def topological_sort(adj):
    n = len(adj)
    indeg = [0] * n
    for v in adj:
        for to in v:
            indeg[to] += 1
    queue = [v for v in range(n) if indeg[v] == 0]
    order = []
    while queue:
        v = queue.pop()
        order.append(v)
        for to in adj[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                queue.append(to)
    if len(order) != n:
        raise ValueError("Граф содержит цикл")
    return order


def dijkstra(adj_w, start):
    INF = 10**18
    n = len(adj_w)
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    pq = []
    heappush(pq, (0, start))
    while pq:
        d, v = heappop(pq)
        if d != dist[v]:
            continue
        for to, w in adj_w[v]:
            if dist[v] + w < dist[to]:
                dist[to] = dist[v] + w
                parent[to] = v
                heappush(pq, (dist[to], to))
    return dist, parent


# Измерение времени
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start


def generate_random_graph(n, edge_factor=3, weighted=False):
    g = AdjacencyListGraph()
    for _ in range(n):
        g.add_vertex()
    edges = []
    for _ in range(n * edge_factor):
        u, v = random.randint(0, n-1), random.randint(0, n-1)
        g.add_edge(u, v)
        w = random.randint(1, 10)
        if weighted:
            edges.append((u, v, w))
    if weighted:
        adj_w = [[] for _ in range(n)]
        for u, v, w in edges:
            adj_w[u].append((v, w))
        return g, adj_w
    return g, None


# Визуализация графа
def draw_graph(adj, title="Graph"):
    G = nx.Graph()
    for i, neighbors in enumerate(adj):
        for j in neighbors:
            G.add_edge(i, j)
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(title)
    plt.show()


def main():
    sizes = [10, 50, 100, 200]  # размер графа
    times_cc = []
    times_ts = []
    times_dj = []

    for n in sizes:
        print(f"\nГраф с {n} вершинами:")
        g, adj_w = generate_random_graph(n, edge_factor=3, weighted=True)

        t_cc = measure_time(connected_components, g.adj)
        times_cc.append(t_cc)
        print(f"connected_components: {t_cc:.6f} с")

        # топологическая сортировка (на небольшом DAG)
        dag = [list(range(i+1, min(i+4, n))) for i in range(n)]
        t_ts = measure_time(topological_sort, dag)
        times_ts.append(t_ts)
        print(f"topological_sort: {t_ts:.6f} с")

        t_dj = measure_time(dijkstra, adj_w, 0)
        times_dj.append(t_dj)
        print(f"Dijkstra: {t_dj:.6f} с")

        # Визуализируем небольшой граф
        if n <= 20:
            draw_graph(g.adj, title=f"Random Graph n={n}")

    # Графики
    plt.plot(sizes, times_cc, 'o-', label='Connected Components')
    plt.plot(sizes, times_ts, 's-', label='Topological Sort')
    plt.plot(sizes, times_dj, '^-', label='Dijkstra')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение времени выполнения алгоритмов')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
