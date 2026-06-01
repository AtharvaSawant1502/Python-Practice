print("~"*10,"Forward Player Selection","~"*10)

name=input("Enter Player Name:")
age=int(input("Enter Player Age:"))
goals=int(input("Enter Number of Goals Scored by Player:"))

if 15<age<36:
    if goals>=15:
        print(name,"is Selected \n CONGRATULATIONS!!!!!!!")
    
    else:
        print(name,"is not selected")

elif age>=36:
    if goals>=25:
        print(name,"is Selected \n CONGRATULATIONS!!!!!!!")
    
    else:
        print(name,"is not selected")

else:
    print(name,"is not selected")



