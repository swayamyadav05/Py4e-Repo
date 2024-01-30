# Python program to print all the even numbers within the given range.

# Input in the range
start = int(input('Enter the starting number: '))
end = int(input('Enter the ending nubmer: '))

# Using a for loop to iterate over the range of nubmers
for num in range(start, end + 1) :
    # Check if the number is even
    if num % 2 == 0 :
        print(num)

