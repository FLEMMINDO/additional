def findDifference(nums1, nums2):
    ans = [[],[]]
    nums1 = set(nums1)
    nums2 = set(nums2)
    for i in nums1:
        if i not in nums2:
            ans[0].append(i)
    for i in nums2:
        if i not in nums1:
            ans[1].append(i)
    return ans


print(findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))