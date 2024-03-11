# Searching a string
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

# Search and Replace
print('\n')
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'X')
print(nstr)

# Stripping Whitespace
print('\n')
greet = '   Hello Bob  '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# Prefixes
print('\n')
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

