"""
Creating, deleting a Linked List.
"""
"""
The runner technique
"""

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

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def size(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.get_next()
            count += 1
        return count

    def search(self, data):
        temp = self.head
        while temp:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        temp = self.head
        prev = None
        while temp:
            if temp.get_data() == data:
                prev.set_next(temp.get_next)
            prev = temp
            temp = temp.get_next()
        return None

list = [1, 2, 3, 4, 5, 6]

curr = None

for i in reversed(list):
    new_node = Node(i, curr)
    curr = new_node

while curr:
    print(curr.data)
    curr = curr.next_node

