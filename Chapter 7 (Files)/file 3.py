# Counting Lines in a File

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count:', count)
