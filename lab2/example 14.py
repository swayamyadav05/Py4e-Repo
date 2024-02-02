# Python program to find the factorial of a given number.

# # Functin to calculate the factorial of a number
# def factorial(n):
#     # Base case: factorial of 0 or 1 is 1
#     if n == 0 or n == 1:
#         return 1
#     else:
#         # Recursive case: n! = n * (n-1)!
#         return n * factorial(n - 1)
    
# # Input: Get a number from the user
# number = int(input('Enter a number to find its factorial: '))

# # Check if the number is non-negative
# if number < 0:
#     print('Factorial is not defined for negative nubmers.')
# else: 
#     # Call the factorial fucntion and print the result
#     result = factorial(number)
#     print(f'The factorial of {number} is {result}')


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input('Enter the number to find factorial: '))
if num < 0:
    print('Factorial is not defined for negative numbers.')
else:
    result = factorial(num)
    print(f'The factorial of {num} is {result}')
