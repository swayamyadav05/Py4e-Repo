# Using re.search() like startswaith()

print("--Using find()--")

hand = open("mbox-short.txt")

for line in hand:
    line = line.rstrip()
    if line.startswith("From"):
        print(line)

print("--Using re.search()--")

import re

hand = open("mbox-short.txt")

for line in hand:
    line = line.rstrip()
    if re.search("^From: ", line):
        print(line)

# We fine-tune what is matched by adding special characters to the string
