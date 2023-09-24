import copy

def replaceElements(arr):
    i = 0
    arr2 = copy.deepcopy(arr)
    arr2.sort(reverse=True)
    while i < len(arr)-1:
        for j in arr2:
            if arr.index(j) > i:
                arr2.remove(arr[i])
                arr[i] = j
                break
        i+=1

    arr[len(arr)-1] = -1
    return arr


print(replaceElements([17,18,5,4,6,1]))