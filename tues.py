array = int(input("Enter the size of the array: "))
arr = []
for i in range(array):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)
print("The array is:", arr)