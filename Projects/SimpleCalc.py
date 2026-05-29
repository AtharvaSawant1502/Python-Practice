a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=input("Enter operation to be performed(+,-,x,/,%):")

if c == "+":
    print(int(a),"+",int(b),"=", a+b)

elif c == "-":
    print(int(a),"-",int(b),"=", a-b)

elif c == "x":
    print(int(a),"x",int(b),"=", a*b)   

elif c == "/":
    print(int(a),"/",int(b),"=", a/b) 

elif c == "%":
    print(a,"%",b,"=", a%b)

else :
    print("invalid operation input")