# Q2. File Handling – Read, Write and Append

filename = "student.txt"

# Write mode creates a new file or replaces existing contents.
with open(filename, "w", encoding="utf-8") as file:
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    student_class = input("Enter class: ")
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_number}\n")
    file.write(f"Class: {student_class}\n")

print("\nComplete file contents after writing:")
file = open(filename, "r", encoding="utf-8")
print(file.read())
file.close()

# Append mode adds records without deleting existing contents.
with open(filename, "a", encoding="utf-8") as file:
    additional_name = input("\nEnter another student name to append: ")
    additional_roll = input("Enter roll number: ")
    file.write(f"\nName: {additional_name}\n")
    file.write(f"Roll Number: {additional_roll}\n")

print("\nRead file line by line:")
file = open(filename, "r", encoding="utf-8")
for line in file:
    print(line, end="")
file.close()

# Display all lines using readlines().
file = open(filename, "r", encoding="utf-8")
all_lines = file.readlines()
print("\n\nAll lines using readlines():")
print(all_lines)
file.close()
