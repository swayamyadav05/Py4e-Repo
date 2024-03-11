# 3.2 Rewrite your pay program using try and except so that your progarm handles non-numeric input garcefully by printing a message and exiting the program.

hrs = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    xh = float(hrs)
    xr = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
print(xh, xr)
if xh <= 40 :
    print('Regular')
    pay = xh * xr
    print(pay)
else :
    print('Overtime')
    reg = 40 * xr
    ovt = (xh - 40) * (xr * 1.5)
    pay = reg + ovt
    print(pay)
