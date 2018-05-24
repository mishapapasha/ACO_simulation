

class Ant:
    _paiDeposite = 1
    _alpha = 2
    _beta = 3
    def __init__(self,graph,vertex):
        self.graph = graph ##reference to an instance of the graph.
        self.UnvisetedVertexes = list(getattr(graph, 'vertexes'))
        self.edgesVisited = []
        self.curentVertex = vertex
        self.popCurrentVertex()
        self.antType = 0

    def popCurrentVertex(self):
        self.UnvisetedVertexes.pop(self.UnvisetedVertexes.index(self.curentVertex))
        #print(len(self.UnvisetedVertexes))

    def move(self):
        return 1


    def pickEdge(self):
        return 1

    def attractiveness(self, targetVertx):
        return 1

    def depositePH(self):
        for edge in self.edgesVisited:
            distanceSum=0
            for edge2 in self.edgesVisited:
                distanceSum+=getattr(edge2,'distance')
            getattr(edge, 'ph')[self.antType]+= (Ant._paiDeposite/distanceSum)  ##formula 2