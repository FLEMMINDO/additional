def sortByBits(arr):
    return sorted(arr, key = lambda x: (bin(x)[2:].count('1'), x))



print(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))