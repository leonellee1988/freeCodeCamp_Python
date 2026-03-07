"""
One of the core characteristics of sets is that they don't store duplicates values.

If you try to add a duplicate value, only one of them will be stored.

Sets are mutable and unorder (we cannot use indices or key).
"""

my_set = {1,2,3,4,5}
print(my_set)

# We can create a set with the built-in fuction set()

#The built-in method '.add()'

my_set.add(6)
print(my_set)

# .remove() and .discard()

my_set.remove(1)
my_set.discard(2)
print(my_set)

# The '.clear()' method removes all the elements from the set

# Python sets also have powerful methods that perform common mathematical set operations:

A = {1, 2, 3, 8}
B = {1, 2, 3, 4, 5}

# Subsets:

print(A.issubset(B)) # True, because all A's elements are in B
print(A.issuperset(B)) # False, because not all B's elements are in A

# Disjoint:

print(A.isdisjoint(B)) # False

# Union:

print(A | B)

# Intersection:

print(A & B)

# Difference:

print(A - B)
print(B - A)

# Symetric difference:

print(A ^ B)

# Sets and loops

my_set_1 = set(['id', 'name', 'age'])

colab = [
    {
        'id': 'P0001',
        'name': 'Edwin',
        'age': 38
    },
    {
        'id': 'P0002',
        'name': 'Noemi',
        'ages': 35
    },
    {
        'id': 'P0003',
        'name': 'Bruce',
        'age': 19
    }
]

for index, dictionary in enumerate(colab):
    dict_keys = set(dictionary.keys())
    print(dict_keys)
    print(my_set_1)