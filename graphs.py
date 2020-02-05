"""
Title: Graphs
Author: Djamil Lakhdar-Hamina
Date: 02/05/2020
"""

## Adjacency Matrix for Fully Connected and "Small" Graph using nested list as representation

## Adjacency List for Graph using Nested Dictionary as Internal Representation
class Vertex:
    def __init__(self,key):
        self.id=key
        self.isconnectedTo={}

    def addNeighbor(self, nbr,weight):
        self.isconnectedTo[nbr]=weight

    def getKey(self):
        return self.id

    def __str__(self):
        return str(self.id) +  ' ' + 'is connected to'  + '' + ':' + str([i for i in self.isconnectedTo.keys()])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVert = 0

    def addVertex(self, key):
        self.numVert += 1
        newVert = Vertex(key)
        self.vertList[key] = newVert
        return newVert

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

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


if __name__=='__main__':
    a=Graph()
    a.addVertex('v1')
    a.addVertex('v2')
    a.addEdge('v1','v2')
    a.getVertexes()
    a.getVert('v1')
    a['v1']
    iter=[]
    for i in a:
        iter.append(i)
    print(i)
