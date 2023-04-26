import random

A = random.randint(1, 100)
B = int(input("Guess the number"))
while True:
   if A == B:
    Print("Wow you got me")
    else:
    print("Opps! That's the wrong number")
    print(B)