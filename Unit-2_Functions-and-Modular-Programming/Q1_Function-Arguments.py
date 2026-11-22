# Q1. Functions and Function Arguments
# Demonstrates positional, keyword and default arguments, and return values.

def add(a, b, operation="addition"):
    return a + b

def subtract(a, b, operation="subtraction"):
    return a - b

def multiply(a, b, operation="multiplication"):
    return a * b

def divide(a, b, operation="division"):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Positional arguments
print("Addition (positional):", add(num1, num2))

# Keyword arguments
print("Subtraction (keyword):", subtract(a=num1, b=num2))
print("Multiplication (keyword):", multiply(a=num1, b=num2))
print("Division (keyword):", divide(a=num1, b=num2))

# Default argument is used when the third argument is not supplied.
print("Default operation label:", add(num1, num2))
