##def remove_duplicates_brute(arr):
##    result = []
##
##    for i in range(len(arr)):
##        found = False
##
##        for j in range(len(result)):
##            if arr[i] == result[j]:
##                found = True
##                break
##
##        if not found:
##            result.append(arr[i])
##
##    return result
##
##arr = [1, 2, 2, 3, 4, 4, 5]
##print(remove_duplicates_brute(arr))


def remove(arr):
    return list(set(arr))
arr =[1,2,2,1,1,1,2,4,3,3]
print(remove(arr))
