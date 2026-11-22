# Q4. Scope, Lifetime and Lambda Functions

global_count = 10  # Global variable: available throughout this module.


def demonstrate_scope():
    local_message = "I am a local variable"
    print("Inside function - global_count:", global_count)
    print("Inside function - local_message:", local_message)


def update_global():
    global global_count
    global_count += 5
    print("Updated global_count inside function:", global_count)


demonstrate_scope()
update_global()
print("Global variable after function calls:", global_count)

# local_message exists only while demonstrate_scope() is executing.
# Trying to access it outside that function would cause NameError.

# Lambda functions
square = lambda number: number ** 2
cube = lambda number: number ** 3
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

x = float(input("Enter a number: "))
a = float(input("Enter first number for comparison/addition: "))
b = float(input("Enter second number for comparison/addition: "))

print("Square:", square(x))
print("Cube:", cube(x))
print("Maximum:", maximum(a, b))
print("Addition:", addition(a, b))
