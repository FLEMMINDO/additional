def maxArea(height):
    maxar = 0
    n = len(height)
    next = 0
    l = 0
    r = n - 1

    while l < r:
        currArea = min(height[l], height[r]) * (r - l)
        maxar = max(maxar, currArea)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxar




print(maxArea([1,8,6,2,5,4,8,3,7]))