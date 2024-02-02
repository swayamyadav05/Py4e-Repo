# Python program to get the Fibonacci series between 0 to 50.
# Define function to generate Fibonacci series up to given limit
def fibonacci_series(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=' ')
        a, b = b, a + b

fibonacci_series(50)
