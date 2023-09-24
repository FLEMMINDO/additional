import collections


def majorityElement(nums):
    l = collections.Counter(nums)
    for key in l:
        if l[key] == max(l.values()):
            return key



print(majorityElement([3,3,4]))