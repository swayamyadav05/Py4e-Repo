# Python program to check if the given string is a palindrome.
def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = ''.join(input_str.split()).lower()

    # Check if the string is the same when reversed 
    return cleaned_str == cleaned_str[::-1]

# Input the string
user_input = input('Enter a string: ')

# Check if the string is a palindrome
if is_palindrome(user_input) :
    print(f'{user_input} is a palindrome.')
else :
    print(f'{user_input} is not a plaindrome.')
