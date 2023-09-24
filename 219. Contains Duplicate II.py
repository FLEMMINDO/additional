def containsNearbyDuplicate(nums, k):
    isFound = False
    i = 0
    while isFound is False and i<len(nums):
        if nums.count(nums[i])>1:
            if i+1+k <= len(nums):
                for j in range(i+1,i+1+k):
                    if nums[j] == nums[i] and j-i<=k:
                        isFound = True
            else:
                for j in range(i+1,len(nums)):
                    if nums[j] == nums[i] and j-i<=k:
                        isFound = True
        i+=1
    return isFound

print(containsNearbyDuplicate(nums = [1,2,3,1], k = 3)) #zaloopa