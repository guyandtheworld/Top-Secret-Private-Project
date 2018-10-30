"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
"""


import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


class Balance:
    def __init__(self):
        self.dict = {}

    def checkHeight(self, root):
        self._calHeight(root, None, 0)
        h = []
        for k in self.dict.values():
            if k[0] == 0:
                h.append(k[1])
        if len(set(h)) > 2:
            return False
        return True

    def _calHeight(self, node, prev, h):
        if node == None:
            self.dict[prev][1] = h
            return

        # Leaf number and height
        self.dict[node] = [0, h]

        # incrementing the leaf number in the dictionary
        if prev is not None:
            self.dict[prev][0] += 1

        self._calHeight(node.left, node, h+1)
        self._calHeight(node.right, node, h+1)


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
        node2.right = node5
        node5.right = node6

        tree = BinTree()
        tree.root = node0
        # tree.view()

        bal = Balance()
        print(bal.checkHeight(node0))


if __name__ == '__main__':
    unittest.main()
