

class Edge:
    def __init__(self, v1, v2):
        self.connect = {v1, v2}
        self.ph = 0

    def printConnect(self):
        vs = list(self.connect)
        print('Connect: {0} with {1}'.format(getattr(vs[0], 'id'), getattr(vs[1], 'id')))
