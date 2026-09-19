def move_zeroes(nums):
    slow = 0

    # Step 1: Move non-zero elements forward
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1

    # Step 2: Fill remaining with zeros
    for i in range(slow, len(nums)):
        nums[i] = 0


nums = [1, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)