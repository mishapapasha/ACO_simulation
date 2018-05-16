# import numpy as np
# import matplotlib.pyplot as plt

import src.util.fileReader as fr
from src.util.EdgeBuilder import EdgeBuilder
from src.Graph import Graph
from src.util.AntBuilder import AntBuilder


fr.createVertexFromFile()
eb = EdgeBuilder(fr.getVertexes())
eb.connectVertexes()
graph = Graph(getattr(eb, 'vertexes'), getattr(eb, 'edges'))
demographics = {
    'classic':  1,
    'ec':       1,
    'ac':       1,
    'gc':       2,
    'bc':       1
}

print("hello darkmess my old friend")
#wtf is this steaming pile of shite
AB = AntBuilder(demographics,graph)