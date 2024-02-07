# Python program to calculate the sum of all the odd numbers within the given range.

start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))
sum = 0
for num in range(start, end + 1) :
    if num % 2 != 0 :
        # print(num)
        sum = sum + num
print(f'The sum of odd numbers between {start} and {end} is:', sum)

# In Python, an f-string is a way to embed expressions inside string literals, using curly braces {}. When an f-string is prefixed with the letter "f" or "F", the expressions inside the curly braces are evaluated at runtime and their values are inserted into the string.

# The f-string makes it concise and readable, especially when combining variables with the text in a string