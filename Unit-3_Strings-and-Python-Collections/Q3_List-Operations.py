# Q3. List Operations and List Comprehension

numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
print("Original list:", numbers)

if numbers:
    position = int(input(f"Enter insertion index (0 to {len(numbers)}): "))
    value = int(input("Enter value to insert: "))
    if 0 <= position <= len(numbers):
        numbers.insert(position, value)
    else:
        print("Invalid insertion index.")

    print("After insert:", numbers)

    remove_value = int(input("Enter a value to remove: "))
    if remove_value in numbers:
        numbers.remove(remove_value)
    else:
        print("Value not found; nothing removed.")

    print("After remove:", numbers)
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    print("Ascending:", ascending)
    print("Descending:", descending)

    print("Maximum:", max(numbers) if numbers else "List is empty")
    print("Minimum:", min(numbers) if numbers else "List is empty")
    print("Sum:", sum(numbers))
    print("Concatenation:", numbers + [100, 200])
    print("Repetition:", numbers * 2)
    print("First element (if available):", numbers[0] if numbers else "N/A")
    search_value = int(input("Enter a value to search: "))
    print("Membership:", search_value in numbers)

    print("Even numbers:", [n for n in numbers if n % 2 == 0])
    print("Odd numbers:", [n for n in numbers if n % 2 != 0])
    print("Squares:", [n ** 2 for n in numbers])

    # Demonstrate append(), extend(), insert(), remove(), pop(), sort(), reverse()
    demo = numbers.copy()
    demo.append(50)
    demo.extend([60, 70])
    demo.insert(0, 40)
    if 40 in demo:
        demo.remove(40)
    if demo:
        removed = demo.pop()
        print("Popped element:", removed)
    demo.sort()
    print("After sort():", demo)
    demo.reverse()
    print("After reverse():", demo)
else:
    print("The list is empty. Enter at least one integer to perform list operations.")
