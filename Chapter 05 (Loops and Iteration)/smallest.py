# Smallest value

# smallest_so_far = -1
# print('Before',smallest_so_far)
# for the_num in [9, 41, 12, 3, 74, 25] :
#     if the_num < smallest_so_far :
#         smallest_so_far = the_num
#     print(smallest_so_far, the_num)
# print('After',smallest_so_far)

# Here we can't put any specific number in place of -1 even if it will be right if we put 100 there but what about 3 digits number. 
# So, there is a variable called None type, None. It only has costant in it. So booleans have true and false, integers have a whole bunch, and then floats have a whole bunch, and None types have one thing, None. We think of it as the absence value.

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 25] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

# We still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest.
