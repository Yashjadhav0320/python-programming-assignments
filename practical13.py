pin=input("enter your pin:")

if len(pin)==4:
    print("pin accepted")
else:
    print("Invalid pin please Enter a Valid Pin")
    exit()

balance=float(input("enter your balance:"))
if balance > 0 :
    print("balance available")
else:
    print("balance should not be zero")
    exit()
withdrawal=float(input("enter your withdrawal amount:"))
if balance<withdrawal:
    print("insufficient balance")
    exit()
    withdrawal=balance-withdrawal
else:
    print(withdrawal,"amount has been debited from your account")

current=float
current=balance-withdrawal
print("your current balance =",current)
    
    
    
