# Q5. Dictionaries, Dictionary Comprehension and Nested Collections

employees = {
    1001: {"name": "Amit", "department": "IT", "salary": 45000},
    1002: {"name": "Neha", "department": "HR", "salary": 38000},
    1003: {"name": "Rahul", "department": "Finance", "salary": 52000}
}

print("Initial employee records:", employees)

# Add a dictionary element
employees[1004] = {"name": "Priya", "department": "IT", "salary": 60000}

# Update an employee's salary
employees[1002]["salary"] = 42000

# Display keys, values and key-value pairs
print("\nEmployee IDs:", employees.keys())
print("Employee records:", employees.values())
print("Employee ID and details:")
for employee_id, details in employees.items():
    print(employee_id, ":", details)

search_id = int(input("\nEnter employee ID to search: "))
if search_id in employees:
    print("Employee found:", employees[search_id])
else:
    print("Employee not found.")

threshold = float(input("Enter minimum salary: "))
high_salary_employees = {
    employee_id: details
    for employee_id, details in employees.items()
    if details["salary"] > threshold
}
print("Employees earning above the specified salary:", high_salary_employees)

delete_id = int(input("Enter employee ID to delete: "))
if delete_id in employees:
    del employees[delete_id]
    print("Employee deleted.")
else:
    print("Employee ID not found.")

print("Final employee records:", employees)
