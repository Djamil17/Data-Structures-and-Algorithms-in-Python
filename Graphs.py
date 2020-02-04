"""

"""

## Adjacency Matrix for Fully Connected and "Small" Graph using nested list as representation

## Adjacency List for Graph using Nested Dictionary as Internal Representation 

Class Vertex:
  def __init__(self,key):
    self.id=key
    self.connectedTo={}
    
  def addNeighbor(self, nbr,weight):
    self.connectedTo[nbr]=weight
  
  def getConnections(self):
    return self.connectedTo.keys()
  
  def getID(self):
    return self.id
  
  def getWeight(self,key):
    return self.connectedTo[key]
  
  def __str__(self):
    return str(self.id) + 'is connected to:' + str(self.connectedTo.values.iters())
