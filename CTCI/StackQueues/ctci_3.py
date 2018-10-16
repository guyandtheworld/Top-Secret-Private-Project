"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
"""

import unittest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, threshold):
        self.stack = None
        self.top = 0
        self.threshold = threshold

    def push(self, value):
        if self.top == self.threshold:
            print("Stack is full!")
            return None
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

    def is_full(self):
        if self.top == self.threshold:
            return True
        return False

    def print_stack(self):
        # Do with yield
        ptr = self.stack
        items = []
        while ptr:
            print(ptr.value)
            print('--')
            ptr = ptr.next


class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.master = [Stack(self.threshold)]
        self.stack_top = 0

    def push(self, value):
        if self.master[self.stack_top].is_full():
            self.master.append(Stack(self.threshold))
            self.stack_top += 1
        self.master[self.stack_top].push(value)

    def pop(self):
        if self.master[self.stack_top].is_empty():
            self.master.pop()
            self.stack_top -= 1
            return None
        item = self.master[self.stack_top].pop()
        return item


    def print_stack(self):
        # Do with yield
        for stack in self.master:
            stack.print_stack()
            print('-----------------')


class Test(unittest.TestCase):
    def test_stack_min(self):
        sos = SetOfStacks(3)
        sos.push(1)
        sos.push(2)
        sos.push(3)
        sos.push(4)
        sos.push(5)
        sos.push(6)
        sos.push(7)
        sos.push(8)
        sos.push(9)
        sos.print_stack()
        sos.pop()
        sos.pop()
        sos.pop()
        sos.print_stack()


if __name__ == "__main__":
    unittest.main()
