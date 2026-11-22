# Q5. Command-Line Arguments
# Example: python Q5_Command-Line-Arguments.py 20 5 +
import sys

if len(sys.argv) != 4:
    print("Usage: python Q5_Command-Line-Arguments.py <number1> <number2> <operator>")
    print("Example: python Q5_Command-Line-Arguments.py 20 5 +")
    sys.exit(1)

try:
    number1 = float(sys.argv[1])
    number2 = float(sys.argv[2])
    operator = sys.argv[3]

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = number1 / number2
    else:
        raise ValueError("Invalid operator. Use +, -, * or /.")

    print(f"{number1} {operator} {number2} = {result}")

except ValueError as error:
    print("Input error:", error)
except ZeroDivisionError as error:
    print("Math error:", error)
