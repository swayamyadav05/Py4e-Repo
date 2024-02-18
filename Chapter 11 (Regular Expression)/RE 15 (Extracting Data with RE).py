import re

# name = input('Enter file: ')
# if len(name) < 1:
name = r'S:\Coursera\Python for Everybody\Programming for Everybody (Get started with Pyhton\Py4e-Repo\Chapter 11 (Regular Expression)\regex_sum_1968506.txt'
fhandle = open(name)
fread = fhandle.read()

y = re.findall('[0-9]+', fread)
# print(y)

sum = 0
for i in range(len(y)):
    int_dig = int(y[i])
    # print(int_dig)
    sum += int_dig
print(sum)