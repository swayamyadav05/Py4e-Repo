# Python program to print a multiplication table of a given number
num = int(input('Enter the number for multiplication table: '))
for i in range(1,11) :
    print(f'{num} x {i} = {num * i}')
