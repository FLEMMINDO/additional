def relativeSortArray(arr1, arr2):
    ans = []
    ans1 = []
    for i in arr1:
        if i not in arr2:
            ans1.append(i)
    ans1.sort()
    for i in arr2:
        for _ in range(arr1.count(i)):
            ans.append(i)
    return ans + ans1


print(relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))