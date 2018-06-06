
class Vertex:
    def __init__(self, id, cX, cY):
        self.id = int(id)
        self.cX = cX
        self.cY = cY
        self.edges = {}

    def getEdge(self, target):
        return self.edges[str(target.id)]

    def printVertex(self):
        print('{0}: x: {1}, y: {2}'.format(self.id, self.cX, self.cY))

    def addEdge(self, edge, vertex):
        self.edges[str(vertex.id)] = edge

    def __str__(self):
        return '{0}: x: {1}, y: {2}'.format(self.id, self.cX, self.cY)

    def __repr__(self):
        return '{0}'.format(self.id)
