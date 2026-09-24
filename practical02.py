salary= float(input("enter your salary:"))

da= salary * 10 / 100
hra = salary * 20 / 100

gross= salary + da + hra
tax = gross * 5 /100

net = gross - tax

print("Da:",da)
print("HRA:",hra)
print("Gross Salary:",gross)
print("Tax:",tax)
print("net",net)
