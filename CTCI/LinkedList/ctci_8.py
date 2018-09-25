"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
"""

"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""

import unittest

from CTCI.LinkedList.LinkedList import LinkedList


def check_loop(head):
    runner = head.next.next
    sup = head.next

    while sup and runner.next:
        if sup == runner:
            return True

        sup = sup.next
        runner = runner.next.next


def loop_detection(ll):
    ptr = ll.head
    if not check_loop(ptr):
        return False

    hash_table = []

    while ptr not in hash_table:
        hash_table.append(ptr)
        ptr = ptr.next
    return ptr


class Test(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        ll.add_multiple(list('abcdefghijk'))
        ptr = ll.head

        while ptr.next:
            ptr = ptr.next
        loop = ll.head

        for _ in range(3):
            loop = loop.next
        ptr.next = loop

        print("loop: ", loop)

        print(loop_detection(ll))


if __name__ == "__main__":
    unittest.main()
