# Definite loops and dictionaries

# Even though dicitonaries are not stored in order, we can write a for loop that goes thorugh all the entries in a dictinary - actually it goes through all of the keys in the dictionary and looks up the values

counts = {'chuck': 1, 'fred': 42 , 'jan': 100}
for key in counts:
    print(key, counts[key])
