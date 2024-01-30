# Python program to calculate the sum of all numbers from 1 to a given number.

start = 1
end = int(input('Enter a number: '))
sum = 0
for num in range(start, end + 1) :
    sum = sum + num 
    # print(sum)
print('The sum is:', sum)
