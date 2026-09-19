#linear search
# # nums = [10, 20, 30, 40]
# target = 30

# found = False

# for i in range(len(nums)):
#     if nums[i] == target:
#         print("Found at index", i)
#         found = True
#         break

# if not found:
#     print("Not found")
 
# n=int(input("Enter the number of inputs:"))
# num=[]
# for i in range (n):
#     lists=(int(input(f"enter elements {i+1}:")))
#     num.append(lists)

# key=30
# found=False
# for i in range (n):
#     if num[i]==key:
#         print("Found @ index",i)
#         found=True
#         break
# if not found:
#     print("Not found")

#binary search
nums = [10, 20, 30, 40, 50]
target = 20

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Found at index", mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Not found")
