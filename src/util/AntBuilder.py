from src.Ant import Ant
from src.Classic import Classic
from src.Egocentric import Egocentric
from src.Altercentric import Altercentric
from src.GoodAC import GoodAC
from src.BadAC import BadAC

class AntBuilder:
    antType = {
        'classic':  Classic,
        'ec':       Egocentric,
        'ac':       Altercentric,
        'gc':       GoodAC,
        'bc':       BadAC
    }
    def __init__(self,demographics,graph):
        self.antList=[]
        for antType in demographics:
            for i in range(demographics[antType]):
                self.antList.append(AntBuilder.antType[antType](graph))


