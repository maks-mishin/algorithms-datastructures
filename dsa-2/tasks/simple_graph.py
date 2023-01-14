from typing import List, Any, Union


class Vertex:

    def __init__(self, val):
        self.Value = val

    def __repr__(self):
        return f'Vertex(val={self.Value})'


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: List[Union[Vertex, None]] = [None] * size
        self.vertex_count = 0

    def AddVertex(self, value: Any) -> None:
        index_new_vertex = self.vertex.index(None)
        self.vertex[index_new_vertex] = Vertex(value)
        self.vertex_count += 1

    def RemoveVertex(self, v: int) -> None:
        for i in range(self.max_vertex):
            self.RemoveEdge(i, v)
        self.vertex[v] = None
        self.vertex_count -= 1

    def IsEdge(self, v1: int, v2: int) -> bool:
        return self.m_adjacency[v1][v2] == self.m_adjacency[v2][v1] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def __repr__(self):
        return '\n'.join(
            [' '.join([str(v) for v in row]) for row in self.m_adjacency]
        )
