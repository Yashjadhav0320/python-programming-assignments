n=int(input("enter a number:"))
original= n
reverse= 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n=n//10
if original == reverse:
    print("the number is palindrome")
else:
    print("the number is not palindrome")
