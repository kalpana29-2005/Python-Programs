def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


nums = [1,1,2,2,3,3]
length = remove_duplicates(nums)

print(length)
print(nums[:length])



# def remove_duplicates_with_tail(nums):
#     if len(nums) == 0:
#         return 0

#     slow = 0
#     duplicates = []

#     for fast in range(1, len(nums)):
#         if nums[fast] != nums[slow]:
#             slow += 1
#             nums[slow] = nums[fast]
#         else:
#             duplicates.append(nums[fast])  # store duplicates

#     # place duplicates at the end
#     index = slow + 1
#     for dup in duplicates:
#         nums[index] = dup
#         index += 1

#     return slow + 1


# nums = [1, 1, 2, 2, 3]
# length = remove_duplicates_with_tail(nums)

# print("Unique length:", length)
# print("Modified array:", nums)
# print("Unique part:", nums[:length])
# print("Duplicates part:", nums[length:])