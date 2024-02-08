# Tuples are Comparable

#= The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ.

print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(('Jones', 'Sally',) < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))
