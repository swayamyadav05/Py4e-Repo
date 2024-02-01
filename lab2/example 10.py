# Python program to check if a given number is an Armstrong number

def is_armstrong(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)

    # Find the number of digits
    num_digits = len(num_str)

    # Calculate the sum of digits each raised to the power of the nubmer of digits
    # armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    armstrong_sum = 0
    for digit in num_str :
        armstrong_sum += int(digit) ** num_digits
    print (armstrong_sum)
    return armstrong_sum == number

# Input the number
num = int(input('Enter a number: '))

# Check if the nubmer is an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    