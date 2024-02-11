# Fine-Tuning Your Match

#- Depending on how "clean" your data is and the purpose of your application, you may want to narrow your match down a bit

import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print (line)
    