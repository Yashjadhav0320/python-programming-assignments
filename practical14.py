income=float(input("enter your annual income:"))

if income <= 400000:
    tax=0
elif income <= 800000:
    tax=(income-400000) * 0.05
elif income <= 1200000:
    tax=(400000 * 0.05) +(income-800000)* 0.10
elif income <=1600000:
    tax=(400000 * 0.05)+(800000 * 0.10) +(income - 1200000)*0.15
else:
    print("invalid amount")
print("annual income:",income)
print("Tax payable",tax)

