import collections


def containsDuplicate(nums):
    l = collections.Counter(nums)
    if max(l.values()) > 1:
        return True
    return False


print(containsDuplicate([0]))


# Input: nums = [1,2,3,1]
# Output: true