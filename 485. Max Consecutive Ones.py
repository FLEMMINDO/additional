def findMaxConsecutiveOnes(nums):
    single = []
    count = 0
    for i in nums:
        if i == 1:
            count +=1
        if i == 0:
            single.append(count)
            count = 0
    single.append(count)
    return max(single)



print(findMaxConsecutiveOnes([1,1,0,0,1,1,1]))