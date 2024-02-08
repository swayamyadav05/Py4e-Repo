# Tuples and Assignment

#- We can also put a tuple on the left-hand side of an assignment statement.
#- We can even omit the parentheses

(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)
x, y = 3, 4
print(y)
x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)
print(sorted(y, reverse=True))
data = [1, 4, 2, 7]
data.sort(reverse=True)
print(data)
