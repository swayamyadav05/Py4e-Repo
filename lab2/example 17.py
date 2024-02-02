# Python program to check the validity of password input by users.

# Funtion to check the validity of a password
def check_password_validity(password):
    # Minimum length requirement
    min_length = 8
    
    # Check if the password meets the minimum length requirement
    if len(password) < min_length:
        return False, "Password must be at least 8 characters long."
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercare letter"
    
    # Check if the password contain at least one digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    
    # If all checks pass, the password is valid
    return True, "Password is valid."

# Input
password = input("Enter a password: ")

#Call
is_valid, message = check_password_validity(password)

#Print
if is_valid:
    print(message)
else:
    print(f"Invalid password: {message}")
    