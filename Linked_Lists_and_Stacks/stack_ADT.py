""" Stack Class implemented as ADT from Node Class """

from node_ADT import Node


class Stack:
    """ Stack Class using Linked List of Nodes """

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def peek(self):
        return None if self.isEmpty() else self.head.data

    def push(self, data):
        if self.head is None:
            self.head = Node(data=data)
            return
        new_node = Node(data=data)
        new_node.setNext(newnext=self.head)
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        removed_node = self.head
        self.head = self.head.next
        removed_node.setNext(newnext=None)
        return removed_node.data

    def deleteStack(self):
        while not self.isEmpty():
            self.pop()















