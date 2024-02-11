# Wild-Card Characters

#- The dot character matches by any character
#- If you add the asterisk character, the character is "any number of times"

print('--Using find()--')

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)

print('--Using re.search()--')

import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print (line)
    