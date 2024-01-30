# Python program to calculate the sum of all the odd numbers within the given range.

start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))
sum = 0
for num in range(start, end + 1) :
    if num % 2 != 0 :
        # print(num)
        sum = sum + num
print(f'The sum of odd numbers between {start} and {end} is:', sum)