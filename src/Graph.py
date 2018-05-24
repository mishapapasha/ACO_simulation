from src import Vertex
from src import Edge

class Graph:
    def __init__(self, V, E):
        self.vertexes = V
        self.edges = E

    def getEdge(self, v1, v2):
        for edge in  self.edges:
            if edge.connect == {v1, v2}:
                return edge
        print('didn\'t find the edge.')


