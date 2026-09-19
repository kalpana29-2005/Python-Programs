# array=[1,2,3,4,5]
# print(array[0:3])
# array.append(6)
# array.append(7)
# print(array)

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for row in matrix:
#     for element in row:
#         print(element,end=" ")
#     print()

#List Comprehension
# squares=[i*i*i for i in range (1,9)]
# print(squares)

#same exapmle using loop (for)

# squares=[]
# for i in range(1,9,2):
#     squares.append(i*i*i)
# print(squares)

# even=[]
# for i in range(1,11):
#     if i%2==0:
#         even.append(i)
# print(even)
# even = [i % 2 == 0 for i in range(1, 11)]
# print(even)


#using max() function to find the maximum element in a list
# nums = [4, 9, 1, 7]
# print(max(nums))

# nums = [4, 9, 1, 7]
# maximum = nums[0]

# for num in nums:
#     if num > maximum:
#         maximum = num

# print(maximum)2

# num=[0,9,1,4,8,3]
# minimum=num[0]
# for i in num:
#     if i<minimum:
#         minimum=i

# print(minimum)

# nums=[0,1,4,2,6,4]
# print(min(nums))

# # Matrix
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = [[int(input(f"Enter element at [{i}][{j}]: ")) 
#            for j in range(rows)] 
#            for i in range(cols)]

# print("\nMatrix is:")
# for rows in matrix:
#     print(rows)

#wiyhout using list comprehension
rows=(int(input("Enter the row:")))
cols=(int(input("Enter the colums:")))
matrix=[]
for i in range(rows):
    row=[]
    for j in range (cols):
        value=int(input(f"Enter the element at [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)
print("\nMatrix is:")
for row in matrix:
    print(*row)