"""
Title: Graphs
Author: Djamil Lakhdar-Hamina
Date: 02/05/2020
"""

from linear_data_structures import Queue, Stack


## Adjacency Matrix for Fully Connected and "Small" Graph using nested list as representation

## Adjacency List for Graph using Nested Dictionary as Internal Representation
class Vertex:
    def __init__(self, key):
        self.id = key
        self.isconnectedTo = {}
        self.color = None
        self.distance = None
        self.pred = []

    def setPred(self, pre):
        self.pred = pre

    def setDistance(self, n):
        self.distance = n

    def setColor(self, flavor):
        self.color = flavor

    def addNeighbor(self, nbr, weight):
        self.isconnectedTo[nbr] = weight

    def getWeight(self, nbr):
        return self.isconnectedTo[nbr]

    def isConnectedto(self):
        return self.isconnectedTo.key()

    def getPred(self):
        return self.Pred

    def getKey(self):
        return self.id

    def getColor(self):
        return self.color

    def __str__(self):
        return str(self.id) + ' ' + 'is connected to' + '' + ':' + str([i for i in self.isconnectedTo.keys()])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVert = 0

    def addVertex(self, key):
        self.numVert += 1
        newVert = Vertex(key)
        self.vertList[key] = newVert
        return newVert

    def addAsymetricEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def addSymetricEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVert(self, key):
        if key in self.vertList:
            return key
        else:
            return None

    def getVertexes(self):
        return self.vertList.keys()

    def __contains__(self, item):
        return item in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())


def buildGraph():
    g = Graph()
    d = {}
    a = ['edge', 'wedge', 'sledge', 'hedge', 'ledge']
    for word in a:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            print(bucket)
            if word in d:
                d[bucket].append([word])
            else:
                d[bucket] = [word]

        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addAsymetricEdge(word1, word2)


def bfs(entry):
    start = Graph().vertList['{}'.format(entry)]
    VertQueue = Queue()
    start.setPred(None)
    start.setColor(None)
    start.setDistance(0)
    VertQueue.enqueue(start)
    while VertQueue.size() > 0:
        currentNode = VertQueue.dequeue()
        for nbr in start.isconnectedTo():
            if nbr.getColor() == 'white':
                nbr.setColor('grey')
                nbr.setDistance(currentNode.getDistance() + 1)
                VertQueue.enqueue(nbr)
                currentNode.setPred(nbr)
        currentNode.setColor('black')


def dfs(entry):
    start = Graph().vertList['{}'.format(entry)]
    start.visited=False
    VertStack=Stack()
    VertStack.push(start)
    while VertStack.size() > 0:
        v=VertStack.pop()
        VertStack.pop()
        start.visited=True
        for nbr in v.isconnectedTo():
            if nbr.visited == False:
                VertStack.push(nbr)
                nbr.visited=True


if __name__ == '__main__':
    a = Graph()
    a.addVertex('v1')
    a.addVertex('v2')
    a.addEdge('v1', 'v2')
    a.getVertexes()
    a.getVert('v1')
    a['v1']
    iter = []
    for i in a:
        iter.append(i)
    print(i)
