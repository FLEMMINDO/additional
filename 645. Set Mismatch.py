def findErrorNums(nums):
    temp1 = 0
    temp2 = 0
    shouldbe = [i for i in range(1, len(nums) + 1)]
    for i in shouldbe:
        if i not in nums:
            temp2 = i
            break
    for i in nums:
        if nums.count(i) > 1:
            temp1 = i
            break
    return [temp1, temp2]




print(findErrorNums(nums = [2,2,1]))