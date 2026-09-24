n=int(input("enter a number:"))

if n <=1:
    print("it is not a prime number")
else:
    count=0

    for i in range(2 , n):
        if n % i == 0:
            count = count + 1
    if count == 0:
        print("prime number")
    else:
        print("it is not a prime number")
