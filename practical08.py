a=int(input("enter triangle first side:"))
b=int(input("enter triangle second side:"))
c=int(input("enter triangle third side:"))

if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        print("it is a valid triangle")

if a == b == c:
    print("it is a equilateral triangle")
elif a == b or b == c or a == c:
    print("it is a is isoceles triangle")
else:
    print("it is a scalen trianle")
