# Q2. String Slicing and String Formatting

full_name = input("Enter student's full name: ").strip()
email = input("Enter email address: ").strip()
mobile = input("Enter mobile number: ").strip()

name_parts = full_name.split()
first_name = name_parts[0] if name_parts else ""
last_name = name_parts[-1] if len(name_parts) > 1 else ""

if "@" in email:
    username, domain = email.split("@", 1)
else:
    username, domain = email, "Invalid email format"

print("\nStudent Information")
print("--------------------")
print(f"First name : {first_name}")
print(f"Last name  : {last_name}")
print(f"Reversed name: {full_name[::-1]}")
print(f"Email username: {username}")
print(f"Email domain  : {domain}")
print(f"Last four mobile digits: {mobile[-4:]}")

# Positive and negative indexing
if full_name:
    print("First character (positive index 0):", full_name[0])
    print("Last character (negative index -1):", full_name[-1])

# Other formatting techniques
print("format() method: Name: {}, Email: {}".format(full_name, email))
print("Percent formatting: Mobile: %s" % mobile)
