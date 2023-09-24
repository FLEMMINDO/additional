def summaryRanges(nums):
    ans = []
    start = 0
    end = 1
    tempstart = 0
    while start != len(nums)-1 and end != len(nums)-1:
        if nums[start] + 1 == nums[end]:
            tempstart = nums[start]
            start+=1
            end+=1
        else:
            ans.append(str(tempstart) + '->' + str(nums[start]))
            start += 1
            end += 1
            tempstart = nums[start]


print(summaryRanges([0,1,3,5,6]))

# answer.append(f'{nums[tonum]}')
# answer.append(f'{nums[fromnum]}->{nums[tonum-1]}')
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"