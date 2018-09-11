"""
A good exercise to practice strings, arrays, and general data structures is to implement your own version of
StringBuilder, HashTable and Array List.
"""

table = [[] for x in range(10)]

def hash_function(x): return x%10

def insert(table, input, value): table[hash_function(input)].append((input, value))

insert(table,41,'apple')
print(table)
insert(table,93,'banana')
print(table)
insert(table,93,'orange')
print(table)