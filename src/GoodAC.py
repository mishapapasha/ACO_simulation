from src.Ant import Ant

class GoodAC(Ant):
    def __init__(self,graph,edge):
        super().__init__(graph,edge)
        print('im GoodAC')