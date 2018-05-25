import random

class Ant:
    _paiDeposite = 1
    _alpha = 2
    _beta = 3
    _best = 100000
    def __init__(self, graph):
        self.graph = graph ##reference to an instance of the graph.
        self.UnvisetedVertexes = []
        self.currentVertex = None
        self.edgesVisited = []
        self.totalDistance = 0

    def popCurrentVertex(self):
        #print(self.currentVertex)
        index = self.UnvisetedVertexes.index(self.currentVertex)
        #print(index)
        self.UnvisetedVertexes.pop(index)
        #print(len(self.UnvisetedVertexes))


    def move(self):
        return 1

    def cycle(self, steps):
        #print('steps:\t{0}'.format(steps))
        self.totalDistance = 0
        self.edgesVisited = []
        self.UnvisetedVertexes = list(getattr(self.graph, 'vertexes'))
        self.currentVertex = random.choice(self.UnvisetedVertexes)
        start = self.currentVertex
        self.popCurrentVertex()
        for step in range(steps):
            self.move()
            self.popCurrentVertex()
        lastEdge = self.currentVertex.getEdge(start)
        self.edgesVisited.append(lastEdge)
        self.totalDistance += lastEdge.distance
        if Ant._best > self.totalDistance:
            Ant._best = self.totalDistance
        print('total:\t{0}'.format(self.totalDistance))
        #print(len(self.edgesVisited))

    def pickVertex(self):
        return 1

    def attractiveness(self, targetVertx):
        return 1

    def retrack(self):
        self.depositePH()

    def depositePH(self):
        pass