#Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)

#Display a message “Done” after successful execution of for loop for 4 iterations
for i in range(5):
    print(i)
else:
    print("done")

#Calculate the sum of all numbers from 1 to N
n=int(input("Enter Number:"))
sum=0
for i in range(1,n+1):
    sum+=i #can also write : sum=sum+i 

print(sum)