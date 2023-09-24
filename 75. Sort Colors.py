# def sortColors(nums):
#     right = len(nums)-1
#     left = 0
#     while left<=right:
#         if nums[left] > nums[right]:
#             tmp = nums[right]
#             nums[right] = nums[left]
#             nums[left] = tmp
#             right-=1
#             left+=1
#         elif nums[left] == nums[right]:
#             right-=1
#         elif nums[left] < nums[right]:
#             left +=1
#     return nums
#
#
# print(sortColors([2,0,1]))


# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def shaker_sort(nums):
    if not nums:
        return
    left = 0
    right = len(nums) - 1
    while left <= right:
        for i in range(right, left, -1):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        left += 1
        for i in range(left, right):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        right -= 1

# Проверяем, что оно работает
random_list_of_nums = [2,0,2,1,1,0]
shaker_sort(random_list_of_nums)
print(random_list_of_nums)