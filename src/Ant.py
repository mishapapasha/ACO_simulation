import random
import sys
class Ant:
    def __init__(self, graph):
        self.graph = graph ##reference to an instance of the graph.
        self.UnvisetedVertexes = []
        self.currentVertex = None
        self.edgesVisited = []
        self.totalDistance = 0

    def popCurrentVertex(self):
        index = self.UnvisetedVertexes.index(self.currentVertex)
        self.UnvisetedVertexes.pop(index)


    def move(self):
        targetVertx = self.pickVertex()
        # print('curr:\t{0},\ttarget:\t{1}'.format(self.currentVertex, targetVertx))
        newEdge = self.currentVertex.getEdge(targetVertx)
        #print(newEdge.distance)
        self.totalDistance += newEdge.distance
        #######################################print('total:\t{0}'.format(self.totalDistance))
        self.edgesVisited.append(newEdge)
        # print(len(self.edgesVisited))
        self.currentVertex = targetVertx

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

        return self.totalDistance

    def pickVertex(self):
        pass

    def attractiveness(self, targetVertx):
        pass

    def retrack(self):
        self.depositePH()

    def depositePH(self):
        pass

    def getType(self):
        pass