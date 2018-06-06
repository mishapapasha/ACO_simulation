from src import Vertex
from src import Edge

class Graph:
    _evaporation = 0.01

    def __init__(self, V, E):
        self.vertexes = V
        self.edges = E

    def phromoneEvaporate(self, type):
        for edge in self.edges:
            edge.ph[type] = (1 - Graph._evaporation) * edge.ph[type]

    def setStartPh(self, ph):
        for edge in self.edges:
            edge.ph = dict(ph)


