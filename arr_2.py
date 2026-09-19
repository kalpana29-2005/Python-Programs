#Reverse array


#Brute force
##def rev(arr):
##    n=len(arr)
##    reversed = []
##    for i in range(n-1,-1,-1):
##        reversed.append(arr[i])
##    return reversed
##arr=[1,2,3,4,5]
##print(rev(arr))

#Better
##def rev(arr):
##    return arr[::-1]
##arr = [1,2,3,4,5]
##print(rev(arr))

#Optimal solution using two pointers
def rev(arr):
    n = len(arr)
    left = 0
    right = len(arr)-1

    while left < right :
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr
arr = [1,2,3,4,5]
print(rev(arr))









    
