# The top 10 most common words

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse= True)

# for val, key in lst[:10]:
#     print(key, val)

# Even Shorter version
sort = sorted ( [ (v,k) for k, v in counts.items() ] ) 
print(sort)
rvssort = sorted(sort, reverse= True)
print(rvssort)
for val, key in rvssort[:10]:
    print(key, val)
    
# List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
