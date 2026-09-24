n=int(input("enter a number:"))
original=n
count=0
temp=n

while temp >0:
    count = count + 1
    temp = temp // 10
    
sum=0
temp=n

while temp >0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10
if sum == original:
    print("it is a armstrong number")
else:
    print("it is not an armstrong number")
