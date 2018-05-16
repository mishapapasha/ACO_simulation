from src.Ant import Ant

class Altercentric(Ant):
    def __init__(self,graph,edge):
        super().__init__(graph,edge)
        print('im altercentric')