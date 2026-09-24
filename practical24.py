n=int(input("enter a number:"))
a=0
b=1
sum=0

print("fibonacci series:")

for i in range(n):
    print(a, end=" ")
    sum = sum + a
    a,b =b, a + b
print()
print("sum =",sum)
