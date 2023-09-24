def threeSumClosest(nums, target):
    ans = 0
    # for i in range(len(nums)):
    #     if i == target:
    #         ans += nums[i]
    #         if nums[i-1]:
    #             ans += nums[i-1]
    #             if len(nums)-1!=i:
    #                 ans+= nums[i+1]
    #                 return ans
    #             else:
    #                 return ans
    if len(nums)-1 >= target:
        ans += nums[target]
        if target-1 >= 0 and nums[target-1]!= None:
            ans+= nums[target-1]
        if len(nums)-1!= target and nums[target+1]!= None:
            ans+= nums[target+1]
    return ans

print(threeSumClosest(nums = [0,1,2], target = 3))

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).