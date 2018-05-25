# import numpy as np
# import matplotlib.pyplot as plt

import src.util.fileReader as fr
from src.util.EdgeBuilder import EdgeBuilder
from src.Graph import Graph
from src.util.AntBuilder import AntBuilder
from src.Ant import Ant


_demographics = {
    'classic':  100,
    'ec':       0,
    'ac':       0,
    'gc':       0,
    'bc':       0
}

fr.createVertexFromFile()
eb = EdgeBuilder(fr.getVertexes())
eb.connectVertexes()
graph = Graph(getattr(eb, 'vertexes'), getattr(eb, 'edges'))

AB = AntBuilder(_demographics, graph)

for itr in range(100):
    print('itr-{0}'.format(itr))
    for ant in AB.antList:
        ant.cycle(len(graph.vertexes) - 1)
    for ant in AB.antList:
        ant.retrack()
    graph.phromoneEvaporate()

print(Ant._best)
    #graph.phromoneEvaporate()
print("hello darkness my old friend")
#wtf is this steaming pile of shite
