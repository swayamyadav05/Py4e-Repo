# Create a guessing game where the user has to guess a randomly generated number. Use branching, looping, and flow control statements to manage the game&#39;s flow.

# Experiment Overview:
# Generate a Random Number:
# Use the random module to generate a random number between a specified range. This will be the number the user needs to guess.
# Use a while loop to repeatedly prompt the user for their guess until they correctly guess the number.
# Use if..else statements to check if the user&#39;s guess is correct, too high, or too low. Provide appropriate feedback.
# Introduce flow control statements like continue to skip certain parts of the loop or break to exit the loop when the correct guess is made.

import random

# Generat a random number between 1 and 100
secret_number = random.randint(1, 100)

print('Welcome to the Guessing Game!')
print('Try to guess the secret number between 1 and 100.')

# Main game loop
while True:
    # Get user's guess
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is correct, too high, or too low
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break # Exit the loop when the correct guess is made
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

