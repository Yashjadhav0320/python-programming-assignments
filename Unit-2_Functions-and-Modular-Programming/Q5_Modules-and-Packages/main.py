# Q5. User-Defined Modules and Packages
import arithmetic  # Import the entire module
from arithmetic import addition, subtraction  # Import selected functions
from student import display_student, calculate_result

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nUsing the complete arithmetic module:")
print("Multiplication:", arithmetic.multiplication(a, b))
try:
    print("Division:", arithmetic.division(a, b))
except ZeroDivisionError as error:
    print("Error:", error)

print("\nUsing selected imported functions:")
print("Addition:", addition(a, b))
print("Subtraction:", subtraction(a, b))

name = input("\nEnter student name: ")
roll = input("Enter roll number: ")
student_class = input("Enter class: ")
marks = [float(value) for value in input("Enter marks separated by spaces: ").split()]

display_student(name, roll, student_class)
total, average = calculate_result(marks)
print("Total marks:", total)
print(f"Average marks: {average:.2f}")
