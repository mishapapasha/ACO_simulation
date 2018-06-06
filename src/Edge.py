import math

class Edge:
    def __init__(self, v1, v2):
        self.connect = {v1, v2}
        px = (getattr(v1, 'cX') - getattr(v2, 'cX')) ** 2
        py = (getattr(v1, 'cY') - getattr(v2, 'cY')) ** 2
        self.distance = math.sqrt(px + py)
        self.ph = { 'classic': 0, 'ec': 0, 'ac': 0, 'gc': 0, 'bc': 0 }  ##pheromone for ant type egocentric

    def printConnect(self):
        vs = list(self.connect)
        print('Connect: {0} with {1} distance: {2}'.format(getattr(vs[0], 'id'), getattr(vs[1], 'id'), self.distance))

    def __str__(self):
        return '{0}'.format(self.connect)

    def __repr__(self):
        return '{0}'.format(self.connect)
