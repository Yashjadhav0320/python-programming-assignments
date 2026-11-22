# Q4(c). datetime standard library
from datetime import datetime, date

current = datetime.now()
print("Current date and time:", current)
print("Day:", current.day)
print("Month:", current.month)
print("Year:", current.year)

first_text = input("Enter first date (YYYY-MM-DD): ")
second_text = input("Enter second date (YYYY-MM-DD): ")

try:
    first_date = date.fromisoformat(first_text)
    second_date = date.fromisoformat(second_text)
    difference = abs((second_date - first_date).days)
    print("Difference between dates:", difference, "days")
except ValueError:
    print("Invalid date. Please use YYYY-MM-DD format.")
