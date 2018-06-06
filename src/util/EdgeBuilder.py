from src.Edge import Edge

class EdgeBuilder:
    def __init__(self, vs):
        self.vertexes = vs
        self.edges = []

    def connectVertexes(self):
        ##connect all vertexes with Undirected edges
        vertexCheck = []
        for v in self.vertexes:
            for vc in vertexCheck:
                e = Edge(v, vc)
                v.addEdge(e, vc)
                vc.addEdge(e , v)
                self.edges.append(e)
            vertexCheck.append(v)

        # for v in self.vs:
        #     print(len(getattr(v, 'edges')))
        #print(len(edges))
        # for e in self.edges:
        #    e.printConnect()