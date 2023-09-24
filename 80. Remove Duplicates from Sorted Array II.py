from collections import Counter


def removeDuplicates(nums):
    s = Counter(nums)
    for i in range(len(nums)-1, 1, -1):
        if nums[i] == nums[i-1] == nums[i-2]:
            del nums[i]
    return len(nums)

print(removeDuplicates([1,2,3,3,3]))