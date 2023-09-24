def sortArrayByParity(nums):
    nums.sort(key = lambda x: x%2==1)
    return nums



print(sortArrayByParity([0]))