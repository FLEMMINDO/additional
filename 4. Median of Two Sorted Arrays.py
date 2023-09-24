import statistics

def findMedianSortedArrays(nums1,nums2):
        data = nums1+nums2
        data.sort()
        return statistics.median(data)


print(findMedianSortedArrays([1,2],[3,4]))