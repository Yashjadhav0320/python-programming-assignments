# Q3. Recursive Functions: factorial and Fibonacci series

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:  # Base condition
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    series = fibonacci(n - 1)
    series.append(series[-1] + series[-2])
    return series


number = int(input("Enter a non-negative number for factorial: "))
try:
    print(f"Factorial of {number} =", factorial(number))
except ValueError as error:
    print("Error:", error)

terms = int(input("Enter number of Fibonacci terms: "))
if terms < 0:
    print("Please enter zero or a positive number.")
else:
    print("Fibonacci series:", *fibonacci(terms))
