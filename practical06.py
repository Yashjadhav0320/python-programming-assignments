p=float(input("enter your percentage:"))

if p<0 or p>100:
    print("invalid percentage")

if p>=90:
    print("grade A")

elif p>=75:
        print("grade B")
elif p>=60:
        print("grade c")
elif p>=40:
        print("grade D")
else:
    print("you are fail Better Luck next time!!!")
