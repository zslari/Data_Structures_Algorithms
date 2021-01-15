""" Vertex Class implemented as ADT """


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, cost=None):
        self.connectedTo[neighbor] = cost

    def __str__(self):
        return str(self.id) + ' connected To: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]
        
