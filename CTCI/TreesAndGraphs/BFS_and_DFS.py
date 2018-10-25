import unittest


class Graph:
    def __init__(self):
        self.nodes = []


class Node:
    def __init__(self):
        self.name = None
        self.children = []


def visit(root):
    print(root.name)


def DFS(root):
    if root == None:
        return
    visit(root)
    root.visited = True
    for node in root.children:
        if node.visited == False:
            DFS(node)


def BFS(root):
    queue = []
    root.marked = True
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        visit(node)
        for n in node.children:
            if n.marked == False:
                n.marked = True
                node.append(n)


class Test(unittest.TestCase):

    def test_graph(self):
        graph = Graph()

        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node5 = Node()

        graph.nodes.extend([node1, node2, node3, node4])
        node1.children.append(node2)
        node2.children.extend([node5, node4])
        node4.children.append(node3)


if __name__ == "__main__":
    unittest.main()
