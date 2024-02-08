# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input('Enter file: ')
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()                                     # Create an empty dictionary
lst = []                                            # Create an empty list

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       # Select lines with 'From'
        # print(words)
        hr = words[5].split(':')
        counts[hr[0]] = counts.get(hr[0], 0) + 1
    else:
        continue
#     print(hr)
# print(counts)

for k, v in counts.items():                         # k = hour, v = count
    lst.append((k, v))                              # append tuples to list
# print(lst)

lst.sort()                                          # sort list by hour
for k,v in lst:                                     # loop thourgh list of tuples
    print(k,v)                                      # print counts sorted by hour
