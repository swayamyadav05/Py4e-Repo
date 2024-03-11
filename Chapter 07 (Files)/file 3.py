# Counting Lines in a File

fhand = open('mbox.txt')    ## Open a file read-only
count = 0
for line in fhand:  # Use a for loop to read each line
    count += 1  # Count the lines
print('Line Count:', count) # Print
