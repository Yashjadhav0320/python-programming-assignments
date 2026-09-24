n=int(input("enter a number:"))
sum=0
product=1
while n > 0:
    digit = n % 10
    sum = sum + digit
    product = digit * product
    n = n // 10
print("sum =", sum)
print("product =", product)
