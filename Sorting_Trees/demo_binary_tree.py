""" 
Test Driver File for binary_tree.py
Created By: Zafir Lari
Application: Finding MAX in Binary Tree

Description: Runs Node Class to demo a sorted
binary tree
"""

from binary_tree import Node, findSize, findHeight, findMaximum, findMinimum
from binary_tree import preorder, inorder, postorder, insert, delete


def testrun():
    test = Node(3)
    test = insert(test, 2)
    test = insert(test, 5)
    test = insert(test, 1)
    test = insert(test, 4)
    test = insert(test, 6)
    test = insert(test, 7)
    print(f"Preorder Traversal:")
    preorder(test)
    print(f"Inorder Traversal:")
    inorder(test)
    print(f"Postorder Traversal:")
    postorder(test)
    print(f"Maximum element is: {findMaximum(test)}")
    print(f"Size of Tree is: {findSize(test)}")
    print(f"Height of Tree is: {findHeight(test)}")
    print("Time Complexity for finding Maximum element is O(n) dependent on "
          "how many nodes are in the tree. Space complexity will remain O(1).")


if __name__ == "__main__":
    testrun()


"""
SAMPLE RUN:
Preorder Traversal:
3
2
1
5
4
6
7
Inorder Traversal:
1
2
3
4
5
6
7
Postorder Traversal:
1
2
4
7
6
5
3
Maximum element is: 7
Size of Tree is: 7
Height of Tree is: 4
Time Complexity for finding Maximum element is O(n) dependent on how many nodes are in the tree. Space complexity will remain O(1).

Process finished with exit code 0
"""
