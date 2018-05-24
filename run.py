# import numpy as np
# import matplotlib.pyplot as plt

import src.util.fileReader as fr
from src.util.EdgeBuilder import EdgeBuilder
from src.Graph import Graph
from src.util.AntBuilder import AntBuilder


_demographics = {
    'classic':  1,
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

print("hello darkmess my old friend")
#wtf is this steaming pile of shite
