
class Vertex:
    def __init__(self, id, cX, cY):
        self.id = int(id)
        self.cX = cX
        self.cY = cY
        self.edges = []

    def getEdge(self, target):
        for edge in  self.edges:
            #print('{0},\t{1}'.format(edge.connect, {v1, v2}))
            if edge.connect == {self, target}:
                return edge
        print('didn\'t find the edge.')
        return None

    def printVertex(self):
        print('{0}: x: {1}, y: {2}'.format(self.id, self.cX, self.cY))

    def addEdge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return '{0}: x: {1}, y: {2}'.format(self.id, self.cX, self.cY)

    def __repr__(self):
        return '{0}'.format(self.id)
