def sortedSquares(nums):
    nums = list(map(lambda i: i ** 2, nums))
    nums.sort()
    return nums

print(sortedSquares(nums = [-7,-3,2,3,11]))