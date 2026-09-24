start=int(input("enter statring number:"))
end=int(input("enter ending number:"))

count = 0

for n in range(start, end + 1):
    if n > 1:
        prime = True

        for i in range(2 , n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)
            count = count + 1
print("total primae numbers = ", count)
