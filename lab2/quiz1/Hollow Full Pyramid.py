rows = 5
for i in range(rows):
    for j in range(rows - i):
        print(' ', end = '')
    for j in range(i + 1):
        if j == 0 or j == i or i == rows-1:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()
