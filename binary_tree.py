"""
Binary Tree
Created By: Zafir Lari
Application: Finding MAX in Binary Tree

Description: Implements a sorted binary tree
made up of nodes
"""


class Node:
    """ Base class establishing root of tree
    and left and right children of root
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder(node):
    """ Print the preorder traversal of the tree """
    if node is not None:
        print(node.data)
        preorder(node=node.left)
        preorder(node=node.right)


def inorder(node):
    """ Print the inorder traversal of the tree """
    if node is not None:
        inorder(node=node.left)
        print(node.data)
        inorder(node=node.right)


def postorder(node):
    """ Print the postorder traversal of the tree """
    if node is not None:
        postorder(node=node.left)
        postorder(node=node.right)
        print(node.data)


def insert(node, data):
    """ Add a new node to the tree """
    if node is None:
        return Node(data=data)
    if data < node.data:
        node.left = insert(node=node.left, data=data)
    else:
        node.right = insert(node=node.right, data=data)
    return node


def delete(node, data):
    """ Remove a node from the tree """
    if node is None:
        return node
    if data < node.data:
        node.left = delete(node=node.left, data=data)
    elif data > node.data:
        node.right = delete(node=node.right, data=data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        temp = findMinimum(node=node.right)
        node.key = temp.data
        node.right = delete(node=node.right, data=temp.data)
    return node


def findMinimum(node):
    """ Helper method for delete function """
    current = node
    while current.left is not None:
        current = current.left
    return current


def findMaximum(node):
    """ Return the highest value node in the tree """
    if node is None:
        return float('-inf')
    current = node.data
    leftsubtree = findMaximum(node=node.left)
    rightsubtree = findMaximum(node=node.right)
    if leftsubtree > rightsubtree:
        current = leftsubtree
    if rightsubtree > leftsubtree:
        current = rightsubtree
    return current


def search(node, data):
    """ Determine if a certain node value is present in tree """
    if node is None:
        return False
    if node.data == data:
        return True
    checkleft = search(node=node.left, data=data)
    if checkleft:
        return True
    checkright = search(node=node.right, data=data)
    return checkright


def findHeight(tree):
    """ Get how many layers are in the tree """
    if tree is None:
        return int(0)
    else:
        leftsubtree = findHeight(tree=tree.left)
        rightsubtree = findHeight(tree=tree.right)
        if leftsubtree > rightsubtree:
            return int(leftsubtree+1)
        else:
            return int(rightsubtree+1)


def findSize(tree):
    """ Get how many nodes are in the tree """
    if tree is None:
        return int(0)
    else:
        return int(findSize(tree=tree.left) + findSize(tree=tree.right) + 1)
