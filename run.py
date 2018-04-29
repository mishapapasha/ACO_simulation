# import numpy as np
# import matplotlib.pyplot as plt

import src.util.fileReader as fr
from src.util.EdgeBuilder import EdgeBuilder

fr.createVertexFromFile()
eb = EdgeBuilder(fr.getVertexes())
eb.connectVertexes()

print("hello darkmess my old friend")
#wtf is this steaming pile of shite