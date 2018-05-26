import numpy as np
import matplotlib.pyplot as plt

import src.util.fileReader as fr
from src.util.EdgeBuilder import EdgeBuilder
from src.Graph import Graph
from src.util.AntBuilder import AntBuilder
from src.Ant import Ant

_iterations = 100

_demographics = {
    'classic':  10,
    'ec':       0,
    'ac':       0,
    'gc':       0,
    'bc':       0
}

plotData = {
    'classic':  [],
    'ec':       [],
    'ac':       [],
    'gc':       [],
    'bc':       []
}

fr.createVertexFromFile()
eb = EdgeBuilder(fr.getVertexes())
eb.connectVertexes()
graph = Graph(getattr(eb, 'vertexes'), getattr(eb, 'edges'))

AB = AntBuilder(_demographics, graph)

for itr in range(_iterations):
    print('itr-{0}'.format(itr))
    itrList = []
    for ant in AB.antList:
        itrList.append(ant.cycle(len(graph.vertexes) - 1))
        ant.retrack()
        graph.phromoneEvaporate()
    plotData['classic'].append(itrList)

print(Ant._best)

x = np.arange(1, _iterations + 1)
y = []
yerr = [[], []]
for data in plotData['classic']:
    avg = sum(data)/float(len(data))
    y.append(avg)
    yerr[0].append(avg - min(data))
    yerr[1].append(max(data) - avg)


print(yerr[0])
print(yerr[1])

plt.xlabel('Iteration', size = 6)
plt.ylabel('Path length', size = 6)
plt.title('File berlin52, Iterations: {0}, Ants: {1}'.format(_iterations, 10), size = 8)
plt.xticks(size = 6)
plt.yticks(size = 6)

plt.errorbar(x, y,
             color='b',
             yerr=yerr,
             elinewidth=0.6,
             fmt='-s',
             markersize=3,
             markerfacecolor='None',
             linewidth=0.8,
             capsize=2,
             capthick=0.6,
             ecolor='b')

plt.show()
print("hello darkness my old friend")
#wtf is this steaming pile of shite
