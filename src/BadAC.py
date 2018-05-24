from src.Ant import Ant

class BadAC(Ant):
    def __init__(self,graph,edge):
        super().__init__(graph,edge)
        print('im badac', end='\t\t\t')