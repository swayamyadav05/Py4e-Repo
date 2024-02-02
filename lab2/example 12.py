# # Python program to display all numbers within a range except the prime numbers.

# # Define a function to check if a number is prime
# def is_prime(num):
#     # Check if the number is less than 2 (not prime)
#     if num < 2:
#         return False
    
#     # Iterate from 2 to the square root of the nubmer
#     for i in range(2, int(num ** 0.5) + 1):
#         # If the number is divisible by any value in the range, it's not prime
#         if  num % i == 0:
#             return False
#     # If no factors are foundd, the number is prime
#     return True

# # Define a function to dispaly non-prime numbers within a range
# def display_non_primes(start, end):
#     # Itereat through the range of numbers
#     for num in range(start, end + 1):
#         # Check if the current number is not prime
#         if not is_prime(num):
#             # Print the non-prime number, ending with a space
#             print(num, end= ' ')

# display_non_primes(1, 20)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_all_primes(start, end):
    for num in range(start, end + 1):
        if not is_prime(num):
            print(num, end= ' ')

display_all_primes(1, 30)