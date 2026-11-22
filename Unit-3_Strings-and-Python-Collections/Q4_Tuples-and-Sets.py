# Q4. Tuples, Sets and Set Operations

roll_numbers = (101, 102, 103, 104, 105)
print("Student roll number tuple:", roll_numbers)
print("Tuple elements:")
for roll in roll_numbers:
    print(roll)

print("Tuple indexing [0]:", roll_numbers[0])
print("Tuple slicing [1:4]:", roll_numbers[1:4])
print("Tuple concatenation:", roll_numbers + (106, 107))

course_a = {101, 102, 103, 104}
course_b = {103, 104, 105, 106}
print("\nCourse A:", course_a)
print("Course B:", course_b)
print("Union:", course_a | course_b)
print("Intersection:", course_a & course_b)
print("Difference (A - B):", course_a - course_b)
print("Symmetric difference:", course_a ^ course_b)

print("A is subset of B:", course_a.issubset(course_b))
print("A is superset of B:", course_a.issuperset(course_b))

course_a.add(107)
print("After add(107):", course_a)
course_a.discard(102)
print("After removing 102:", course_a)

even_squares = {n ** 2 for n in range(1, 11) if n % 2 == 0}
print("Squares of even numbers from 1 to 10:", even_squares)
