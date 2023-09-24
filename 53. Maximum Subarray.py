def maxSubArray(nums):
    dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            dp[i][j] = dp[i-1][j-1] + nums[i] + nums[j]
    return dp




print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))