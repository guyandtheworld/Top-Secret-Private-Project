"""
Design an algorithm and write code to find the first common ancestor of two nodes in a  binary tree. 
Avoid storing additional nodes in a data structure. 
"""


import sys
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


class BinTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if node.value < value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._add(node.right, value)
        else:
            if node.left == None:
                node.right = Node(value)
            else:
                self._add(node.left, value)

    def view(self):
        if self.root is not None:
            self._view(self.root)

    def _view(self, node):
        if node is not None:
            self._view(node.left)
            print(node.value)
            self._view(node.right)


def findAns(root, p, q):
    if root == None:
        return None
    if p == root or q == root:
        return root

    x = findAns(root.left, p, q)

    if x != None and x != p and x != q:
        # We have found the ancestor in some subtree
        return x

    y = findAns(root.right, p, q)

    if y != None and y != p and y != q:
        return y

    if x != None and y != None:
        return root
    elif root == p or root == q:
        return root
    else:
        if x is None:
            return y
        else:
            return x


class Test(unittest.TestCase):

    def test_check_if_balanced(self):
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)

        node0.left = node1
        node0.right = node2
        node1.left = node3
        node1.right = node4
        node3.left = node5
        node3.right = node6

        tree = BinTree()
        tree.root = node0
        # tree.view()

        print(findAns(tree.root, node5, node4))


if __name__ == '__main__':
    unittest.main()
