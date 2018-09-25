"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""

import unittest

from CTCI.LinkedList.LinkedList import LinkedList


def is_palindrome(runner_beg, runner_end):
    if not runner_end.next:
        return runner_beg.next, runner_beg.value == runner_end.value
    start, flag = is_palindrome(runner_beg, runner_end.next)
    if flag:
        return start.next, start.value == runner_end.value
    return start.next, flag


def is_palindrome_v2(ll):
    fast = slow = ll.head

    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        fast = fast.next.next
        slow = slow.next

    while slow:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True

class Test(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        ll.add_multiple(['m', 'a', 'l', 'l', 'a', 'm'])
        print(ll)
        print(is_palindrome(ll.head, ll.head))
        print(is_palindrome_v2(ll))


if __name__ == "__main__":
    unittest.main()
