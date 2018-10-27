"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algo-rithm to create a binary search tree with minimal height.
"""

import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
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


def fromArray(arr, l, r):
    if r >= l:
        mid = l + (r - l)//2
        node = Node(arr[mid])
        node.left = fromArray(arr, l, mid-1)
        node.right = fromArray(arr, mid+1, r)
        return node
    else:
        return None


def create_balanced_tree(array):
    tree = Tree()
    tree.root = fromArray(array, 0, len(array)-1)
    return tree


class Test(unittest.TestCase):

    def test_graph(self):
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tree = create_balanced_tree(sorted_array)
        tree.view()


if __name__ == '__main__':
    unittest.main()
