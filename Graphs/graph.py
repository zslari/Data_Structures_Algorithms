""" 
Implementation of Graph Class and Vertices from vertex.py
Created By: Zafir Lari
Application: Graph Abstract Data Type Representation

Description: Implements a representation of the graph below

5 vertices (a, b, c, d, e)
Weighted edges: a->b 4; a->c 1; c->b 2; b->e 4; c->d 4
"""

from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newvertex = Vertex(key)
        self.vertList[key] = newvertex
        return newvertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return self.vertList.values()

    def print(self):
        print(f"Our graph has {len(self.getVertices())} vertices:")
        print("(", end=" ")
        for i in self.getVertices():
            print(f'{i},', end=" ")
        print(")", end=" ")
        print("\nWith the following Edges:")
        for from_id in self.getVertices():
            t = tuple(f'Vertex: {node.id}, Weight: {weight}' for node, weight in
                      self.getVertex(from_id).connectedTo.items())
            print(f"Vertex {from_id} is connected to: --> {t}")


def main():
    g = Graph()
    g.addVertex("a")
    g.addVertex("b")
    g.addVertex("c")
    g.addVertex("d")
    g.addVertex("e")
    g.addEdge("a", "b", 4)
    g.addEdge("a", "c", 1)
    g.addEdge("c", "b", 2)
    g.addEdge("b", "e", 4)
    g.addEdge("c", "d", 4)
    g.print()


if __name__ == "__main__":
    main()


"""
SAMPLE RUN:

Our graph has 5 vertices:
( a, b, c, d, e, ) 
With the following Edges:
Vertex a is connected to: --> ('Vertex: b, Weight: 4', 'Vertex: c, Weight: 1')
Vertex b is connected to: --> ('Vertex: e, Weight: 4',)
Vertex c is connected to: --> ('Vertex: b, Weight: 2', 'Vertex: d, Weight: 4')
Vertex d is connected to: --> ()
Vertex e is connected to: --> ()

Process finished with exit code 0


"""
