import unittest


class Node:
    def __init__(self, name=None):
        self.name = name
        self.visited = False
        self.children = []


def BFS(source, destination):
    queue = []
    source.visited = True
    queue.append(source)

    if source == destination:
        return True

    while len(queue) != 0:
        node = queue.pop(0)

        for n in node.children:
            if n == destination:
                return True
            if not n.visited:
                n.visited = True
                queue.append(n)

    return False


class Test(unittest.TestCase):

    def test_graph(self):

        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        node0.children.extend([node1, node2])
        node1.children.extend([node2])
        node2.children.extend([node0, node3])
        print(BFS(node1, node3))


if __name__ == '__main__':
    unittest.main()
