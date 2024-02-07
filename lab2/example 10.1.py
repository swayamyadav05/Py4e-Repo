num = int(input('Enter a number: '))
num_str = str(num)
num_digits = len(num_str)
armstrong_sum = 0
for digit in num_str:
    armstrong_sum += int(digit) ** num_digits
    # print(armstrong_sum)
print(f'Armstrong sum is: {armstrong_sum}')
if armstrong_sum == num:
    print(f'{num} is an Armstrong number')
else:
    print(f'{num} is not an Armstrong number')
