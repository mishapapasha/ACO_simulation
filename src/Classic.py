from src.Ant import Ant
import random

class Classic(Ant):
    _paiDeposite = 1.0
    _alpha = 1.0
    _beta = 2.0
    def __init__(self, graph):
        super().__init__(graph)

    def attractiveness(self, targetVertx):
        ans = 0
        edge = self.currentVertex.getEdge(targetVertx)#ph**a/dis**b
        ph = edge.ph['classic']
        dis = edge.distance
        ans = (ph ** self._alpha)/(dis ** self._beta)
        return ans

    def pickVertex(self):
        attractivenessArray = ar = []
        totalAR = 0
        for vertex in self.UnvisetedVertexes:
            at = self.attractiveness(vertex)
            totalAR += at
            ar.append(at)
        ar = list(map(lambda x: x / totalAR, ar))
        prob = random.uniform(0, 1)
        #print('prob:\t{0}'.format(prob))
        totalI = 0
        for i in range(len(ar)):
            totalI += ar[i]
            if prob < totalI:
                return self.UnvisetedVertexes[i]

    def depositePH(self):
        for edge in self.edgesVisited:
            edge.ph['classic'] += (self._paiDeposite/self.totalDistance)
