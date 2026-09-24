n=int(input("enter a number:"))
count=0

for i in range(1 , n + 1):
    if n % i == 0:
        print("factor=", i)
        count=count+1
print("total numbers", count)
