# Q2. Variable-Length Arguments and Return Statement

def calculate_result(student_name, *marks, **student_info):
    if not marks:
        return 0, 0, None

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    print("\nStudent Result")
    print("------------------------------")
    print(f"Name       : {student_name}")
    for key, value in student_info.items():
        print(f"{key.replace('_', ' ').title():<11}: {value}")
    print(f"Subject marks: {marks}")

    return total, average, highest


name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
student_class = input("Enter class: ")

count = int(input("Enter number of subjects: "))
marks_list = []
for i in range(count):
    marks_list.append(float(input(f"Enter marks for subject {i + 1}: ")))

total, average, highest = calculate_result(
    name,
    *marks_list,
    roll_number=roll_no,
    student_class=student_class
)

print(f"Total marks : {total:.2f}")
print(f"Average     : {average:.2f}")
print(f"Highest     : {highest:.2f}" if highest is not None else "Highest     : No marks entered")
