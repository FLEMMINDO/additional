def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)





# if target in nums:
#     return nums.index(target)
# else:
#     tolower = target-1
#     toupper = target+1
#     found = False
#     while found is False:
#         if tolower in nums:
#             return nums.index(tolower)+1
#         elif toupper in nums:
#             return nums.index(toupper)-1
#         else:
#             tolower-=1
#             toupper+=1


print(searchInsert(nums = [1,3,5,6], target = 0))

# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4