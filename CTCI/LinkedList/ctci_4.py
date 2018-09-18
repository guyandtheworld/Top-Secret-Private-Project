"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
"""

import unittest

from CTCI.LinkedList.LinkedList import LinkedList


def partition_lists(node, value):
    head = curr = node.head
    prev = head
    curr = curr.next

    while curr:
        next = curr.next
        if curr.value < value:
            prev.next = next
            curr.next = node.head
            node.head = curr
        else:
            prev = curr
        curr = next


class Test(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        ll.add_multiple([5, 10, 3, 5, 8, 5, 10, 2, 1])
        print(ll)
        partition_lists(ll, 5)
        print(ll)


if __name__ == "__main__":
    unittest.main()
