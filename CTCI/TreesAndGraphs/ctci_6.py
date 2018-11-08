"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a 
given node in a binary search tree. You may assume that each node has a link to its parent. 
"""

import sys
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


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


def get_left_most(node):
    if node == None:
        return None

    while node.left != None:
        node = node.left

    return node


def get_right_subtree(node):
    pass


def checkNode(node):
    if node.right:
        next_node = get_left_most(node.right)

    if node.parent.right == node:
        get_right_subtree(node)
    else:
        return node.parent

    return next_node


class Test(unittest.TestCase):

    def test_check_if_balanced(self):
        node3 = Node(3)
        node1 = Node(1)
        node5 = Node(5)
        node2 = Node(2)
        node4 = Node(4)
        node6 = Node(6)

        node6.left = node2
        node2.parent = node6

        node2.left = node1
        node2.right = node3
        node1.parent = node2
        node3.parent = node2

        node3.left = node4
        node3.right = node5
        node4.parent = node3
        node5.parent = node3

        tree = BinTree()
        tree.root = node6
        tree.view()


if __name__ == '__main__':
    unittest.main()
