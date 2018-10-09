"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time. 
"""


import unittest


class Node:
    def __init__(self, value, next=None, min=None):
        self.value = value
        self.min = min
        self.next = None


class Stack:
    def __init__(self, stack_size):
        self.stack = None
        self.top = 0

    def push(self, value):
        node =  Node(value)
        node.next = self.stack
        self.stack = node
        self.top += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        popped = self.stack
        self.stack = self.stack.next
        self.top -= 1
        return popped.value

    def isEmpty(self):
        if not self.stack:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack.value


class Test(unittest.TestCase):
    def test_stack_min(self):
        stack = Stack(100)
        stack.push(100)
        print(stack.peek())
        print(stack.pop())
        print(stack.peek())


if __name__ == "__main__":
    unittest.main()
