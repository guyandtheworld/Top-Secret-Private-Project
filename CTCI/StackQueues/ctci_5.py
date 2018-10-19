"""
    Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
    an additional temporary stack, but you may not copy the elements into any other data structure
    (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty. 
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

    def peek(self):
        return self.stack.value

    def view(self):
        ptr = self.stack
        while ptr:
            print(ptr.value, end=" | ")
            ptr = ptr.next
        print()


class Test(unittest.TestCase):

    def sort_with_top(self):
        top = self.mStack.top
        for i in range(top):
            print("Iter : ", i)
            tmax = self.mStack.pop()
            for j in range(top-1):
                temp = self.mStack.pop()
                if temp > tmax:
                    self.tStack.push(tmax)
                    tmax = temp
                else:
                    self.tStack.push(temp)
            self.mStack.push(tmax)
            for j in range(top-1):
                self.mStack.push(self.tStack.pop())
            top -= 1
            self.mStack.view()
            print()

    def sort(self):
        self.tStack.push(self.mStack.pop())

        while not self.mStack.is_empty():

            count = 0
            item = self.mStack.pop()
            if self.tStack.peek() < item:
                while not self.tStack.is_empty() and self.tStack.peek() < item:
                    self.mStack.push(self.tStack.pop())
                    count += 1

            self.tStack.push(item)

            for _ in range(count):
                self.tStack.push(self.mStack.pop())
            self.tStack.view()

    def test_stack_min(self):
        self.mStack = Stack()
        self.tStack = Stack()

        self.mStack.push(1)
        self.mStack.push(9)
        self.mStack.push(3)
        self.mStack.push(8)
        self.mStack.push(6)

        self.sort()


if __name__ == "__main__":
    unittest.main()
