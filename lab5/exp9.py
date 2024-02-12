#Experiment-9: Create a set to store unique elements and perform set operations such as union, intersection, and difference.

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

union = set1.union(set2)
print("Union:", union)

intersect = set1.intersection(set2)
print("Intersection:", intersect)

difference = set1.difference(set2)
print("Difference (set1 - set2):", difference)

difference = set2.difference(set1)
# sdiff = sorted(difference)
print("Difference (set2 - set1):", difference)
