name=input("Enter Full Name:")
m1=int(input("Enter Maths Marks:"))
m2=int(input("Enter Science Marks:"))
m3=int(input("Enter English Marks:"))
m4=int(input("Enter History Marks:"))
m5=int(input("Enter Geography Marks:"))

total_marks=m1+m2+m3+m4+m5
percentage=(total_marks/500)*100

print("*"*30)
print("*"*30)
print("Name of Student:",name)
print("Mathematics:",m1)
print("Science:",m2)
print("English:",m3)
print("History:",m4)
print("Geography:",m5)
print("Total marks:",total_marks,"/500")
print("Percentage:",f"{percentage:.2f}","%")

if percentage>=90 :
    print("Grade:A")

elif 75<=percentage<=89 :
    print("Grade:B")

elif 50<=percentage<=74 :
    print("Grade:C")

elif 35<=percentage<=49 :
    print("Grade:D")    

else :
    print("Grade:Fail")

print("*"*30)
print("*"*30)

