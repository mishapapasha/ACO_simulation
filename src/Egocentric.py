from src.Ant import Ant

class Egocentric(Ant):
    def __init__(self,graph,edge):
        super().__init__(graph,edge)
        print('Im egocentric', end='\t\t')
        print('starting point:\t{0}'.format(self.curentVertex.id))