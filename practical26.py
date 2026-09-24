a=int(input("enter first positive integer:"))
b=int(input("enter second positive integer:"))

x=a
y=b

while y != 0:
    r=x % y
    x=y
    y=r
gcd = x

lcm = (a*b)//gcd

print("GCD =", gcd)
print("LCM =",lcm)
