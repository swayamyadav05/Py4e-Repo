size = 5

for i in range(size):
    for j in range(size - i - 1):
        print(' ', end=' ')
    
    for k in range(i + 1):
        print("*", end=' ')
    print()
