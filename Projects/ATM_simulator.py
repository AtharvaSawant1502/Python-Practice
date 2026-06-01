init_balance= 100000

name=input("Enter Name:")
option=int(input("What would you like to do? \n Enter [1] for Withdrawing money \n Enter [2] for Depositing money \n Enter:" ))


if option==1:
  withdraw=int(input("Enter amout to withdraw:"))
  if withdraw<init_balance:
    current= init_balance-withdraw
    print("Current Amount:",current)

  else:
    print("Insufficient Balance")

elif option==2:
    deposit=int(input("Enter amout to deposit:"))
    current= init_balance+deposit
    print("Current Amount:",current)

else:
   print("Wrong Input")

  

if option == 1:
   print("="*30)
   print("="*30)
   print("Transaction History:")
   print(name,"Withdrawed Rs.",withdraw, "\nCurrent amount:",current)
   print("="*30)
   print("="*30)

elif option == 2:
   print("="*30)
   print("="*30)
   print("Transaction History:")
   print(name,"Deposited Rs.",deposit, "\nCurrent amount:",current)
   print("="*30)
   print("="*30)

else:
   print("Error")



