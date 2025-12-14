from collections import deque
from graph_representation import AdjacencyListGraph
from graph_traversal import connected_components, topological_sort


# Кратчайший путь в лабиринте
def shortest_path_maze(maze, start, end):
    n, m = len(maze), len(maze[0])
    queue = deque([start])
    visited = [[False]*m for _ in range(n)]
    parent = [[None]*m for _ in range(n)]
    visited[start[0]][start[1]] = True

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # вправо, вниз, влево, вверх

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy in dirs:
            nx_, ny_ = x+dx, y+dy
            if 0 <= nx_ < n and 0 <= ny_ < m and maze[nx_][ny_] == 0 and not visited[nx_][ny_]:
                visited[nx_][ny_] = True
                parent[nx_][ny_] = (x, y)
                queue.append((nx_, ny_))

    # восстановление пути
    path = []
    cur = end
    while cur:
        path.append(cur)
        cur = parent[cur[0]][cur[1]]
    path.reverse()

    if path[0] != start:
        return []  # путь не найден
    return path


# Проверка связности сети
def is_network_connected(adj):
    comps = connected_components(adj)
    return len(comps) == 1


# Топологическая сортировка
def solve_topo(adj):
    return topological_sort(adj)


def main():
    # Пример лабиринта: 0 - свободная клетка, 1 - стена
    maze = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start, end = (0, 0), (3, 3)
    path = shortest_path_maze(maze, start, end)
    print("Кратчайший путь в лабиринте:", path)

    # Пример сети
    g = AdjacencyListGraph()
    for _ in range(5):
        g.add_vertex()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    print("Сеть связна?", is_network_connected(g.adj))

    # Пример DAG для топологической сортировки
    dag = [
        [1, 2],
        [3],
        [3],
        []
    ]
    print("Топологическая сортировка:", solve_topo(dag))


if __name__ == "__main__":
    main()
