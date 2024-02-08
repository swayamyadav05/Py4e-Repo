# Sorting lists of Tuples

#- We can take advantage of the ability to sort a list of typles to get a sorted version of a dictionary
#- First we sort the dictionary by the key using the items() method and sorted() funtion

d = {'a': 10,  'c': 22, 'b': 1}
print(d.items())
print(sorted(d.items()))

t = sorted(d.items())
print(t)
for k, v in sorted(d.items()):
    print(k, v)
