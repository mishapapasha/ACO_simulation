import numpy as np
import matplotlib.pyplot as plt
import math
import sys, datetime, time
import src.util.fileReader as fr
from src.util.EdgeBuilder import EdgeBuilder
from src.Graph import Graph
from src.util.AntBuilder import AntBuilder

def simulate(_demographics):
    graph.setStartPh(_ph)
    AB = AntBuilder(_demographics, graph)
    antList = al = AB.antList
    bests = [[] for i in range(_iterations)]
    diff = 0
    for sim in range(_simolations):
        print('sim\t\t-\t{0}'.format(sim + 1))
        startTime = time.time()
        print('start\t\t-\t{0}'.format(time.ctime(startTime)))
        for itr in range(_iterations):
            #print('itr-{0}'.format(itr + 1))
            best = sys.maxsize
            start = 0
            for type in _demographics:
                for index in range(_demographics[type]):
                    #print('{0}-{1}'.format(start + index, al[start+index].getType()))
                    ans = al[start + index].cycle(len(graph.vertexes) - 1)
                    #plotData['classic'][itr].append(ans)
                    if ans < best:
                        best = ans
                    al[start + index].retrack()
                start += _demographics[type]
            for t in _demographics:
                graph.phromoneEvaporate(t)
            bests[itr].append(best)
        ##clear simulation
        endTime = time.time()
        print('end\t\t\t-\t{0}'.format(time.ctime(endTime)))
        diff += endTime - startTime
        graph.setStartPh(_ph)
        # print('duration\t-\t{0}'.format(diff))
    return bests, diff

def setPlotdata(bests, color, sign, label):
    x = np.arange(1, _iterations + 1)
    y = []
    yerr = [[]]
    for sample in bests:
        N = len(sample)
        avg = sum(sample)/float(N)
        #print(avg)
        y.append(avg)
        var = list(map(lambda x: (x - avg) ** 2, sample))
        dev = math.sqrt(sum(var) / N)
        yerr[0].append(dev)
    yerr.append(yerr[0])
    plt.errorbar(x, y,
                 color=color,
                 yerr=yerr,
                 elinewidth=1,
                 fmt='-' + sign,
                 markersize=3,
                 markerfacecolor='None',
                 linewidth=1,
                 capsize=2,
                 capthick=1,
                 ecolor=color,
                 label=label)

_simolations = 12

_iterations = 100

_classicPh = 0.01
_mulPh = 0.0001

_ph = { 'classic': _classicPh, 'ec': _mulPh, 'ac': _mulPh, 'gc': _mulPh, 'bc': _mulPh }

_classicDemographics = {
    'classic':  100
}

_csDemographics = {
    'ec':       22,
    'ac':       15,
    'gc':       45,
    'bc':       18
}

_asDemographics = {
    'ec':       3,
    'ac':       46,
    'gc':       23,
    'bc':       28
}

_gcDemographics = {
    'ec':       6,
    'ac':       6,
    'gc':       63,
    'bc':       25
}

fr.createVertexFromFile()
eb = EdgeBuilder(fr.getVertexes())
eb.connectVertexes()
graph = Graph(getattr(eb, 'vertexes'), getattr(eb, 'edges'))

##Simulate
print('Classic')
bests, diff = simulate(_classicDemographics)
best = min(list(map(lambda x: min(x), bests)))
setPlotdata(bests, 'xkcd:fuchsia', 's', 'Classic')
print('{0}:\tsimulations, Classic, time:\t-\t{1}, best:\t{2}'.format(_simolations, diff, best))

print('Control sample')
bests, diff = simulate(_csDemographics)
best = min(list(map(lambda x: min(x), bests)))
setPlotdata(bests, 'r', '_', 'Control sample')
print('{0}:\tsimulations, Control sample, time:\t-\t{1}, best:\t{2}'.format(_simolations, diff, best))

_ph = { 'classic': _classicPh, 'ec': _mulPh*100, 'ac': _mulPh*100, 'gc': _mulPh*100, 'bc': _mulPh*100 }

print('Increased Altercentricity')
bests, diff = simulate(_asDemographics)
setPlotdata(bests, 'b', '*', 'Increased Altercentricity')
print('{0}:\tsimulations, Increased Altercentricity, time:\t-\t{1}, best:\t{2}'.format(_simolations, diff, best))

print('Increased conflict handling')
bests, diff = simulate(_gcDemographics)
best = min(list(map(lambda x: min(x), bests)))
setPlotdata(bests, 'xkcd:bright green', 'x', 'Increased conflict handling')
print('{0}:\tsimulations, Increased conflict handling, time:\t-\t{1}, best:\t{2}'.format(_simolations, diff, best))

plt.xlabel('Iteration', size = 6)
plt.ylabel('Path length', size = 6)
plt.title('File berlin52, Iterations: {0}, Ants: {1}'.format(_iterations, 100), size = 8)
plt.xticks(size = 6)
plt.yticks(size = 6)
plt.legend(loc='upper right', prop={'size': 6})
plt.show()
print("hello darkness my old friend")


#wtf is this steaming pile of shite