"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
"""

import unittest

from CTCI.LinkedList.LinkedList import LinkedList


def del_mid_node(node):
    if not node.next:
        return
    node.value = node.next.value
    node.next = node.next.next


class Test(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        ll.add_multiple([0, 1, 2, 3, 4])
        middle_node = ll.add(5)
        ll.add_multiple([0, 1, 2, 3, 4])
        print(ll)
        del_mid_node(middle_node)
        print(ll)


if __name__ == "__main__":
    unittest.main()
