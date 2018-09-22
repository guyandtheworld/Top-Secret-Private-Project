"""
 You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
"""

import unittest

from CTCI.LinkedList.LinkedList import LinkedList, LinkedListNode


def add_lists(l1, l2):
    l3 = LinkedList()
    l1_ptr = l1.head
    l2_ptr = l2.head

    c = 0

    while l1_ptr or l2_ptr:

        if l1_ptr and l2_ptr:
            value = l1_ptr.value + l2_ptr.value + c
        elif l1_ptr:
            value = l1_ptr.value + c
        else:
            value = l2_ptr.value + c
        s = value % 10
        l3.add(s)
        c = value // 10

        if l1_ptr:
            l1_ptr = l1_ptr.next
        if l2_ptr:
            l2_ptr = l2_ptr.next

    if c:
        l3.add(c)

    return l3


def add_lists_recursive(l1, l2, carry=0):
    if not l1 and not l2 and carry == 0:
        return None

    value = carry

    next1 = next2 = None

    if l1:
        value += l1.value
        next1 = l1.next
    if l2:
        value += l2.value
        next2 = l2.next

    result = LinkedListNode(value%10)

    ptr = add_lists_recursive(next1, next2, value//10)

    result.next = ptr
    return result

class Test(unittest.TestCase):

    def test_linked_list(self):
        l1 = LinkedList()
        l1.add_multiple([4, 2, 6, 5, 9, 1])

        l2 = LinkedList()
        l2.add_multiple([7, 5, 6, 2, 2, 2])
        print("recursive: ", add_lists_recursive(l1.head, l2.head))
        new = add_lists(l1, l2)
        print(new)


if __name__ == "__main__":
    unittest.main()
