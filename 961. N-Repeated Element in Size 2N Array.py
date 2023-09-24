def repeatedNTimes(nums):
    return max(set(nums), key= lambda x: nums.count(x))


print(repeatedNTimes([1,2,3,3]))