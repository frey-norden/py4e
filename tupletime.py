#!/usr/bin/env python3
# File: tupletime.py

# comparison operators
print("x = (0, 1, 2) < (5, 2, 2)")
print("print(x)")
x = (0, 1, 2) < (5, 2, 2)
print(x)

print("l = (0, 1, 200000) < (0, 3, 4)")
print("print(l)")
l = (0, 1, 200000) < (0, 3, 4)
print(l)

print("g = ( 'Jones', 'Mandy') < ('Jones', 'Craig')")
print("print(g)")
g = ( 'Jones', 'Mandy') < ('Jones', 'Craig')
print(g)

print("fri = ('Smokie', 'Craig') > ('Deebo', 'Big Perm')")
print("print(fri)")
fri = ('Smokie', 'Craig') > ('Deebo', 'Big Perm')
print(fri)

# sorting lists of tuples
# we can take advantage of the python's ability to sort
# a list of tuples to get a sorted version of a dictionary
# First we sort the dictionary by the key using the items() method
# and sorted() function
print('\n')
print("d = {'a':10, 'b':1, 'c':22}")
print("print(d.items())")
d = {'a':10, 'b':1, 'c':22}
print(d.items())
print('\n')
print("sorted(d.items())")
print(sorted(d.items()))
# We can do this even more directly using the built-in function
# sorted that takes a sequence as a parameter and returns a
# sorted sequence
print('\n')
print("t = sorted(d.items())")
t = sorted(d.items())
print(t)
print("for k,v in sorted(d.items()):")
print("    print(k, v)")
for k,v in sorted(d.items()):
    print(k, v)
