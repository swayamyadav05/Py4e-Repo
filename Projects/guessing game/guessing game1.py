import random # Module to generate a random number

secret_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("Try to guess the secret number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulation! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again")
        
    