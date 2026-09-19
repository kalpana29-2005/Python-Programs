#Check if array is sorted

#Brute Force
##def sorting(arr):
##    n = len(arr)
##
##    for i in range (n):
##        for j in range (i+1,n):
##            if arr[i] > arr[j]:
##                return False
##
##    return True
##arr = [1,2,2,3]
##print(sorting(arr))


#Better Approach
##def sorting(arr):
##    return arr == sorted(arr)
##arr = [1,2,4,2,3]
##print(sorting(arr))


#Optimal

def sorting(arr):
    n = len(arr)

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
arr = [1,2,3,4]
print(sorting(arr))












