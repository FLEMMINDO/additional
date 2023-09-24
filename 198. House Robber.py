def rob(nums):
    fib = [0 for _ in range(nums)]
    fib[0] = 1
    fib[1] = 1
    for i in range(2, len(fib)):
        fib[i] = fib[i-1]+fib[i-2]
    return fib







print(rob(10))