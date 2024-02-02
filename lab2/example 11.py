# Python program to count the number of even and odd numbers from a series of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count_even = 0
count_odd = 0

for n in numbers:
    if n % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers: ", count_even)
print("Number of odd numbers: ", count_odd)
