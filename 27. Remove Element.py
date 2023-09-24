def removeElement(nums, val):
    count = 0
    i = 0
    r = len(nums)
    while i<r:
        if nums[i] != val:
            count+=1
            i += 1
        else:
            nums.remove(nums[i])
            r-=1
    return count, nums


print(removeElement(nums = [3,2,2,3], val = 2))