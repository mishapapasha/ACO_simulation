
class Vertex:
    def __init__(self, id, cX, cY):
        self.id = id
        self.cX = cX
        self.cY = cY
        self.edges = []

    def printVertex(self):
        print('{0}: x: {1}, y: {2}'.format(self.id, self.cX, self.cY))

    def addEdge(self, edge):
        self.edges.append(edge)
