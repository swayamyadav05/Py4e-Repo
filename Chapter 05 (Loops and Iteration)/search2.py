# Search Using a Boolean Variable

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
        break
    print(found, value)
print('After', found)

# If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.
