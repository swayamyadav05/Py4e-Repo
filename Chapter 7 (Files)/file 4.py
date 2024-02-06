# Reading the *Whole* file

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
print(inp)