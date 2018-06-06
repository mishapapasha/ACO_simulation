from src.Ant import Ant
import random
import math

class GoodAC(Ant):
    _paiDeposite = 1.0
    _alpha = 2.0
    _beta = 3.0
    def __init__(self, graph):
        super().__init__(graph)

    def attractiveness(self, targetVertx):
        ans = 0
        edge = self.currentVertex.getEdge(targetVertx)  # ph**a/dis**b
        ph = (14 * edge.ph['ec']) + (2 * edge.ph['ac']) + (2.5 * edge.ph['gc']) + (0.5 * edge.ph['bc'])
        ans = ph ** self._alpha
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
        #print('prob:\t{0}'.format(sum(ar)))
        totalI = 0
        for i in range(len(ar)):
            totalI += ar[i]
            if prob <= totalI:
                return self.UnvisetedVertexes[i]

    def depositePH(self):
        # print(self.totalDistance)
        for edge in self.edgesVisited:
            # print('before:\t{}'.format(edge.ph['gc']))
            edge.ph['gc'] += (self._paiDeposite/self.totalDistance)
            # print('after:\t{}'.format(edge.ph['gc']))

    def getType(self):
        return 'gc'