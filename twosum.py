# for printing the sum of two numbers in an array that equals a target value
# # def two_sum_sorted(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         total = arr[left]+ arr[right]
#         if total == target:
#             return [arr[left], arr[right]]
#         elif total < target:
#             left += 1
#         else:
#             right -= 1
#     return None
# print(two_sum_sorted([0, 2, 4, 6, 8, 10], 10))

# for printing the sum of two numbers in an array that equals a target value different pairs can be printed
def two_sum_all_pairs(arr, target):
    left = 0
    right = len(arr) - 1
    result = []

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            result.append([arr[left], arr[right]]) #add the pair to the result list
            left += 1
            right -= 1   # move both to find new pairs

        elif total < target:
            left += 1
        else:
            right -= 1

    return result

sum=two_sum_all_pairs([1,1, 2, 4, 6, 8, 9,9], 10)
print(set(tuple(pair) for pair in sum))
