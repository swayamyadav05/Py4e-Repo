# Get the number of rows for the hourglass
rows = int(input("Enter the number of rows: "))

# Upper part
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '* ' * i)
# Lower part
for i in range(2, rows + 1):
    print(' ' * (rows - i) + '* ' * i)
    