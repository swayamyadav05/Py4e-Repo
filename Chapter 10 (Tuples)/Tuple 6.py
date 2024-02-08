# Sort by values instead of key

#- If we could construct a list of tuples of the form (value, key) we could sort by value
#- We do this with a for loop that creates a list of tuples

c = {'a': 10,  'c': 22, 'b': 1}
temp = list()
for k, v in c.items():
    temp.append((v, k))
print(temp)
tep = sorted(temp)
print(tep)
temp = sorted(temp, reverse = True)
print(temp)
