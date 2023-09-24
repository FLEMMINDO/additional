def thirdMax(nums):
    nums = set(nums)
    if len(nums) < 3:
        return max(nums)
    else:
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)


print(thirdMax([2,2,3,1]))