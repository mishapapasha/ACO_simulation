from src.Edge import Edge

class EdgeBuilder:
    def __init__(self, vs):
        self.vs = vs

    def connectVertexes(self):
        vertexCheck = []
        edges = []
        for v in self.vs:
            for vc in vertexCheck:
                edges.append(Edge(v, vc))
            vertexCheck.append(v)
        #print(len(edges))
        # for e in edges:
        #    e.printConnect()