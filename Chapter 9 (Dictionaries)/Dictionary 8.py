# Counting pattern

counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# The general pattern to count the words in a line of text is to split the line into words, then loop thorugh the words and use a dicitonary to track the count of each word indepenently.
