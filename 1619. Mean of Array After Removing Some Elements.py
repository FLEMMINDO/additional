from statistics import mean

def trimMean(arr):
    count = int(len(arr) * (5/100))
    for _ in range(count):
        arr.remove(max(arr))
        arr.remove(min(arr))
    return mean(arr)




print(trimMean(arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))