def decompressRLElist(nums):
    # ans = []
    # for i in range(0, len(nums) - 1,2):
    #     ans += [nums[i + 1] for _ in range (nums[i])]
    # return ans
    # number 1
    ans = []
    for i in range(0, len(nums), 2):
        for _ in range(nums[i]):
            ans.append(nums[i + 1])
    return ans



print(decompressRLElist([1,2,3,4]))