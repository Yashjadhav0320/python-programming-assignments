# Q4(a). math standard library
import math

number = float(input("Enter a non-negative number: "))
if number < 0:
    print("Square root is not real for a negative number.")
else:
    print("Square root:", math.sqrt(number))

integer = int(input("Enter a non-negative integer for factorial: "))
if integer < 0:
    print("Factorial is not defined for negative integers.")
else:
    print("Factorial:", math.factorial(integer))

base = float(input("Enter base: "))
exponent = float(input("Enter exponent: "))
print("Power:", math.pow(base, exponent))

value = float(input("Enter a decimal number for ceiling and floor: "))
print("Ceiling:", math.ceil(value))
print("Floor:", math.floor(value))
