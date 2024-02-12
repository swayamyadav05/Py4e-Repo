#Experiment-8: Create a tuple to represent an immutable collection and try accessing elements and performing basic operations.

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)

print("Element at index 1:", my_tuple[1])
print("Last elemnt:", my_tuple[-1])

a, b, c, d, e = my_tuple     #Unpacking
a = 8
print("Tuple unpacking:", a, b, c, d, e)
print("Length of tuple:", len(my_tuple))

another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple
print("Concatenated tuple:", combined_tuple)
      