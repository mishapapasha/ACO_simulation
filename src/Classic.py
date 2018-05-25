from src.Ant import Ant
import random

class Classic(Ant):
    def __init__(self, graph):
        super().__init__(graph)

    def attractiveness(self, targetVertx):
        ans = 0
        # print('current:\t{0}'.format(self.currentVertex))
        edge = self.currentVertex.getEdge(targetVertx)#ph**a/dis**b
        ph = edge.ph['classic']
        dis = edge.distance
        ans = (ph ** Ant._alpha)/(dis ** Ant._beta)
        return ans

    def pickVertex(self):
        attractivenessArray = ar = []
        totalAR = 0
        for vertex in self.UnvisetedVertexes:
            #print(vertex)
            at = self.attractiveness(vertex)
            totalAR += at
            ar.append(at)
        #print('vertexes to check:\t{0}'.format(len(ar)))
        #print('totalAR:\t{0}'.format(totalAR))
        ar = list(map(lambda x: x / totalAR, ar))
        prob = random.uniform(0, 1)
        #print('prob:\t{0}'.format(prob))
        totalI = 0
        for i in range(len(ar)):
            totalI += ar[i]
            #print('ar[{0}]:\t{1}'.format(i, ar[i]))
            if prob <= totalI:
                #print('totalI:\t{0}'.format(totalI))
                return self.UnvisetedVertexes[i]

    def move(self):
        targetVertx = self.pickVertex()
        #print('curr:\t{0},\ttarget:\t{1}'.format(self.currentVertex, targetVertx))
        newEdge = self.currentVertex.getEdge(targetVertx)
        #######################################print(newEdge.distance)
        self.totalDistance += newEdge.distance
        #######################################print('total:\t{0}'.format(self.totalDistance))
        self.edgesVisited.append(newEdge)
        #print(len(self.edgesVisited))
        self.currentVertex = targetVertx

    def depositePH(self):
        for edge in self.edgesVisited:
            edge.ph['classic'] += (Ant._paiDeposite/self.totalDistance)
