"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""

import unittest

from CTCI.LinkedList.LinkedList import LinkedList


def calculate_length(l):
    count = 0
    while l:
        count += 1
        l = l.next
    return count

def find_intersection(L1, L2):
    len1 = calculate_length(L1.head)
    len2 = calculate_length(L2.head)

    shorter = L1 if len1 < len2 else L2
    longer = L1 if len1 > len2 else L2

    ptr1, ptr2 = longer.head, shorter.head

    for _ in range(abs(len1 - len2)):
        ptr1 = ptr1.next

    while ptr1 and ptr2:
        if ptr1 == ptr2:
            return ptr1
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return None

class Test(unittest.TestCase):

    def test_linked_list(self):
        l1 = LinkedList()
        l1.add_multiple(['j', 'z', 'm', 'a', 'l'])

        common = LinkedList()
        common.add_multiple(['f', 'g', 'k'])

        l2 = LinkedList()
        l2.add_multiple(['u', 'p', 'e'])

        ptr1 = l1.head

        ptr2 = l2.head

        while ptr1.next:
            ptr1 = ptr1.next

        while ptr2.next:
            ptr2 = ptr2.next

        ptr1.next = common.head
        ptr2.next = common.head

        print(find_intersection(l1, l2))

if __name__ == "__main__":
    unittest.main()
