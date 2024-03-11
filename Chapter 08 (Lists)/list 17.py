line = "A lot                of spaces"
etc = line.split()
print(etc)
line = "first;second;third"
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(";")
print(thing)
print(len(thing))


# When you do not specify a delimiter, multiple spaces are treated like one delimiter
# You can specify what delimiter character to use in the splitting
