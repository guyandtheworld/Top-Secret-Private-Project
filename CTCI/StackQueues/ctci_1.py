""" Describe how you could use a single array to implement three stacks. """
import unittest


class TriStack:
    def __init__(self):
        self.tri_stack = ['0']*300
        self.stack_index = {
            0: 0,
            1: 0,
            2: 0,
        }

    def push(self, stack, value):
        index = stack * 100 + self.stack_index[stack]
        self.tri_stack[index] = value
        self.stack_index[stack] += 1

    def pop(self, stack):
        index = stack * 100 + self.stack_index[stack]
        self.tri_stack[index] = 0
        self.stack_index[stack] -= 1


class Test(unittest.TestCase):

    def test_tri_stack(self):
        stack = TriStack()
        stack.push(0, 100)
        stack.push(1, 300)
        stack.push(2, 500)
        stack.push(0, 100)
        stack.push(1, 300)
        stack.push(2, 500)
        stack.push(0, 100)
        stack.push(1, 300)
        stack.push(2, 500)


if __name__ == "__main__":
    unittest.main()
