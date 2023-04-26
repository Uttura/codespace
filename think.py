import random

A = random.randint(1, 100)
B = int(input("Guess the number3"))
while True:
   if A == B:
    Print("Wow you got me")
    break
else:
    print("Opps! That's the wrong number")
