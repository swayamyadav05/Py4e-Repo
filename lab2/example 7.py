# Python program to count the total number of digits in a number.

# Input the nubmer
number = int(input('Enter a number: '))

# Convert the number to a string and calculate the length
num_str = str(number)
num_digits = len(num_str)

# Display the result
print(f'The total number of digits in {number} is : {num_digits}')

def countDigit(n) :
    count = 0
    while n != 0:
        n //= 0
        count += 1
    return count

num = int(input('Enter number: '))
print(countDigit(num))
