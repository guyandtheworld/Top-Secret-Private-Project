"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure. 
"""


import unittest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
            return self.head
        self.tail.next = node
        self.tail = node
        return node

    def dequeue(self):
        if self.head == None:
            return None
        removed = self.head
        self.head = self.head.next
        return removed

    def front(self):
        if self.head:
            return self.head.value
        return None

    def view(self):
        ptr = self.head
        while ptr:
            print(ptr.value, end="<-")
            ptr = ptr.next
        print()


class Pets:
    def __init__(self):
        self.pet = 1
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, species):
        if species == "dog":
            self.dogs.enqueue(self.pet)
        else:
            self.cats.enqueue(self.pet)
        self.pet += 1

    def dequeueAny(self):
        if self.cats.front() < self.dogs.front():
            return self.cats.dequeue()
        else:
            return self.dogs.dequeue()

    def dequeueCat(self):
        return self.cats.dequeue()

    def dequeueDog(self):
        return self.dogs.dequeue()

    def view(self):
        print("Dogs: ")
        self.dogs.view()
        print("Cats: ")
        self.cats.view()


class Test(unittest.TestCase):

    def test_stack_min(self):
        pets = Pets()
        pets.enqueue('dog')
        pets.enqueue('cat')
        pets.enqueue('dog')
        pets.enqueue('cat')
        pets.enqueue('dog')
        pets.enqueue('cat')
        pets.enqueue('cat')
        pets.enqueue('dog')
        pets.enqueue('dog')
        pets.enqueue('cat')
        pets.enqueue('cat')
        pets.enqueue('cat')
        pets.enqueue('dog')
        pets.view()

        print("I want any")

        pets.dequeueAny()
        pets.dequeueAny()

        pets.dequeueDog()
        pets.view()


if __name__ == "__main__":
    unittest.main()
