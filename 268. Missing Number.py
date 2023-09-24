def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] != 1:
            return nums[i]+1
    if 0 in nums:
        return nums[-1]+1
    else:
        return 0


print(missingNumber([0,2,4,3,1,5]))
# nums = [9,6,4,2,3,5,7,0,1]