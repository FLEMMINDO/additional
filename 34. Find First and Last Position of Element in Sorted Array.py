def searchRange(nums, target):
    l = nums.count(target)
    ans = [-1, -1]
    for i in range(len(nums)):
        if nums[i] == target:
            l-=1
            if nums.count(target)-l==1:
                ans[0] = i
            elif l == 0:
                ans[1] = i
    if ans[0] != -1 and ans[1] == -1:
        ans[1] = ans[0]
    return ans


print(searchRange([5,7,7,8,8,10] , target = 8))

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]