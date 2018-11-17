"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project). All of a project's dependencies must be built
before the project is. Find a build order that will allow the projects to be built. If there is no valid
build order, return an error.
"""

import unittest


class Node:
    def __init__(self, name=None):
        self.name = name
        self.visited = False
        self.children = []

    def __repr__(self):
        return str(self.name)


def BFS(root):
    queue = []
    root.visited = True
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        print(node, end='->')
        for n in node.children:
            if not n.visited:
                n.visited = True
                queue.append(n)


def create(node, depends):
    if node not in depends:
        return

    for child in depends[node]:
        if child not in node.children:
            node.children.append(child)
            create(child, depends)


def create_build(projects, dependencies):
    depends = {}
    non_dependent_nodes = []
    for p in projects:
        flag = False
        for d in dependencies:
            if d[1] == p:
                flag = True
                break
        if not flag:
            non_dependent_nodes.append(p)

    if not len(non_dependent_nodes):
        raise("No valid build order")

    for d in dependencies:
        if d[0] in depends:
            depends[d[0]].append(d[1])
        else:
            depends[d[0]] = [d[1]]

    for head in non_dependent_nodes:
        create(head, depends)
        BFS(head)


class Test(unittest.TestCase):

    def test_graph(self):

        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')

        project = [a, b, c, d, e, f, g]
        dependencies = [(f, a), (f, b), (f, c), (c, a),
                        (b, a), (a, e), (b, e), (d, g)]
        # dependencies = [(a, d), (f, b), (b, d), (f, a), (d, c), (d, e), (c, f)]

        create_build(project, dependencies)


if __name__ == '__main__':
    unittest.main()
