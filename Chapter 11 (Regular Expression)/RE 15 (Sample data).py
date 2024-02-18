import re

name = input('Enter file: ')
if len(name) < 1:
    name = r'S:\Coursera\Python for Everybody\Programming for Everybody (Get started with Pyhton\Py4e-Repo\Chapter 11 (Regular Expression)\regex_sum_42.txt'
fhandle = open(name)
fread = fhandle.read()

# y = re.findall('[0-9]+', fread)
# print(y)

dig_list = []
with open('S:\Coursera\Python for Everybody\Programming for Everybody (Get started with Pyhton\Py4e-Repo\Chapter 11 (Regular Expression)\regex_sum_42.txt', 'r') as fread:
    for line in fread:
        print("Line from file:", line)  # Debug print to check the line
        digits = re.findall('[0-9]+', line)
        print("Digits found:", digits)  # Debug print to check the digits found
        dig_list.append(digits)

print("All digits found in the file:", dig_list)
# sum = 0
# for i in range(len(y)):
#     int_dig = int(y[i])
#     print(int_dig)
#     sum += int_dig
# print(sum)