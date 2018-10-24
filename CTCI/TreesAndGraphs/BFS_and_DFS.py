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
