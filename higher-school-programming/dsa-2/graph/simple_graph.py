from typing import List, Any, Union


class Vertex:

    def __init__(self, val) -> None:
        self.Value = val
        self.hit = False

    def __repr__(self):
        return f'Vertex(val={self.Value}, hit={self.hit})'


class SimpleGraph:

    def __init__(self, size) -> None:
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: List[Union[Vertex, None]] = [None] * size

    def AddVertex(self, value: Any) -> None:
        if self.vertex.count(None) == 0:
            return
        index_new_vertex = self.vertex.index(None)
        self.vertex[index_new_vertex] = Vertex(value)

    def RemoveVertex(self, v: int) -> None:
        for i in range(self.max_vertex):
            self.RemoveEdge(i, v)
        self.vertex[v] = None

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
    
    def _reset_vertices_hit(self):
        for i, vert in enumerate(self.vertex):
            if vert is not None:
                self.vertex[i].hit = False
        
    def _depth_first_search(self, v_from, v_to, result):
        if not self.vertex[v_from].hit:
            self.vertex[v_from].hit = True
            result.append(self.vertex[v_from])
            if self.IsEdge(v_from, v_to):
                result.append(self.vertex[v_to])
                return result
        for i in range(self.max_vertex):
            if self.m_adjacency[v_from][i] and not self.vertex[i].hit:
                return self._depth_first_search(i, v_to, result)
        result.pop()
        if not len(result):
            return []
        return self._depth_first_search(len(result)-1, v_to, result)

    def DepthFirstSearch(self, v_from, v_to):
        self._reset_vertices_hit()
        return self._depth_first_search(v_from, v_to, [])
