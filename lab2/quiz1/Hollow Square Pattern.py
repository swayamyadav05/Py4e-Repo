# rows = 5
# for i in range(rows):
#     print('*', end = ' ')
# print()
# for i in range(rows - 2):
#     print('*' + ' ' * (rows + 2) + '*')
# for i in range(rows):
#     print('*', end = ' ')
    

rows = 5
# Iterate through each row
for i in range(rows):
    # Iterate through each column
    for j in range(rows):
        # Check if it's the first or last row, or the first or last column
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            # Print asterisk for the first or last row, or first or last column
            print('*', end = ' ')
        else:
            # Print a space for the inner positions
            print(' ', end = ' ')
    print() # Move to the next line after each row is printed
