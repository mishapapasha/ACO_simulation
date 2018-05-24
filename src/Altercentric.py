from src.Ant import Ant

class Altercentric(Ant):
    def __init__(self,graph,edge):
        super().__init__(graph,edge)
        print('Im altercentric', end='\t\t')
        print('starting point:\t{0}'.format(self.curentVertex.id))