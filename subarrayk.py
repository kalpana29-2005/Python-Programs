def subarrarySum(nums,k):
    mp={0:1}
    count = 0
    curr_sum = 0

    for num in nums :
        curr_sum += num
        if curr_sum - k in mp:
            count += mp[curr_sum-k]
        mp[curr_sum]=mp.get(curr_sum,0)+1

    return count
nums=[1,2,3,4,5]
k = 3
print(subarrarySum(nums,k))


    
