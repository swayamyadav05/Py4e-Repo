size = 5
# for i in range(size):
#     print(' ' * (size - i), end='')
#     print('* ' * (i + 1))

for i in range(size):
    for j in range(size - i):
        print(' ', end = '')
    for k in range(i + 1):
        print('*', end = ' ')
    print()
    