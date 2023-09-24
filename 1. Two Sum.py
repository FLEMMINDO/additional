def twoSum(nums, target):
    left = 0
    right = len(nums)-1
    while left!=right:
        if nums[left] + nums[right] == target:
            return (left,right)
        elif (target - nums[left]) in nums[left+1:]:
            right-=1
        elif (target-nums[right]) in nums[:right]:
            left+=1
        else:
            left+=1
    # numToIndex = {}
    # for i in range(len(nums)):
    #     if target - nums[i] in numToIndex:
    #         return [numToIndex[target - nums[i]], i]
    #     numToIndex[nums[i]] = i
    # return [] OPTIMIZED#NOTMINE




print(twoSum(nums = [2,5,5,11], target = 10))