import collections


def singleNumber(nums):
    # l = collections.Counter(nums)
    # for k, v in l.items():
    #     if v == 1:
    #         return k
    n = len(nums)
    c = 0
    for i in range(n):
        c = c ^ nums[i]
    return c

print(singleNumber(nums = [4,1,2,1,2]))