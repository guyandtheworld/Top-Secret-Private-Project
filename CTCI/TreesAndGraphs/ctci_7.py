"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project). All of a project's dependencies must be built 
before the project is. Find a build order that will allow the projects to be built. If there is no valid 
build order, return an error. EXAMPLE Input: projects: a, b, c, d, e, f dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 
Output: f, e, a, b, d, c 
"""

import unittest


class Node:
    def __init__(self, name=None):
        self.name = name
        self.visited = False
        self.children = []


class Test(unittest.TestCase):

    def test_graph(self):

        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')

        project = [a, b, c, d, e, f]
        dependencies = [()]


if __name__ == '__main__':
    unittest.main()
