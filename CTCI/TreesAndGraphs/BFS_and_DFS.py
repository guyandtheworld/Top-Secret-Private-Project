import unittest


class Graph:
    def __init__(self):
        self.nodes = []


class Node:
    def __init__(self, name=None):
        self.name = name
        self.visited = False
        self.children = []


def visit(root):
    print(root.name)


def DFS(root):
    if root is None:
        return
    visit(root)
    root.visited = True
    for node in root.children:
        if not node.visited:
            DFS(node)


def BFS(root):
    queue = []
    root.visited = True
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        visit(node)
        for n in node.children:
            if not n.visited:
                n.visited = True
                queue.append(n)


class Test(unittest.TestCase):

    def test_graph(self):
        graph = Graph()

        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        graph.nodes.extend([node0, node1, node2, node3, node4, node5])
        node0.children.extend([node1, node4, node5])
        node1.children.extend([node4, node3])
        node3.children.extend([node4, node2])
        node2.children.extend([node1])
        BFS(node0)
