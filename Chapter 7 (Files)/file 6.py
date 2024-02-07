# Skipping with Continue

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue    # We can conveniently skip a line by using the continue statement
    print(line)
