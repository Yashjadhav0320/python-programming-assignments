maths=int(input("enter your mathematics marks:"))
physics=int(input("enter your physics marks:"))
chemistry=int(input("enter your chemistry marks:"))

total_marks=maths+physics+chemistry
print("total marks obtained:",total_marks)

percentage=total_marks /3
print("your percentage is=",percentage)

if percentage>=60:
    print("you are eligible for admission with amount of donation 50000")
elif percentage>=90:
    print("you are eligible for taking admission without donation")
else:
    print("you are not eligible for admission better luck next time!!")
