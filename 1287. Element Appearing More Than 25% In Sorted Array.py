def findSpecialInteger(arr):
    count = (0.25 * len(arr))
    for i in arr:
        if arr.count(i) > count:
            return i


print(findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))