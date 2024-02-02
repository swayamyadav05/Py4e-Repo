# Python program that accepts a string and calculates the number of digits and letters.

def conut_digit_and_letters(input_string):
    digit_count = 0
    letter_count = 0
    
    for char in input_string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
    return digit_count, letter_count

input_string = input('Enter a string: ')
digits, letters = conut_digit_and_letters(input_string)
print(f'Number of digits: {digits}')
print(f'Number of letters: {letters}')
