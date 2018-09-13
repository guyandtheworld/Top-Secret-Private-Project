"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

from .LinkedList import LinkedList

import unittest


def find_k(l1, k):
    print(l1)
    curr = l1.head
    tracer = l1.head

    for i in range(k + 1):
        curr = curr.next

    while curr:
        tracer = tracer.next
        print(curr.value, "-> ", end="")
        curr = curr.next
    print('')
    return tracer


class Test(unittest.TestCase):

    def setUp(self):
        self.l1 = LinkedList()
        self.l1.generate(19, 0, 9)

    def test_linked_list(self):
        print(find_k(self.l1, 5))


if __name__ == "__main__":
    unittest.main()
