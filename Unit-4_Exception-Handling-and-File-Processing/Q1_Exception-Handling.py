# Q1. Exception Handling

# Handle invalid numerical input and division by zero.
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division result:", result)
finally:
    print("Division operation completed.")

# Handle an invalid list index.
values = [10, 20, 30]
try:
    index = int(input("\nEnter list index (0, 1 or 2): "))
    print("Selected value:", values[index])
except ValueError:
    print("Please enter an integer index.")
except IndexError:
    print("Invalid index. The list has indexes 0 to 2.")
else:
    print("List access completed successfully.")
finally:
    print("List operation finished.")

# Use raise when age is less than 18.
try:
    age = int(input("\nEnter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
except ValueError as error:
    print("Age validation:", error)
else:
    print("Age requirement satisfied.")
finally:
    print("Age validation completed.")
