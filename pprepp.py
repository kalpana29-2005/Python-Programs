nums=[1,2,3,4,5]
key=3
found = False
left =0
right = len(nums)-1
while(left <= right):
    mid = (left + right) // 2
    if  nums[mid] == key:
        print("Found",mid)
        found == True
        break
    elif nums[mid]< key:
        left = mid+1
    else :
        right = mid - 1
if found == -1:
    print("Not found")
