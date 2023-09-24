def moveZeroes(nums):
    count = 0
    while 0 in nums:
        del nums[nums.index(0)]
        count +=1
    for i in range(count):
        nums.append(0)
    return nums



print(moveZeroes([0,1,0,3,12]))

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]