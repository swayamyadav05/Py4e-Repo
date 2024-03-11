# Searching through a file

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()    # We can strip the whitespace fron the right-hand side of the string using rstrip() form the string library
    if line.startswith('From:') :
        print(line)
