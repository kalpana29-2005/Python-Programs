#mini calculator
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("1.add")
print("2.sub")
choice = int(input("Enter the choice 1 /2:"))
if choice == 1:
    print("Result:",a+b)
else:
    print("Result:",a-b)
