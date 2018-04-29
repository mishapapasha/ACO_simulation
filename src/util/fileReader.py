import os.path
import numpy as np

from src.Vertex import Vertex

Column = {"id": 0, "cX": 1, "cY": 2}
_vs = []
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../assets/Berlin52.txt")

try:
    node_file = open(path, "r")
except ValueError:
    print("File not opend!!!@!@!@")

def createVertexFromFile():
    for line in node_file:
        columns = np.fromstring(line, dtype=float, sep=' ')
        v = Vertex(columns[Column['id']], columns[Column['cX']], columns[Column['cY']])
        ##v.printVertex()
        _vs.append(v)

def getVertexes():
    return _vs
