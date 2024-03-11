# if we use loop instead of using function 

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total += value
    count += 1
print(total)
print(count)
average = total / count
print('Average:', average)

# if we use functions

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average:', average)
