from src.Ant import Ant
from random import randint

class BadAC(Ant):
    _paiDeposite = 1.0
    _alpha = 2.0
    _beta = 3.0
    def __init__(self, graph):
        super().__init__(graph)

    def attractiveness(self, targetVertx):
        vertexCount = self.UnvisetedVertexes
        return 1 / len(vertexCount)

    def pickVertex(self):
        index = randint(0, len(self.UnvisetedVertexes) - 1)
        return self.UnvisetedVertexes[index]
        # attractivenessArray = ar = []
        # totalAR = 0
        # for vertex in self.UnvisetedVertexes:
        #     at = self.attractiveness(vertex)
        #     totalAR += at
        #     ar.append(at)
        #
        # ar = list(map(lambda x: x / totalAR, ar))
        # prob = random.uniform(0, 1)
        # #print('prob:\t{0}'.format(sum(ar)))
        # totalI = 0
        # for i in range(len(ar)):
        #     totalI += ar[i]
        #     if prob <= totalI:
        #         return self.UnvisetedVertexes[i]

    def depositePH(self):
        # print(self.totalDistance)
        for edge in self.edgesVisited:
            edge.ph['bc'] += (self._paiDeposite/self.totalDistance)
            #print(edge.ph['bc'])

    def getType(self):
        return 'bc'
