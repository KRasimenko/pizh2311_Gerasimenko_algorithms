import unittest

from graph_representation import (
    AdjacencyListGraph,
    bfs_with_paths,
    dfs_recursive,
    dfs_iterative,
    restore_path,
)


from graph_traversal import (
    connected_components,
    topological_sort,
    dijkstra,
)


class TestGraphAlgorithms(unittest.TestCase):

    # ---------------- BFS ---------------- #
    def test_bfs_basic(self):
        g = AdjacencyListGraph()
        for _ in range(5):
            g.add_vertex()

        edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
        for u, v in edges:
            g.add_edge(u, v)

        dist, parent = bfs_with_paths(g.adj, 0)

        self.assertEqual(dist, [0, 1, 1, 2, 3])
        self.assertEqual(restore_path(parent, 4), [0, 1, 3, 4])

    # ---------------- DFS ---------------- #
    def test_dfs_recursive(self):
        g = AdjacencyListGraph()
        for _ in range(4):
            g.add_vertex()

        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)

        visited = dfs_recursive(g.adj, 0)
        self.assertEqual(visited, [True, True, True, True])

    def test_dfs_iterative(self):
        g = AdjacencyListGraph()
        for _ in range(4):
            g.add_vertex()

        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)

        visited = dfs_iterative(g.adj, 0)
        self.assertEqual(visited, [True, True, True, True])

    # ---------------- Connected Components ---------------- #
    def test_connected_components(self):
        g = AdjacencyListGraph()
        for _ in range(6):
            g.add_vertex()

        edges = [(0, 1), (1, 2), (3, 4)]
        for u, v in edges:
            g.add_edge(u, v)

        comps = connected_components(g.adj)
        comps = [sorted(c) for c in comps]
        comps.sort()

        expected = [[0, 1, 2], [3, 4], [5]]
        self.assertEqual(comps, expected)

    # ---------------- Topological Sort ---------------- #
    def test_topological_sort(self):
        dag = [
            [1, 2],
            [3],
            [3],
            []
        ]

        order = topological_sort(dag)
        self.assertTrue(order.index(0) < order.index(1))
        self.assertTrue(order.index(0) < order.index(2))
        self.assertTrue(order.index(1) < order.index(3))
        self.assertTrue(order.index(2) < order.index(3))

    def test_topological_sort_cycle(self):
        cyclic = [
            [1],
            [2],
            [0],  # цикл
        ]
        with self.assertRaises(ValueError):
            topological_sort(cyclic)

    # ---------------- Dijkstra ---------------- #
    def test_dijkstra(self):
        adj_w = [
            [(1, 4), (2, 1)],
            [(3, 1)],
            [(1, 2), (3, 5)],
            []
        ]

        dist, parent = dijkstra(adj_w, 0)
        self.assertEqual(dist, [0, 3, 1, 4])  # корректнейшие дистанции
        self.assertEqual(parent[3], 1)


if __name__ == "__main__":
    unittest.main()
