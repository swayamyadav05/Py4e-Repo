# Python program to count the total number of digits in a number.

# Input the nubmer
number = int(input('Enter a number: '))

# Convert the number to a string and calculate the length
num_str = str(number)
num_digits = len(num_str)

# Display the result
print(f'The total number of digits in {number} is : {num_digits}')

# with function
def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

n = int(input('Enter number: '))
print(countDigit(n))
