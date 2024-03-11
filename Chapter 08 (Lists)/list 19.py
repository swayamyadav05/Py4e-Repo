# The double split pattern
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    word = line.split()
    # print(word[1])
    # domain = word[1]
    # pieces = domain.split('@')
    domain = word[1].split('@')
    print(domain[1])

# List Summary 
# Concept of a collection 
# Slicing lists
# Lists and definite loops
# Indexing and lookup
# List mutability
# Functions: len, min, max, sum
# List methods: append, remove
# Sorting lists
# Splitting strings into lists of words
# Using split to parse strings
