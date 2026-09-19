# Largest and second largest

# arr = [1,5,7,2,5,7,3,4]
# print(max(arr))


# arr = [1,2,3,4,5]
# largest = arr[0]
# for i in arr:
#    if i > largest:
#        largest = i
# print(largest)


# arr=[1,8,4,6,5]
# arr.sort()
# n=len(arr)
# largest=arr[n-1]
# second = arr[n-2]
# print("Second Largest:",second)

#Brute force method for solving 2nd largest
##def slargest(arr):
##    if len(arr)<2:
##        return None
##    arr.sort()
##    largest = arr[-1]
##    for i in range(len(arr)-2,-1,-1):
##        if arr[i]<largest:
##            return arr[i]
##    return None
##arr=[1,8,3,5,7,2]
##print(slargest(arr))

#Better solution
##def second_largest_better(arr):
##    if len(arr) < 2:
##        return None
##
##    largest = max(arr)
##    second_largest = float('-inf')
##
##    for num in arr:
##        if num != largest and num > second_largest:
##            second_largest = num
##
##    if second_largest == float('-inf'): #this is to check if there is same elements exists
##        return None
##
##    return second_largest
##arr=[10,2,3,33,42,23,55]
##print(second_largest_better(arr))


# Optimal solution
def slargest(arr):
    if len(arr)<2:
        return None
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num < largest and num > second:
            second = num
    if second == float('-inf'):
        return None
    return second
arr=[10,2,3,33,42,23,55]
print(slargest(arr))







    
    





















