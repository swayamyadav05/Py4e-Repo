# Tuples are like lists
# Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0

x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(y)
print(max(y))
for iter in y:
    print(iter)

# but... Tuples are "immutable"
# - Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string.

x = [9, 8, 7]
x[2] = 6
print(x)

y = 'ABC'
# y[2] = 'D'

z = (5, 4, 3)
z[2] = 0
print(z)