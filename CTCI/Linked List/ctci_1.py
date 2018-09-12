"""
R�mov� Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
import unittest


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next_node = next

    def get_next(self):
        return self.next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def get(self):
        return self.head


def remove_dup(head):
    values = []
    prev_pointer = None
    curr_pointer = head
    while curr_pointer:
        if curr_pointer.get_data() in values:
            prev_pointer.set_next(curr_pointer.get_next())
        else:
            values.append(curr_pointer.get_data())
            prev_pointer = curr_pointer
        curr_pointer = curr_pointer.get_next()

    return head


def remove_dup_followup(head):
    curr_pointer = head
    while curr_pointer:
        runner = curr_pointer
        while runner.get_next():
            if runner.get_next().get_data() == curr_pointer.get_data():
                runner.set_next(runner.get_next().get_next())
            else:
                runner = runner.get_next()
        curr_pointer = curr_pointer.get_next()

    return head


class Test(unittest.TestCase):

    def setUp(self):
        self.data = [1, 3, 4, 6, 3, 2, 4]
        next = None
        for i in reversed(self.data):
            temp = Node(i, next)
            next = temp

        self.head = next

    def test_linked_list(self):
        temp = self.head
        while temp:
            temp = temp.get_next()

    def test_remove_dup(self):
        head = remove_dup(self.head)

        values = []
        while head:
            values.append(head.get_data())
            head = head.get_next()

        assert(set(values) == set(self.data))

    def test_remove_followup_dup(self):
        head = remove_dup_followup(self.head)

        values = []
        while head:
            values.append(head.get_data())
            head = head.get_next()

        assert(set(values) == set(self.data))


if __name__ == "__main__":
    unittest.main()
