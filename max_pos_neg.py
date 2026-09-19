#To find maximum positive and negative values
#Using two binary search
nums=[-3,-2,-1,0,0,1,2]
n=len(nums)
left,right=0,n

while left<right:
    mid = (left +right )//2
    if nums[mid] < 0: #checks whether the middle element is negative.
        left = mid+1 #Move left to the position after mid.
    else :
        right = mid #Move right to the position mid.
neg=left

left,right=0,n
while left<right:
    mid = (left +right )//2
    if nums[mid] <=0:
        left = mid+1
    else:
        right = mid
pos = n-left
print(max(pos,neg))

