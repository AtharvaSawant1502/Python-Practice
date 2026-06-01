init_list=[100,50,400,500,700]
print("Initial List:",init_list)

#change element
init_list[1]= 200
print("\nChanged List:",init_list)

#append element
init_list.append(900)
print("\nAppended List:",init_list)

#inserting element
init_list.insert(0,15)
print("\nInserted List:",init_list)

#removing element
init_list.remove(15)
print("\nRemoved List:",init_list)

#popping element(remove element from particular index)
init_list.pop(4)
print("\nPopped List:",init_list)

#list reversing
init_list.reverse()
print("\nReversed List:",init_list)

#list sorting
init_list.sort()
print("\nSorted List:",init_list)

