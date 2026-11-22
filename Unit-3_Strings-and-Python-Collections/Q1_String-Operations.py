# Q1. String Operations and String Methods

sentence = input("Enter a sentence: ")
print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Without leading/trailing spaces:", sentence.strip())

old_word = input("Enter the word to replace: ")
new_word = input("Enter the replacement word: ")
print("After replacement:", sentence.replace(old_word, new_word))

character = input("Enter one character to count: ")
if len(character) == 1:
    print(f"Occurrences of {character!r}:", sentence.count(character))
else:
    print("Please enter exactly one character.")

prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")
print("Starts with prefix:", sentence.startswith(prefix))
print("Ends with suffix:", sentence.endswith(suffix))

# Concatenation, repetition and membership
print("Concatenation:", sentence + " - Python")
print("Repetition:", sentence * 2)
word = input("Enter text to search in the sentence: ")
print("Membership:", word in sentence)
