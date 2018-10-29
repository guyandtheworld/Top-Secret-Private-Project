"""
Given a binary tree,design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists). 
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

    def fromArray(self, arr, l, r):
        if r >= l:
            mid = l + (r - l)//2
            node = Node(arr[mid])
            node.left = self.fromArray(arr, l, mid-1)
            node.right = self.fromArray(arr, mid+1, r)
            return node
        else:
            return None

    def create_balanced_tree(self, array):
        self.root = self.fromArray(array, 0, len(array)-1)
        return self.root


class LinkedNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return "Whatsup"


class ListOfDepth:

    def __init__(self):
        self.head_of_levels = []

    def create_levels(self, node, level):
        if node == None:
            return

        l_node = LinkedNode(node.value)
        if len(self.head_of_levels) >= level+1:
            ptr = self.head_of_levels[level]
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = l_node
        else:
            self.head_of_levels.append(l_node)

        self.create_levels(node.left, level+1)
        self.create_levels(node.right, level+1)

    def _view(self, head):
        while head:
            print(head.value, ' -> ', end="")
            head = head.next

    def view(self):
        # print(len(self.head_of_levels))
        for i, head in enumerate(self.head_of_levels):
            print("Level: ", i)
            self._view(head)
            print("")


class Test(unittest.TestCase):

    def setUp(self):
        # Create binary tree for execution
        self.tree = BinTree()
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.tree.create_balanced_tree(sorted_array)

    def test_creation_linked_list(self):
        l = ListOfDepth()
        l.create_levels(self.tree.getRoot(), 0)
        # l.create_levels(self.tree.getRoot().left, 1)
        # l.create_levels(self.tree.getRoot().left.left, 2)
        # l.create_levels(self.tree.getRoot().left.right, 2)
        # l.create_levels(self.tree.getRoot().right, 1)
        # l.create_levels(self.tree.getRoot().right.left, 2)
        # l.create_levels(self.tree.getRoot().right.right, 2)
        l.view()


if __name__ == '__main__':
    unittest.main()
