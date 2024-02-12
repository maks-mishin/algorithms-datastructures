import unittest
from unittest import TestCase

from simple_graph import SimpleGraph, Vertex


def make_small_graph() -> SimpleGraph:
    graph = SimpleGraph(3)
    for i in range(4):
        graph.AddVertex(i)
    return graph


def add_edges_to_small_graph(graph: SimpleGraph) -> SimpleGraph:
    graph.AddEdge(0, 1)
    graph.AddEdge(1, 2)
    graph.AddEdge(0, 2)
    # Добавляем петлю к вершине 0
    graph.AddEdge(0, 0)
    return graph


def create_test_graph() -> SimpleGraph:
    """create test graph for further testing"""

    sgraph = SimpleGraph(7)
    sgraph.m_adjacency = [
        [0, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    sgraph.vertex = [
        Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5),
        None, None
    ]
    for i, vert in enumerate(sgraph.vertex):
        if vert is not None:
            vert.index = i
    return sgraph


class TestSimpleGraph(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)

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

        graph = make_small_graph()
        self.assertEqual(len(graph.vertex), 3)
        graph.AddVertex(12)
        self.assertEqual(len(graph.vertex), 3)

    def test_remove_vertex_without_edges(self):
        graph = make_small_graph()
        self.assertListEqual(
            graph.m_adjacency, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        )
        self.assertEqual(graph.vertex[0].Value, 0)
        graph.RemoveVertex(0)
        self.assertEqual(graph.vertex[0], None)

    def test_remove_vertex_with_edges(self):
        graph = add_edges_to_small_graph(make_small_graph())
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
        graph = add_edges_to_small_graph(make_small_graph())
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(0, 2))
        self.assertTrue(graph.IsEdge(1, 2))
        self.assertTrue(graph.IsEdge(0, 0))

        graph = make_small_graph()
        graph.AddEdge(0, 1)
        self.assertFalse(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(0, 2))

    def test_remove_edge(self):
        graph = add_edges_to_small_graph(make_small_graph())
        graph.RemoveEdge(0, 1)
        self.assertEqual(graph.m_adjacency[1][0], 0)
        self.assertEqual(graph.m_adjacency[0][1], 0)

    def test_add_edge(self):
        graph = make_small_graph()
        for row in graph.m_adjacency:
            for col in range(graph.max_vertex):
                self.assertEqual(row[col], 0)
        graph.AddEdge(0, 1)
        self.assertEqual(graph.m_adjacency[1][0], 1)
        self.assertEqual(graph.m_adjacency[0][1], 1)

    def test_depth_first_search(self):
        """testing find path between 2 vertexes"""

        sgraph = create_test_graph()
        self.assertListEqual(
            sgraph.DepthFirstSearch(0, 4),
            [sgraph.vertex[0], sgraph.vertex[1], sgraph.vertex[4]]
        )
        sgraph.RemoveEdge(0, 1)
        sgraph.RemoveEdge(0, 3)
        self.assertListEqual(
            sgraph.DepthFirstSearch(0, 4),
            [sgraph.vertex[0], sgraph.vertex[2],
             sgraph.vertex[3], sgraph.vertex[4]]
        )

    def test_depth_first_search2(self):
        """more testing find path between 2 vertexes"""

        sgraph = create_test_graph()
        sgraph.RemoveEdge(1, 3)
        sgraph.AddVertex(6)
        sgraph.AddVertex(7)
        sgraph.AddEdge(4, 5)
        sgraph.AddEdge(4, 6)
        self.assertListEqual(
            sgraph.DepthFirstSearch(0, 6),
            [sgraph.vertex[0], sgraph.vertex[1],
             sgraph.vertex[4], sgraph.vertex[6]]
        )

    def test_depth_first_search_no_path(self):
        """testing path should not exist"""

        sgraph = create_test_graph()
        sgraph.RemoveEdge(1, 4)
        sgraph.RemoveEdge(3, 4)
        self.assertListEqual(sgraph.DepthFirstSearch(0, 4), [])

    def test_breadth_first_search(self):
        """testing find path between 2 vertexes"""

        sgraph = create_test_graph()
        self.assertListEqual(
            sgraph.BreadthFirstSearch(0, 4),
            [sgraph.vertex[0], sgraph.vertex[1], sgraph.vertex[4]]
        )
        sgraph.RemoveEdge(0, 1)
        sgraph.RemoveEdge(0, 3)
        self.assertListEqual(
            sgraph.BreadthFirstSearch(0, 4),
            [sgraph.vertex[0], sgraph.vertex[2],
             sgraph.vertex[3], sgraph.vertex[4]]
        )

    def test_breadth_first_search2(self):
        """more testing find path between 2 vertexes"""

        sgraph = create_test_graph()
        sgraph.RemoveEdge(0, 1)
        sgraph.AddVertex(6)
        sgraph.AddVertex(7)
        sgraph.AddEdge(4, 5)
        sgraph.AddEdge(4, 6)
        self.assertListEqual(
            sgraph.BreadthFirstSearch(0, 6),
            [sgraph.vertex[0], sgraph.vertex[3],
             sgraph.vertex[4], sgraph.vertex[6]]
        )

    def test_breadth_first_search_no_path(self):
        """testing path should not exist"""

        sgraph = create_test_graph()
        sgraph.RemoveEdge(1, 4)
        sgraph.RemoveEdge(3, 4)
        self.assertListEqual(sgraph.BreadthFirstSearch(0, 4), [])

    def test_breadth(self):
        self.graph.AddVertex('A')
        self.graph.AddVertex('B')
        self.graph.AddVertex('C')
        self.graph.AddVertex('D')
        self.graph.AddVertex('E')

        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(3, 4)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 2):
            res.append(i.Value)

        self.assertEqual(['A', 'C'], res)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 4):
            res.append(i.Value)

        self.assertEqual(['A', 'B', 'E'], res)

        self.graph.RemoveEdge(1, 4)
        self.graph.RemoveEdge(3, 4)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 4):
            res.append(i.Value)

        self.assertEqual([], res)

        self.graph.RemoveEdge(0, 3)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 3):
            res.append(i.Value)

        self.assertEqual(['A', 'B', 'D'], res)

    def test_breadth1(self):
        self.graph = SimpleGraph(8)

        self.graph.AddVertex('A')
        self.graph.AddVertex('B')
        self.graph.AddVertex('C')
        self.graph.AddVertex('D')
        self.graph.AddVertex('E')
        self.graph.AddVertex('G')
        self.graph.AddVertex('F')
        self.graph.AddVertex('M')

        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(3, 4)
        self.graph.AddEdge(4, 5)
        self.graph.AddEdge(4, 6)
        self.graph.AddEdge(5, 7)
        self.graph.AddEdge(6, 7)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 7):
            res.append(i.Value)

        self.assertEqual(['A', 'B', 'E', 'G', 'M'], res)

        self.graph.RemoveEdge(4, 5)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 7):
            res.append(i.Value)

        self.assertEqual(['A', 'B', 'E', 'F', 'M'], res)

        res = []
        for i in self.graph.BreadthFirstSearch(4, 6):
            res.append(i.Value)

        self.assertEqual(['E', 'F'], res)

        self.graph.RemoveEdge(0, 3)
        self.graph.RemoveEdge(1, 4)
        self.graph.RemoveEdge(1, 3)

        res = []
        for i in self.graph.BreadthFirstSearch(1, 5):
            res.append(i.Value)

        self.assertEqual(['B', 'A', 'C', 'D', 'E', 'F', 'M', 'G'], res)

        self.graph.RemoveEdge(3, 4)
        self.assertEqual([], self.graph.BreadthFirstSearch(1, 5))

    def test_weak_vertices(self):
        sgraph = SimpleGraph(9)
        for i in range(9):
            sgraph.AddVertex(i)
        sgraph.AddEdge(0, 1)
        sgraph.AddEdge(0, 3)
        sgraph.AddEdge(0, 2)
        sgraph.AddEdge(2, 1)
        sgraph.AddEdge(2, 3)
        sgraph.AddEdge(4, 1)
        sgraph.AddEdge(5, 4)
        sgraph.AddEdge(5, 2)
        sgraph.AddEdge(5, 6)
        sgraph.AddEdge(5, 7)
        sgraph.AddEdge(6, 7)
        sgraph.AddEdge(7, 8)
        self.assertListEqual(
            sgraph.WeakVertices(), [sgraph.vertex[4], sgraph.vertex[8]]
        )


if __name__ == '__main__':
    unittest.main()
