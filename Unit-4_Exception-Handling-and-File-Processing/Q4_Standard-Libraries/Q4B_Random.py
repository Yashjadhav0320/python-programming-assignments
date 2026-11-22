# Q4(b). random standard library
import random

print("Random integer between 1 and 100:", random.randint(1, 100))

items = ["Python", "Java", "C", "C++", "JavaScript"]
print("Original list:", items)
print("Randomly selected element:", random.choice(items))

random.shuffle(items)
print("List after shuffle:", items)
