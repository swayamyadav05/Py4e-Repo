count = 0
sum = 0 
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / value)

# An average just combines the counting and sum patterns and divides when the loop is done.
