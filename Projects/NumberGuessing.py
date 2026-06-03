import random
num= random.randint(1, 100)
chance=0

while chance<=10:
    i=int(input("\nYou have 10 chances\nGuess the Hidden Number Between 1 to 100:"))
    if i==num:
         print("CORRECT!!!!!!!!")
         break
    elif i<num:
        print("Higher")
        chance+=1
    elif i>num:
        print("Lower")
        chance+=1
    else:
        print("Wrong Guess X")
        chance+=1

if chance==10:
    print("CHANCE OVER :(")
    


  