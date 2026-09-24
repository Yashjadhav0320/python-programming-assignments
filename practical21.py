secret =3
num=int(input("enter a guess number:"))

if num == secret:
    print("your guess is correct")
elif num > secret:
    print("your guess is too high")
elif num < secret:
    print("your guess is too low")
    
