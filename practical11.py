age=int(input("enter your age:"))
salary=int(input("enter your month salary:"))
score=float(input("enter your credit score:"))

if age>=18 and salary >= 25000 and score>=500:
    print("you are eligible for loan")
else:
    print("you are not eligible")
