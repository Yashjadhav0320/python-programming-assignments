'''Write a Python program to accept the price and quantity of three products
 and calculate the subtotal, discount, GST, and final payable amount.'''

seconds = int(input("Enter duration: "))

hours = seconds // 3600

seconds = seconds % 3600

minutes = seconds // 60

seconds = seconds % 60

print(hours, "hour", minutes, "minute", seconds, "seconds")
