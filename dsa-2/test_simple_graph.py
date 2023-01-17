import unittest
from tasks.simple_graph import SimpleGraph


def make_test_graph() -> SimpleGraph:
    graph = SimpleGraph(3)
    for i in range(4):
        graph.AddVertex(i)
    return graph


def add_edges_to_graph(graph: SimpleGraph) -> SimpleGraph:
    graph.AddEdge(0, 1)
    graph.AddEdge(1, 2)
    graph.AddEdge(0, 2)
    # Добавляем петлю к вершине 0
    graph.AddEdge(0, 0)
    return graph


class TestSimpleGraph(unittest.TestCase):
    def test_constructor(self):
        test_max_vertex_list = [0, 1, 2, 3]
        test_vertex_list = [
            [], [None], [None, None], [None, None, None]
        ]
        test_m_adjacency = [
            [], [[0]], [[0, 0], [0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]
        for i in range(4):
            graph = SimpleGraph(i)
            self.assertEqual(graph.max_vertex, test_max_vertex_list[i])
            self.assertListEqual(graph.vertex, test_vertex_list[i])
            self.assertListEqual(graph.m_adjacency, test_m_adjacency[i])
            self.assertEqual(graph.vertex_count, 0)

    def test_add_vertex(self):
        graph = SimpleGraph(1)
        graph.AddVertex('A')
        self.assertEqual(graph.vertex[0].Value, 'A')
        self.assertListEqual(graph.m_adjacency, [[0]])

        graph = SimpleGraph(2)
        graph.AddVertex('A')
        graph.AddVertex('B')
        self.assertEqual(graph.vertex[0].Value, 'A')
        self.assertEqual(graph.vertex[1].Value, 'B')
        self.assertListEqual(graph.m_adjacency, [[0, 0], [0, 0]])

    def test_cannot_add_vertex(self):
        graph = SimpleGraph(0)
        graph.AddVertex(12)
        self.assertListEqual(graph.vertex, [])
        self.assertListEqual(graph.m_adjacency, [])

        graph = make_test_graph()
        self.assertEqual(len(graph.vertex), 3)
        graph.AddVertex(12)
        self.assertEqual(len(graph.vertex), 3)

    def test_remove_vertex_without_edges(self):
        graph = make_test_graph()
        self.assertListEqual(
            graph.m_adjacency, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        )
        self.assertEqual(graph.vertex[0].Value, 0)
        graph.RemoveVertex(0)
        self.assertEqual(graph.vertex[0], None)

    def test_remove_vertex_with_edges(self):
        graph = add_edges_to_graph(make_test_graph())
        self.assertEqual(graph.m_adjacency[0][0], 1)
        self.assertEqual(graph.m_adjacency[0][1], 1)
        self.assertEqual(graph.m_adjacency[1][0], 1)
        self.assertEqual(graph.m_adjacency[0][2], 1)
        self.assertEqual(graph.m_adjacency[2][0], 1)
        self.assertEqual(graph.m_adjacency[2][1], 1)
        graph.RemoveVertex(0)
        self.assertEqual(graph.m_adjacency[2][1], 1)
        self.assertEqual(graph.m_adjacency[0][0], 0)
        self.assertEqual(graph.m_adjacency[0][1], 0)
        self.assertEqual(graph.m_adjacency[1][0], 0)
        self.assertEqual(graph.m_adjacency[0][2], 0)
        self.assertEqual(graph.m_adjacency[2][0], 0)

    def test_is_edge(self):
        graph = add_edges_to_graph(make_test_graph())
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(0, 2))
        self.assertTrue(graph.IsEdge(1, 2))
        self.assertTrue(graph.IsEdge(0, 0))

        graph = make_test_graph()
        graph.AddEdge(0, 1)
        self.assertFalse(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(0, 2))

    def test_remove_edge(self):
        graph = add_edges_to_graph(make_test_graph())
        graph.RemoveEdge(0, 1)
        self.assertEqual(graph.m_adjacency[1][0], 0)
        self.assertEqual(graph.m_adjacency[0][1], 0)

    def test_add_edge(self):
        graph = make_test_graph()
        for row in graph.m_adjacency:
            for col in range(graph.max_vertex):
                self.assertEqual(row[col], 0)
        graph.AddEdge(0, 1)
        self.assertEqual(graph.m_adjacency[1][0], 1)
        self.assertEqual(graph.m_adjacency[0][1], 1)


if __name__ == '__main__':
    unittest.main()