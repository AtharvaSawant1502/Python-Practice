i=0
j=0
item_list=[]
price_list=[]

while i<3 :
       item=input("Enter item:")
       item_list.append(item)
       price=int(input("Enter price:Rs."))
       price_list.append(price)
       i=i+1
       
Total=sum(price_list)
print("="*30)
print("       Grocery Bill   ")
print("="*30)

print("ITEMS:")
while j<3:
       print (item_list[j] ,f"  Rs.:{price_list[j]}")
       j+=1

print("\n")
print("Total Amount=", Total)

if Total>=1000:
       discount=int(0.1*Total)
       print(f"\nDiscount=Rs.{discount}")
       final=Total-discount
       print(f"\nFinal Amount=Rs.{final}")
       

else:
       final=Total
       print(f"\nFinal Amount=Rs.{final}")

print("="*30)
print("="*30)