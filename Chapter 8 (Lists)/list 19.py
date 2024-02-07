# The double split pattern
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    word = line.split()
    # print(word[1])
    domain = word[1]
    pieces = domain.split('@')
    print(pieces[1])
