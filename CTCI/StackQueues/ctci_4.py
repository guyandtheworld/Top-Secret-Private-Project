"""
    Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks. 
"""


import unittest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.stack = None
        self.top = 0

    def push(self, value):
        node = Node(value)
        node.next = self.stack
        self.stack = node
        self.top += 1

    def pop(self):
        if self.is_empty():
            return None
        popped = self.stack
        self.stack = self.stack.next
        self.top -= 1
        return popped.value

    def is_empty(self):
        if not self.stack:
            return True
        return False


class QueueUsingStack:
    def __init__(self):
        self.stack_new = Stack()
        self.stack_old = Stack()

    def enqueue(self, item):
        self.stack_new.push(item)

    def dequeue(self):
        if self.stack_new.is_empty():
            return None
    
        if self.stack_old.is_empty():
            while not self.stack_new.is_empty():
                self.stack_old.push(self.stack_new.pop())
        item = self.stack_old.pop()
        return item

    def view(self):
        head = self.stack_new.stack
        while head:
            print(head.value, "-> ", end="")
            head = head.next
        arr = []
        head = self.stack_old.stack
        while head:
            arr.append(head.value)
            head = head.next
        for i in reversed(arr):
            print(i, "-> ", end="")
        print()


class Test(unittest.TestCase):
    def test_stack_min(self):
        queue = QueueUsingStack()
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(6)
        queue.dequeue()
        queue.enqueue(0)
        queue.enqueue(12)
        queue.enqueue(67)
        queue.view()

if __name__ == "__main__":
    unittest.main()
