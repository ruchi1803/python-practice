import random

num = random.randrange(1,10)
i=1

while i<=3:
    inp = int(input("Guess a number between 1 to 10:"))
    if num == inp:
        print("Yay, congrats You have guessed the correct number")
        break
    elif (num < inp):
        print("Sorry! guess again too High")
    elif num > inp:
        print("Sorry! guess again too Low")
    i = i+1

print(f"The correct number is {num}")
