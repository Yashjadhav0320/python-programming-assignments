gb=float(input("enter your monthly data usage in GB:"))

if gb <= 1:
    bill = 50
elif gb <= 5:
    bill = 100
elif gb <= 10:
    bill = 200
elif gb <= 15:
    bill = 250
else:
    bill = 400

print("your total bill is ₹", bill)
    
