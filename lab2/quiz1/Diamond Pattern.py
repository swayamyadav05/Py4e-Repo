size = 4
for i in range(size):
    print(' ' * (size - i), end = '')
    print('* ' * (i + 1))
for i in range(size):
    for j in range(i + 2):
        print(' ', end = '')
    for k in range(size - i - 1):
        print('*', end = ' ')
    print()
