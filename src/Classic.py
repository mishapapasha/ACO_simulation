from src.Ant import Ant

class Classic(Ant):
    def __init__(self,graph,edge):
        super().__init__(graph,edge)
        print('Im classic', end='\t\t\t')
        print('starting point:\t{0}'.format(self.curentVertex.id))

    def attractiveness(self, targetVertx):
        ans = 0
        edge = self.graph.getEdge(self.curentVertex, targetVertx)#ph**a/dis**b
        ph = edge.ph['classic']
        dis = edge.distance
        ans = (ph**Ant._alpha)/(dis**Ant._beta)
        return ans
