# Mini Calculator

print("Mini Calculator")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("Select choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation")

choice = int(input("Enter choice (1/2/3/4/5/6):"))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
elif choice == 5:
    print("Result =", a % b)
elif choice == 6:
    print("Result =", a ** b)
else:
    print("Invalid choice")

