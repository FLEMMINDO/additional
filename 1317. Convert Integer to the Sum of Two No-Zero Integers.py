def getNoZeroIntegers(n):
    ans = [0,0]
    ans[0] = n-1
    ans[1] = 1
    if ans[0]%10==0:
        ans[0] -= 1
        ans[1] += 1
    return ans

print(getNoZeroIntegers(2))