# str = "My name is swayam"
# spstr = str.split()
# print(spstr)
# jostr = ''.join(spstr)
# print(jostr)
# lostr= jostr.lower()
# print(lostr[::-1])

num = int(input("enter a no. "))

def armstrongg(num):
    count = 0
    onum = num
    while (onum>0):
        onum = onum//10
        count += 1
    print(f'total no. of digits: {count}')
    onum = num #reset onum to original num value as while loop mein it is getting changed
    summ = 0
    while (onum>0):
        lastdigit = onum % 10
        s = lastdigit ** count
        summ += s
        onum = onum//10
        
    print(summ)
    if(summ==num):
        print(f'{num} is an armstrong no.')
    else:
        print(f'{num} is not an armstrong no.')

armstrongg(num)
